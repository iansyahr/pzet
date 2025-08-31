from manim import *
import numpy as np

# --- The Robust Helper Function from our previous discussion ---
def get_sloppy_vmobject(source_vmobject, num_points=300, amplitude=0.05, num_octaves=5):
    """
    Takes any VMobject and returns a new VMobject that looks hand-drawn.
    This version uses a more robust manual point sampling method.
    """
    is_originally_closed = source_vmobject.is_closed()
    
    points = np.array([
        source_vmobject.point_from_proportion(alpha)
        for alpha in np.linspace(0, 1, num_points)
    ])

    n_points = len(points)
    next_points = np.roll(points, -1, axis=0)
    prev_points = np.roll(points, 1, axis=0)
    tangents = next_points - prev_points
    
    if not is_originally_closed:
        tangents[0] = points[1] - points[0]
        tangents[-1] = points[-1] - points[-2]
    
    norms = np.linalg.norm(tangents, axis=1)
    norms[norms == 0] = 1.0
    tangents_norm = tangents / norms[:, np.newaxis]
    
    perp_vectors = np.array([-tangents_norm[:, 1], tangents_norm[:, 0], np.zeros(n_points)]).T

    displacements = np.zeros(n_points)
    random_phases = np.random.rand(num_octaves) * 2 * PI
    current_amplitude = amplitude
    current_frequency = 3.0

    for i in range(num_octaves):
        x_vals = np.linspace(0, current_frequency * PI, n_points)
        displacements += current_amplitude * np.sin(x_vals + random_phases[i])
        current_frequency *= 2.0
        current_amplitude *= 0.5
    
    new_points = points + (displacements[:, np.newaxis] * perp_vectors)

    sloppy_path = VMobject()
    sloppy_path.set_points_as_corners(new_points)
    
    if is_originally_closed:
        sloppy_path.close_path()

    return sloppy_path


class SloppyStarScene(Scene):
    def construct(self):
        self.camera.background_color = "#1E1E1E" # Dark background for the star
        
        # --- Parameters for the star ---
        STAR_COLOR = GOLD
        NUM_STROKES = 1  # Let's use 3 strokes for a nice sketchy feel
        STROKE_WIDTH = 6
        AMPLITUDE = 0.06 # A bit more wobble for a more dynamic shape
        NUM_OCTAVES = 5
        NUM_POINTS_PER_STROKE = 400

        # 1. Create a standard Manim Star as the base shape.
        # This will not be displayed, it's just a template.
        base_star = Star(
            n=5,  # 5 points
            outer_radius=3.0,
            inner_radius=1.5,
            color=STAR_COLOR # Set color here for simplicity
        )

        # 2. Create a VGroup to hold the sloppy strokes.
        sketchy_star = VGroup()
        for _ in range(NUM_STROKES):
            new_stroke = get_sloppy_vmobject(
                base_star,
                num_points=NUM_POINTS_PER_STROKE,
                amplitude=AMPLITUDE,
                num_octaves=NUM_OCTAVES
            )
            sketchy_star.add(new_stroke)
        
        # 3. Style the final VGroup
        sketchy_star.set_style(
            stroke_color=STAR_COLOR,
            stroke_width=STROKE_WIDTH,
            fill_opacity=0
        )
        
        # Let's add a title
        title = Text("Hand-Drawn Star Effect", font_size=40).to_edge(UP)

        self.play(Write(title))
        self.wait(0.5)

        # Animate the star being drawn
        self.play(
            Create(sketchy_star, lag_ratio=0.15, run_time=3)
        )
        
        self.wait(3)
