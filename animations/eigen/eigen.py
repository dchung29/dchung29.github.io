from manim import *
import numpy as np

config.frame_width = 18
config.frame_height = 10
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 60


#######################################################################################
# Question 1: Basic Transformation and Invariance 
# "In linear algebra, an eigenvector or characteristic vector is a vector that has its direction unchanged (or reversed) by a given linear transformation."
# "A linear transformation's eigenvectors are those vectors that are only stretched or shrunk, with neither rotation or shear. The corresponding eigenvalue is the factor by whihc an eigenvector is stretched or shrunk. If the eigenvalue is negative, the eigenvector's direction is reversed."
# https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors

# Question: Based on this visualization, which vectors are eigenvectors (given their corresponding linear transformations)?
# Answer: Vector B & Vector D
# Other Options
# Vector A & Vector C
# Vector C & Vector B
# All Vectors
#######################################################################################

class Eigenvectors(Scene):
    def construct(self):
        # axes
        axes = Axes(
            x_range=[-6, 6, 1],
            y_range=[-5, 5, 1],
            x_length=10,
            y_length=8,
            tips=True
        )
        self.play(Create(axes))
        self.wait(1)

        # Introducing vector A
        vector_A = Vector([1, 1], color=ORANGE)
        vector_A.shift(axes.coords_to_point(0, 0))
        label_A = Text("Vector A", font_size=24, color=ORANGE).next_to(vector_A.get_end(), UP)
        self.play(Create(vector_A), Write(label_A))

        # Matrices M_1 and M_2 (linear transformation)
        M1_text = Text(
            "Transformation M_1 =\n"
            "⎡ 2   0 ⎤\n"
            "⎣ 0   ½ ⎦",
            font_size=40, color=ORANGE
        )

        M1_text.to_edge(UL)

        M2_text = Text(
            "Transformation M_2 =\n"
            "⎡ -2   0 ⎤\n"
            "⎣  0   ½ ⎦",
            font_size=40, color=PURPLE
        )
        M2_text.to_edge(UL)

        # Apply transformation A = [[2, 0], [0, 0.5]] to Vector A slowly.
        self.play(Write(M1_text))
        self.wait(1)
        A = [[2, 0], [0, 0.5]]
        self.play(ApplyMatrix(A, vector_A, run_time=3))
        self.wait(1)

        # Introducing vector B (eigenvector)

        vector_B = Vector([2, 0], color=GREEN)
        vector_B.shift(axes.coords_to_point(0, 0))
        label_B = Text("Vector B", font_size=24, color=GREEN).next_to(vector_B.get_end(), DOWN)
        self.play(Create(vector_B), Write(label_B))

        # Apply A to Vector B slowly.
        # Since B is along the x-axis, it is an eigenvector for A.
        self.play(FadeOut(M1_text))
        M1_text = Text(
            "Transformation M_1 =\n"
            "⎡ 2   0⎤\n"
            "⎣ 0   ½⎦",
            font_size=40, color=GREEN
        )
        M1_text.to_edge(UL)
        self.play(Write(M1_text))
        self.wait(1)
        self.play(ApplyMatrix(A, vector_B, run_time=3))
        self.wait(1)

        # Introducing vector C
        vector_C = Vector([1, 2], color=RED)
        vector_C.shift(axes.coords_to_point(0, 0))
        label_C = Text("Vector C", font_size=24, color=RED).next_to(vector_C.get_end(), UP)
        self.play(Create(vector_C), Write(label_C))

        # Apply A to Vector C slowly.
        self.play(FadeOut(M1_text))
        M1_text = Text(
            "Transformation M_1 =\n"
            "⎡ 2   0 ⎤\n"
            "⎣ 0   ½ ⎦",
            font_size=40, color=RED
        )
        M1_text.to_edge(UL)
        self.play(Write(M1_text))
        self.wait(1)
        self.play(ApplyMatrix(A, vector_C, run_time=3))
        self.wait(1)
        self.play(FadeOut(M1_text))
        self.wait(1)

        # Introducing vector D (also eigenvector)
        vector_D = Vector([3, 0], color=PURPLE)
        vector_D.shift(axes.coords_to_point(0, 0))
        label_D = Text("Vector D", font_size=24, color=PURPLE).next_to(vector_D.get_end(), UP)
        self.play(Create(vector_D), Write(label_D))

        # modified transformation B = [[-2, 0], [0, 0.5]] (reverses the direction of vectors along the x-axis.)
        self.play(Transform(M1_text, M2_text))
        self.wait(1)
        B = [[-2, 0], [0, 0.5]]
        self.play(FadeOut(label_D))
        self.play(ApplyMatrix(B, vector_D, run_time=3))
        self.wait(1)
        label_D = Text("Vector D", font_size=24, color=PURPLE).next_to(vector_D.get_end(), UP)
        self.play(Write(label_D))
        self.wait(1)
        self.play(FadeOut(M2_text))
        self.wait(1)

        eigenvector_explanation = Text(
            "An eigenvector of a linear transformation T is a vector\n"
            "that remains on its span (only scaled, not rotated) by T.\n\n"
            "Based on this visualization, which vectors are eigenvectors\n"
            "(given their corresponding linear transformations)?",
            font_size=24,
            color="#fb8535"
        )
        eigenvector_explanation.to_edge(DL)
        self.play(Write(eigenvector_explanation))
        self.wait(4)


