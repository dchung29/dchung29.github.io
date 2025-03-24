from manim import *

config.frame_width = 18
config.frame_height = 10
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 60


class ColumnRowRankVectors(ThreeDScene):
    def construct(self):

        # Define matrix as a simple table
        matrix = Table(
            [["1", "1", "1"],
             ["1", "2", "3"]],
            include_outer_lines=True
        ).scale(0.8)

        matrix_title = Text("2×3 Matrix").next_to(matrix, UP)

        self.play(Write(matrix_title))
        self.play(Create(matrix))
        self.wait(1)
        self.play(FadeOut(matrix, matrix_title))

        axes = ThreeDAxes()

        v1_coords = np.array([1, 1, 0])
        v2_coords = np.array([1, 2, 0])
        v3_coords = np.array([1, 3, 0])

        # Create Arrow3D objects
        v1 = Arrow3D(start=ORIGIN, end=v1_coords, color=BLUE)
        v2 = Arrow3D(start=ORIGIN, end=v2_coords, color=GREEN)
        v3 = Arrow3D(start=ORIGIN, end=v3_coords, color=RED)
        # v4 = Arrow3D(start=ORIGIN, end=v4_coords, color=YELLOW)

        # Define two spanning directions in the plane
        direction1 = v2_coords - v1_coords  # One basis vector
        direction2 = v3_coords - v1_coords  # Another basis vector

        # Extend the plane by scaling the basis vectors
        plane_points = [
            np.array([-3, -3, 0]),  # Point 1: (-3, -3, 0)
            np.array([3, -3, 0]),   # Point 2: (3, -3, 0)
            np.array([3, 3, 0]),    # Point 3: (3, 3, 0)
            np.array([-3, 3, 0])    # Point 4: (-3, 3, 0)
        ]

        column_vectors = VGroup(v1, v2, v3)
        col_title = Text("Column Space (in R³)").to_edge(UP)

        self.set_camera_orientation(phi=75 * DEGREES, theta=-15 * DEGREES)
        self.play(Create(axes))
        self.wait(1)
        # self.play(Write(col_title), Create(column_vectors))
        self.add_fixed_in_frame_mobjects(col_title)
        self.wait(2)

        # Show that all column vectors lie on the same plane
        self.play(FadeIn(column_vectors))
        plane = Polygon(*plane_points, color=WHITE, fill_opacity=0.3)
        self.play(FadeIn(plane))
        span_text = Text("Column Space is a plane - all vectors lie in this plane").to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(span_text)
        self.wait(5)

        # Transition to Row Space
        self.play(FadeOut(column_vectors, plane, col_title, span_text))

        r1_coords = np.array([1, 1, 1])
        r2_coords = np.array([1, 2, 3])

        # Define a third point (arbitrary choice for spanning)
        r3_coords = np.array([2, 1, 2])

        # Compute two spanning vectors
        direction1 = r2_coords - r1_coords
        direction2 = r3_coords - r1_coords

        # Create four corner points to define a rectangle on the plane
        plane_corners = [
            r1_coords - 2 * direction1 - 2 * direction2,  # Bottom-left
            r1_coords + 2 * direction1 - 2 * direction2,  # Bottom-right
            r1_coords + 2 * direction1 + 2 * direction2,  # Top-right
            r1_coords - 2 * direction1 + 2 * direction2   # Top-left
        ]

        # Row vectors (in R³ for visualization)
        r1 = Arrow3D(start=ORIGIN, end=r1_coords, color=BLUE)
        r2 = Arrow3D(start=ORIGIN, end=r2_coords, color=GREEN)
        # r3 = Arrow3D(start=ORIGIN, end=v3_coords, color=RED)

        row_vectors = VGroup(r1, r2)
        row_title = Text("Row Space (in R³)").to_edge(UP)

        self.add_fixed_in_frame_mobjects(row_title)
        self.play(Create(row_vectors))
        plane = Polygon(*plane_corners, color=WHITE, fill_opacity=0.3)
        self.play(FadeIn(plane))
        row_span_text = Text("Row Space also forms a plane").to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(row_span_text)
        self.wait(5)

        # Conclusion: Rank is the same
        # self.play(FadeOut(row_vectors, row_title, row_span_text))
        # final_text = Text("Column Rank = Row Rank").scale(1.2)
        # self.add_fixed_in_frame_mobjects(final_text)
        # self.wait(3)