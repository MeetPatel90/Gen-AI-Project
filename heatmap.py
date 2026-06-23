import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt

def visualize_geometric_heatmap(file_path, k_neighbors=30):
    print("Loading mesh...")
    mesh = o3d.io.read_triangle_mesh(file_path)
    
    # Ensure the mesh has vertices
    if not mesh.has_vertices():
        raise ValueError("The provided file does not contain valid mesh vertices.")
        
    vertices = np.asarray(mesh.vertices)
    num_vertices = len(vertices)
    print(f"Loaded mesh with {num_vertices} vertices.")

    # Build a KDTree for fast local neighborhood lookups
    pcd = o3d.geometry.PointCloud()
    pcd.points = mesh.vertices
    kdtree = o3d.geometry.KDTreeFlann(pcd)
    
    # Array to store the Sphericality Index for each vertex
    sphericality = np.zeros(num_vertices)
    
    print("Computing local covariance matrices and eigenvalues...")
    for i in range(num_vertices):
        # Query the K-Nearest Neighbors around the current vertex
        [_, idx, _] = kdtree.search_knn_vector_3d(vertices[i], k_neighbors)
        
        if len(idx) < 4:
            sphericality[i] = 0.0
            continue
            
        # Extract the spatial coordinates of the neighborhood
        neighborhood = vertices[idx]
        
        # Compute the 3x3 spatial covariance matrix
        centroid = np.mean(neighborhood, axis=0)
        cov = np.cov(neighborhood - centroid, rowvar=False)
        
        # Compute eigenvalues
        # np.linalg.eigh returns eigenvalues in ASCENDING order (w[0] <= w[1] <= w[2])
        # Therefore: w[0] is lambda_min, w[2] is lambda_max
        eigenvalues, _ = np.linalg.eigh(cov)
        
        l_min = eigenvalues[0]
        l_max = eigenvalues[2]
        
        # Calculate Sphericality Index (S = l_min / l_max)
        if l_max > 1e-8:
            sphericality[i] = l_min / l_max
        else:
            sphericality[i] = 0.0

    print("Mapping metrics to colormap...")
    # Normalize the index between 0 and 1 for the colormap
    # You can adjust vmin and vmax to change the contrast of the heatmap
    norm = plt.Normalize(vmin=sphericality.min(), vmax=sphericality.max())
    cmap = plt.get_cmap('jet') # 'jet', 'plasma', or 'inferno' work well for noise mapping
    
    # Map the scalar sphericality values to RGB colors
    vertex_colors = cmap(norm(sphericality))[:, :3] # Strip alpha channel
    
    # Assign the calculated colors back to the mesh object
    mesh.vertex_colors = o3d.utility.Vector3dVector(vertex_colors)
    
    # Compute normals purely for proper interactive lighting rendering
    mesh.compute_vertex_normals()
    
    print("Opening interactive 3D viewer...")
    print("Controls: Left-click + drag to rotate | Right-click + drag to pan | Scroll to zoom")
    o3d.visualization.draw_geometries([mesh],
                                      window_name="Geometric Signal-to-Noise Heatmap",
                                      width=1280, height=720,
                                      left=50, top=50,
                                      mesh_show_wireframe=False,
                                      mesh_show_back_face=True)

if __name__ == "__main__":
    # Replace with the path to one of your SUM Helsinki tile files
    FILE_PATH = "your_mesh_file.ply" 
    
    # k_neighbors acts as the geometric proxy for your k-ring neighborhood.
    # Increase it (e.g., 50) for a wider evaluation, decrease it (e.g., 15) for tight local evaluation.
    K_NEIGHBORS = 30 
    
    visualize_geometric_heatmap(FILE_PATH, k_neighbors=K_NEIGHBORS)
