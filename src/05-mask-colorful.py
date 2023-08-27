import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
text = open(os.path.join(d, 'text', 'constitution.txt')).read()

# Read the mask image
mask = np.array(Image.open(os.path.join(d, 'mask', "python-colorful.png")))

# Generate a word cloud image
wordcloud = WordCloud(
        background_color="white",
        max_words=1000,
        random_state=42,
        max_font_size=40,
        mask=mask
    ).generate(text)

# Export to an image
wordcloud.to_file(os.path.join('/data', '05-mask-colorful-s1.png'))

# Create coloring from image
image_colors = ImageColorGenerator(mask)
wordcloud.recolor(color_func=image_colors)

# Export to an image with image color
wordcloud.to_file(os.path.join('/data', '05-mask-colorful-s2.png'))
