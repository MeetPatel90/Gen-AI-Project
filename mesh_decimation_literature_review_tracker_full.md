# Mesh Decimation / Simplification for Large City Meshes in AR/VR
## Literature Review Master Tracker

---

# Paper Categories

| Category | Description |
|-----------|-------------|
| Classical | Traditional mesh simplification algorithms |
| Feature-Preserving | Preserve geometric structures and sharp features |
| Semantic-Aware | Use semantic labels to guide simplification |
| Neural | Learning-based simplification methods |
| Segmentation | Semantic understanding of urban meshes |
| LOD | Multi-resolution and level-of-detail generation |
| AR/VR | Rendering and perceptual evaluation |
| City Reconstruction | Large-scale urban mesh generation |

---

# Literature Database

| Publication | Year | Category | Brief Summary | Dataset Used | Scale | Semantic Aware | Texture Aware | Code Available | Key Contribution | Limitations |
|------------|------|----------|---------------|--------------|--------|---------------|--------------|---------------|-----------------|-------------|
| Surface Simplification Using Quadric Error Metrics (QEM) | 1997 | Classical | Foundational mesh simplification algorithm using quadric error metrics. | Generic meshes | Object | No | No | Yes | Foundation of most modern simplification algorithms | No feature or semantic awareness |
| Progressive Meshes | 1996 | Classical / LOD | Introduces progressive mesh representation through edge collapse sequences. | Generic meshes | Object | No | No | Yes | Foundation of LOD systems | Outdated for modern city-scale requirements |
| Neural Mesh Simplification | 2022 | Neural | Learns simplification operations directly from mesh data. | ShapeNet | Object | No | No | Yes | Learning-based simplification | Not scalable to city meshes |
| PSSNet: Planarity-Sensible Semantic Segmentation of Large-Scale Urban Meshes | 2022 | Segmentation | Semantic segmentation of urban meshes using graph neural networks. | SUM Benchmark | Urban Scale | Yes | Yes | Yes | Urban mesh semantic understanding | Segmentation only |
| Feature-Preserving 3D Mesh Simplification for Urban Buildings | 2021 | Feature-Preserving | Preserves planar structures and architectural edges during simplification. | Building datasets | Building | No | No | No | Urban feature preservation | No semantic awareness |
| Designing and Evaluating a Mesh Simplification Algorithm for Virtual Reality | 2018 | AR/VR | Studies perceptual effects of mesh simplification in VR. | VR scene datasets | Scene | No | Partial | No | VR-oriented evaluation | Limited modern relevance |
| Semantic-aware Multi-Scale Simplification of Urban-Scale 3D Real-Scene Mesh Models | 2025 | Semantic-Aware | Uses semantic importance to guide urban mesh simplification. | Urban city meshes | City Scale | Yes | Partial | No | Directly relevant city-scale semantic simplification | Limited reproducibility |
| Feature-Preserving Mesh Decimation for Normal Integration | 2025 | Feature-Preserving | Preserves geometric details during decimation. | Reconstruction meshes | Object | No | No | Yes | Feature-aware simplification | Not urban-focused |
| Simplifying Textured Triangle Meshes in the Wild | 2025 | Texture-Aware | Preserves texture quality during simplification. | Real-world textured meshes | Scene | No | Yes | Coming Soon | Texture-aware simplification | Not city-scale |
| A Structure-Aware Triangular Mesh Simplification Based on GNN-Guided QEM | 2026 | Neural + QEM | Uses graph neural networks to guide QEM simplification. | Standard benchmarks | Object | No | No | Unknown | Structure-aware simplification | No urban validation |
| Structure- and Semantics-Aware Mesh Simplification for Generating Lightweight 3D Building Models | 2026 | Semantic-Aware | Joint semantic and structural constraints during simplification. | SUM, STPLS3D, ArCH | Building / Urban | Yes | No | Unknown | Strong semantic preservation | Mostly building-scale |
| Fast and Robust Mesh Simplification for Generated and Real-World 3D Assets (FA-QEM) | 2026 | Feature-Preserving | Modernized QEM with feature awareness and curvature constraints. | Thingi10K, Real-World Assets | Large Meshes | No | Partial | Not Yet | State-of-the-art QEM variant | Not urban-focused |
| Semantic Segmentation of Textured Non-Manifold 3D Meshes Using Transformers | 2026 | Segmentation | Transformer-based semantic segmentation on textured meshes. | SUM | Urban Scale | Yes | Yes | Unknown | Texture-aware semantic understanding | Segmentation only |
| Building LOD Representation for 3D Urban Scenes | 2025 | LOD | Structure-aware LOD hierarchy generation for urban scenes. | 21 Urban Datasets | Urban Scale | Yes | Partial | No | Urban LOD-Tree representation | Not simplification-focused |
| Efficient Four-Level LOD Simplification for Single- and Multi-Building Models | 2026 | LOD | Multi-resolution hierarchy generation for urban models. | Building datasets | Building / Urban | Partial | No | Unknown | Practical LOD generation | Limited semantic usage |
| Balancing Semantic and Geometric Lightweighting for Building Models | 2026 | Semantic-Aware / LOD | Studies trade-offs between semantic preservation and geometric simplification. | BIM / GIS datasets | Building / Urban | Yes | No | Unknown | Semantic-geometric optimization | Building-centric |
| City-Mesh3R: Simulation-Ready City-Scale 3D Mesh Reconstruction from Multi-View Images | 2026 | City Reconstruction | Large-scale city reconstruction with adaptive remeshing. | City-scale datasets | City Scale | Partial | Partial | Unknown | Simulation-ready city meshes | Not simplification-focused |
| GS4City: Hierarchical Semantic Gaussian Splatting via City-Model Priors | 2026 | Semantic Urban Representation | Uses semantic city priors for large-scale urban scene representation. | TUM2TWIN, Gold Coast | City Scale | Yes | Yes | Yes | Hierarchical semantic representation | Not mesh simplification |

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

