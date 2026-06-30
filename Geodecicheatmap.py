import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra
import time
import os

# Note: You may need to pip install tqdm if you don't have it. 
# It provides a progress bar, which is vital for a ~200k Dijkstra loop.
from tqdm import tqdm 

def run_geodesic_pca_experiment(file_path):
    print(f"Loading mesh from {file_path}...")
    mesh = o3d.io.read_triangle_mesh(file_path)
    
    if not mesh.has_vertices() or not mesh.has_triangles():
        raise ValueError("Invalid mesh. Ensure it has vertices and triangles.")
    
    vertices = np.asarray(mesh.vertices)
    triangles = np.asarray(mesh.triangles)
    num_vertices = len(vertices)
    
    print(f"Mesh loaded: {num_vertices} vertices, {len(triangles)} faces.")

    # ---------------------------------------------------------
    # STEP 1: Construct the Mesh Graph
    # ---------------------------------------------------------
    print("Extracting unique edges and calculating Euclidean weights...")
    # Extract all edges from triangles
    edges = np.vstack([
        triangles[:, [0, 1]], 
        triangles[:, [1, 2]], 
        triangles[:, [2, 0]]
    ])
    # Sort and find unique edges to build an undirected graph
    edges = np.sort(edges, axis=1)
    edges = np.unique(edges, axis=0)
    
    # Calculate Euclidean edge lengths
    edge_lengths = np.linalg.norm(vertices[edges[:, 0]] - vertices[edges[:, 1]], axis=1)
    
    # Calculate target radius (R) based on average edge length
    avg_length = np.mean(edge_lengths)
    R = 20.0 * avg_length
    sigma = R / 2.0
    print(f"Average Edge Length: {avg_length:.6f}")
    print(f"Geodesic Search Radius (R): {R:.6f}")
    print(f"Gaussian Sigma (σ): {sigma:.6f}")

    # Build the sparse adjacency matrix
    row = np.hstack([edges[:, 0], edges[:, 1]])
    col = np.hstack([edges[:, 1], edges[:, 0]])
    data = np.hstack([edge_lengths, edge_lengths])
    
    adj_matrix = csr_matrix((data, (row, col)), shape=(num_vertices, num_vertices))

    # ---------------------------------------------------------
    # STEP 2, 3 & 4: Truncated Dijkstra & PCA Variants
    # ---------------------------------------------------------
    planarity_A = np.zeros(num_vertices)
    planarity_B = np.zeros(num_vertices)
    
    print("Running Geodesic Search and PCA (This may take a few minutes)...")
    start_time = time.time()
    
    for i in tqdm(range(num_vertices), desc="Processing vertices"):
        # Truncated Dijkstra: Stops expanding when distance > R
        distances = dijkstra(csgraph=adj_matrix, directed=False, indices=i, limit=R)
        
        # Mask valid neighbors within radius R (ignoring 'inf' for unreachable nodes)
        mask = distances <= R
        neighbors = np.where(mask)[0]
        neighbor_distances = distances[mask]
        
        if len(neighbors) >= 3:
            neighborhood_pts = vertices[neighbors]
            
            # --- VARIANT A: Unweighted Covariance ---
            cov_A = np.cov(neighborhood_pts, rowvar=False, ddof=0)
            eigenvalues_A, _ = np.linalg.eigh(cov_A)
            
            l3_A = max(0.0, eigenvalues_A[0])
            l2_A = max(0.0, eigenvalues_A[1])
            l1_A = max(0.0, eigenvalues_A[2])
            
            if l1_A > 1e-8:
                p_A = (l2_A - l3_A) / l1_A
                planarity_A[i] = max(0.0, min(1.0, p_A))
                
            # --- VARIANT B: Gaussian Weighted Covariance ---
            # w_i = exp(-d_i^2 / (2 * sigma^2))
            weights = np.exp(-(neighbor_distances**2) / (2 * sigma**2))
            
            # ddof=0 is required when using arbitrary float weights to prevent division scaling errors
            cov_B = np.cov(neighborhood_pts, rowvar=False, aweights=weights, ddof=0)
            eigenvalues_B, _ = np.linalg.eigh(cov_B)
            
            l3_B = max(0.0, eigenvalues_B[0])
            l2_B = max(0.0, eigenvalues_B[1])
            l1_B = max(0.0, eigenvalues_B[2])
            
            if l1_B > 1e-8:
                p_B = (l2_B - l3_B) / l1_B
                planarity_B[i] = max(0.0, min(1.0, p_B))

    print(f"Computation completed in {time.time() - start_time:.2f} seconds.")

    # ---------------------------------------------------------
    # STEP 5: Outputs & Visualization Mapping
    # ---------------------------------------------------------
    norm = plt.Normalize(vmin=0.0, vmax=1.0)
    cmap = plt.get_cmap('jet') 

    # Prepare Mesh A (Unweighted)
    colors_A = cmap(norm(planarity_A))[:, :3]
    mesh_A = o3d.geometry.TriangleMesh(mesh)
    mesh_A.vertex_colors = o3d.utility.Vector3dVector(colors_A)
    
    # Prepare Mesh B (Weighted)
    colors_B = cmap(norm(planarity_B))[:, :3]
    mesh_B = o3d.geometry.TriangleMesh(mesh)
    mesh_B.vertex_colors = o3d.utility.Vector3dVector(colors_B)

    # Save to disk for MeshLab inspection
    file_dir = os.path.dirname(os.path.abspath(file_path))
    path_A = os.path.join(file_dir, "Heatmap_Variant_A_Unweighted.ply")
    path_B = os.path.join(file_dir, "Heatmap_Variant_B_Weighted.ply")
    
    o3d.io.write_triangle_mesh(path_A, mesh_A)
    o3d.io.write_triangle_mesh(path_B, mesh_B)
    
    print(f"Saved Variant A to: {path_A}")
    print(f"Saved Variant B to: {path_B}")

    # Launch sequential interactive viewers
    print("\n--- Displaying Variant A: Unweighted Surface-Geodesic PCA ---")
    print("Close the viewer window to proceed to Variant B.")
    o3d.visualization.draw_geometries([mesh_A],
                                      window_name="Variant A: Unweighted Geodesic PCA",
                                      width=1280, height=720, left=50, top=50)
                                      
    print("\n--- Displaying Variant B: Gaussian Weighted Surface-Geodesic PCA ---")
    o3d.visualization.draw_geometries([mesh_B],
                                      window_name="Variant B: Gaussian Weighted Geodesic PCA",
                                      width=1280, height=720, left=50, top=50)

if __name__ == "__main__":
    # Ensure this points to your specific SUM dataset tile
    FILE_PATH = "your_mesh_file.ply" 
    run_geodesic_pca_experiment(FILE_PATH)
