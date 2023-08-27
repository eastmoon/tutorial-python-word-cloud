import os
import random
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator

# Declare function : Grey color return by state
def grey_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
text = open(os.path.join(d, 'text', 'constitution.txt')).read()

# Read the mask image
mask = np.array(Image.open(os.path.join(d, 'mask', "python.png")))

# Generate a word cloud image
wordcloud = WordCloud(
        background_color="white",
        max_words=1000,
        random_state=1,
        max_font_size=40,
        mask=mask
    ).generate(text)

# Export to an image
wordcloud.to_file(os.path.join('/data', '06-custom-color-s1.png'))

# Create coloring from image
wordcloud.recolor(color_func=grey_color_func, random_state=3)

# Export to an image with image color
wordcloud.to_file(os.path.join('/data', '06-custom-color-s2.png'))
