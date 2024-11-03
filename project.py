news_articles = [
    {"text": "This is a real news article about politics.", "label": 0},
    {"text": "This is a fake news article spreading false information.", "label": 1},
    # Add more articles as needed
]

# Function to preprocess text
def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()
    # Remove punctuation
    text = ''.join(char for char in text if char.isalnum() or char == ' ')
    return text

# Function to extract features
def extract_features(text):
    # Simple feature extraction - count the number of words
    return len(text.split())

# Function to train a simple classifier
def train_classifier(data):
    # Naive classification based on number of words in the article
    threshold = 10  # Adjust threshold as needed
    return threshold

# Function to classify news articles
def classify_news(article, threshold):
    # Preprocess article text
    preprocessed_text = preprocess_text(article["text"])
    # Extract features
    num_words = extract_features(preprocessed_text)
    # Classify based on number of words
    if num_words >= threshold:
        return "Real News"
    else:
        return "Fake News"

# Train classifier
threshold = train_classifier(news_articles)

# Test classifier
test_article = {"text": "This is a short article with very few words.", "label": 0}
classification = classify_news(test_article, threshold)
print("Classification:", classification)
