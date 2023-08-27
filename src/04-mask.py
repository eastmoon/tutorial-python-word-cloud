import os
import numpy as np
from PIL import Image
from wordcloud import WordCloud

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
text = open(os.path.join(d, 'text', 'constitution.txt')).read()

# Read the mask image
mask = np.array(Image.open(os.path.join(d, 'mask', "python.png")))

# Generate a word cloud image
wordcloud = WordCloud(background_color="white", max_words=1000, mask=mask).generate(text)

# Export to an image
wordcloud.to_file(os.path.join('/data', '04-mask.png'))
