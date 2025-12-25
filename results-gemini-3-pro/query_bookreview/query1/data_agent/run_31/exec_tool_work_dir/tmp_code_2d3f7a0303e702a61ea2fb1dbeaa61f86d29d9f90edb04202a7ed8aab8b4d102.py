code = """import json
import re
import pandas as pd

# Load data
with open(locals()['var_function-call-8722545173891324635'], 'r') as f:
    books_data = json.load(f)

with open(locals()['var_function-call-5690128409881835106'], 'r') as f:
    reviews_data = json.load(f)

# Helper to extract year
def extract_year(details_str):
    # Look for "Month Day, Year" or "Month Year" patterns first
    # e.g. "January 1, 2004", "May 20, 1996", "September 1, 1987", "January 2004"
    months = r"(?:January|February|March|April|May|June|July|August|September|October|November|December)"
    
    # Pattern 1: Month Day, Year
    match = re.search(months + r"\s+\d{1,2},?\s+(\d{4})", details_str)
    if match:
        return int(match.group(1))
    
    # Pattern 2: Month Year
    match = re.search(months + r"\s+(\d{4})", details_str)
    if match:
        return int(match.group(1))
        
    # Pattern 3: "published ... on Year" or similar? Less likely.
    # Fallback: Find all 4 digit numbers starting with 19 or 20.
    # Filter out those that might be part of ISBNs if possible?
    # ISBNs in the text: "ISBN-10 of ...", "ISBN-13 of ..."
    # We can rely on the fact that years usually stand alone or are near 'published'.
    
    candidates = re.findall(r"\b(19\d{2}|20\d{2})\b", details_str)
    if candidates:
        # If multiple, prefer the one earlier in string? Or later?
        # Usually publication date is early in the description.
        # But edition dates might be later.
        # Let's take the first one found.
        return int(candidates[0])
    
    return None

# Map book_number -> year
book_year_map = {}
for book in books_data:
    b_id = book['book_id'] # e.g. "bookid_1"
    # Extract number
    try:
        b_num = int(b_id.split('_')[1])
    except:
        continue
    
    year = extract_year(book['details'])
    if year:
        book_year_map[b_num] = year

# Process reviews
decade_ratings = {} # decade -> list of ratings
decade_books = {}   # decade -> set of book_nums

for review in reviews_data:
    p_id = review['purchase_id'] # e.g. "purchaseid_186"
    try:
        b_num = int(p_id.split('_')[1])
    except:
        continue
    
    if b_num in book_year_map:
        year = book_year_map[b_num]
        decade = (year // 10) * 10
        dec_str = f"{decade}s"
        
        rating = float(review['rating'])
        
        if dec_str not in decade_ratings:
            decade_ratings[dec_str] = []
            decade_books[dec_str] = set()
        
        decade_ratings[dec_str].append(rating)
        decade_books[dec_str].add(b_num)

# Analyze
results = []
for dec, ratings in decade_ratings.items():
    distinct_books = len(decade_books[dec])
    if distinct_books >= 10:
        avg_rating = sum(ratings) / len(ratings)
        results.append({
            "decade": dec,
            "avg_rating": avg_rating,
            "distinct_books": distinct_books
        })

# Sort by avg_rating descending
results.sort(key=lambda x: x['avg_rating'], reverse=True)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-5481701502992022581': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'var_function-call-6525217930011602390': [{'count': '200'}], 'var_function-call-8708875793343688653': ['review'], 'var_function-call-18354940517746745019': [{'COUNT(*)': '1833'}], 'var_function-call-8722545173891324635': 'file_storage/function-call-8722545173891324635.json', 'var_function-call-5690128409881835106': 'file_storage/function-call-5690128409881835106.json'}

exec(code, env_args)
