import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

st.set_page_config(page_title="Perimeter vs Area Scaling", layout="wide")

# Title and introduction
st.title("🔍 Perimeter vs Area Scaling Demo")
st.markdown("### When you triple the perimeter, the area grows 9 times!")

# Sidebar for controls
st.sidebar.header("Controls")
scale_factor = st.sidebar.slider(
    "Scale Factor", 
    min_value=1.0, 
    max_value=5.0, 
    value=3.0, 
    step=0.5,
    help="How much to scale the original shape"
)

# Original dimensions
original_width = 4
original_height = 3

# Scaled dimensions
scaled_width = original_width * scale_factor
scaled_height = original_height * scale_factor

# Calculations
original_perimeter = 2 * (original_width + original_height)
scaled_perimeter = 2 * (scaled_width + scaled_height)
original_area = original_width * original_height
scaled_area = scaled_width * scaled_height

perimeter_multiplier = scaled_perimeter / original_perimeter
area_multiplier = scaled_area / original_area

# Main layout with columns
col1, col2 = st.columns(2)

# Calculate common axis limits for same scale
max_width = scaled_width + 1
max_height = scaled_height + 1

# Original Rectangle
with col1:
    st.subheader("Original Rectangle")
    
    fig1, ax1 = plt.subplots(figsize=(6, 6))
    rect1 = patches.Rectangle((0, 0), original_width, original_height, 
                               linewidth=3, edgecolor='#2e7d32', 
                               facecolor='#4caf50', alpha=0.7)
    ax1.add_patch(rect1)
    
    # Add grid
    for i in range(1, int(original_width)):
        ax1.axvline(x=i, color='#81c784', linewidth=0.5, alpha=0.7)
    for i in range(1, int(original_height)):
        ax1.axhline(y=i, color='#81c784', linewidth=0.5, alpha=0.7)
    
    # Use same scale for both plots
    ax1.set_xlim(-0.5, max_width)
    ax1.set_ylim(-0.5, max_height)
    ax1.set_aspect('equal')
    ax1.grid(True, alpha=0.3)
    ax1.set_xlabel('Width (units)', fontsize=12)
    ax1.set_ylabel('Height (units)', fontsize=12)
    
    st.pyplot(fig1)
    plt.close()
    
    # Measurements
    st.info(f"""
    **Measurements:**
    - Width: **{original_width} units**
    - Height: **{original_height} units**
    - Perimeter: **{original_perimeter} units** ({original_width} + {original_width} + {original_height} + {original_height})
    - Area: **{original_area} square units** ({original_width} × {original_height})
    """)

# Scaled Rectangle
with col2:
    st.subheader(f"Scaled Rectangle ({scale_factor}×)")
    
    fig2, ax2 = plt.subplots(figsize=(6, 6))
    rect2 = patches.Rectangle((0, 0), scaled_width, scaled_height, 
                               linewidth=3, edgecolor='#1565c0', 
                               facecolor='#2196f3', alpha=0.7)
    ax2.add_patch(rect2)
    
    # Add grid
    for i in range(1, int(scaled_width)):
        ax2.axvline(x=i, color='#64b5f6', linewidth=0.5, alpha=0.7)
    for i in range(1, int(scaled_height)):
        ax2.axhline(y=i, color='#64b5f6', linewidth=0.5, alpha=0.7)
    
    # Use same scale for both plots
    ax2.set_xlim(-0.5, max_width)
    ax2.set_ylim(-0.5, max_height)
    ax2.set_aspect('equal')
    ax2.grid(True, alpha=0.3)
    ax2.set_xlabel('Width (units)', fontsize=12)
    ax2.set_ylabel('Height (units)', fontsize=12)
    
    st.pyplot(fig2)
    plt.close()
    
    # Measurements
    st.info(f"""
    **Measurements:**
    - Width: **{scaled_width:.1f} units** ({original_width} × {scale_factor})
    - Height: **{scaled_height:.1f} units** ({original_height} × {scale_factor})
    - Perimeter: **{scaled_perimeter:.1f} units** ({original_perimeter} × {scale_factor})
    - Area: **{scaled_area:.1f} square units** ({original_area} × {scale_factor**2:.1f})
    """)

# Key Discovery section
st.success(f"""
### 🎯 Key Discovery:
- **Perimeter multiplied by:** {original_perimeter} × {scale_factor} = {scaled_perimeter:.1f} ✓
- **Area multiplied by:** {original_area} × {area_multiplier:.1f} = {scaled_area:.1f} ✓

**Notice:** {scaled_area:.1f} ÷ {original_area} = **{area_multiplier:.1f}**  
The area grew by **{area_multiplier:.1f} times** (which is {scale_factor}²)!
""")

# Grid visualization
st.markdown("---")

if scale_factor == int(scale_factor):
    st.subheader(f"🎨 {int(scale_factor**2)} copies of the original rectangle fit perfectly!")
    
    fig3, ax3 = plt.subplots(figsize=(12, 9))
    
    # Draw the large scaled rectangle
    rect_large = patches.Rectangle((0, 0), scaled_width, scaled_height, 
                                    linewidth=4, edgecolor='#1565c0', 
                                    facecolor='none')
    ax3.add_patch(rect_large)
    
    # Draw individual copies with different colors
    colors = plt.cm.Set3(np.linspace(0, 1, int(scale_factor**2)))
    copy_num = 1
    
    for row in range(int(scale_factor)):
        for col in range(int(scale_factor)):
            x = col * original_width
            y = row * original_height
            rect_copy = patches.Rectangle((x, y), original_width, original_height, 
                                         linewidth=2, edgecolor='#333', 
                                         facecolor=colors[copy_num-1], alpha=0.6)
            ax3.add_patch(rect_copy)
            
            # Add number label
            ax3.text(x + original_width/2, y + original_height/2, 
                    str(copy_num), fontsize=20, weight='bold',
                    ha='center', va='center', color='white',
                    bbox=dict(boxstyle='round', facecolor='black', alpha=0.7))
            copy_num += 1
    
    ax3.set_xlim(-0.5, scaled_width + 0.5)
    ax3.set_ylim(-0.5, scaled_height + 0.5)
    ax3.set_aspect('equal')
    ax3.grid(True, alpha=0.3)
    ax3.set_xlabel('Width (units)', fontsize=12)
    ax3.set_ylabel('Height (units)', fontsize=12)
    ax3.set_title(f'{int(scale_factor**2)} copies of the original fit perfectly inside the scaled version!', 
                 fontsize=14, weight='bold')
    
    st.pyplot(fig3)
    plt.close()
elif scale_factor != int(scale_factor):
    st.warning("⚠️ The grid visualization works best with whole number scale factors. Try 2, 3, 4, or 5!")

# Explanation section
st.markdown("---")
st.markdown("### 💡 Why Does This Happen?")

col_exp1, col_exp2 = st.columns([1, 1])

with col_exp1:
    st.markdown(f"""
    **When you scale by factor {scale_factor}:**
    - **Width** becomes {scale_factor}× larger
    - **Height** becomes {scale_factor}× larger
    - **Area = Width × Height**, so:  
      {scale_factor} × {scale_factor} = **{scale_factor**2:.1f}× larger**
    """)

with col_exp2:
    st.markdown("""
    **General Rule:**  
    If perimeter is multiplied by *n*,  
    then area is multiplied by ***n²***
    
    This works for **any polygon**:
    - Triangles
    - Rectangles
    - Pentagons
    - Hexagons
    - And more!
    """)