#######################################################################################
# Question 2: Matrix Symmetry and Orthogonal Eigenvectors
# “If A is symmetric, then any two eigenvectors from different eigenspaces are orthogonal” [textbook]. Moreover, “and n x n symmetric matrix A … has n real eigenvalues, counting multiplicities[,] … the eigenspaces are mutually orthogonal, … [and] A is orthogonally diagonalizable” [textbook]. The visualization first shows that the given symmetric matrix A is “orthogonally diagonalizable if there are an orthogonal matrix P (with P -1 = PT ) and a diagonal matrix D such that A = PDPT = PDP -1 … [or when] AT = (PDPT)T = PTTDTPT = PDPT = A” [textbook].  Here, matrices AT and A are equated to each other, proving this property. Matrix A, being a 2 x 2 orthogonally diagonalizable matrix, is then shown to have 2 real eigenvalues. The eigenvectors corresponding to these two eigenvalues are animated, and their orthogonality emphasized. Students are then asked to determine which concept is best represented by this visualization in relation to the real symmetric matrix A. They should be able to draw upon their knowledge of orthogonality and eigenspaces, as well as the explanations provided in the MANIM visualization to conclude that eigenvalues corresponding to distinct eigenvalues of symmetric matrix A are orthogonal.

# Question: Symmetric matrix A = [[2, 1], [1, 2]] is orthogonally diagonalizable because A^T = A. Based on this visualization, which of the following statements is true?
# Answer: Eigenvectors corresponding to distinct eigenvalues of A (different eigenspaces) are always orthogonal.
# Other Options
# A is symmetric but its eigenvectors are not related to the eigenvalues.
# A is symmetric because it equals its transpose, but eigenvectors corresponding to different eigenvalues can be arbitrarily oriented.
# A is diagonalizable with real eigenvalues, but the orthogonality of its eigenvectors is not guaranteed.
#######################################################################################

