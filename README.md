# Perimeter vs Area Scaling Demo

An interactive Streamlit app that visually demonstrates the mathematical relationship between perimeter and area scaling for polygons. Perfect for 7th-grade math classes and beyond!

## 🎯 What Does This App Teach?

When you scale a polygon by multiplying its perimeter by a factor *n*, the area increases by *n²*. For example:
- **Triple the perimeter** (×3) → **Area increases 9 times** (3² = 9)
- **Double the perimeter** (×2) → **Area increases 4 times** (2² = 4)
- **Scale by 5** → **Area increases 25 times** (5² = 25)

This fundamental concept applies to **all polygons**: triangles, rectangles, pentagons, hexagons, and more!

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone or download this repository**
```bash
git clone <your-repo-url>
cd perimeter-area-scaling
```

2. **Install required packages**
```bash
pip install streamlit matplotlib numpy
```

### Running the App

```bash
streamlit run app.py
```

The app will automatically open in your default web browser at `http://localhost:8501`

## 📚 Features

### Interactive Scale Factor Slider
- Adjust the scale factor from 1× to 5× using the sidebar slider
- See real-time updates to all calculations and visualizations
- Works with both whole numbers and decimals (0.5 increments)

### Side-by-Side Comparison
- Original rectangle (4 × 3 units) shown in green
- Scaled rectangle shown in blue
- **Both rectangles displayed on the same scale** for accurate size comparison
- Grid overlays show individual unit squares

### Detailed Measurements
Each rectangle displays:
- Width and height
- Perimeter calculation (with formula breakdown)
- Area calculation (with formula breakdown)
- Scaling factors applied

### Visual Grid Demonstration
For whole number scale factors (2, 3, 4, 5):
- Shows exactly how many copies of the original rectangle fit inside the scaled version
- Each copy is numbered and color-coded
- Proves visually that the area multiplier equals the scale factor squared

### Educational Explanations
- **Key Discovery section**: Highlights the mathematical relationship
- **Why Does This Happen?**: Explains the reasoning behind the n² rule
- **General Rule**: Shows how this applies to all polygons

## 🎓 Educational Context

### Grade Level
- Primary: 7th Grade
- Also suitable for: 6th-8th grade students learning about area, perimeter, and scaling

### Common Core Standards
- **7.G.A.1**: Solve problems involving scale drawings of geometric figures
- **7.G.B.6**: Solve real-world problems involving area of two-dimensional objects

### Learning Objectives
Students will be able to:
1. Understand the relationship between linear scaling and area
2. Explain why area scales by the square of the linear scale factor
3. Apply this concept to solve real-world problems
4. Visualize mathematical relationships through interactive exploration

## 📖 How to Use in the Classroom

### Lesson Plan Suggestions

1. **Introduction (5 minutes)**
   - Start with the default 3× scale factor
   - Ask students to predict what happens to the area

2. **Exploration (10 minutes)**
   - Let students experiment with different scale factors
   - Have them record perimeter and area multipliers in a table
   - Identify the pattern (n² relationship)

3. **Visual Proof (10 minutes)**
   - Use the grid visualization to show how 9 copies fit inside
   - Discuss why 3 × 3 = 9 makes sense geometrically

4. **Extension Activities**
   - Challenge students to predict results for scale factors beyond 5
   - Apply the concept to real-world scenarios (model buildings, maps, etc.)

## 🛠️ Customization

### Changing the Original Rectangle Dimensions
Edit lines 22-23 in `app.py`:
```python
original_width = 4  # Change to any positive number
original_height = 3  # Change to any positive number
```

### Adjusting the Scale Factor Range
Edit lines 10-16 in `app.py`:
```python
scale_factor = st.sidebar.slider(
    "Scale Factor", 
    min_value=1.0,   # Minimum scale
    max_value=5.0,   # Maximum scale
    value=3.0,       # Default value
    step=0.5,        # Increment size
)
```

## 📸 Screenshots

### Main Interface
The app displays two rectangles side-by-side on the same scale, making the size difference immediately apparent.

### Grid Visualization
For whole number scale factors, the app shows how multiple copies of the original fit perfectly inside the scaled version.

## 🐛 Troubleshooting

### App won't start
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check Python version: `python --version` (needs 3.7+)

### Plots not displaying
- Try clearing Streamlit cache: `streamlit cache clear`
- Restart the app

### Port already in use
- Use a different port: `streamlit run app.py --server.port 8502`

## 📦 Dependencies

```
streamlit>=1.28.0
matplotlib>=3.7.0
numpy>=1.24.0
```

## 🤝 Contributing

Contributions are welcome! Some ideas for enhancements:
- Add support for other polygon shapes (triangles, hexagons)
- Include practice problems with answer checking
- Add animation showing the scaling transformation
- Export visualizations as images for homework

## 📄 License

This project is licensed under the MIT License - feel free to use it in your classroom!

## 👨‍🏫 Author

Created for educators teaching geometry and scaling concepts.

## 🙏 Acknowledgments

- Designed with 7th-grade math curriculum in mind
- Built with Streamlit for easy deployment and sharing
- Uses matplotlib for clear, educational visualizations

---

**Have questions or suggestions?** Open an issue or reach out!

**Want to share how you're using this in your classroom?** We'd love to hear about it!