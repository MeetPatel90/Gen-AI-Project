# Mesh Decimation / Simplification for Large City Meshes in AR/VR

## Literature Review Tracker

---

# Paper Categories

| Category            | Description                                      |
| ------------------- | ------------------------------------------------ |
| Classical           | Traditional mesh simplification algorithms       |
| Feature-Preserving  | Preserve geometric structures and sharp features |
| Semantic-Aware      | Use semantic labels to guide simplification      |
| Neural              | Learning-based simplification methods            |
| Segmentation        | Semantic understanding of urban meshes           |
| LOD                 | Multi-resolution and level-of-detail generation  |
| AR/VR               | Rendering and perceptual evaluation              |
| City Reconstruction | Large-scale urban mesh generation                |

---

# Literature Database

| Publication                                                                                      | Year | Category                      | Brief Summary                                                                  | Dataset Used                 | Scale            | Semantic Aware | Texture Aware | Code Available | Key Contribution                                     | Code Link                                                   | Paper link                                                                 | Limitations                                 |
| ------------------------------------------------------------------------------------------------ | ---- | ----------------------------- | ------------------------------------------------------------------------------ | ---------------------------- | ---------------- | -------------- | ------------- | -------------- |------------------------------------------------------|-------------------------------------------------------------|----------------------------------------------------------------------------| ------------------------------------------- |
| Surface Simplification Using Quadric Error Metrics (QEM)                                         | 1997 | Classical                     | Foundational mesh simplification algorithm using quadric error metrics.        | Generic meshes               | Object           | No             | No            | Yes            | Foundation of most modern simplification algorithms  | Many implementations                                        | https://www.cs.cmu.edu/~garland/Papers/quadrics.pdf                        | No feature or semantic awareness            |
| Progressive Meshes                                                                               | 1996 | Classical / LOD               | Introduces progressive mesh representation through edge collapse sequences.    | Generic meshes               | Object           | No             | No            | Yes            | Foundation of LOD systems                            | Many implementations                                        | https://dl.acm.org/doi/10.1145/237170.237216                               | Outdated for modern city-scale requirements |
| Neural Mesh Simplification                                                                       | 2022 | Neural                        | Learns simplification operations directly from mesh data.                      | ShapeNet                     | Object           | No             | No            | Yes            | Learning-based simplification                        | https://github.com/martinnormark/neural-mesh-simplification | https://openaccess.thecvf.com/content/CVPR2022                             | Not scalable to city meshes                 |
| Feature-Preserving 3D Mesh Simplification for Urban Buildings                                    | 2021 | Feature-Preserving            | Preserves planar structures and architectural edges during simplification.     | Building datasets            | Building         | No             | No            | No             | Urban feature preservation                           | -                                                           | https://www.sciencedirect.com/science/article/abs/pii/S092427162100006X    | No semantic awareness                       |
| Designing and Evaluating a Mesh Simplification Algorithm for Virtual Reality                     | 2018 | AR/VR                         | Studies perceptual effects of mesh simplification in VR.                       | VR scene datasets            | Scene            | No             | Partial       | No             | VR-oriented evaluation                               | -                                                           | https://dl.acm.org/doi/10.1145/3213512.3213529                             | Limited modern relevance                    |
| Semantic-aware Multi-Scale Simplification of Urban-Scale 3D Real-Scene Mesh Models               | 2025 | Semantic-Aware                | Uses semantic importance to guide urban mesh simplification.                   | Urban city meshes            | City Scale       | Yes            | Partial       | No             | Directly relevant city-scale semantic simplification | -                                                           | https://isprs-archives.copernicus.org/articles/XLVIII-4-W14-2025/333/2025/ | Limited reproducibility                     |
| Feature-Preserving Mesh Decimation for Normal Integration                                        | 2025 | Feature-Preserving            | Preserves geometric details during decimation.                                 | Reconstruction meshes        | Object           | No             | No            | Yes            | Feature-aware simplification                         | https://moritzheep.github.io/anisotropic-decimation/        | https://arxiv.org                                                          | Not urban-focused                           |
| Simplifying Textured Triangle Meshes in the Wild                                                 | 2025 | Texture-Aware                 | Preserves texture quality during simplification.                               | Real-world textured meshes   | Scene            | No             | Yes           | Coming Soon    | Texture-aware simplification                         | -                                                           | https://arxiv.org                                                          | Not city-scale                              |
| A Structure-Aware Triangular Mesh Simplification Based on GNN-Guided QEM                         | 2026 | Neural + QEM                  | Uses graph neural networks to guide QEM simplification.                        | Standard benchmarks          | Object           | No             | No            | Unknown        | Structure-aware simplification                       | -                                                           | https://www.preprints.org/manuscript/202604.1809                           | No urban validation                         |
| Structure- and Semantics-Aware Mesh Simplification for Generating Lightweight 3D Building Models | 2026 | Semantic-Aware                | Joint semantic and structural constraints during simplification.               | SUM, STPLS3D, ArCH           | Building / Urban | Yes            | No            | Unknown        | Strong semantic preservation                         | -                                                           | https://www.mdpi.com/2072-4292/18/6/914                                    | Mostly building-scale                       |
| Fast and Robust Mesh Simplification for Generated and Real-World 3D Assets (FA-QEM)              | 2026 | Feature-Preserving            | Modernized QEM with feature awareness and curvature constraints.               | Thingi10K, Real-World Assets | Large Meshes     | No             | Partial       | Not Yet        | State-of-the-art QEM variant                         | -                                                           | https://arxiv.org/abs/2605.14029                                           | Not urban-focused                           |
| Semantic Segmentation of Textured Non-Manifold 3D Meshes Using Transformers                      | 2026 | Segmentation                  | Transformer-based semantic segmentation on textured meshes.                    | SUM                          | Urban Scale      | Yes            | Yes           | Unknown        | Texture-aware semantic understanding                 | -                                                           | https://arxiv.org/abs/2604.01836                                           | Segmentation only                           |
| PSSNet: Planarity-Sensible Semantic Segmentation of Large-Scale Urban Meshes                     | 2022 | Segmentation                  | Semantic segmentation of urban meshes using graph neural networks.             | SUM Benchmark                | Urban Scale      | Yes            | Yes           | Yes            | Urban mesh semantic understanding                    | https://github.com/WeixiaoGao/PSSNet                        | https://arxiv.org/abs/2202.03209                                           | Segmentation only                           |
| Building LOD Representation for 3D Urban Scenes                                                  | 2025 | LOD                           | Structure-aware LOD hierarchy generation for urban scenes.                     | 21 Urban Datasets            | Urban Scale      | Yes            | Partial       | No             | Urban LOD-Tree representation                        | -                                                           | https://www.sciencedirect.com/science/article/abs/pii/S0924271625001625    | Not simplification-focused                  |
| Efficient Four-Level LOD Simplification for Single- and Multi-Building Models                    | 2026 | LOD                           | Multi-resolution hierarchy generation for urban models.                        | Building datasets            | Building / Urban | Partial        | No            | Unknown        | Practical LOD generation                             | -                                                           | https://www.mdpi.com/2220-9964/15/2/61                                     | Limited semantic usage                      |
| Balancing Semantic and Geometric Lightweighting for Building Models                              | 2026 | Semantic-Aware / LOD          | Studies trade-offs between semantic preservation and geometric simplification. | BIM / GIS datasets           | Building / Urban | Yes            | No            | Unknown        | Semantic-geometric optimization                      | -                                                           | https://www.sciencedirect.com/science/article/abs/pii/S0926580526002633    | Building-centric                            |
| City-Mesh3R: Simulation-Ready City-Scale 3D Mesh Reconstruction from Multi-View Images           | 2026 | City Reconstruction           | Large-scale city reconstruction with adaptive remeshing.                       | City-scale datasets          | City Scale       | Partial        | Partial       | Unknown        | Simulation-ready city meshes                         | -                                                           | https://arxiv.org/abs/2605.30310                                           | Not simplification-focused                  |
| GS4City: Hierarchical Semantic Gaussian Splatting via City-Model Priors                          | 2026 | Semantic Urban Representation | Uses semantic city priors for large-scale urban scene representation.          | TUM2TWIN, Gold Coast         | City Scale       | Yes            | Yes           | Yes            | Hierarchical semantic representation                 | Yes                                                         | https://arxiv.org/abs/2604.11401                                           | Not mesh simplification                     |

