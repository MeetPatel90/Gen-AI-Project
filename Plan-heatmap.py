import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt
import os

def visualize_planar_constraint(file_path, k_neighbors=40, output_weights_file="planar_weights.txt"):
    print(f"Loading mesh from {file_path}...")
    mesh = o3d.io.read_triangle_mesh(file_path)
    
    if not mesh.has_vertices():
        raise ValueError("Invalid mesh.")
        
    mesh.compute_vertex_normals()
    vertices = np.asarray(mesh.vertices)
    num_vertices = len(vertices)
    print(f"Loaded mesh with {num_vertices} vertices.")

    # Build KDTree for spatial neighborhood
    pcd = o3d.geometry.PointCloud()
    pcd.points = mesh.vertices
    kdtree = o3d.geometry.KDTreeFlann(pcd)
    
    planarity_scores = np.zeros(num_vertices)
    
    print("Computing PCA Planarity metric...")
    for i in range(num_vertices):
        [_, idx, _] = kdtree.search_knn_vector_3d(vertices[i], k_neighbors)
        
        if len(idx) < 4:
            planarity_scores[i] = 0.0
            continue
            
        # Extract purely spatial coordinates (No normals needed for this)
        neighborhood_pts = vertices[idx]
        centroid = np.mean(neighborhood_pts, axis=0)
        cov = np.cov(neighborhood_pts - centroid, rowvar=False)
        
        # np.linalg.eigh returns eigenvalues in ascending order: w[0] <= w[1] <= w[2]
        # Therefore: w[0] = lambda_3, w[1] = lambda_2, w[2] = lambda_1
        eigenvalues, _ = np.linalg.eigh(cov)
        
        l_3 = max(0.0, eigenvalues[0])
        l_2 = max(0.0, eigenvalues[1])
        l_1 = max(0.0, eigenvalues[2])
        
        # PCA Planarity Metric: P = (lambda_2 - lambda_3) / lambda_1
        # If it's a perfect plane, lambda_3 is 0, and lambda_2 is close to lambda_1, so P approaches 1.0.
        # If it's a line/edge or a 3D blob (tree), P drops near 0.0.
        if l_1 > 1e-8:
            planarity = (l_2 - l_3) / l_1
        else:
            planarity = 0.0
            
        planarity_scores[i] = max(0.0, min(1.0, planarity))

    # Apply a strict threshold: Only reward regions that are HIGHLY planar.
    # By squaring it, a score of 0.9 (mostly flat) stays high (0.81), 
    # but a score of 0.5 (bumpy/curved) gets crushed down (0.25).
    planarity_scores = np.power(planarity_scores, 2)

    # Export weights for FA-QEM
    print(f"Exporting QEM weights to {output_weights_file}...")
    # In FA-QEM, lower cost = collapses first.
    # We want planes (Score = 1.0) to have a tiny cost (e.g., 0.01).
    # We want non-planes (Score = 0.0) to have a normal cost (1.0).
    qem_weights = 1.0 - (planarity_scores * 0.99) 
    np.savetxt(output_weights_file, qem_weights, fmt="%.6f")

    # Visualization Mapping
    print("Mapping Planarity to colormap...")
    # For this colormap: Red/Hot = Massive Flat Plane. Blue/Cold = Edges, Trees, Chimneys.
    norm = plt.Normalize(vmin=0.0, vmax=1.0)
    cmap = plt.get_cmap('jet') 
    
    vertex_colors = cmap(norm(planarity_scores))[:, :3] 
    mesh.vertex_colors = o3d.utility.Vector3dVector(vertex_colors)
    
    print("Opening interactive 3D viewer...")
    o3d.visualization.draw_geometries([mesh],
                                      window_name="PCA Planarity Constraint Heatmap",
                                      width=1280, height=720,
                                      left=50, top=50,
                                      mesh_show_wireframe=False,
                                      mesh_show_back_face=True)

if __name__ == "__main__":
    FILE_PATH = "your_mesh_file.ply" 
    # K=40 is great for finding massive macro-planes while ignoring small bumps
    visualize_planar_constraint(FILE_PATH, k_neighbors=40)
