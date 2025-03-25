import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from collections import Counter
import string

# Read file
df = pd.read_csv("./ICC Project Survey (Responses) - Form responses 1.csv")

# Column index
column_index = 22

# Get the column
column = df.iloc[:, column_index]

# Get the text, filtering out NaN values
text = ""

for i in range(len(column)):
    if pd.notna(column[i]):  # Only add non-NaN values
        text += str(column[i]) + " "

# Remove punctuation and split into words
text = text.translate(str.maketrans("", "", string.punctuation))
words = text.split()

# Filter out stopwords and short words (length 2 or less)
filtered_words = [word for word in words if word.lower() not in STOPWORDS and len(word) > 2]

# Generate word cloud
wordcloud = WordCloud(width=800, height=800, background_color="white", stopwords=STOPWORDS, min_font_size=10).generate(" ".join(filtered_words))

# Plot the WordCloud image
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

# Save the WordCloud image
wordcloud.to_file("22.png")

# Count word frequencies
word_counts = Counter(filtered_words)

# Get the top number one word
top_word, top_word_count = word_counts.most_common(1)[0]

print(f"Top word: {top_word} with frequency: {top_word_count}")
