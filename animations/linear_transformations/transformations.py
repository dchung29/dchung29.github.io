from manim import *
import numpy as np

config.frame_width = 18
config.frame_height = 10
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 60


class BaseTransformation(Scene):
    def setup_scene(self):
        # Create and add the plane
        self.plane = NumberPlane(
            x_range=[-12, 12, 1],
            y_range=[-8, 8, 1],
            axis_config={"color": WHITE, "stroke_width": 1.5},
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 0.8,
                "stroke_opacity": 0.2
            }
        )
        self.add(self.plane)
        # Setup the initial vector
        self.start_point = np.array([0, 0, 0])
        self.end_point = np.array([2, 1, 0])
        self.vector = Vector(self.end_point, color=BLUE, stroke_width=6)
        self.add(self.vector)
        self.play(FadeIn(self.vector))
        self.wait(1)

    def apply_transformation(self, matrix):
        # Compute the new endpoint after applying the matrix
        transformed_end = np.dot(matrix, self.end_point[:2])
        transformed_end = np.append(transformed_end, 0)
        transformed_vector = Vector(transformed_end, color=BLUE, stroke_width=6)
        self.play(
            ReplacementTransform(self.vector, transformed_vector),
            run_time=2,
            rate_func=smooth
        )
        self.vector = transformed_vector
        self.end_point = transformed_end
        self.wait(1)


class ScalingTransformation(BaseTransformation):
    def construct(self):
        self.setup_scene()
        matrix = [[2, 0], [0, 2]]
        self.apply_transformation(matrix)


class RotationTransformation(BaseTransformation):
    def construct(self):
        self.setup_scene()
        matrix = [[0, -1], [1, 0]]  # 90° rotation
        self.apply_transformation(matrix)


class ReflectionTransformation(BaseTransformation):
    def construct(self):
        self.setup_scene()
        matrix = [[-1, 0], [0, 1]]  # Reflection over Y-axis
        self.apply_transformation(matrix)


class ShearTransformation(BaseTransformation):
    def construct(self):
        self.setup_scene()
        matrix = [[1, 1], [0, 1]]  # Shear transformation
        self.apply_transformation(matrix)


class ProjectionTransformation(BaseTransformation):
    def construct(self):
        self.setup_scene()
        matrix = [[1, 0], [0, 0]]  # Projection transformation
        self.apply_transformation(matrix)