class SymmetricMatrixVisualization(Scene):
    def construct(self):
        # intro
        matrix_A = Text("Symmetric Matrix A \n"
                        "⎡ 2   1 ⎤\n"
                        "⎣ 1   2 ⎦", font_size=32, color=BLUE).to_edge(UL)
        self.play(Write(matrix_A))
        self.wait(2)

        # Display the transpose of A and show equality
        transpose_A = Text("And Its Transpose, A^T=\n"
                           "⎡ 2   1 ⎤\n"
                           "⎣ 1   2 ⎦", font_size=32, color=BLUE).to_edge(UR)
        self.play(Write(transpose_A))
        self.wait(1)

        eq_arrow = Arrow(start=matrix_A.get_right(), end=transpose_A.get_left(), buff=0.1, stroke_width=3, color=BLUE)
        eq_text = Text("Are Equivalent: A = A^T", font_size=32, color=BLUE).to_edge(UP)
        self.play(Create(eq_arrow), Write(eq_text))
        self.wait(2)
        self.play(FadeOut(matrix_A, transpose_A, eq_arrow, eq_text))
        symmetry_explanation = Text("A is thus symmetric and orthogonally diagonalizable", font_size=32,
                                    color=PURPLE).to_edge(UP)
        self.play(Write(symmetry_explanation))
        self.wait(2)

        # axes
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-4, 4, 1],
            x_length=8,
            y_length=6,
            tips=True
        )
        self.play(Create(axes))
        self.wait(1)

        self.play(FadeOut(symmetry_explanation))
        eigen_text = Text("Eigenvalues of A:\n"
                          "λ = 3 and  λ = 1", font_size=32, color=BLUE).to_edge(UP)
        self.play(Write(eigen_text))
        self.wait(1)
        eigenvector_text1 = Text("For λ = 3, eigenvector v_1 =  [1, 1]", font_size=32, color=PINK).to_edge(UL)
        eigenvector_text2 = Text("For λ = 1, eigenvector v_2 =  [1, -1]", font_size=32, color=GREEN).to_edge(UR)
        self.play(FadeOut(eigen_text), Write(eigenvector_text1), Write(eigenvector_text2))

        # eigenvectors
        v1 = np.array([1, 1])
        v2 = np.array([1, -1])

        # normalize eigenvectors
        v1 = v1 / np.linalg.norm(v1)
        v2 = v2 / np.linalg.norm(v2)

        # draw eigenvectors
        eigenvector1 = Vector(direction=v1, color=PINK).shift(ORIGIN)
        eigenvector2 = Vector(direction=v2, color=GREEN).shift(ORIGIN)
        self.play(Create(eigenvector1), Create(eigenvector2))
        self.wait(1)

        label_v1 = Text("v1", color=PINK).scale(0.4).next_to(eigenvector1.get_end(), RIGHT * 0.2)
        label_v2 = Text("v2", color=GREEN).scale(0.4).next_to(eigenvector2.get_end(), LEFT * 0.9)
        self.play(Write(label_v1), Write(label_v2))
        self.wait(2)

        # orthogonality
        # square corners
        p1 = 0.3 * np.array([v1[0], v1[1], 0])
        p2 = 0.3 * np.array([v2[0], v2[1], 0])
        p3 = p1 + p2

        right_angle_marker = Polygon(
            ORIGIN,
            p1,
            p3,
            p2,
            color=PURPLE,
            fill_color=PURPLE,
            fill_opacity=0.5
        )
        self.play(Create(right_angle_marker))

        self.play(FadeOut(eigenvector_text1, eigenvector_text2))

        # question
        question = Text("Based on this visualization, which of the following statements is true?", font_size=32,
                        color=PURPLE).to_edge(DOWN)
        self.play(Write(question))
        self.wait(3)


#######################################################################################
# Question 3: Understanding eigenvectors intuitively via 3D rotations
# Show a couple different vectors, with one along the z axis. Then apply the same 3D rotation to each vector. Observe as all vectors are rotated off their span, except for the vector along the axis of rotation (z axis). Intuitively, this should be understood to be an eigenvector
# From Week 5 Lecture

# Question Statement: What does the vector along the axis of rotation represent?
# Correct Option: an eigenvector with eigenvalue 1
# Other Options:
# A normal vector that changes direction under rotation (normal vectors don't always stay unchanged in rotation anyway)
# A vector that undergoes scaling but not rotation (vector isn't scaled, it remains completely unchanged since the applied transformation was a rotation)
# A basis vector for the plane of rotation (not a basis for the *plane* of rotation; it's the axis around which the plane rotates)
#######################################################################################

