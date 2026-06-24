import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt

def visualize_normal_tensor_heatmap(file_path, k_neighbors=30):
    print("Loading mesh...")
    mesh = o3d.io.read_triangle_mesh(file_path)
    
    if not mesh.has_vertices():
        raise ValueError("The provided file does not contain valid mesh vertices.")
    
    # CRITICAL STEP: Compute vertex normals on the pristine high-poly mesh upfront
    print("Computing initial mesh vertex normals...")
    mesh.compute_vertex_normals()
    
    vertices = np.asarray(mesh.vertices)
    normals = np.asarray(mesh.vertex_normals)
    num_vertices = len(vertices)
    print(f"Loaded mesh with {num_vertices} vertices.")

    # Build KDTree using spatial coordinates for neighborhood lookups
    pcd = o3d.geometry.PointCloud()
    pcd.points = mesh.vertices
    kdtree = o3d.geometry.KDTreeFlann(pcd)
    
    sphericality = np.zeros(num_vertices)
    
    print("Computing normal covariance matrices and eigenvalues...")
    for i in range(num_vertices):
        # Find spatial neighbors within the k-ring proxy
        [_, idx, _] = kdtree.search_knn_vector_3d(vertices[i], k_neighbors)
        
        if len(idx) < 4:
            sphericality[i] = 0.0
            continue
            
        # CRITICAL FIX: Extract the normal vectors of the neighborhood, not the spatial positions
        neighborhood_normals = normals[idx]
        
        # Compute the 3x3 normal covariance matrix
        centroid = np.mean(neighborhood_normals, axis=0)
        cov = np.cov(neighborhood_normals - centroid, rowvar=False)
        
        # Compute eigenvalues (np.linalg.eigh returns them in ascending order: w[0] <= w[1] <= w[2])
        eigenvalues, _ = np.linalg.eigh(cov)
        
        l_min = eigenvalues[0]
        l_max = eigenvalues[2]
        
        # Prevent negative eigenvalues due to floating-point precision limits
        l_min = max(0.0, l_min)
        l_max = max(0.0, l_max)
        
        # Calculate Sphericality Index of the Normals (S = l_min / l_max)
        if l_max > 1e-8:
            sphericality[i] = l_min / l_max
        else:
            sphericality[i] = 0.0

    print("Mapping normal deviations to colormap...")
    # Using a tight percentile clipping (e.g., 99th percentile) can help enhance contrast
    # if extreme photogrammetry noise squashes the color dynamic range.
    v_max = np.percentile(sphericality, 99) if sphericality.max() > 0 else 1.0
    norm = plt.Normalize(vmin=0.0, vmax=v_max)
    cmap = plt.get_cmap('jet') 
    
    # Map scalar metrics directly to RGB
    vertex_colors = cmap(norm(sphericality))[:, :3] 
    mesh.vertex_colors = o3d.utility.Vector3dVector(vertex_colors)
    
    print("Opening interactive 3D viewer...")
    o3d.visualization.draw_geometries([mesh],
                                      window_name="Normal Tensor Signal-to-Noise Heatmap",
                                      width=1280, height=720,
                                      left=50, top=50,
                                      mesh_show_wireframe=False,
                                      mesh_show_back_face=True)

if __name__ == "__main__":
    # Replace with your local SUM Helsinki tile file path
    FILE_PATH = "your_mesh_file.ply" 
    
    # For normal tensors, a slightly larger neighborhood (e.g., 30 to 50) stabilizes 
    # the covariance estimation against fine-grained surface roughness.
    K_NEIGHBORS = 40 
    
    visualize_normal_tensor_heatmap(FILE_PATH, k_neighbors=K_NEIGHBORS)
