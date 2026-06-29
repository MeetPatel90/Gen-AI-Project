import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt

def visualize_planarity_ratio(file_path, ring_size=3):
    print(f"Loading mesh from {file_path}...")
    mesh = o3d.io.read_triangle_mesh(file_path)
    
    if not mesh.has_vertices() or not mesh.has_triangles():
        raise ValueError("Invalid mesh. Ensure it has vertices and triangles.")
        
    # Vertex normals computed purely so the 3D viewer has lighting
    mesh.compute_vertex_normals()
    
    vertices = np.asarray(mesh.vertices)
    num_vertices = len(vertices)
    
    print("Building topological adjacency map...")
    mesh.compute_adjacency_list()
    adjacency = mesh.adjacency_list
    
    planarity_scores = np.zeros(num_vertices)
    
    print(f"Evaluating {ring_size}-ring topological covariance and Planarity Ratio (p)...")
    for i in range(num_vertices):
        # 1. Topological Neighborhood Extraction
        ring_nodes = set([i])
        current_level = set([i])
        
        # Traverse the graph outward by 'ring_size' edges
        for _ in range(ring_size):
            next_level = set()
            for node in current_level:
                for neighbor in adjacency[node]:
                    if neighbor not in ring_nodes:
                        next_level.add(neighbor)
                        ring_nodes.add(neighbor)
            current_level = next_level
            
        ring_list = list(ring_nodes)
        
        # 2. PCA and Planarity Calculation
        if len(ring_list) >= 3:
            neighborhood_pts = vertices[ring_list]
            centroid = np.mean(neighborhood_pts, axis=0)
            cov = np.cov(neighborhood_pts - centroid, rowvar=False)
            
            eigenvalues, _ = np.linalg.eigh(cov)
            
            # np.linalg.eigh returns ascending order: w[0] <= w[1] <= w[2]
            l_3 = max(0.0, eigenvalues[0]) # Smallest (Normal variance)
            l_2 = max(0.0, eigenvalues[1]) # Middle 
            l_1 = max(0.0, eigenvalues[2]) # Largest (Principal variance)
            
            if l_1 > 1e-8:
                # Planarity Ratio: p = (lambda_2 - lambda_3) / lambda_1
                p = (l_2 - l_3) / l_1
                
                # Clamp between 0 and 1 to handle floating point precision limits
                planarity_scores[i] = max(0.0, min(1.0, p))
            else:
                planarity_scores[i] = 0.0

    # 3. Visualization Mapping
    print("Mapping Planarity Ratio to colormap...")
    # RED (1.0) = Perfect Flat Plane
    # BLUE (0.0) = 3D Blob, Noise, or 1D Line
    norm = plt.Normalize(vmin=0.0, vmax=1.0)
    cmap = plt.get_cmap('jet') 
    
    vertex_colors = cmap(norm(planarity_scores))[:, :3] 
    mesh.vertex_colors = o3d.utility.Vector3dVector(vertex_colors)
    
    print("Opening interactive 3D viewer...")
    o3d.visualization.draw_geometries([mesh],
                                      window_name=f"Planarity Ratio (p) Heatmap - {ring_size}-Ring",
                                      width=1280, height=720,
                                      left=50, top=50,
                                      mesh_show_wireframe=False,
                                      mesh_show_back_face=True)

if __name__ == "__main__":
    FILE_PATH = "your_mesh_file.ply" 
    
    # You can easily test how the topology scale affects the planarity detection
    # If 3-ring is too microscopic to see the massive walls, bump this to 5 or 10.
    RING_SIZE = 3 
    
    visualize_planarity_ratio(FILE_PATH, ring_size=RING_SIZE)