# Research Questions

## RQ1
How can semantic information improve mesh simplification decisions in urban environments?

## RQ2
How can important architectural structures be preserved under aggressive decimation?

## RQ3
How should simplification quality be evaluated for AR/VR applications?

## RQ4
How can semantic segmentation and simplification be integrated into a unified pipeline?

## RQ5
How can city-scale meshes containing 100M+ triangles be simplified efficiently?

## RQ6
How can texture quality be preserved alongside geometry?

## RQ7
How should multi-level LOD hierarchies be generated for urban digital twins?

---

# Major Gaps Identified

## Well Studied
- Classical mesh simplification
- QEM variants
- Building-level feature preservation

## Moderately Studied
- Semantic-aware simplification
- Texture-aware simplification
- Neural simplification

## Underexplored
- City-scale semantic-aware simplification
- AR/VR-oriented evaluation
- Semantic-aware LOD generation
- Semantic + texture + geometry preservation
- End-to-end urban streaming pipelines
- Large-scale urban digital twins

---

# Top 10 Papers to Read Deeply

1. Semantic-aware Multi-Scale Simplification of Urban-Scale 3D Real-Scene Mesh Models (2025)
2. Structure- and Semantics-Aware Mesh Simplification for Generating Lightweight 3D Building Models (2026)
3. Building LOD Representation for 3D Urban Scenes (2025)
4. City-Mesh3R (2026)
5. PSSNet (2022)
6. Fast and Robust Mesh Simplification for Generated and Real-World 3D Assets (FA-QEM) (2026)
7. Feature-Preserving 3D Mesh Simplification for Urban Buildings (2021)
8. Neural Mesh Simplification (2022)
9. Progressive Meshes (1996)
10. Surface Simplification Using Quadric Error Metrics (1997)

---

# Potential Thesis Directions

## Option A (Recommended)
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

## Option B
Perceptually Optimized Urban Mesh Simplification for AR/VR

Focus:
- Human perception
- Visual quality
- Frame rate
- Latency

---

## Option C
Semantic-Aware City-Scale Streaming and LOD System

Focus:
- Massive urban meshes
- Streaming
- Runtime LOD selection
- Mobile AR/VR deployment

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
