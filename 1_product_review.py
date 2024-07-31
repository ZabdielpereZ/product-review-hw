def d():
    print('='*50)

# 1. Product Review Analysis

# Objective: The aim of this assignment is to extract insights from product reviews by using string manipulation to categorize and summarize customer feedback for a SaaS product.

# Task 1: Keyword Highlighter

# Write a program that searches through a series of product reviews for keywords such as "good", "excellent", "bad", "poor", and "average". Print out each review with the keywords in uppercase so they stand out.

python_reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "This was a poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]

d()

keywords = ["good", "excellent", "bad", "poor", "average"]

for review in python_reviews:
    for word in keywords:
        if word in review:
            x = review.replace(word, word.upper())
            print(x)


# Task 2: Sentiment Tally

# Develop a function that tallies the number of positive and negative words in each review. Use a predefined list of positive and negative words to check against. The function should return the count of positive and negative words for each review.

python_positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"] 
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

for review in python_reviews:
    pos_count = 0
    neg_count = 0
    for word in python_positive_words:
        if word in python_positive_words:
            if word in review:
                pos_count += 1
    for word in negative_words:
        if word in negative_words:
            if word in review:
                neg_count += 1
    d()
    print(review)
    print(f"Positive words: {pos_count}")
    print(f"Negative words: {neg_count}")
    d()

d()

# Task 3: Review Summary

# Implement a function that takes the first 30 characters of a review and appends "…" to create a summary. (Bonus) Ensure that the summary does not cut off in the middle of a word.

# look at each review individually
# slpit each review into a list of words 
# iterate through that list and add each word to my summary while also counting the length of each word untill I get to at least thirty 

def summary_maker(reviews):
    for review in reviews:
        char_count = 0
        summary = []
        words = review.split()
        for word in words:
            if len(' '.join(summary)) <= 30:
                summary.append(word)

        ans = ' '.join(summary) + '...'
        print(ans)
        print(len(ans))
        # summary = review[:31] + '...'
        # print(summary)

summary_maker(python_reviews)

# extra credit !!