class EigenvectorsUnderRotation(ThreeDScene):
    def construct(self):
        # 3D space (pls render plsplsplsplspls)
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        axes = ThreeDAxes()
        self.add(axes)
        self.wait(1)

        # Axis labels
        x_label = Text("X-Axis", font_size=24, color="#fb8535").next_to(axes.x_axis, RIGHT)
        y_label = Text("Y-Axis", font_size=24, color="#fb8535").move_to([3, 1, -1])
        z_label = Text("Z-Axis", font_size=24, color="#fb8535").move_to([0, 4, 0])
        self.add_fixed_in_frame_mobjects(x_label, y_label, z_label)
        self.wait(2)

        # Axis of rotation (this is where the eigenvector will be)
        eigenvector = np.array([0, 0, 1])  # Z-axis (unchanged in rotation)
        eigen_arrow = Arrow3D(ORIGIN, eigenvector, color="#fb8535")
        eigen_label = Text("Vector A", font_size=24).next_to(eigen_arrow, UP)

        # Non-eigenvectors
        vec1 = np.array([1.0, 1.0, 0.0])
        vec2 = np.array([-1.0, 1.0, 0.0])
        vec3 = np.array([1.0, -1.0, 0.0])

        vec1_arrow = Arrow3D(ORIGIN, vec1, color=BLUE)
        vec2_arrow = Arrow3D(ORIGIN, vec2, color=GREEN)
        vec3_arrow = Arrow3D(ORIGIN, vec3, color=YELLOW)

        vec1_label = Text("Vector B", font_size=24, color=BLUE).move_to([1, -1, 1])
        vec2_label = Text("Vector C", font_size=24, color=GREEN).move_to([1, 1, 1])
        vec3_label = Text("Vector D", font_size=24, color=YELLOW).move_to([-1, -1, -1])

        self.play(Create(eigen_arrow), run_time=1)
        self.add_fixed_in_frame_mobjects(eigen_label)
        self.wait(1)
        self.play(Create(vec1_arrow), run_time=1)
        self.add_fixed_in_frame_mobjects(vec1_label)
        self.wait(1)
        self.play(Create(vec2_arrow), run_time=1)
        self.add_fixed_in_frame_mobjects(vec2_label)
        self.wait(1)
        self.play(Create(vec3_arrow), run_time=1)
        self.add_fixed_in_frame_mobjects(vec3_label)
        self.wait(2)

        rotation_label = Text("Applying a 3D rotation (transformation) about the Z axis gives us: ", font_size=28,
                              color="#fb8535").to_edge(UP)
        self.add_fixed_in_frame_mobjects(rotation_label)
        self.wait(1)

        # rotate vectors around z-axis (90 degrees)
        self.play(Rotate(vec1_arrow, angle=90 * DEGREES, axis=eigenvector), run_time=2)
        self.wait(1)
        self.play(Rotate(vec2_arrow, angle=90 * DEGREES, axis=eigenvector), run_time=2)
        self.wait(1)
        self.play(Rotate(vec3_arrow, angle=90 * DEGREES, axis=eigenvector), run_time=2)
        self.wait(2)

        # Question
        question_text = Text("What does the vector along the axis of rotation represent?", font_size=36,
                             color="#fb8535").to_edge(DOWN)
        self.play(FadeOut(rotation_label))
        self.add_fixed_in_frame_mobjects(question_text)
        self.wait(2)


#######################################################################################
# Question 4: Eigendecomposition of a matrix
# "Let A be a square n × n matrix with n linearly independent eigenvectors qi (where i = 1, ..., n). Then A can be factored as A = QΛQ^-1 where Q is the square n × n matrix whose ith column is the eigenvector qi of A, and Λ is the diagonal matrix whose diagonal elements are the corresponding eigenvalues, Λii = λi"
# https://en.wikipedia.org/wiki/Eigendecomposition_of_a_matrix
# Here we're going to take a vector and transform it using a matrix M
# Then we're going to take the same vector and transform it using QΛQ^-1 to demonstrate the concept of eigendecomp

# Question: What does the process in this visualization (basis change --> scaling --> basis change back) represent?
# Answer: Eigendecomposition: a way to break the original transformation into simpler steps using eigenbasis
# Other options:
# A random sequence of transformations unrelated to the original matrix M
# A partial pivoting procedure from row reduction
# A method to make all vectors rotate without scaling
#######################################################################################

