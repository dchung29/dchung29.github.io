from manim import *


class RankNullityTheoremVisualization(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES, theta=45 * DEGREES)

        # Create axes
        axes = ThreeDAxes(x_range=[-3, 3], y_range=[-3, 3], z_range=[-3, 3])
        self.add(axes)

        # Column space visualization (Rank)
        column_space_plane = Surface(
            lambda u, v: np.array([u, v, 0]),
            u_range=[-2, 2], v_range=[-2, 2],
            color=BLUE
        )
        column_space_label = Text("Column Space (Rank)", color=BLUE).scale(0.5).to_edge(UP)
        self.add_fixed_in_frame_mobjects(column_space_label)

        # Null space visualization
        null_space_line = Line3D(start=[-3, -3, -3], end=[3, 3, 3], color=GREEN)
        null_space_label = Text("Null Space (Nullity)", color=GREEN).scale(0.5).to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(null_space_label)

        # Display rank-nullity formula
        formula = Text("Rank(A) + Nullity(A)").scale(0.8).to_edge(LEFT)
        self.add_fixed_in_frame_mobjects(formula)

        # Animations
        self.play(Create(column_space_plane), Write(column_space_label))
        self.wait(1)

        self.play(Create(null_space_line), Write(null_space_label))
        self.wait(1)

        self.play(Write(formula))
        self.wait(2)

        # Demonstrate rank increase (reduce nullity)
        new_column_space_plane = Surface(
            lambda u, v: np.array([u, v, v]),
            u_range=[-2, 2], v_range=[-2, 2],
            color=BLUE
        )
        self.play(Transform(column_space_plane, new_column_space_plane))
        self.wait(1)

        # Reduce null space
        new_null_space_line = Line3D(start=[-1, -1, -1], end=[1, 1, 1], color=GREEN)
        self.play(Transform(null_space_line, new_null_space_line))
        self.wait(1)

        # Final explanation
        explanation_text = Text("As Rank Increases, Nullity Decreases").scale(0.6).to_edge(RIGHT)
        self.add_fixed_in_frame_mobjects(explanation_text)
        self.play(Write(explanation_text))
        self.wait(2)

        # End Scene
        self.play(FadeOut(column_space_plane, null_space_line, column_space_label, null_space_label, formula, explanation_text))
        self.wait(1)