---

# Literature Map

```text
City Mesh Processing
│
├── Classical Simplification
│   ├── QEM
│   └── Progressive Meshes
│
├── Feature-Preserving
│   ├── Urban Buildings
│   ├── FA-QEM
│   └── Normal Integration
│
├── Semantic-Aware
│   ├── Semantic-aware Multi-Scale Simplification
│   ├── Structure- and Semantics-Aware Simplification
│   └── Semantic-Geometric Lightweighting
│
├── Neural
│   ├── Neural Mesh Simplification
│   └── GNN-Guided QEM
│
├── Semantic Understanding
│   ├── PSSNet
│   └── Transformer Mesh Segmentation
│
├── LOD Generation
│   ├── Progressive Meshes
│   ├── Urban LOD-Tree
│   └── Four-Level LOD
│
├── AR/VR Evaluation
│   └── VR Simplification Evaluation
│
└── City-Scale Reconstruction
    ├── City-Mesh3R
    └── GS4City
```

---
# Potential Directions

Semantic-Aware Feature-Preserving Adaptive LOD Generation for Large-Scale Urban Meshes in AR/VR

Pipeline:

Urban Mesh
→ Semantic Segmentation
→ Feature Detection
→ Importance Scoring
→ Adaptive Simplification
→ Multi-Level LOD Generation
→ AR/VR Rendering

---


# Next Action Items

1. Collect PDFs for all papers.
2. Add citation count.
3. Add benchmark datasets used.
4. Add evaluation metrics.
5. Add runtime and scalability information.
6. Build comparison matrix.
7. Reproduce one baseline (QEM or FA-QEM).
8. Obtain one city-scale dataset.
9. Benchmark current methods.
10. Identify the first real bottleneck before proposing a novel method.

# Mesh Decimation / Simplification for Large City Meshes in AR/VR

## Literature Review Tracker

---

# Paper Categories

| Category            | Description                                      |
| ------------------- | ------------------------------------------------ |
| Classical           | Traditional mesh simplification algorithms       |
| Feature-Preserving  | Preserve geometric structures and sharp features |
| Semantic-Aware      | Use semantic labels to guide simplification      |
| Neural              | Learning-based simplification methods            |
| Segmentation        | Semantic understanding of urban meshes           |
| LOD                 | Multi-resolution and level-of-detail generation  |
| AR/VR               | Rendering and perceptual evaluation              |
| City Reconstruction | Large-scale urban mesh generation                |

---

# Literature Database

