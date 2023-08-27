import os
import numpy as np
from PIL import Image
from wordcloud import WordCloud

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
text = open(os.path.join(d, 'text', 'su-shi.txt')).read()

# Font from Google Noto Sans Traditional Chinese
## Ref : https://fonts.google.com/noto/specimen/Noto+Sans+TC
font_path = os.path.join(d, 'font', 'NotoSansTC-Light.ttf')

# Generate a word cloud image
wordcloud = WordCloud(
        font_path=font_path,
        background_color="white",
        max_words=1000
    ).generate(text)

# Export to an image
wordcloud.to_file(os.path.join('/data', '07-chinese.png'))
