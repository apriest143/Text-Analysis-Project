
import string
import urllib.request
import re
from collections import Counter

import random
import sys
from unicodedata import category


def process_text(text, skip_header):
    """Makes a histogram that counts the words from a file.

    filename: string
    skip_header: boolean, whether to skip the Gutenberg header

    returns: map from each word to the number of times it appears.
    """
    hist = {}
    

    # strippables = string.punctuation + string.whitespace
    strippables = "".join(
        chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")
    )  # Unicode punctuation characters. Ref: https://stackoverflow.com/a/60983895


    starting = not skip_header

    starting = False
    for line in text.split('\n'):
        if skip_header and not starting:
            if line.startswith("*** START OF THE PROJECT"):
                starting = True
            continue
        
        if line.startswith("*** END OF THE PROJECT"):
            break

        line = line.replace("-", " ")
        line = line.replace(chr(8212), " ")  # Em dash replacement

        for word in line.split():
            word = word.strip(strippables)
            word = word.lower()

            hist[word] = hist.get(word, 0) + 1

    return hist


###Clean text for later chapter analysis:
def clean_text(text):
    '''This function will clean the text file by removing the Gutenberg headers, and the table of contents.
    This will be used later for analysing each chapter indicvidually.'''

    start_case = "(Supplied by a Late Consumptive"
    end_case = "*** END OF THE PROJECT"

    
    start_pos = text.find(start_case)
    end_pos = text.find(end_case)

    if start_pos != -1 and end_pos != -1:
        return text[start_pos + len(start_case): end_pos].strip()
    else:
        return text
    

def process_by_chapter(clean_text):
    '''Using the Cleaned text, this function looks for instances of "CHAPTER" followed by 1-3 numbers and seperates these chapters
    into seperate histograms and removes stop words, and also sets case to lower'''
    chapters = re.split(r"(CHAPTER \d{1,3})", clean_text)
    chapter_histograms = {}
    stop_words = set(stopwords.words("english"))

    for i in range(1, len(chapters), 2):
        chapter_title = chapters[i].strip()  # Title like "CHAPTER 1"
        chapter_text = chapters[i + 1].strip() if (i + 1) < len(chapters) else ""

        # Process text for each chapter and create histogram
        words = chapter_text.lower().split()
        words = [word.strip(".,!?;:") for word in words if word not in stop_words]  # Clean punctuation and remove stopwords

        # Create histogram
        hist = Counter(words)
        
        # Store histogram in dictionary by chapter title
        chapter_histograms[chapter_title] = dict(hist, reverse = True)

    return chapter_histograms

### Analyse and classify each chapter based on topics seen in said chapter.
def analyze_topics(chapter_histograms):
    '''Analyze each chapter histogram and identify topics based on keywords from each chapter.'''
    
    topics = {
        "Technical Sailing/Whaling": {"skull", "scientific", "blubber", "sperm", "sharks", "ship", "chart", "study", "oil", "fish", "diameter", "whaling", "skeleton"},
        "Plot/Story": {"ahab", "queequeg", "stubb", "captain", "moby", "struck", "white", "starbuck", "pequod"},
        "Introspective": {"ishmael", "heart", "god", "life", "i", "soul", "vast", "lord", "call", "vast", "loom"}
    }

    for chapter, hist in chapter_histograms.items():
        topic_count = {topic: 0 for topic in topics.keys()}  
        for word, count in hist.items():
            for topic, keywords in topics.items():
                if word in keywords:
                    topic_count[topic] += count
        
        chapter_histograms[chapter]['topics'] = topic_count

    return chapter_histograms






###Computing Summary Statistics
def most_common_words(hist):
    """Sorts words by frequency in descending order."""
    sorted_counts = sorted(hist.items(), key=lambda item: item[1], reverse=True)
    return sorted_counts

### How many different words in the text?
def different_words(hist):
    """Returns the number of different words in a histogram."""
    return len(hist)



###Download required packages for stopword removal:
import nltk
from nltk.corpus import stopwords
nltk.download("stopwords")

### Creating New Histogram without stop words
def removing_stop_words(hist):
    '''Using NLTK, this function will remove stopwords and store the new histogram'''
    stop_words = set(stopwords.words("english"))

    cleaned_hist = dict(sorted(
        {word: count for word, count in hist.items() if word not in stop_words}.items(),
        key=lambda item: item[1],
        reverse=True))

    return cleaned_hist


###






###Main Function, Hopefully will run all analysis and loading cleanly
def main():
    url = 'https://www.gutenberg.org/cache/epub/2701/pg2701.txt'
    with urllib.request.urlopen(url) as f:
        text = f.read().decode('utf-8')

    # Process text and clean it
    hist = process_text(text, skip_header=True)
    cleaned_text = clean_text(text)  # Use cleaned text in further functions

    # Output and analysis
    print(f"Total word count: {sum(hist.values())}")
    print(f"Number of different words: {different_words(hist)}")
    print("Most common words:")
    print(most_common_words(hist)[:50])  
    
    # Histogram without stopwords
    cleaned_hist = removing_stop_words(hist)
    print("Most common words without stopwords:")
    print(most_common_words(cleaned_hist)[:50])
    
    # Process by chapter
    chapter_histograms = process_by_chapter(cleaned_text)
    print("\nChapter histograms (word counts):")
    for title, hist in chapter_histograms.items():
        print(f"\n{title}:")
        print(most_common_words(hist)[:20])


    #Classify chapters based on common topics.
    chapter_histograms_with_topics = analyze_topics(chapter_histograms)
    for chapter, data in chapter_histograms_with_topics.items():
        print(f"{chapter}: {data['topics']}")




    

if __name__ == "__main__":
    main()
