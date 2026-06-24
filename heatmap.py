import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt
import os

def process_joint_tensor_heatmap(file_path, k_neighbors=40, output_weights_file="vertex_weights.txt"):
    print(f"Loading mesh from {file_path}...")
    mesh = o3d.io.read_triangle_mesh(file_path)
    
    if not mesh.has_vertices():
        raise ValueError("The provided file does not contain valid mesh vertices.")
    
    # 1. Pre-compute normals on the pristine high-poly mesh
    print("Computing mesh vertex normals...")
    mesh.compute_vertex_normals()
    
    vertices = np.asarray(mesh.vertices)
    normals = np.asarray(mesh.vertex_normals)
    num_vertices = len(vertices)
    print(f"Loaded mesh with {num_vertices} vertices.")

    # 2. Build Spatial KDTree for neighborhood queries
    pcd = o3d.geometry.PointCloud()
    pcd.points = mesh.vertices
    kdtree = o3d.geometry.KDTreeFlann(pcd)
    
    joint_sphericality = np.zeros(num_vertices)
    
    print("Computing joint spatial and normal covariance tensors...")
    for i in range(num_vertices):
        [_, idx, _] = kdtree.search_knn_vector_3d(vertices[i], k_neighbors)
        
        if len(idx) < 4:
            joint_sphericality[i] = 0.0
            continue
            
        # --- SPATIAL TENSOR ---
        neighborhood_pts = vertices[idx]
        centroid_space = np.mean(neighborhood_pts, axis=0)
        cov_space = np.cov(neighborhood_pts - centroid_space, rowvar=False)
        eigen_space, _ = np.linalg.eigh(cov_space)
        
        # Ensure non-negative due to float precision
        l_min_space = max(0.0, eigen_space[0])
        l_max_space = max(0.0, eigen_space[2])
        s_spatial = l_min_space / l_max_space if l_max_space > 1e-8 else 0.0
        
        # --- NORMAL TENSOR ---
        neighborhood_normals = normals[idx]
        centroid_normal = np.mean(neighborhood_normals, axis=0)
        cov_normal = np.cov(neighborhood_normals - centroid_normal, rowvar=False)
        eigen_normal, _ = np.linalg.eigh(cov_normal)
        
        l_min_normal = max(0.0, eigen_normal[0])
        l_max_normal = max(0.0, eigen_normal[2])
        s_normal = l_min_normal / l_max_normal if l_max_normal > 1e-8 else 0.0
        
        # --- JOINT METRIC ---
        # Squaring the spatial component heavily punishes noisy flat planes (roofs)
        joint_sphericality[i] = np.power(s_spatial, 2) * s_normal

    # 3. Export the QEM Multiplier Weights for C++
    print(f"Exporting QEM weights to {output_weights_file}...")
    # We invert the metric: Chaos = 0.0 (cheap to collapse), Structure = 1.0 (expensive to collapse)
    # Applying a slight exponent creates a sharper mathematical boundary
    qem_weights = np.power(1.0 - joint_sphericality, 4)
    
    # Save as a simple text file (one float per line, matching vertex order)
    np.savetxt(output_weights_file, qem_weights, fmt="%.6f")
    print(f"Weights successfully saved to {os.path.abspath(output_weights_file)}")

    # 4. Visualization Mapping
    print("Mapping joint metric to colormap for visualization...")
    v_max = np.percentile(joint_sphericality, 99) if joint_sphericality.max() > 0 else 1.0
    norm = plt.Normalize(vmin=0.0, vmax=v_max)
    cmap = plt.get_cmap('jet') 
    
    vertex_colors = cmap(norm(joint_sphericality))[:, :3] 
    mesh.vertex_colors = o3d.utility.Vector3dVector(vertex_colors)
    
    print("Opening interactive 3D viewer...")
    o3d.visualization.draw_geometries([mesh],
                                      window_name="Joint Normal-Spatial Tensor Heatmap",
                                      width=1280, height=720,
                                      left=50, top=50,
                                      mesh_show_wireframe=False,
                                      mesh_show_back_face=True)

if __name__ == "__main__":
    # Ensure this points to your specific SUM dataset tile
    FILE_PATH = "your_mesh_file.ply" 
    
    process_joint_tensor_heatmap(
        file_path=FILE_PATH, 
        k_neighbors=40, 
        output_weights_file="vertex_weights.txt"
    )
