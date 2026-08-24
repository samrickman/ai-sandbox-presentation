# uv run --with matplotlib lethal_trifecta.py
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as patches


# ---------- Styling ----------

BG = "#f8f8f8"
TEXT = "#0b0c0c"
MUTED = "#505a5f"

PASTEL_YELLOW = "#FCE28F"
PASTEL_GREEN = "#B8DFB9"
PASTEL_PINK = "#F5AEC2"

ALPHA = 0.75

RADIUS = 0.55
CENTER_TOP = (0.0, 0.30)
CENTER_LEFT = (-0.30, -0.20)
CENTER_RIGHT = (0.30, -0.20)

X_LIMS = (-1.10, 1.10)
Y_LIMS = (-0.90, 1.12)


# ---------- Figure helpers ----------

def setup_figure(figsize=(10, 8)):
    fig, ax = plt.subplots(figsize=figsize, facecolor=BG)
    ax.set_facecolor(BG)
    ax.set_xlim(*X_LIMS)
    ax.set_ylim(*Y_LIMS)
    ax.set_aspect("equal")
    ax.axis("off")
    return fig, ax


def save_figure(fig, filename):
    fig.tight_layout()
    fig.savefig(
        filename,
        dpi=300,
        facecolor=fig.get_facecolor(),
        bbox_inches="tight",
    )
    plt.close(fig)


def add_title(ax, title):
    ax.text(
        0,
        1.03,
        title,
        ha="center",
        va="center",
        fontsize=27,
        fontweight="bold",
        color=TEXT,
        family="sans-serif",
    )


# ---------- Base circles ----------

def add_trifecta_circles(ax):
    circles = {
        "top": patches.Circle(
            CENTER_TOP,
            RADIUS,
            facecolor=PASTEL_YELLOW,
            edgecolor="none",
            alpha=ALPHA,
        ),
        "left": patches.Circle(
            CENTER_LEFT,
            RADIUS,
            facecolor=PASTEL_GREEN,
            edgecolor="none",
            alpha=ALPHA,
        ),
        "right": patches.Circle(
            CENTER_RIGHT,
            RADIUS,
            facecolor=PASTEL_PINK,
            edgecolor="none",
            alpha=ALPHA,
        ),
    }

    for circle in circles.values():
        ax.add_patch(circle)

    return circles


# ---------- Labels ----------

def add_original_labels(ax):
    base = {
        "ha": "center",
        "va": "center",
        "color": TEXT,
        "family": "sans-serif",
        "fontweight": "bold",
        "zorder": 20,
    }

    ax.text(0.00, 0.62, "Access to\nPrivate Data", fontsize=14, **base)
    ax.text(-0.45, -0.43, "Ability to\nExternally\nCommunicate", fontsize=14, **base)
    ax.text(0.45, -0.43, "Exposure to\nUntrusted Content", fontsize=14, **base)
    ax.text(0.00, 0.02, "THE LETHAL\nTRIFECTA", fontsize=12, **base)


def add_docker_labels(ax):
    """
    Main labels repositioned to sit in the remaining coloured area,
    away from the removed pizza slices.
    """
    base = {
        "ha": "center",
        "va": "center",
        "color": TEXT,
        "family": "sans-serif",
        "fontweight": "bold",
        "zorder": 20,
    }

    # Lower than the original so it stays below the top slice
    ax.text(0.00, 0.49, "Access to\nPrivate Data", fontsize=14, **base)

    # Shifted rightward within the green circle to avoid the left slice
    ax.text(-0.22, -0.46, "Ability to\nExternally\nCommunicate", fontsize=14, **base)

    # Shifted leftward within the pink circle to avoid the right slice
    ax.text(0.40, -0.45, "Exposure to\nUntrusted Content", fontsize=14, **base)

    ax.text(0.00, 0.02, "THE LETHAL\nTRIFECTA", fontsize=12, **base)


def add_pairwise_overlap_labels(ax):
    style = {
        "ha": "center",
        "va": "center",
        "color": TEXT,
        "family": "sans-serif",
        "fontsize": 10,
        "fontweight": "bold",
        "zorder": 20,
    }

    box = dict(
        boxstyle="round,pad=0.22",
        facecolor=BG,
        edgecolor="none",
        alpha=0.92,
    )

    ax.text(-0.27, 0.18, "No injection\npath", bbox=box, **style)
    ax.text(0.27, 0.18, "No secrets\nto steal", bbox=box, **style)
    ax.text(0.00, -0.30, "No exfiltration\npath", bbox=box, **style)


# ---------- Slice overlay ----------

def add_removed_slice(ax, centre, theta1, theta2):
    """
    Draw a true pizza-slice wedge from the centre of the circle.
    """
    slice_patch = patches.Wedge(
        center=centre,
        r=RADIUS + 0.001,
        theta1=theta1,
        theta2=theta2,
        facecolor=BG,
        edgecolor=MUTED,
        linewidth=1.25,
        hatch="///",
        zorder=10,
    )
    ax.add_patch(slice_patch)


def add_docker_default_slices(ax):
    # Top circle: remove a large top-centred slice
    add_removed_slice(
        ax,
        CENTER_TOP,
        theta1=52,
        theta2=128,
    )

    # Left circle: remove a large far-left slice
    add_removed_slice(
        ax,
        CENTER_LEFT,
        theta1=145,
        theta2=215,
    )

    # Right circle: remove a large far-right slice
    add_removed_slice(
        ax,
        CENTER_RIGHT,
        theta1=-35,
        theta2=35,
    )


# ---------- Outputs ----------

def draw_original(output_path):
    fig, ax = setup_figure()
    add_title(ax, "The lethal trifecta")
    add_trifecta_circles(ax)
    add_original_labels(ax)
    save_figure(fig, output_path)


def draw_docker_default(output_path):
    fig, ax = setup_figure()
    add_title(ax, "Docker sandboxes with default settings")
    add_trifecta_circles(ax)
    add_docker_default_slices(ax)
    add_docker_labels(ax)
    add_pairwise_overlap_labels(ax)
    save_figure(fig, output_path)


def main():
    out_dir = Path("img")
    out_dir.mkdir(parents=True, exist_ok=True)

    original = out_dir / "lethal_trifecta.png"
    docker = out_dir / "lethal_trifecta_docker_default.png"

    draw_original(original)
    draw_docker_default(docker)

    print("Wrote:")
    print(f"  {original}")
    print(f"  {docker}")


if __name__ == "__main__":
    main()