class Eigendecomposition(Scene):
    def construct(self):
        # axes
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            x_length=8,
            y_length=8,
            tips=True
        )
        self.play(Create(axes))
        self.wait(1)

        # matrix M (diagonalizable)
        M = np.array([[2, 1],
                      [0, 3]])

        # eigenbasis Q (columns = M's eigenvectors)
        Q = np.array([[1, 1],
                      [0, 1]])

        # matrix D (diagonal; reps the eigenvalues in that basis)
        D = np.array([[2, 0],
                      [0, 3]])

        # Transforming vector v via three steps QDQ^-1 vs transforming vector v via matrix M
        v = np.array([2, 1])

        original_vector = Vector(v, color="#fb8535")
        original_vector.shift(axes.coords_to_point(0, 0))
        label_v = Text("v", font_size=24, color="#fb8535").next_to(original_vector.get_end(), UP)
        self.play(Create(original_vector), Write(label_v))
        self.wait(2)

        # Direct transformation of v by M (to compare at the end)
        direct_transformation_label = Text("Let's transform vector v using matrix M =\n"
                                           "⎡ 2   1 ⎤\n"
                                           "⎣ 0   3 ⎦", font_size=28, color="#fb8535").to_edge(UP)
        self.play(Write(direct_transformation_label))
        self.wait(2)

        direct_vector = original_vector.copy().apply_matrix(M)
        direct_vector.set_color(BLUE)
        label_v_prime = Text("v'", font_size=24, color=BLUE).next_to(direct_vector.get_end(), UP)
        # keep a copy of original_vector for the stepwise transformations
        stepwise_vector = original_vector.copy().set_color("#fb8535")
        # transform with M
        self.play(Create(stepwise_vector), Transform(original_vector, direct_vector), Write(label_v_prime), run_time=3)
        self.wait(2)

        self.play(FadeOut(direct_transformation_label))
        self.wait(1)
        stepwise_transformation_label = Text(
            "Now let's transform the original vector v using the following stepwise transformation process",
            font_size=28, color="#fb8535").to_edge(UP)
        self.play(Write(stepwise_transformation_label))
        self.wait(1)
        self.play(FadeOut(stepwise_transformation_label))

        # Step 1: Move to the new basis (this is basically multiplying by Q^-1)
        step1_text = Text("Step 1: Move Vector v to New Basis", font_size=28, color="#fb8535")
        step1_text.to_edge(UP)
        self.play(Write(step1_text), FadeOut(label_v))
        self.wait(1)

        Q_inv = np.linalg.inv(Q)
        self.play(ApplyMatrix(Q_inv, stepwise_vector), run_time=2)
        self.wait(1)
        self.play(FadeOut(step1_text))

        # Step 2: Scale in that basis (Apply D)
        step2_text = Text("Step 2: Scale Vector v in the New Basis", font_size=28, color="#fb8535")
        step2_text.to_edge(UP)
        self.play(Write(step2_text))
        self.wait(1)

        self.play(ApplyMatrix(D, stepwise_vector), run_time=2)
        self.wait(1)
        self.play(FadeOut(step2_text))

        # Step 3: Return to original basis (Apply Q)
        step3_text = Text("Step 3: Return Vector v to Original Basis", font_size=28, color="#fb8535")
        step3_text.to_edge(UP)
        self.play(Write(step3_text))
        self.wait(1)

        self.play(ApplyMatrix(Q, stepwise_vector), run_time=2)
        self.wait(1)
        self.play(FadeOut(step3_text))

        # Final result of the stepwise_vector is the same as applying M once
        final_text = Text("Stepwise Transformation vs Direct Transformation", font_size=28, color="#fb8535")
        final_label_v = Text("v", font_size=28, color="#fb8535").next_to(direct_vector.get_end(), UP)
        final_text.to_edge(UP)
        self.play(Write(final_text), FadeOut(label_v_prime), Write(final_label_v))
        self.wait(2)

        # Question
        question_text = Text("What does the stepwise process represent?\n"
                             "(Basis Change → Scaling → Basis Change Back)", font_size=32, color="#fb8535").to_edge(
            DOWN)
        self.play(FadeOut(final_text), Write(question_text))
        self.wait(2)


