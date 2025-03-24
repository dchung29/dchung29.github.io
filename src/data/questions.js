const questions = [
  {
    /* scaling question */
    id: 1,
    prompt: "Let's start simple: What transformation does this visualization represent?",
    visualization: "/videos/ScalingTransformation.mp4",
    options: [
      { text: "Scaling", isCorrect: true },
      { text: "Rotation", isCorrect: false },
      { text: "Shear", isCorrect: false },
      { text: "Reflection", isCorrect: false },
      { text: "Projection", isCorrect: false }
    ]
  },
  {
    /* shear question */
    id: 2,
    prompt: "What transformation does this visualization represent?",
    visualization: "/videos/ShearTransformation.mp4",
    options: [
      { text: "Scaling", isCorrect: false },
      { text: "Rotation", isCorrect: false },
      { text: "Shear", isCorrect: true },
      { text: "Reflection", isCorrect: false },
      { text: "Projection", isCorrect: false }
    ]
  },
  {
    /* rotation question */
    id: 3,
    prompt: "What transformation does this visualization represent?",
    visualization: "/videos/RotationTransformation.mp4",
    options: [
      { text: "Scaling", isCorrect: false },
      { text: "Rotation", isCorrect: true },
      { text: "Shear", isCorrect: false },
      { text: "Reflection", isCorrect: false },
      { text: "Projection", isCorrect: false }
    ]
  },
  {
    /* reflection question */
    id: 4,
    prompt: "What transformation does this visualization represent?",
    visualization: "/videos/ReflectionTransformation.mp4",
    options: [
      { text: "Scaling", isCorrect: false },
      { text: "Rotation", isCorrect: false },
      { text: "Shear", isCorrect: false },
      { text: "Reflection", isCorrect: true },
      { text: "Projection", isCorrect: false }
    ]
  },
  {
    /* projection question */
    id: 5,
    prompt: "What transformation does this visualization represent?",
    visualization: "/videos/ProjectionTransformation.mp4",
    options: [
      { text: "Scaling", isCorrect: false },
      { text: "Rotation", isCorrect: false },
      { text: "Shear", isCorrect: false },
      { text: "Reflection", isCorrect: false },
      { text: "Projection", isCorrect: true }
    ]
  },
  {
    /* basic transformation and invariance question */
    id: 6,
    prompt: "Based on this visualization, which vectors are eigenvectors (given their corresponding linear transformations)?",
    visualization: "/videos/Eigenvectors.mp4",
    options: [
      { text: "Option 1: Vector A & Vector C", isCorrect: false },
      { text: "Option 2: Vector B & Vector C", isCorrect: false },
      { text: "Option 3: Vector B & Vector D", isCorrect: true },
      { text: "Option 4: All Vectors", isCorrect: false },
    ]
  },
  {
    /* Vector Decomposition into Eigenvectors question */
    id: 7,
    prompt: "Which of these statements is true based on the visualization?",
    visualization: "/videos/VectorEigenComponents.mp4",
    options: [
      { text: "Option 1: The sum of the transformed components is different from the transformed vector v", isCorrect: false },
      { text: "Option 2: The linear transformation preserves vector direction", isCorrect: false },
      { text: "Option 3: The transformed eigen-components v_x' and v_y' always sum to the transformed vector v', but only if the transformation is a rotation", isCorrect: false },
      { text: "Option 4: The transformed eigen-components v_x' and v_y' always sum to the transformed corresponding vector v'", isCorrect: true },
      { text: "Option 5: Each transformed eigen-component stays on its original span when the transformation is diagonalizable (possesses a basis of eigenvectors)", isCorrect: true},
    ]
  },
  {
    /* Eigenspace question */
    id: 8,
    prompt: "What does an eigenspace represent?",
    visualization: "/videos/Eigenspace.mp4",
    options: [
      { text: "Option 1: A set of vectors unaffected by the linear transformation", isCorrect: false },
      { text: "Option 2: A set of vectors  that stay on their original span after the linear transformation", isCorrect: true },
      { text: "Option 3: The transformed eigen-components v_x' and v_y' always sum to the transformed vector v', but only if the transformation is a rotation", isCorrect: false },
      { text: "Option 4: All of the above.", isCorrect: false },
    ]
  },
  {
    /* 3D Rotation question */
    id: 9,
    prompt: "What does the vector along the axis of rotation represent?",
    visualization: "/videos/EigenvectorsUnderRotation.mp4",
    options: [
      { text: "A vector that is unaffected by the rotation (transformation)", isCorrect: true },
      { text: "A vector in the null space of the rotation (transformation)", isCorrect: false },
      { text: "A basis vector for the plan of rotation", isCorrect: false },
      { text: "An eigenvector with eigenvalue 1", isCorrect: true },
    ]
  },
  {
    /* Eigendecomposition of a matrix question */
    id: 10,
    prompt: "Eigendecomposition of a matrix: What does the process in this visualization (basis change --> scaling --> basis change back) represent?",
    visualization: "/videos/Eigendecomposition.mp4",
    options: [
      { text: "A random sequence of transformations unrelated to the original matrix M", isCorrect: false },
      { text: "A partial pivoting procedure from row reduction", isCorrect: false },
      { text: "Eigendecomposition: a way to break the original transformation into simpler steps using eigenbasis", isCorrect: true },
      { text: "A method to make all vectors rotate without scaling", isCorrect: false },
    ]
  },
  {
    /* Column Rank vs Row Rank question */
    id: 11,
    prompt: "What does the plane with the collapsed vectors represent in this visualization?",
    visualization: "/videos/NullSpaceVisualization.mp4",
    options: [
      { text: "Column Space", isCorrect: true },
      { text: "Null Space", isCorrect: false },
      { text: "Row Space", isCorrect: false },
      { text: "Arbitrary Coordinate Plane", isCorrect: false },
    ]
  },
  {
    /* Squishifying into Null Space question */
    id: 12,
    prompt: "A 2x3 matrix has 2 linearly independent rows. What can we conclude about its column space and row space?",
    visualization: "/videos/ColumnRowRankVectors.mp4",
    options: [
      { text: "The column space has dimension 3, and the row space has dimension 2.", isCorrect: false },
      { text: "The row space and column space always have the same dimension.", isCorrect: true },
      { text: "The row space has dimension 3, while the column space has dimension 2.", isCorrect: false },
      { text: "None of the above", isCorrect: false },
    ]
  },
  {
    /* Rank-Nullity Theorem question */
    id: 13,
    prompt: "Which of the following correctly describes the Rank-Nullity Theorem?",
    visualization: "/videos/RankNullityTheorem.mp4",
    options: [
      { text: "The sum of the dimensions of the null space and column space of a linear transformation equals the dimension of the domain.", isCorrect: true },
      { text: "The sum of the dimensions of the null space and column space of a linear transformation equals the dimension of the codomain.", isCorrect: false },
      { text: "The sum of the dimensions of the null space and domain equals the dimension of the column space.", isCorrect: false },
      { text: "The dimension of the null space is always greater than the dimension of the column space.", isCorrect: false },
    ]
  },
  {
    /* Column Space Representation question */
    id: 14,
    prompt: "What does the plane with the collapsed vectors represent in this visualization?",
    visualization: "/videos/NullSpaceVisualization.mp4",
    options: [
      { text: "Column Space", isCorrect: true },
      { text: "Null Space", isCorrect: false },
      { text: "Row Space", isCorrect: false },
      { text: "Arbitrary Coordinate Plane", isCorrect: false },
    ]
  },
  {
    /* Rank representation question */
    id: 15,
    prompt: "What does the fact that both the column space and row space form planes suggest about the rank of the matrix?",
    visualization: "/videos/NullSpaceVisualization.mp4",
    options: [
      { text: "The rank is 3 because the column space and row space span 3D space.", isCorrect: false },
      { text: "The rank is 1 because both spaces are one-dimensional.", isCorrect: false },
      { text: "The rank is 2 because both spaces are two-dimensional subspaces of 3D space.", isCorrect: true },
      { text: "The rank is 0 because the column and row spaces are both empty.", isCorrect: false },
    ]
  },
];

export default questions;
