# Linear Algebra Jeopardy Game with MANIM Visualizations

Our project centers around making abstract linear algebra concepts easier to understand through visualizations. Using MANIM, we created animations that show how different linear transformations like scaling, rotation, reflection, shear, and projection affect vectors and subspaces in 2D and 3D spaces. We explored the concept of eigenspace, eigenvalues, and eigenvectors by visualizing them in a vector space and applying different transformations to understand how they work. Finally, we created visualizations to represent Rank-Nullity Theorem including null space, row/column rank and space. We hope this project helps people understand linear algebra in a more fun and intuitive way!

## Features

- Interactive Jeopardy-style game interface
- MANIM-powered visualizations for linear algebra concepts
- Three main categories:
  - Linear Transformations
  - Eigenvalues and Eigenvectors
  - Null Space and Rank-Nullity Theorem
- Team-based scoring system
- Engaging visual feedback for correct/incorrect answers

## Prerequisites

- Node.js (v14 or higher)
- Python 3.7+
- MANIM (for visualization development)

## Installation

1. Clone the repository:
```bash
git clone [your-repository-url]
cd linalg-quiz-app
```

2. Install Node.js dependencies:
```bash
npm install
```

3. Install Python dependencies (if you want to modify/create visualizations):
```bash
pip install manim
```

## Running the Application

1. Start the development server:
```bash
npm start
```

2. Open [http://localhost:3000](http://localhost:3000) in your browser.

## Project Structure

- `/src` - React application source code
- `/public` - Static assets and index.html
- `/animations` - MANIM animation source files
  - `/linear_transformations` - Linear transformation visualizations
  - `/eigen` - Eigenvalue and eigenvector visualizations
  - `/null_space` - Null space and rank-nullity theorem visualizations

## Technologies:
Frontend Technologies:
- React.js (v19.0.0) – Used for building the user interface and managing application state.
- React Router (v7.4.0) – Handles navigation and routing within the React application.
- CSS3 – Used for styling, including animations, flexbox/grid layouts, and responsive design.

MANIM (Mathematical Animation Engine):
- Python 3.x
- MANIM Library – mathematical visualizations for concepts used.

Development Tools:
- Node.js – runtime environment for running the React application.
- npm – Package manager for managing JavaScript dependencies.

Additional Features:
- Interactive Game Interface: React