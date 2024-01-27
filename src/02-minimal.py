import os

from os import path
from wordcloud import WordCloud

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
text = open(path.join(d, 'text', 'constitution.txt')).read()

# Generate a word cloud image
wordcloud = WordCloud(background_color="white", width=800, height=400, max_words=1000).generate(text)

# Export to an image
wordcloud.to_file(path.join('/data', '02-minimal.png'))
