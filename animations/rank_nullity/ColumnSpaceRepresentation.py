from manim import *
import numpy as np


# Custom 3D arrow built from a cylinder (shaft) and a cone (tip).
class Arrow3D(VMobject):
    def __init__(self, start=ORIGIN, end=ORIGIN, color=WHITE, **kwargs):
        super().__init__(**kwargs)
        self.start = np.array(start)
        self.end = np.array(end)
        self.color = color
        self.build_arrow()

    def build_arrow(self):
        direction = self.end - self.start
        length = np.linalg.norm(direction)
        norm_dir = direction / length if length != 0 else np.array([0, 0, 1])

        # Parameters for shaft and tip.
        tip_height = 0.3
        tip_radius = 0.1
        shaft_radius = 0.05
        shaft_height = length - tip_height if length > tip_height else 0

        # Create the shaft if it has nonzero length.
        if shaft_height > 0:
            shaft = Cylinder(
                radius=shaft_radius,
                height=shaft_height,
                fill_color=self.color,
                stroke_color=self.color
            )
            shaft.move_to(self.start + norm_dir * (shaft_height / 2))
            shaft.rotate(
                angle=np.arccos(np.dot(norm_dir, [0, 0, 1])),
                axis=np.cross([0, 0, 1], norm_dir)
            )

        # Create the tip as a cone.
        tip = Cone(
            base_radius=tip_radius,
            height=tip_height,
            fill_color=self.color,
            stroke_color=self.color
        )
        tip_start = self.start + norm_dir * shaft_height
        tip.move_to(tip_start + norm_dir * (tip_height / 2))
        tip.rotate(
            angle=np.arccos(np.dot(norm_dir, [0, 0, 1])),
            axis=np.cross([0, 0, 1], norm_dir)
        )

    def get_end(self):
        return self.end


class NullSpaceVisualization(ThreeDScene):
    def construct(self):
        # Stage 1: Set up the scene.
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=60 * DEGREES, theta=-45 * DEGREES)
        self.play(Create(axes))
        self.wait(1)

        # Create a yellow cylinder to highlight the z-axis.
        # By default, Cylinder() is centered at the origin, so it "goes through" the origin.
        z_axis_highlight = Cylinder(
            radius=0.02,
            height=5,
            fill_color=YELLOW,
            stroke_color=YELLOW
        )
        self.play(FadeIn(z_axis_highlight), run_time=1)
        self.wait(1)

        # Stage 2: Animate a group of blue vectors.
        vectors = VGroup(*[
            Arrow3D(start=ORIGIN, end=[x, 2 * x, 1], color=BLUE)
            for x in np.linspace(-1, 1, 5)
        ])
        self.play(LaggedStart(*[GrowFromCenter(v) for v in vectors], lag_ratio=0.1))
        self.wait(1)

        # Stage 3: Display the horizontal projection plane.
        plane = Rectangle(width=8, height=8, fill_color=GREEN, fill_opacity=0.2)
        # Rectangle by default lies in the xy-plane.
        self.play(FadeIn(plane), run_time=2)
        self.wait(1)

        # Slightly adjust the camera for a better view of the plane.
        self.move_camera(phi=70 * DEGREES, theta=-45 * DEGREES, run_time=2)
        self.wait(1)

        # Stage 4: Apply the projection transformation (collapse the z-component).
        def projection(point):
            x, y, z = point
            return np.array([x, y, 0])

        projected_vectors = VGroup(*[
            Arrow3D(start=ORIGIN, end=projection(v.get_end()), color=RED)
            for v in vectors
        ])
        self.play(Transform(vectors, projected_vectors), run_time=3)
        self.wait(2)

        # Stage 5: Fade out the yellow cylinder to indicate the loss of the z-component.
        self.play(FadeOut(z_axis_highlight), run_time=2)
        self.wait(1)

        # Stage 6: Return the camera to its original view and clean up.
        self.move_camera(phi=60 * DEGREES, theta=-45 * DEGREES, run_time=2)
        self.wait(1)
        self.play(
            FadeOut(plane),
            FadeOut(axes),
            FadeOut(vectors)
        )
        self.wait(1)
