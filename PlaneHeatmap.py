import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt

def visualize_topological_structure(file_path, output_weights_file="mdpi_structural_weights.txt"):
    print(f"Loading mesh from {file_path}...")
    mesh = o3d.io.read_triangle_mesh(file_path)
    
    if not mesh.has_vertices() or not mesh.has_triangles():
        raise ValueError("Invalid mesh. Ensure it has vertices and triangles.")
        
    print("Computing vertex and triangle normals...")
    mesh.compute_vertex_normals()
    mesh.compute_triangle_normals()
    
    vertices = np.asarray(mesh.vertices)
    vertex_normals = np.asarray(mesh.vertex_normals)
    face_normals = np.asarray(mesh.triangle_normals)
    triangles = np.asarray(mesh.triangles)
    num_vertices = len(vertices)
    
    print("Building topological adjacency and incident face maps...")
    mesh.compute_adjacency_list()
    adjacency = mesh.adjacency_list
    
    # Map each vertex to its incident faces (1-ring)
    vertex_to_faces = [[] for _ in range(num_vertices)]
    for f_idx, tri in enumerate(triangles):
        for v_idx in tri:
            vertex_to_faces[v_idx].append(f_idx)

    # Storage for the two metrics
    g_saliency = np.zeros(num_vertices)
    alpha_max = np.zeros(num_vertices)
    
    print("Evaluating 3-ring covariance and 1-ring normal inconsistency...")
    for i in range(num_vertices):
        # ---------------------------------------------------------
        # 1. Three-Ring Neighborhood Extraction (Topological Search)
        # ---------------------------------------------------------
        ring_3_nodes = set([i])
        current_level = set([i])
        
        # Traverse the graph to a depth of 3 edges
        for _ in range(3):
            next_level = set()
            for node in current_level:
                for neighbor in adjacency[node]:
                    if neighbor not in ring_3_nodes:
                        next_level.add(neighbor)
                        ring_3_nodes.add(neighbor)
            current_level = next_level
            
        ring_3_list = list(ring_3_nodes)
        
        # Calculate Geometric Saliency from Covariance
        if len(ring_3_list) >= 3:
            neighborhood_pts = vertices[ring_3_list]
            centroid = np.mean(neighborhood_pts, axis=0)
            cov = np.cov(neighborhood_pts - centroid, rowvar=False)
            
            eigenvalues, _ = np.linalg.eigh(cov)
            # Ensure non-negative and sorted: l_1 <= l_2 <= l_3
            l_1 = max(0.0, eigenvalues[0])
            l_2 = max(0.0, eigenvalues[1])
            l_3 = max(0.0, eigenvalues[2])
            
            # Standard surface variation formula
            total_variance = l_1 + l_2 + l_3
            if total_variance > 1e-8:
                g_saliency[i] = l_1 / total_variance
                
        # ---------------------------------------------------------
        # 2. Local Normal Inconsistency (1-Ring Incident Faces)
        # ---------------------------------------------------------
        incident_faces = vertex_to_faces[i]
        if len(incident_faces) > 0:
            f_norms = face_normals[incident_faces]
            v_norm = vertex_normals[i]
            
            # Calculate angle deviation in degrees
            dots = np.clip(np.dot(f_norms, v_norm), -1.0, 1.0)
            angles_rad = np.arccos(dots)
            angles_deg = np.degrees(angles_rad)
            alpha_max[i] = np.max(angles_deg)

    print("Applying structural thresholds...")
    # Normalize Geometric Saliency to [0, 1] for relative thresholding
    max_g = np.max(g_saliency)
    if max_g > 0:
        g_saliency = g_saliency / max_g
        
    # The thresholds as defined in the referenced methodology
    T_g = 0.65
    T_alpha = 60.0 
    
    # Create the final weight array
    # 1.0 = High Penalty (Preserve this structure)
    # 0.1 = Low Penalty (This is a flat plane, decimate it)
    qem_weights = np.full(num_vertices, 0.1)
    
    # Apply dual constraints
    structural_mask = (g_saliency >= T_g) | (alpha_max >= T_alpha)
    qem_weights[structural_mask] = 1.0

    print(f"Exporting QEM weights to {output_weights_file}...")
    np.savetxt(output_weights_file, qem_weights, fmt="%.2f")

    # ---------------------------------------------------------
    # 3. Visualization Mapping
    # ---------------------------------------------------------
    print("Mapping structural layout to colormap...")
    # For visual clarity: 
    # RED (1.0) = Structural Edges / Chimneys / Noise (Preserved)
    # BLUE (0.1) = Massive Flat Planes (Decimated)
    norm = plt.Normalize(vmin=0.0, vmax=1.0)
    cmap = plt.get_cmap('jet') 
    
    vertex_colors = cmap(norm(qem_weights))[:, :3] 
    mesh.vertex_colors = o3d.utility.Vector3dVector(vertex_colors)
    
    print("Opening interactive 3D viewer...")
    o3d.visualization.draw_geometries([mesh],
                                      window_name="Topological Structural Constraint Heatmap",
                                      width=1280, height=720,
                                      left=50, top=50,
                                      mesh_show_wireframe=False,
                                      mesh_show_back_face=True)

if __name__ == "__main__":
    # Replace with your mesh file path
    FILE_PATH = "your_mesh_file.ply" 
    visualize_topological_structure(FILE_PATH)
