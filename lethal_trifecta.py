# uv run --with matplotlib lethal_trifecta.py
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 1. Setup figure and GOV.UK background color
fig, ax = plt.subplots(figsize=(9, 7), facecolor='#f1f1f1')
ax.set_facecolor('#f1f1f1')

# 2. Define soft pastel colors
pastel_yellow = '#FCE28F'
pastel_green  = '#B8DFB9'
pastel_pink   = '#F5AEC2'

# 3. Define circle geometry (Radius and Centers)
r = 0.55
c_top = (0, 0.3)
c_left = (-0.3, -0.2)
c_right = (0.3, -0.2)
alpha_val = 0.75 # Slight transparency to show the mixing in overlaps

# 4. Draw the three circles
circle_top = patches.Circle(c_top, r, facecolor=pastel_yellow, edgecolor='none', alpha=alpha_val)
circle_left = patches.Circle(c_left, r, facecolor=pastel_green, edgecolor='none', alpha=alpha_val)
circle_right = patches.Circle(c_right, r, facecolor=pastel_pink, edgecolor='none', alpha=alpha_val)

ax.add_patch(circle_top)
ax.add_patch(circle_left)
ax.add_patch(circle_right)

# 5. Add Text Labels (Mathematically positioned to prevent overlapping)
text_kwargs = {'ha': 'center', 'va': 'center', 'color': '#0b0c0c', 'family': 'sans-serif'}

# Title
plt.text(0, 1.05, "The lethal trifecta", fontsize=32, fontweight='bold', **text_kwargs)

# Top Circle Text
plt.text(0, 0.62, "Access to\nPrivate Data", fontsize=14, fontweight='bold', **text_kwargs)

# Bottom Left Circle Text
plt.text(-0.45, -0.4, "Ability to\nExternally\nCommunicate", fontsize=14, fontweight='bold', **text_kwargs)

# Bottom Right Circle Text
plt.text(0.45, -0.4, "Exposure to\nUntrusted Content", fontsize=14, fontweight='bold', **text_kwargs)

# Center Overlap Text
plt.text(0, 0.02, "THE LETHAL\nTRIFECTA", fontsize=12, fontweight='black', **text_kwargs)

# 6. Finalize layout and hide axes
ax.set_xlim(-1, 1)
ax.set_ylim(-0.9, 1.2)
ax.axis('off')

# Save as a tight PNG for your Quarto slide
plt.tight_layout()
plt.savefig('img/lethal_trifecta.png', dpi=300, facecolor=fig.get_facecolor(), bbox_inches='tight')
plt.show()