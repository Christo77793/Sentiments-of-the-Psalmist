import csv
import matplotlib.pyplot as plt
from textblob import TextBlob

csv_file_path = "psalm_text.csv"  # CSV file path


def fn1():
    # Load the Psalms data from the CSV file
    with open(csv_file_path, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)

        next(reader, None)  # Skipping the header
        psalms_data = [row[0] for row in reader]

    # Perform sentiment analysis using TextBlob
    sentiments = [TextBlob(verse).sentiment.polarity for verse in psalms_data]

    return sentiments


sentiments = fn1()

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(range(1, len(sentiments) + 1), sentiments, color="blue")
plt.xlabel("Verse Number")
plt.ylabel("Sentiment Polarity")
plt.title("Sentiment Analysis of Psalms")
plt.show()
