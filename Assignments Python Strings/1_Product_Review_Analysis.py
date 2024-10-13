# 1. Product Review Analysis
# Task 1: Keyword Highlighter
# Write a program that searches through reviews list and looks for keywords such as "good", "excellent", "bad", "poor", and "average". We want you to capitalize those keywords then print out each review. Print out each review with the keywords in uppercase so they stand out.
reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]
keywords = ["good", "excellent", "bad", "poor", "average"]

# Print each review with keywords in uppercase.
for review in reviews:
    for keyword in keywords:
        if keyword in review:
            review = review.replace(keyword, keyword.upper())   
    print(review)

# Task 2: Sentiment Tally
# Develop a function that tallies the number of positive and negative words in each review.  The function should return the total count of positive and negative words.
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

# Function that tallies the number of positive and negative words in each review.
def tally_sentiment(review):
    positive_count = 0
    negative_count = 0
    words = review.split()
    
    for word in words:
        if word.lower() in positive_words:  # Convert to lowercase for case-insensitive matching
            positive_count += 1
        elif word.lower() in negative_words:
            negative_count += 1
    
    return positive_count, negative_count, len(words)

# Print the total count of positive and negative words for each review.
for review in reviews:
    positive_count, negative_count, total_count = tally_sentiment(review)
    print(f"Review: {review}")
    print(f"Positive words: {positive_count}")
    print(f"Negative words: {negative_count}")
    print(f"Total words: {total_count}")
    print()
# Task 3: Review Summary
# Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. Ensure that the summary does not cut off in the middle of a word.
summary_length = 30
summary_separator = "..."

# Function that creates a summary of a review.
def create_summary(review):
    if len(review) <= summary_length:
        return review  # If the review is shorter than or equal to the summary length, return it as is.
    else:
        # Find the last space within the first summary_length characters
        last_space_index = review[:summary_length].rfind(" ")
        if last_space_index == -1:  # If no space is found, cut at the summary length
            return review[:summary_length] + summary_separator
        else:
            return review[:last_space_index] + summary_separator

# Print the summary for each review.
for review in reviews:
    summary = create_summary(review)
    print(f"Review: {review}")
    print(f"Summary: {summary}")
    print()