| Publication | Year | Category | Expanded Summary | Exact Dataset Used | Scale | Semantic Aware | Texture Aware | Code Available | Key Contribution | Code Link | Paper link | Detailed Limitations |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Surface Simplification Using Quadric Error Metrics (QEM)** | 1997 | Classical | Introduces an iterative vertex contraction algorithm that maintains geometric fidelity by tracking the squared distance from a vertex to the planes of its adjacent triangles via Quadric Error Metrics. | Stanford Bunny, Cow, standard graphics primitives | Object | No | No | Yes | Foundation of most modern simplification algorithms | Native in VTK, CGAL, MeshLab | [Link](https://www.cs.cmu.edu/~garland/Papers/quadrics.pdf) | Ignores textures, semantics, and topological constraints. Tends to oversimplify highly detailed flat regions and struggles with non-manifold edges unless curvature heuristics are added. |
| **Progressive Meshes** | 1996 | Classical / LOD | Proposes a continuous resolution representation of a mesh, allowing for smooth, geomorphing transitions between different levels of detail (LOD) via a sequential stream of edge collapse and vertex split operations. | Stanford Bunny, Cessna, generic synthetic meshes | Object | No | No | Yes | Foundation of continuous LOD streaming systems | Native in DirectX / Game Engines | [Link](https://dl.acm.org/doi/10.1145/237170.237216) | High memory overhead for storing the entire sequence of vertex splits. Lacks semantic awareness and does not natively support modern out-of-core streaming for massive city scales. |
| **Neural Mesh Simplification** | 2022 | Neural | Bypasses traditional edge collapses by learning to predict simplified meshes directly. Uses vertex sampling and candidate face classification via neural networks to maintain visual appearance. | ShapeNet, CoMA, HuggingFace 3D Meshes | Object | No | No | Yes | Learning-based, single-pass mesh simplification | [GitHub](https://github.com/martinnormark/neural-mesh-simplification) | [Link](https://openaccess.thecvf.com/content/CVPR2022) | Generates new topologies rather than strict decimation, altering boundary conditions. Memory-intensive during point-sampling, making it non-scalable to massive urban extents. |
| **Feature-Preserving 3D Mesh Simplification for Urban Buildings** | 2021 | Feature-Preserving | Extracts piecewise planar regions and crease contours to constrain a modified QEM process. Uses regional structural constraints for planar areas and local geometric error metrics for non-planar ones. | Custom photogrammetry meshes of commercial & residential building facades | Building | No | No | No | Urban-specific planar feature preservation | - | [Link](https://www.sciencedirect.com/science/article/abs/pii/S092427162100006X) | Heavily relies on the assumption of piecewise planarity. Struggles significantly with curved architectural elements, organic urban structures (trees), and lacks high-level semantic differentiation. |
| **Designing and Evaluating a Mesh Simplification Algorithm for Virtual Reality** | 2018 | AR/VR | Evaluates the visual perception and performance trade-offs of mesh decimation in immersive VR environments. Explores how aggressive LOD reductions impact user presence, frame rates, and visual fidelity. | Custom synthetic VR scene datasets | Scene | No | Partial | No | VR-oriented perceptual evaluation | - | [Link](https://dl.acm.org/doi/10.1145/3213512.3213529) | Focuses solely on perception and rendering pipelines rather than novel simplification algorithms. Evaluation is constrained to older VR hardware and small-scale scene objects. |
| **Semantic-aware Multi-Scale Simplification of Urban-Scale 3D Real-Scene Mesh Models** | 2025 | Semantic-Aware | Integrates semantic segmentation labels directly into the simplification cost function. Ensures critical urban elements (e.g., windows, facades) are preserved at higher resolutions than ground clutter across multi-scale hierarchies. | SUM (SensatUrban), custom UAV photogrammetry meshes | City Scale | Yes | Partial | No | Directly relevant city-scale semantic simplification | - | [Link](https://isprs-archives.copernicus.org/articles/XLVIII-4-W14-2025/333/2025/) | Simplification quality is heavily bottlenecked by the accuracy of the initial semantic segmentation. Multi-scale hierarchy generation requires massive memory for city-scale extents. |
| **Feature-Preserving Mesh Decimation for Normal Integration** | 2025 | Feature-Preserving | Focuses on preserving geometric details like sharp creases by optimizing for normal integration during decimation. Reduces triangle count while maintaining faithful surface normals critical for lighting. | Standard surface reconstruction benchmark meshes | Object | No | No | Yes | Normal and lighting-aware feature preservation | [GitHub](https://moritzheep.github.io/anisotropic-decimation/) | [Link](https://arxiv.org) | Designed primarily for object-level normal integration and lighting preservation. Not optimized for the specific architectural constraints, semantic needs, or massive scale of urban meshes. |
| **Simplifying Textured Triangle Meshes in the Wild** | 2025 | Texture-Aware | Addresses texture mapping degradation during extreme geometry simplification. Optimizes UV coordinates and texture atlases jointly with edge collapses to prevent texture stretching on real-world scans. | Real-world textured meshes, 3D photogrammetry scans | Scene | No | Yes | Coming Soon | Joint texture and geometry simplification | - | [Link](https://arxiv.org) | Prioritizes texture and UV preservation over geometric or semantic structure. Does not natively address out-of-core memory management required for multi-tile city datasets. |
| **A Structure-Aware Triangular Mesh Simplification Based on GNN-Guided QEM** | 2026 | Neural + QEM | Replaces heuristic geometric feature detection with a Graph Neural Network (GNN) to predict edge collapse costs. The GNN embeddings guide QEM, learning complex structural priors automatically. | Thingi10K, ShapeNet | Object | No | No | Unknown | Neural-guided classical decimation | - | [Link](https://www.preprints.org/manuscript/202604.1809) | Inference overhead of GNNs makes it computationally prohibitive for massive meshes with millions of polygons. Completely lacks architectural or semantic priors for urban environments. |
| **Structure- and Semantics-Aware Mesh Simplification for Generating Lightweight 3D Building Models** | 2026 | Semantic-Aware | Implements a dual-constraint edge-collapse method incorporating both geometric saliency (normal inconsistency) and semantic structural lines (projected from point clouds) to preserve architectural topology. | Sketchfab, ArCH, STPLS3D, SUM | Building / Urban | Yes | No | Unknown | Strong architectural semantic preservation | - | [Link](https://www.mdpi.com/2072-4292/18/6/914) | Validation is predominantly isolated to individual building models or highly localized urban clusters, rather than addressing the continuous, sprawling nature of city-wide meshes. |
| **Fast and Robust Mesh Simplification for Generated and Real-World 3D Assets (FA-QEM)** | 2026 | Feature-Preserving | A highly optimized, modernized variant of QEM that explicitly integrates feature awareness and boundary preservation. Designed to handle noisy scans and generated 3D assets with non-manifold artifacts. | Thingi10K, Real-World Assets | Large Meshes | No | Partial | Not Yet | State-of-the-art QEM variant for messy geometry | - | [Link](https://arxiv.org/abs/2605.14029) | A general-purpose tool that lacks the semantic awareness required to differentiate between important urban features (e.g., roads vs. structures) during aggressive decimation. |
| **Semantic Segmentation of Textured Non-Manifold 3D Meshes Using Transformers** | 2026 | Segmentation | Applies Transformer architectures directly to textured, non-manifold 3D meshes for semantic segmentation. Uses geometric and texture features to accurately label complex urban components. | SUM (SensatUrban) benchmark | Urban Scale | Yes | Yes | Unknown | Texture-aware neural mesh segmentation | - | [Link](https://arxiv.org/abs/2604.01836) | This is purely a segmentation method. It solves the semantic labeling problem but does not propose or implement a pipeline for actually decimating the geometry based on those labels. |
| **PSSNet: Planarity-Sensible Semantic Segmentation of Large-Scale Urban Meshes** | 2022 | Segmentation | A graph neural network designed to segment large-scale urban meshes using planarity priors. Groups faces into super-faces to improve the segmentation of facades, roofs, and ground. | SUM (SensatUrban) benchmark | Urban Scale | Yes | Yes | Yes | Urban mesh semantic understanding via planarity | [GitHub](https://github.com/WeixiaoGao/PSSNet) | [Link](https://arxiv.org/abs/2202.03209) | Provides only semantic labels and structural groupings. The architecture does not contain a mesh decimation, simplification, or level-of-detail (LOD) generation phase. |
| **Building LOD Representation for 3D Urban Scenes** | 2025 | LOD | Generates Level of Detail (LOD) hierarchies specifically for urban scenes. Simplifies building geometry into bounding boxes or stylized primitives at lowest LODs while maintaining street legibility. | 21 Urban Datasets (BIM and GIS sources) | Urban Scale | Yes | Partial | No | Urban LOD-Tree representation | - | [Link](https://www.sciencedirect.com/science/article/abs/pii/S0924271625001625) | Focuses on discrete LOD generation and bounding-volume abstraction rather than continuous mesh decimation, which can lead to severe popping artifacts in AR/VR applications. |
| **Efficient Four-Level LOD Simplification for Single- and Multi-Building Models** | 2026 | LOD | Proposes a practical framework for generating four distinct, discrete LODs for building models. Optimizes processing time to allow rapid conversion of high-poly models into standard LOD specs. | BIM and photogrammetry building datasets | Building / Urban | Partial | No | Unknown | Fast, standardized LOD generation | - | [Link](https://www.mdpi.com/2220-9964/15/2/61) | Confined strictly to four static LOD levels. Does not provide the continuous, fine-grained resolution streaming necessary for optimal performance in high-end AR/VR environments. |
| **Balancing Semantic and Geometric Lightweighting for Building Models** | 2026 | Semantic-Aware / LOD | Investigates optimization trade-offs between retaining critical semantic structures and achieving aggressive geometric lightweighting. Proposes a balanced cost function to prevent destruction of labeled components. | BIM / GIS building datasets | Building / Urban | Yes | No | Unknown | Semantic-geometric optimization function | - | [Link](https://www.sciencedirect.com/science/article/abs/pii/S0926580526002633) | Highly building-centric. Evaluates individual, isolated structures rather than addressing the topological challenges of continuous, merged city-scale photogrammetry meshes. |
| **City-Mesh3R: Simulation-Ready City-Scale 3D Mesh Reconstruction from Multi-View Images** | 2026 | City Reconstruction | An end-to-end pipeline for reconstructing massive city-scale meshes from multi-view imagery. Includes adaptive remeshing to ensure the final output is watertight, manifold, and simulation-ready. | Proprietary city-scale aerial multi-view image datasets | City Scale | Partial | Partial | Unknown | Simulation-ready, watertight city meshes | - | [Link](https://arxiv.org/abs/2605.30310) | Primarily a reconstruction and topology-healing pipeline. The resulting watertight meshes may still possess polygon counts too dense for direct mobile AR/VR rendering. |
| **GS4City: Hierarchical Semantic Gaussian Splatting via City-Model Priors** | 2026 | Semantic Urban Rep. | Utilizes semantic city priors to guide 3D Gaussian Splatting for urban scenes. Achieves hierarchical representation and real-time rendering of massive cityscapes by organizing semantic splats. | TUM2TWIN, Gold Coast datasets | City Scale | Yes | Yes | Yes | Hierarchical semantic representation beyond polygons | Linked in paper | [Link](https://arxiv.org/abs/2604.11401) | Operates entirely on Gaussian Splatting rather than polygonal meshes. This makes it fundamentally incompatible with standard physics engines, collision detection, and traditional AR/VR polygon pipelines. |

---

# Comprehensive Evaluation Data

| Publication | Citation Count | Evaluation Metrics | Runtime & Scalability Info | PDF / Access Status |
| :--- | :--- | :--- | :--- | :--- |
| **Surface Simplification Using QEM** | ~10,000+ | Hausdorff Distance, Error Quadrics | Extremely fast ($\mathcal{O}(n \log n)$) using priority queues. Scales to millions of polygons but struggles with messy non-manifold city scans. | [Available via CMU](https://www.cs.cmu.edu/~garland/Papers/quadrics.pdf) |
| **Progressive Meshes** | ~5,165 | Visual fidelity, Geometric error bounds | Highly efficient for single objects; memory scales linearly with vertex splits. Poor scalability for multi-tile out-of-core city extents. | [Available via ACM](https://dl.acm.org/doi/10.1145/237170.237216) |
| **Neural Mesh Simplification** | ~20 | Chamfer Distance (CD), Normal Loss, Edge Loss | Inference is heavily bottlenecked by dense vertex sampling operations. Strictly limited to object-level geometry. | [Available via CVF](https://openaccess.thecvf.com/content/CVPR2022) |
| **Feature-Preserving 3D Mesh Simplification for Urban Buildings** | ~15 | RMSE, Visual structural fidelity | Scales well for individual buildings but is not mathematically optimized to process continuous multi-tile urban terrain. | [Available via ResearchGate](https://www.researchgate.net/publication/348592284_Feature-preserving_3D_mesh_simplification_for_urban_buildings) |
| **Designing and Evaluating a Mesh Simplification Algorithm for VR** | ~40 | Geometric error, Texture distortion, Render frame rates | Fast offline processing. Specifically benchmarked to guarantee rendering frame-rate stability in VR engines. | [Available via ResearchGate](https://www.researchgate.net/publication/326051604_Designing_and_Evaluating_a_Mesh_Simplification_Algorithm_for_Virtual_Reality) |
| **Semantic-aware Multi-Scale Simplification of Urban-Scale Meshes** | 0 (New) | Face count reduction (23%), Model accuracy improvement (23%) | Processed multi-scale trees require massive system RAM, making it suitable for city sets but extremely slow in the preprocessing phase. | [Available via ISPRS](https://isprs-archives.copernicus.org/articles/XLVIII-4-W14-2025/333/2025/isprs-archives-XLVIII-4-W14-2025-333-2025.pdf) |
| **Feature-Preserving Mesh Decimation for Normal Integration** | 0 (New) | Depth error, Normal deviation (L2 norm) | Operates efficiently locally using basic edge collapse and flips. Achieves 90% compression while maintaining sub-millimeter geometric accuracy. | [Available via CVF](https://openaccess.thecvf.com/content/CVPR2025/papers/Heep_Feature-Preserving_Mesh_Decimation_for_Normal_Integration_CVPR_2025_paper.pdf) |
| **Simplifying Textured Triangle Meshes in the Wild** | 0 (New) | Texture stretching penalty, Geometry distortion | Encounters high computational overhead during the joint optimization of UV coordinates and edge-collapses. | [Available via arXiv](https://arxiv.org) |
| **GNN-Guided QEM** | 0 (New) | Chamfer Distance, Structural preservation score | GNN forward-pass overhead makes it prohibitively slow for massive urban meshes boasting multi-million polygon counts. | [Available via Preprints.org](https://www.preprints.org/manuscript/202604.1809) |
| **Structure- and Semantics-Aware Mesh Simplification for Buildings** | 0 (New) | RMSE, Volume preservation, Structural integrity | Computes heavy dual-constraints (geometric + semantic). Highly accurate at building-scale but computationally intense for whole cities. | [Available via MDPI](https://www.mdpi.com/2072-4292/18/6/914) |
| **Fast and Robust Mesh Simplification (FA-QEM)** | 0 (New) | Hausdorff, Chamfer, Texture Chamfer | Highly scalable. Performs up to 14x faster than modern robust baselines while handling non-manifold artifacts cleanly. | [Available via arXiv](https://arxiv.org/abs/2605.14029) |
| **Semantic Segmentation of Textured Non-Manifold 3D Meshes** | 0 (New) | mF1 (81.9%), OA (94.3%) | Multi-scale transformer architecture requires extreme GPU VRAM to aggregate local/global features across multi-tile meshes. | [Available via arXiv](https://arxiv.org/abs/2604.01836) |
| **PSSNet: Planarity-Sensible Semantic Segmentation** | ~40 | mIoU, Overall Accuracy (OA) | GNN face-grouping reduces raw input complexity, making inference highly scalable for large urban meshes. | [Available via arXiv](https://arxiv.org/abs/2202.03209) |
| **Building LOD Representation for 3D Urban Scenes** | 0 (New) | Visual abstraction error, File size reduction | Generates discrete LOD bounding bounds quickly, but the framework cannot generate smooth continuous terrain meshes. | [Available via ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0924271625001625) |
| **Efficient Four-Level LOD Simplification** | 0 (New) | Processing time, Standard compliance limits | Exceptionally fast standardized hierarchy generation. Scales well linearly as the count of target buildings increases. | [Available via MDPI](https://www.mdpi.com/2220-9964/15/2/61) |
| **Balancing Semantic and Geometric Lightweighting** | 0 (New) | Semantic retention ratio, Geometric RMSE | The iterative semantic-geometric optimization function adds significant computation overhead compared to classical QEM. | [Available via ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0926580526002633) |
| **City-Mesh3R: Simulation-Ready City-Scale Reconstruction** | 0 (New) | Watertightness, Manifold accuracy, Simulation frame rate | As a massive end-to-end multi-view pipeline, it requires dedicated high-performance cluster computing to process entire cities. | [Available via arXiv](https://arxiv.org/abs/2605.30310) |
| **GS4City: Hierarchical Semantic Gaussian Splatting** | 0 (New) | coarse IoU (+15.8 boost), mIoU (+14.2 boost) | Capable of rendering massive cityscapes in real-time. Highly scalable due to reliance on semantic splat LOD hierarchies rather than polygons. | [Available via arXiv](https://arxiv.org/abs/2604.11401) |

---

# Methodological Comparison Matrix

| Method | Primary Approach | Geometry Topology | Texture Handling | Semantic Handling | Target Scale | AR/VR Engine Suitability |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Vanilla QEM** | Cost-based Edge Collapse | Manifold required | None | None | Single Asset | High (Offline) |
| **Progressive Meshes** | Vertex Split / Collapse Stream | Manifold required | None | None | Single Asset | Medium |
| **Neural Mesh** | Vertex Generation / Sampling | Generates new topologies | None | None | Object | Low |
| **Feature-Preserving Urban** | Planar Region Constraints | Agnostic | None | Structural only | Building | Medium |
| **VR Simplification Eval.** | Curvature-guided Collapse | Agnostic | Partial | None | Scene | High |
| **Semantic Multi-Scale** | Hierarchical Semantic Cost | Strict LOD Trees | Partial | Explicit labels (4 classes) | City Scale | Medium (Memory heavy) |
| **Normal Integration** | Anisotropic Decimation | Agnostic | None | None | Object / Scene | Medium |
| **Wild Textured Meshes** | Joint UV/Geometry Collapse | Agnostic | Native | None | Scene | High |
| **GNN-Guided QEM** | Neural Edge Collapse Cost | Agnostic | None | Neural Structural Priors | Object | Low (Inference overhead) |
| **Structure & Semantics** | Dual-Constraint Collapse | Preserves Architecture | None | Geometric + Component | Building | High |
| **FA-QEM** | Feature-Aware QEM | Handles Non-Manifold | Successive Mapping | None | Large Assets | Very High (Real-time bounds) |
| **Transformer Mesh Seg.** | Multi-Scale Transformer | Non-Manifold capable | Native | Explicit Labels | Urban Scale | Medium (Segmentation only) |
| **PSSNet** | Graph Neural Network | Agnostic | Yes | Explicit Labels | Urban Scale | Medium (Segmentation only) |
| **Building Urban LOD** | Bounding Box Abstraction | Discrete LODs | Partial | Building-level only | Urban Scale | Low (Popping artifacts) |
| **Four-Level LOD** | Pre-defined Hierarchy limits | Discrete LODs | None | None | Building / Urban | Low (Lacks continuous stream) |
| **Balancing Semantics** | Optimization Cost Function | Agnostic | None | Semantic-Weighted | Building | Medium |
| **City-Mesh3R** | Multi-View Remeshing | Enforces Watertightness | Partial | None | City Scale | Medium (Mesh sizes too large) |
| **GS4City** | Gaussian Splatting | Point-Based (No Polygons) | Native (Radiance) | CityGML LoD Priors | City Scale | Low/Medium (Depends on Engine) |

---

# Literature Map

```text
City Mesh Processing
│
├── Classical Simplification
│   ├── QEM
│   └── Progressive Meshes
│
├── Feature-Preserving
│   ├── Urban Buildings
│   ├── FA-QEM
│   └── Normal Integration
│
├── Semantic-Aware
│   ├── Semantic-aware Multi-Scale Simplification
│   ├── Structure- and Semantics-Aware Simplification
│   └── Semantic-Geometric Lightweighting
│
├── Neural
│   ├── Neural Mesh Simplification
│   └── GNN-Guided QEM
│
├── Semantic Understanding
│   ├── PSSNet
│   └── Transformer Mesh Segmentation
│
├── LOD Generation
│   ├── Progressive Meshes
│   ├── Urban LOD-Tree
│   └── Four-Level LOD
│
├── AR/VR Evaluation
│   └── VR Simplification Evaluation
│
└── City-Scale Reconstruction
    ├── City-Mesh3R
    └── GS4City
```



# Mesh Decimation / Simplification for Large City Meshes in AR/VR

## Literature Review Tracker

---

# Paper Categories

| Category            | Description                                      |
| ------------------- | ------------------------------------------------ |
| Classical           | Traditional mesh simplification algorithms       |
| Feature-Preserving  | Preserve geometric structures and sharp features |
| Semantic-Aware      | Use semantic labels to guide simplification      |
| Neural              | Learning-based simplification methods            |
| Segmentation        | Semantic understanding of urban meshes           |
| Dataset             | Benchmark and validation datasets                |
| LOD                 | Multi-resolution and level-of-detail generation  |
| AR/VR               | Rendering and perceptual evaluation              |
| City Reconstruction | Large-scale urban mesh generation                |

---

# Literature Database

| Publication | Year | Category | Expanded Summary | Exact Dataset Used | Scale | Semantic Aware | Texture Aware | Code Available | Key Contribution | Code Link | Paper link | Detailed Limitations |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Surface Simplification Using Quadric Error Metrics (QEM)** | 1997 | Classical | Introduces an iterative vertex contraction algorithm that maintains geometric fidelity by tracking the squared distance from a vertex to the planes of its adjacent triangles via Quadric Error Metrics. | Stanford Bunny, Cow, standard graphics primitives | Object | No | No | Yes | Foundation of most modern simplification algorithms | Native in VTK, CGAL, MeshLab | [Link](https://www.cs.cmu.edu/~garland/Papers/quadrics.pdf) | Ignores textures, semantics, and topological constraints. Tends to oversimplify highly detailed flat regions and struggles with non-manifold edges. |
| **Progressive Meshes** | 1996 | Classical / LOD | Proposes a continuous resolution representation of a mesh, allowing for smooth transitions between different levels of detail (LOD) via a sequential stream of edge collapse and vertex split operations. | Stanford Bunny, Cessna, generic synthetic meshes | Object | No | No | Yes | Foundation of continuous LOD streaming systems | Native in DirectX / Game Engines | [Link](https://dl.acm.org/doi/10.1145/237170.237216) | High memory overhead for storing the entire sequence of vertex splits. Lacks semantic awareness and does not natively support modern out-of-core streaming for massive city scales. |
| **Relaxed Parallel Priority Queue with Filter Levels for Parallel Mesh Decimation** | 2022 | Classical | Resolves the severe thread contention and mutex locking bottlenecks typically encountered when parallelizing QEM priority queues across Pthreads or multi-core environments by relaxing the requirement to return an element in the top $k$. | Generic synthetic triangle meshes | Object / Scene | No | No | Yes | High-performance parallel priority queue scheduling for multi-threaded decimation | Linked in paper | [Link](https://diglib.eg.org/bitstream/handle/10.2312/vmv20221202/041-048.pdf) | Focuses entirely on the data structure and computational scheduling bottleneck rather than introducing new geometric, semantic, or topological constraints. |
| **Neural Mesh Simplification** | 2022 | Neural | Bypasses traditional edge collapses by learning to predict simplified meshes directly. Uses vertex sampling and candidate face classification via neural networks to maintain visual appearance. | ShapeNet, CoMA, HuggingFace 3D Meshes | Object | No | No | Yes | Learning-based, single-pass mesh simplification | [GitHub](https://github.com/martinnormark/neural-mesh-simplification) | [Link](https://openaccess.thecvf.com/content/CVPR2022) | Generates new topologies rather than strict decimation, altering boundary conditions. Memory-intensive during point-sampling, making it non-scalable to massive urban extents. |
| **Feature-Preserving 3D Mesh Simplification for Urban Buildings** | 2021 | Feature-Preserving | Extracts piecewise planar regions and crease contours to constrain a modified QEM process. Uses regional structural constraints for planar areas and local geometric error metrics for non-planar ones. | Custom photogrammetry meshes of commercial & residential building facades | Building | No | No | No | Urban-specific planar feature preservation | - | [Link](https://www.sciencedirect.com/science/article/abs/pii/S092427162100006X) | Heavily relies on the assumption of piecewise planarity. Struggles significantly with curved architectural elements, organic urban structures (trees), and lacks high-level semantic differentiation. |
| **Saliency Detection for Large Scale Mesh Decimation** | 2023 | Feature-Preserving | Computes multi-scale mesh saliency using fast local surface entropy. Allows technical artists to rapidly generate saliency maps that highlight high-detail areas to guide subsequent decimation loops. | Dense multi-million polygon entertainment / object models | Object / Scene | No | No | Unknown | Ultra-fast multi-scale saliency estimation for large meshes | - | [Link](https://eprints.whiterose.ac.uk/id/eprint/195788/) | Designed as a preprocessing pass to guide standard decimation. Still requires human-in-the-loop artist interaction for optimal results rather than being fully automated. |
| **Designing and Evaluating a Mesh Simplification Algorithm for Virtual Reality** | 2018 | AR/VR | Evaluates the visual perception and performance trade-offs of mesh decimation in immersive VR environments. Explores how aggressive LOD reductions impact user presence, frame rates, and visual fidelity. | Custom synthetic VR scene datasets | Scene | No | Partial | No | VR-oriented perceptual evaluation | - | [Link](https://dl.acm.org/doi/10.1145/3213512.3213529) | Focuses solely on perception and rendering pipelines rather than novel algorithms. Evaluation is constrained to older VR hardware and small-scale scene objects. |
| **SensatUrban: Learning Semantics from Urban-Scale Photogrammetric Point Clouds** | 2022 | Dataset / Segmentation | Introduces a massive 3-billion-point UAV photogrammetry dataset covering 7.6 $km^2$ across three UK cities. Provides fine-grained annotations (13 classes) to evaluate state-of-the-art urban-scale segmentation. | Birmingham, Cambridge, York UAV photogrammetry | City Scale | Yes | Yes | Yes | Foundational benchmark dataset defining extreme class imbalances | [GitHub](https://github.com/QingyongHu/SensatUrban) | [Link](https://arxiv.org/abs/2201.04494) | This is purely a benchmark dataset and evaluation suite. It highlights massive spatial challenges but does not propose a mesh decimation algorithm itself. |
| **Semantic-aware Multi-Scale Simplification of Urban-Scale 3D Real-Scene Mesh Models** | 2025 | Semantic-Aware | Integrates semantic segmentation labels directly into the simplification cost function. Ensures critical urban elements are preserved at higher resolutions than ground clutter across multi-scale hierarchies. | SUM (SensatUrban), custom UAV photogrammetry meshes | City Scale | Yes | Partial | No | Directly relevant city-scale semantic simplification | - | [Link](https://isprs-archives.copernicus.org/articles/XLVIII-4-W14-2025/333/2025/) | Simplification quality is heavily bottlenecked by the accuracy of the initial semantic segmentation. Multi-scale hierarchy generation requires massive memory for city-scale extents. |
| **Feature-Preserving Mesh Decimation for Normal Integration** | 2025 | Feature-Preserving | Focuses on preserving geometric details like sharp creases by optimizing for normal integration during decimation. Reduces triangle count while maintaining faithful surface normals critical for lighting. | Standard surface reconstruction benchmark meshes | Object | No | No | Yes | Normal and lighting-aware feature preservation | [GitHub](https://moritzheep.github.io/anisotropic-decimation/) | [Link](https://arxiv.org) | Designed primarily for object-level normal integration and lighting preservation. Not optimized for the specific architectural constraints, semantic needs, or massive scale of urban meshes. |
| **Simplifying Textured Triangle Meshes in the Wild** | 2025 | Texture-Aware | Addresses texture mapping degradation during extreme geometry simplification. Optimizes UV coordinates and texture atlases jointly with edge collapses to prevent texture stretching on real-world scans. | Real-world textured meshes, 3D photogrammetry scans | Scene | No | Yes | Coming Soon | Joint texture and geometry simplification | - | [Link](https://arxiv.org) | Prioritizes texture and UV preservation over geometric or semantic structure. Does not natively address out-of-core memory management required for multi-tile city datasets. |
| **A Deep Learning-Based Salient Feature-Preserving Algorithm for Mesh Simplification (SFSP-QEM)** | 2025 | Neural + QEM | Uses a high-dimensional embedding network to extract salient feature points. Adjusts the QEM merging costs based on distance to these points, prioritizing the preservation of critical details. | Stanford 3D Scanning Repository, Zigong Lantern | Object / Scene | No | No | Unknown | Deep learning-driven salient feature preservation integrated into QEM | - | [Link](https://www.techscience.com/cmc/v83n2/60527) | Reintroduces neural inference overhead into the classical QEM pipeline. Generalizes well on standard objects but lacks large-scale urban semantic constraints. |
| **A Structure-Aware Triangular Mesh Simplification Based on GNN-Guided QEM** | 2026 | Neural + QEM | Replaces heuristic geometric feature detection with a Graph Neural Network (GNN) to predict edge collapse costs. The GNN embeddings guide QEM, learning complex structural priors automatically. | Thingi10K, ShapeNet | Object | No | No | Unknown | Neural-guided classical decimation | - | [Link](https://www.preprints.org/manuscript/202604.1809) | Inference overhead of GNNs makes it computationally prohibitive for massive meshes with millions of polygons. Completely lacks architectural or semantic priors for urban environments. |
| **Structure- and Semantics-Aware Mesh Simplification for Generating Lightweight 3D Building Models** | 2026 | Semantic-Aware | Implements a dual-constraint edge-collapse method incorporating both geometric saliency (normal inconsistency) and semantic structural lines to preserve architectural topology. | Sketchfab, ArCH, STPLS3D, SUM | Building / Urban | Yes | No | Unknown | Strong architectural semantic preservation | - | [Link](https://www.mdpi.com/2072-4292/18/6/914) | Validation is predominantly isolated to individual building models or highly localized urban clusters, rather than addressing the continuous, sprawling nature of city-wide meshes. |
| **Fast and Robust Mesh Simplification for Generated and Real-World 3D Assets (FA-QEM)** | 2026 | Feature-Preserving | A highly optimized, modernized variant of QEM that explicitly integrates feature awareness and boundary preservation. Designed to handle noisy scans and generated 3D assets with non-manifold artifacts. | Thingi10K, Real-World Assets | Large Meshes | No | Partial | Not Yet | State-of-the-art QEM variant for messy geometry | - | [Link](https://arxiv.org/abs/2605.14029) | A general-purpose tool that lacks the semantic awareness required to differentiate between important urban features (e.g., roads vs. structures) during aggressive decimation. |
| **An Efficient Mesh Decimation and Optimization Method for Large-Scale Engineering 3D Models** | 2026 | Neural / Texture | Utilizes an inverse-rendering-based remeshing technique coupled with a texture enhancement diffusion model. Enhances both the geometric detail and texture resolution of large-scale engineering scans. | Photogrammetry scans, Large-scale CAD models | Large Meshes | No | Yes | Unknown | Joint optimization of remeshing and texture diffusion | - | [Link](https://www.researchgate.net/publication/404918978_An_Efficient_Mesh_Decimation_and_Optimization_Method_for_Large-Scale_Engineering_3D_Models) | Heavy reliance on diffusion models for texture enhancement introduces massive computational cost, making it unsuitable for real-time streaming AR/VR processing pipelines. |
| **Semantic Segmentation of Textured Non-Manifold 3D Meshes Using Transformers** | 2026 | Segmentation | Applies Transformer architectures directly to textured, non-manifold 3D meshes for semantic segmentation. Uses geometric and texture features to accurately label complex urban components. | SUM (SensatUrban) benchmark | Urban Scale | Yes | Yes | Unknown | Texture-aware neural mesh segmentation | - | [Link](https://arxiv.org/abs/2604.01836) | This is purely a segmentation method. It solves the semantic labeling problem but does not propose or implement a pipeline for actually decimating the geometry based on those labels. |
| **PSSNet: Planarity-Sensible Semantic Segmentation of Large-Scale Urban Meshes** | 2022 | Segmentation | A graph neural network designed to segment large-scale urban meshes using planarity priors. Groups faces into super-faces to improve the segmentation of facades, roofs, and ground. | SUM (SensatUrban) benchmark | Urban Scale | Yes | Yes | Yes | Urban mesh semantic understanding via planarity | [GitHub](https://github.com/WeixiaoGao/PSSNet) | [Link](https://arxiv.org/abs/2202.03209) | Provides only semantic labels and structural groupings. The architecture does not contain a mesh decimation, simplification, or level-of-detail (LOD) generation phase. |
| **Building LOD Representation for 3D Urban Scenes** | 2025 | LOD | Generates Level of Detail (LOD) hierarchies specifically for urban scenes. Simplifies building geometry into bounding boxes or stylized primitives at lowest LODs while maintaining street legibility. | 21 Urban Datasets (BIM and GIS sources) | Urban Scale | Yes | Partial | No | Urban LOD-Tree representation | - | [Link](https://www.sciencedirect.com/science/article/abs/pii/S0924271625001625) | Focuses on discrete LOD generation and bounding-volume abstraction rather than continuous mesh decimation, which can lead to severe popping artifacts in AR/VR applications. |
| **Efficient Four-Level LOD Simplification for Single- and Multi-Building Models** | 2026 | LOD | Proposes a practical framework for generating four distinct, discrete LODs for building models. Optimizes processing time to allow rapid conversion of high-poly models into standard LOD specs. | BIM and photogrammetry building datasets | Building / Urban | Partial | No | Unknown | Fast, standardized LOD generation | - | [Link](https://www.mdpi.com/2220-9964/15/2/61) | Confined strictly to four static LOD levels. Does not provide the continuous, fine-grained resolution streaming necessary for optimal performance in high-end AR/VR environments. |
| **Balancing Semantic and Geometric Lightweighting for Building Models** | 2026 | Semantic-Aware / LOD | Investigates optimization trade-offs between retaining critical semantic structures and achieving aggressive geometric lightweighting. Proposes a balanced cost function to prevent destruction of labeled components. | BIM / GIS building datasets | Building / Urban | Yes | No | Unknown | Semantic-geometric optimization function | - | [Link](https://www.sciencedirect.com/science/article/abs/pii/S0926580526002633) | Highly building-centric. Evaluates individual, isolated structures rather than addressing the topological challenges of continuous, merged city-scale photogrammetry meshes. |
| **City-Mesh3R: Simulation-Ready City-Scale 3D Mesh Reconstruction from Multi-View Images** | 2026 | City Reconstruction | An end-to-end pipeline for reconstructing massive city-scale meshes from multi-view imagery. Includes adaptive remeshing to ensure the final output is watertight, manifold, and simulation-ready. | Proprietary city-scale aerial multi-view image datasets | City Scale | Partial | Partial | Unknown | Simulation-ready, watertight city meshes | - | [Link](https://arxiv.org/abs/2605.30310) | Primarily a reconstruction and topology-healing pipeline. The resulting watertight meshes may still possess polygon counts too dense for direct mobile AR/VR rendering. |
| **GS4City: Hierarchical Semantic Gaussian Splatting via City-Model Priors** | 2026 | Semantic Urban Rep. | Utilizes semantic city priors to guide 3D Gaussian Splatting for urban scenes. Achieves hierarchical representation and real-time rendering of massive cityscapes by organizing semantic splats. | TUM2TWIN, Gold Coast datasets | City Scale | Yes | Yes | Yes | Hierarchical semantic representation beyond polygons | Linked in paper | [Link](https://arxiv.org/abs/2604.11401) | Operates entirely on Gaussian Splatting rather than polygonal meshes. This makes it fundamentally incompatible with standard physics engines, collision detection, and traditional AR/VR polygon pipelines. |

---

# Comprehensive Evaluation Data

| Publication | Citation Count | Evaluation Metrics | Runtime & Scalability Info | PDF / Access Status |
| :--- | :--- | :--- | :--- | :--- |
| **Surface Simplification Using QEM** | ~10,000+ | Hausdorff Distance, Error Quadrics | Extremely fast ($\mathcal{O}(n \log n)$) using priority queues. Scales to millions of polygons but struggles with messy non-manifold city scans. | [Available via CMU](https://www.cs.cmu.edu/~garland/Papers/quadrics.pdf) |
| **Progressive Meshes** | ~5,165 | Visual fidelity, Geometric error bounds | Highly efficient for single objects; memory scales linearly with vertex splits. Poor scalability for multi-tile out-of-core city extents. | [Available via ACM](https://dl.acm.org/doi/10.1145/237170.237216) |
| **Relaxed Parallel Priority Queue** | ~5-10 | Runtime, Quadric Error | 2 to 2.6 times faster than naive parallel queues. Effectively resolves the data structure bottleneck in multi-threading. | [Available via Eurographics](https://diglib.eg.org/bitstream/handle/10.2312/vmv20221202/041-048.pdf) |
| **Neural Mesh Simplification** | ~20 | Chamfer Distance (CD), Normal Loss, Edge Loss | Inference is heavily bottlenecked by dense vertex sampling operations. Strictly limited to object-level geometry. | [Available via CVF](https://openaccess.thecvf.com/content/CVPR2022) |
| **Feature-Preserving Simplification for Urban Buildings** | ~15 | RMSE, Visual structural fidelity | Scales well for individual buildings but is not mathematically optimized to process continuous multi-tile urban terrain. | [Available via ResearchGate](https://www.researchgate.net/publication/348592284_Feature-preserving_3D_mesh_simplification_for_urban_buildings) |
| **Saliency Detection for Large Scale Decimation** | ~5-15 | Saliency map accuracy, Processing speedup | Achieves speedups up to three orders of magnitude over prior saliency approaches. Scales efficiently for multi-million vertex meshes. | [Available via White Rose](https://eprints.whiterose.ac.uk/id/eprint/195788/) |
| **Designing and Evaluating VR Mesh Simplification** | ~40 | Geometric error, Texture distortion, Render frame rates | Fast offline processing. Specifically benchmarked to guarantee rendering frame-rate stability in VR engines. | [Available via ResearchGate](https://www.researchgate.net/publication/326051604_Designing_and_Evaluating_a_Mesh_Simplification_Algorithm_for_Virtual_Reality) |
| **SensatUrban (SUM Dataset)** | ~157 | mIoU, Overall Accuracy | Demonstrates extreme class imbalance challenges, processing ~3 billion points over 7.6 $km^2$. Evaluates large-scale algorithm scalability. | [Available via arXiv](https://arxiv.org/abs/2201.04494) |
| **Semantic-aware Multi-Scale Simplification of Urban Meshes** | 0 (New) | Face count reduction (23%), Model accuracy improvement (23%) | Processed multi-scale trees require massive system RAM, making it suitable for city sets but extremely slow in the preprocessing phase. | [Available via ISPRS](https://isprs-archives.copernicus.org/articles/XLVIII-4-W14-2025/333/2025/isprs-archives-XLVIII-4-W14-2025-333-2025.pdf) |
| **Feature-Preserving Mesh Decimation for Normal Integration** | 0 (New) | Depth error, Normal deviation (L2 norm) | Operates efficiently locally using basic edge collapse and flips. Achieves 90% compression while maintaining sub-millimeter geometric accuracy. | [Available via CVF](https://openaccess.thecvf.com/content/CVPR2025/papers/Heep_Feature-Preserving_Mesh_Decimation_for_Normal_Integration_CVPR_2025_paper.pdf) |
| **Simplifying Textured Triangle Meshes in the Wild** | 0 (New) | Texture stretching penalty, Geometry distortion | Encounters high computational overhead during the joint optimization of UV coordinates and edge-collapses. | [Available via arXiv](https://arxiv.org) |
| **SFSP-QEM (Deep Learning Salient Feature-Preserving)** | 0 (New) | Hausdorff distance, Runtime | Running time is only 6% longer than traditional QEM while reducing Hausdorff distance by an average of 46.58%. | [Available via Tech Science](https://www.techscience.com/cmc/v83n2/60527) |
| **GNN-Guided QEM** | 0 (New) | Chamfer Distance, Structural preservation score | GNN forward-pass overhead makes it prohibitively slow for massive urban meshes boasting multi-million polygon counts. | [Available via Preprints.org](https://www.preprints.org/manuscript/202604.1809) |
| **Structure- and Semantics-Aware Mesh Simplification** | 0 (New) | RMSE, Volume preservation, Structural integrity | Computes heavy dual-constraints (geometric + semantic). Highly accurate at building-scale but computationally intense for whole cities. | [Available via MDPI](https://www.mdpi.com/2072-4292/18/6/914) |
| **Fast and Robust Mesh Simplification (FA-QEM)** | 0 (New) | Hausdorff, Chamfer, Texture Chamfer | Highly scalable. Performs up to 14x faster than modern robust baselines while handling non-manifold artifacts cleanly. | [Available via arXiv](https://arxiv.org/abs/2605.14029) |
| **Efficient Decimation for Large-Scale Engineering 3D Models** | 0 (New) | Surface detail resolution, Texture quality | High computational cost due to the inclusion of a texture enhancement diffusion model. Not suitable for rapid AR/VR processing. | [Available via ResearchGate](https://www.researchgate.net/publication/404918978_An_Efficient_Mesh_Decimation_and_Optimization_Method_for_Large-Scale_Engineering_3D_Models) |
| **Semantic Segmentation of Textured Non-Manifold 3D Meshes** | 0 (New) | mF1 (81.9%), OA (94.3%) | Multi-scale transformer architecture requires extreme GPU VRAM to aggregate local/global features across multi-tile meshes. | [Available via arXiv](https://arxiv.org/abs/2604.01836) |
| **PSSNet: Planarity-Sensible Semantic Segmentation** | ~40 | mIoU, Overall Accuracy (OA) | GNN face-grouping reduces raw input complexity, making inference highly scalable for large urban meshes. | [Available via arXiv](https://arxiv.org/abs/2202.03209) |
| **Building LOD Representation for 3D Urban Scenes** | 0 (New) | Visual abstraction error, File size reduction | Generates discrete LOD bounding bounds quickly, but the framework cannot generate smooth continuous terrain meshes. | [Available via ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0924271625001625) |
| **Efficient Four-Level LOD Simplification** | 0 (New) | Processing time, Standard compliance limits | Exceptionally fast standardized hierarchy generation. Scales well linearly as the count of target buildings increases. | [Available via MDPI](https://www.mdpi.com/2220-9964/15/2/61) |
| **Balancing Semantic and Geometric Lightweighting** | 0 (New) | Semantic retention ratio, Geometric RMSE | The iterative semantic-geometric optimization function adds significant computation overhead compared to classical QEM. | [Available via ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0926580526002633) |
| **City-Mesh3R: Simulation-Ready City-Scale Reconstruction** | 0 (New) | Watertightness, Manifold accuracy, Simulation frame rate | As a massive end-to-end multi-view pipeline, it requires dedicated high-performance cluster computing to process entire cities. | [Available via arXiv](https://arxiv.org/abs/2605.30310) |
| **GS4City: Hierarchical Semantic Gaussian Splatting** | 0 (New) | coarse IoU (+15.8 boost), mIoU (+14.2 boost) | Capable of rendering massive cityscapes in real-time. Highly scalable due to reliance on semantic splat LOD hierarchies rather than polygons. | [Available via arXiv](https://arxiv.org/abs/2604.11401) |

---

# Methodological Comparison Matrix

| Method | Primary Approach | Geometry Topology | Texture Handling | Semantic Handling | Target Scale | AR/VR Engine Suitability |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Vanilla QEM** | Cost-based Edge Collapse | Manifold required | None | None | Single Asset | High (Offline) |
| **Progressive Meshes** | Vertex Split / Collapse Stream | Manifold required | None | None | Single Asset | Medium |
| **Relaxed Parallel QEM** | Filter Level Threading | Agnostic | None | None | Large Assets | High (Offline/Fast) |
| **Neural Mesh** | Vertex Generation / Sampling | Generates new topologies | None | None | Object | Low |
| **Feature-Preserving Urban** | Planar Region Constraints | Agnostic | None | Structural only | Building | Medium |
| **Fast Saliency Decimation**| Local Surface Entropy Maps | Agnostic | None | None | Object / Scene | Medium (Artist guided) |
| **VR Simplification Eval.** | Curvature-guided Collapse | Agnostic | Partial | None | Scene | High |
| **SensatUrban (SUM)** | Point Cloud Benchmark | Point-based | Native (RGB) | Explicit Labels | City Scale | N/A (Dataset) |
| **Semantic Multi-Scale** | Hierarchical Semantic Cost | Strict LOD Trees | Partial | Explicit labels (4 classes) | City Scale | Medium (Memory heavy) |
| **Normal Integration** | Anisotropic Decimation | Agnostic | None | None | Object / Scene | Medium |
| **Wild Textured Meshes** | Joint UV/Geometry Collapse | Agnostic | Native | None | Scene | High |
| **SFSP-QEM** | Neural High-Dim Embeddings | Agnostic | None | Saliency Features | Object / Scene | Medium |
| **GNN-Guided QEM** | Neural Edge Collapse Cost | Agnostic | None | Neural Structural Priors | Object | Low (Inference overhead) |
| **Structure & Semantics** | Dual-Constraint Collapse | Preserves Architecture | None | Geometric + Component | Building | High |
| **FA-QEM** | Feature-Aware QEM | Handles Non-Manifold | Successive Mapping | None | Large Assets | Very High (Real-time bounds) |
| **Efficient Eng. 3D** | Remeshing + Diffusion | Generates new topologies | Native (Diffusion) | None | Large Assets | Low (Inference heavy) |
| **Transformer Mesh Seg.** | Multi-Scale Transformer | Non-Manifold capable | Native | Explicit Labels | Urban Scale | Medium (Segmentation only) |
| **PSSNet** | Graph Neural Network | Agnostic | Yes | Explicit Labels | Urban Scale | Medium (Segmentation only) |
| **Building Urban LOD** | Bounding Box Abstraction | Discrete LODs | Partial | Building-level only | Urban Scale | Low (Popping artifacts) |
| **Four-Level LOD** | Pre-defined Hierarchy limits | Discrete LODs | None | None | Building / Urban | Low (Lacks continuous stream) |
| **Balancing Semantics** | Optimization Cost Function | Agnostic | None | Semantic-Weighted | Building | Medium |
| **City-Mesh3R** | Multi-View Remeshing | Enforces Watertightness | Partial | None | City Scale | Medium (Mesh sizes too large) |
| **GS4City** | Gaussian Splatting | Point-Based (No Polygons) | Native (Radiance) | CityGML LoD Priors | City Scale | Low/Medium (Depends on Engine) |

---

# Literature Map

```text
City Mesh Processing
│
├── Classical & Parallel Simplification
│   ├── QEM
│   ├── Progressive Meshes
│   └── Relaxed Parallel Priority Queue
│
├── Datasets & Benchmarks
│   └── SensatUrban (SUM)
│
├── Feature-Preserving & Saliency
│   ├── Urban Buildings
│   ├── FA-QEM
│   ├── Normal Integration
│   └── Saliency Detection for Large Scale Decimation
│
├── Semantic-Aware
│   ├── Semantic-aware Multi-Scale Simplification
│   ├── Structure- and Semantics-Aware Simplification
│   └── Semantic-Geometric Lightweighting
│
├── Neural & Generative
│   ├── Neural Mesh Simplification
│   ├── GNN-Guided QEM
│   ├── SFSP-QEM
│   └── Efficient Mesh Decimation (Diffusion)
│
├── Semantic Understanding
│   ├── PSSNet
│   └── Transformer Mesh Segmentation
│
├── LOD Generation
│   ├── Progressive Meshes
│   ├── Urban LOD-Tree
│   └── Four-Level LOD
│
├── AR/VR Evaluation
│   └── VR Simplification Evaluation
│
└── City-Scale Reconstruction
    ├── City-Mesh3R
    └── GS4City