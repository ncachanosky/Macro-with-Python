+++
# A Demo section created with the Blank widget.
# Any elements can be added in the body: https://wowchemy.com/docs/writing-markdown-latex/
# Add more sections by duplicating this file and customizing to your requirements.

widget = "blank"  # See https://wowchemy.com/docs/page-builder/
headless = true  # This file represents a page section.
active = true  # Activate this widget? true/false
weight = 10  # Order that this section will appear.

title = "Macro with Python"
subtitle = ""

[design]
  # Choose how many columns the section has. Valid values: 1 or 2.
  columns = "1"

[design.background]
  # Apply a background color, gradient, or image.
  #   Uncomment (by removing `#`) an option to apply it.
  #   Choose a light or dark text color by setting `text_color_light`.
  #   Any HTML color name or Hex value is valid.

  # Background color.
   color = "white"
  
  # Background gradient.
  # gradient_start = "DarkGreen"
  # gradient_end = "ForestGreen"
  
  # Background image.
  # image = "image.jpg"  # Name of image in `static/media/`.
  # image_darken = 0.6  # Darken the image? Range 0-1 where 0 is transparent and 1 is opaque.
  # image_size = "cover"  #  Options are `cover` (default), `contain`, or `actual` size.
  # image_position = "center"  # Options include `left`, `center` (default), or `right`.
  # image_parallax = true  # Use a fun parallax-like fixed background effect? true/false
  
  # Text color (true=light or false=dark).
  text_color_light = false

[design.spacing]
  # Customize the section spacing. Order is top, right, bottom, left.
  padding = ["20px", "0", "20px", "0"]

[advanced]
 # Custom CSS. 
 css_style = ""
 
 # CSS class.
 css_class = ""
+++

**Macro with Python** uses typical topics covered in an Intermediate (or advanced) macroeconomics course to offer introductory examples to [Python](https://www.python.org/). The examples assume an introductiry knowledge of Python and same familiarity with intermediate macroeconomic models.

The examples are intended to learn to use Python in the context of macroeconomic models. The examples are not intended to offer complete discussion of the models or coding techniques. The intention of **Macro with Python** is to get started with **how** to use Python in macroeconomics. [QuantEcon](https://quantecon.org/) offers more advanced an detailed documentation.

The **GitHub** repository of this project is located [here](https://github.com/ncachanosky/Macro-with-Python).


> **Macro with Python** is an ongoing project. More examples will be added as they become available.
> [Submission](https://github.com/ncachanosky/Macro-with-Python/issues) of issues and recommendations are welcome.


## Macro with Python: Notebooks

All notebooks make use of [NumPy](https://numpy.org/) and [Matplotlib](https://matplotlib.org/).

For an example on symbolic mathematics and LaTeX format, see **The Solow Model** (section 1). 

For examples of how to find the roots ([SciPy](https://www.scipy.org/)) of a system of equations, see **The Labor Market** (section 3) and **The AD-AS Model** (sections 5 and 6). 

For a shooting algorithm, see **A Simple Ramsey Model** (section 5). 

### List of Models and Applications

1. [The Labor Market][01]
2. [The IS-LM Model][02]
3. [The AD-AS Model][03]
4. [The Solow Model][04]
5. [The R&D Growth Model][05]
6. [A Simple Ramsey Model][06]