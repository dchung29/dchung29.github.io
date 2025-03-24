from manim import *

config.frame_width = 18
config.frame_height = 10
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 60

"""
TODO:
- fix vector label positions
- come up with better explanation text
"""

class RankNullityTheorem(ThreeDScene):
    def construct(self):

        # Define matrix as a simple table
        matrix = Table(
            [["1", "0", "0"],
             ["0", "1", "0"]],
            include_outer_lines=True
        ).scale(0.8)

        matrix_title = Text("Transformation Matrix A").next_to(matrix, UP)

        self.play(Write(matrix_title))
        self.play(Create(matrix))
        self.wait(2)
        self.play(FadeOut(matrix, matrix_title))

        # Set up 3D space
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        axes = ThreeDAxes()

        # Define basis vectors in R^3
        v1 = Arrow3D(start=ORIGIN, end=[2, 1, 1], color=BLUE)
        v2 = Arrow3D(start=ORIGIN, end=[-1, 2, 1], color=ORANGE)
        v3 = Arrow3D(start=ORIGIN, end=[0, 0, 1], color=RED)  # Null space vector

        # Labels
        v1_label = Text("v1", font_size=24, color=ORANGE).next_to(v1, RIGHT)
        v2_label = Text("v2", font_size=24, color=BLUE).move_to([-1, -1, 1])
        v3_label = Text("v3 (in null space)", font_size=24, color=RED).next_to(v3, UP)
        transformation_text = Text("Apply Transformation A").to_edge(UP)

        # Display original space
        self.add(axes)
        self.play(Create(v1), Create(v2), Create(v3))
        self.add_fixed_in_frame_mobjects(v1_label)
        self.add_fixed_in_frame_mobjects(v2_label)
        self.add_fixed_in_frame_mobjects(v3_label)
        self.wait(3)
        self.add_fixed_in_frame_mobjects(transformation_text)
        self.wait(2)

        # Apply transformation A (mapping to R^2)
        v1_trans = Arrow3D(start=ORIGIN, end=[2, 1, 0], color=BLUE)
        v2_trans = Arrow3D(start=ORIGIN, end=[-1, 2, 0], color=ORANGE)
        v3_trans = Arrow3D(start=ORIGIN, end=[0, 0, 0], color=RED)  # Maps to zero

        self.play(Transform(v1, v1_trans), Transform(v2, v2_trans), Transform(v3, v3_trans))
        self.wait(3)
        self.play(FadeOut(v1_label), FadeOut(v2_label), FadeOut(v3_label), FadeOut(transformation_text))
        self.wait(1)

        # Transition to 2D
        # self.play(FadeOut(v1, v2, v3))
        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES, gamma=0 * DEGREES, run_time=2)
        plane = NumberPlane()
        self.play(FadeIn(plane))

        # 2D Transformed vectors
        # v1_2d = Arrow(start=ORIGIN, end=[2, 1, 0], color=BLUE)
        # v2_2d = Arrow(start=ORIGIN, end=[-1, 2, 0], color=BLUE)

        # self.play(Create(v1_2d), Create(v2_2d))
        self.wait(1)

        # Show Rank + Nullity concept
        rank_text = Text("v1 & v2 get mapped to R2, v3 gets mapped to 0").to_edge(UP)
        theorem_text = Text("Rank = 2, Nullity = 1").to_edge(DOWN)

        self.play(Write(rank_text), Write(theorem_text))
        self.wait(4)