code = """import json
import re
import pandas as pd

# Load data
with open('var_function-call-6471655823817105898.json', 'r') as f:
    books_data = json.load(f)
    
with open('var_function-call-1730286370156019482.json', 'r') as f:
    reviews_data = json.load(f)

# Create DataFrames
books_df = pd.DataFrame(books_data)
reviews_df = pd.DataFrame(reviews_data)

# Extract ID number
def extract_id(s, prefix):
    # s is like "bookid_1" or "purchaseid_186"
    # remove prefix and return int
    try:
        if s.startswith(prefix):
            return int(s[len(prefix):])
        # fallback if format is different (e.g. just number or different prefix)
        # Find all digits
        nums = re.findall(r'\d+', s)
        if nums:
            return int(nums[0])
        return None
    except:
        return None

books_df['id_num'] = books_df['book_id'].apply(lambda x: extract_id(x, 'bookid_'))
reviews_df['id_num'] = reviews_df['purchase_id'].apply(lambda x: extract_id(x, 'purchaseid_'))

# Extract year from details
def extract_year(text):
    if not text:
        return None
    # Look for "published ... on ... YYYY" or "released ... on ... YYYY"
    # Regex to find a year (19xx or 20xx) that appears after "published" or "released"
    # and "on" or "in".
    # Pattern: (published|released).*?(\d{4})
    # But need to be careful about not capturing ISBNs.
    # Usually year is preceded by month/day or comma.
    
    # Let's try to find patterns like "on [Month] [Day], [Year]" or "in [Month] [Year]"
    # or just look for the first 4 digit number that looks like a year (1800-2023) 
    # appearing after "published" or "released".
    
    match = re.search(r'(?:published|released).*?(\d{4})', text, re.IGNORECASE)
    if match:
        year = int(match.group(1))
        if 1800 <= year <= 2024:
            return year
            
    # Fallback: search for any year-like number if the specific pattern fails, 
    # but risk of ISBN is high.
    # Let's stick to the specific pattern first.
    return None

books_df['year'] = books_df['details'].apply(extract_year)

# Drop books without year or id
books_valid = books_df.dropna(subset=['year', 'id_num'])

# Join reviews with books
# reviews_df may have multiple reviews for same book.
merged_df = pd.merge(reviews_df, books_valid[['id_num', 'year']], on='id_num', how='inner')

# Convert rating to float
merged_df['rating'] = pd.to_numeric(merged_df['rating'], errors='coerce')

# Calculate decade
# Decade: 1980s means 1980-1989.
# Calculation: (year // 10) * 10
merged_df['decade'] = (merged_df['year'] // 10) * 10

# We need to calculate:
# 1. Distinct books per decade (count distinct id_num)
# 2. Average rating per decade.
# Note: Is average rating calculated as (sum of all ratings for decade) / (total number of ratings for decade)
# OR (average of (average rating per book))?
# Usually "average rating among decades" implies the average of all individual review ratings in that decade.
# However, "average rating" of a decade could also be the average of the books' average ratings.
# Given the phrasing "Which decade ... has the highest average rating", and "among decades with at least 10 distinct books",
# it's usually average of all reviews.
# But let's consider the user might mean average of book ratings.
# Usually in such problems if not specified, average of all ratings is safer or average of book averages.
# Let's check if the result differs significantly or if the phrasing implies one.
# "highest average rating among decades".
# I'll calculate average of all ratings in that decade.

decade_stats = merged_df.groupby('decade').agg(
    distinct_books=('id_num', 'nunique'),
    avg_rating=('rating', 'mean'),
    review_count=('rating', 'count')
).reset_index()

# Filter for decades with at least 10 distinct books
decade_filtered = decade_stats[decade_stats['distinct_books'] >= 10]

# Sort by avg_rating descending
result = decade_filtered.sort_values(by='avg_rating', ascending=False)

print("__RESULT__:")
print(result.to_json(orient='records'))"""

env_args = {'var_function-call-16860782672685490858': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'var_function-call-4638717322374855253': ['review'], 'var_function-call-9045376360600189485': [{'rating': '4', 'purchase_id': 'purchaseid_186'}, {'rating': '4', 'purchase_id': 'purchaseid_191'}, {'rating': '4', 'purchase_id': 'purchaseid_190'}, {'rating': '5', 'purchase_id': 'purchaseid_8'}, {'rating': '4', 'purchase_id': 'purchaseid_178'}], 'var_function-call-14349481852396192255': [{'count': '200'}], 'var_function-call-10098910783103785038': [{'count(*)': '1833'}], 'var_function-call-6471655823817105898': 'file_storage/function-call-6471655823817105898.json', 'var_function-call-1730286370156019482': 'file_storage/function-call-1730286370156019482.json'}

exec(code, env_args)
