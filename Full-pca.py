import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt

def process_bandpass_thresholds(file_path, k_neighbors=40, output_weights_file="vertex_weights.txt"):
    print(f"Loading mesh from {file_path}...")
    mesh = o3d.io.read_triangle_mesh(file_path)
    
    if not mesh.has_vertices():
        raise ValueError("Invalid mesh.")
        
    mesh.compute_vertex_normals()
    vertices = np.asarray(mesh.vertices)
    normals = np.asarray(mesh.vertex_normals)
    num_vertices = len(vertices)

    pcd = o3d.geometry.PointCloud()
    pcd.points = mesh.vertices
    kdtree = o3d.geometry.KDTreeFlann(pcd)
    
    qem_weights = np.ones(num_vertices) # Default everything to 1.0 (Protected)
    color_map = np.zeros((num_vertices, 3)) # For visualization
    
    # --- YOUR DEFINED THRESHOLDS ---
    THRESHOLD_PLANAR = 0.75          # PCA Planarity lower bound (Bright Yellow/Red)
    THRESHOLD_NORMAL_LOW = 0.25      # Normal Tensor lower bound (Cyan)
    THRESHOLD_NORMAL_HIGH = 0.60     # Normal Tensor upper bound (Light Green)
    # Note: Anything above 0.60 is classified as extreme scattering (poles/chimneys) and protected.

    print("Computing unified tensors and applying band-pass thresholds...")
    for i in range(num_vertices):
        [_, idx, _] = kdtree.search_knn_vector_3d(vertices[i], k_neighbors)
        
        if len(idx) < 4:
            color_map[i] = [0, 0, 1] # Blue (Protected)
            continue
            
        # 1. CALCULATE PCA PLANARITY
        neighborhood_pts = vertices[idx]
        centroid_pts = np.mean(neighborhood_pts, axis=0)
        cov_pts = np.cov(neighborhood_pts - centroid_pts, rowvar=False)
        eigen_pts, _ = np.linalg.eigh(cov_pts)
        
        l_3 = max(0.0, eigen_pts[0])
        l_2 = max(0.0, eigen_pts[1])
        l_1 = max(0.0, eigen_pts[2])
        
        p_spatial = (l_2 - l_3) / l_1 if l_1 > 1e-8 else 0.0
        
        # 2. CALCULATE NORMAL TENSOR
        neighborhood_normals = normals[idx]
        centroid_normals = np.mean(neighborhood_normals, axis=0)
        cov_normals = np.cov(neighborhood_normals - centroid_normals, rowvar=False)
        eigen_normals, _ = np.linalg.eigh(cov_normals)
        
        n_min = max(0.0, eigen_normals[0])
        n_max = max(0.0, eigen_normals[2])
        
        s_normal = n_min / n_max if n_max > 1e-8 else 0.0
        
        # 3. APPLY YOUR LOGIC GATES (Band-Pass)
        if p_spatial > THRESHOLD_PLANAR:
            # It's a massive flat plane. Crush it.
            qem_weights[i] = 0.01
            color_map[i] = [1, 0, 0] # Visualizer: Red
            
        elif THRESHOLD_NORMAL_LOW < s_normal < THRESHOLD_NORMAL_HIGH:
            # It's in the vegetation/noise mid-band. Crush it.
            qem_weights[i] = 0.05
            color_map[i] = [0, 1, 0] # Visualizer: Green
            
        else:
            # It's a chimney, pole (extreme scattering), or sharp edge. Protect it.
            qem_weights[i] = 1.0
            color_map[i] = [0, 0, 1] # Visualizer: Blue

    print(f"Exporting final unified QEM weights to {output_weights_file}...")
    np.savetxt(output_weights_file, qem_weights, fmt="%.6f")

    print("Opening interactive 3D viewer to verify threshold segmentation...")
    mesh.vertex_colors = o3d.utility.Vector3dVector(color_map)
    o3d.visualization.draw_geometries([mesh],
                                      window_name="Band-Pass Threshold Logic",
                                      width=1280, height=720,
                                      left=50, top=50,
                                      mesh_show_wireframe=False,
                                      mesh_show_back_face=True)

if __name__ == "__main__":
    FILE_PATH = "your_mesh_file.ply" 
    process_bandpass_thresholds(FILE_PATH, k_neighbors=40)