#######################################################################################
# Question 5: Eigenspace
# "The set of all eigenvectors of T corresponding to the same eigenvalue, together with the zero vector, is called an eigenspace, or the characteristic space of T associated with that eigenvalue."
# "In essence, an eigenvector v of a linear transformation T is a nonzero vector that, when T is applied to it, does not change direction. Applying T to the eigenvector only scales the eigenvector by the scalar value λ, called an eigenvalue. This condition can be written as the equation T(v) = λv, referred to as the eigenvalue equation or eigenequation. In general, λ may be any scalar. For example, λ may be negative, in which case the eigenvector reverses direction as part of the scaling, or it may be zero or complex."
# https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors#:~:text=The%20set%20of%20all%20eigenvectors%20of%20T%20corresponding%20to%20the,basis%20is%20called%20an%20eigenbasis.

# Question: What does an eigenspace represent?
# Answer: A set of vectors  that stay on their original span after the linear transformation
# Other Options
# A set of vectors unaffected by the linear transformation
# A basis for the null space of the linear transformation
# All of the above.
#######################################################################################

class Eigenspace(Scene):
    def construct(self):
        # axes
        axes = Axes(
            x_range=[-6, 6, 1],
            y_range=[-5, 5, 1],
            x_length=10,
            y_length=8,
            tips=True
        )
        self.play(Create(axes))
        self.wait(1)

        # transformation matrix (shear transformation)
        matrix = [[2, 0], [0, 1]]

        # highlight eigenspace (x-axis)
        eigenspace = Line(start=LEFT * 4, end=RIGHT * 4, color="#fb8535")
        label_eigenspace = Text("Eigenspace", font_size=24, color="#fb8535").next_to(eigenspace, UR)
        eigenspace_text_one = Text("Let's define an eigenspace", font_size=28, color="#fb8535").to_edge(UP)
        self.play(Create(eigenspace), Write(label_eigenspace), Write(eigenspace_text_one))
        self.wait(2)

        # Vectors inside eigenspace (these are gonna stay on span)
        eig_vec1 = Vector([1, 0], color=BLUE)
        eig_vec2 = Vector([-2, 0], color=BLUE)
        eigenspace_text_two = Text("Now let's define vectors inside this eigenspace", font_size=28, color=BLUE).to_edge(
            UP)
        self.play(FadeOut(eigenspace_text_one), Write(eigenspace_text_two))
        self.play(Create(eig_vec1))
        self.wait(1)
        self.play(Create(eig_vec2))
        self.wait(2)

        # Vectors outside eigenspace (these will shear)
        non_eig_vec1 = Vector([2, 1], color=GREEN)
        non_eig_vec2 = Vector([-2, -1], color=GREEN)
        eigenspace_text_three = Text("Finally let's define vectors outside the eigenspace", font_size=28,
                                     color=GREEN).to_edge(UP)
        self.play(FadeOut(eigenspace_text_two), Write(eigenspace_text_three))
        self.play(Create(non_eig_vec1))
        self.wait(1)
        self.play(Create(non_eig_vec2))
        self.wait(2)

        # transform all of them
        transformed_eig_vec1 = eig_vec1.copy().apply_matrix(matrix)
        transformed_eig_vec2 = eig_vec2.copy().apply_matrix(matrix)
        transformed_non_eig_vec1 = non_eig_vec1.copy().apply_matrix(matrix)
        transformed_non_eig_vec2 = non_eig_vec2.copy().apply_matrix(matrix)

        eigenspace_text_four = Text(
            "Observe as all four vectors, inside and outside the eigenspace, undergo a shear transformation",
            font_size=28, color="#fb8535").to_edge(UP)
        self.play(FadeOut(eigenspace_text_three), Write(eigenspace_text_four))
        self.wait(1)
        self.play(Transform(eig_vec1, transformed_eig_vec1))
        self.play(Transform(eig_vec2, transformed_eig_vec2))
        self.wait(1)

        self.play(Transform(non_eig_vec1, transformed_non_eig_vec1))
        self.play(Transform(non_eig_vec2, transformed_non_eig_vec2))
        self.wait(2)

        # Question
        question = Text("Based on this visualization, what does an eigenspace represent?", font_size=32,
                        color="#fb8535").to_edge(DOWN)
        self.play(FadeOut(eigenspace_text_four), Write(question))
        self.wait(3)

