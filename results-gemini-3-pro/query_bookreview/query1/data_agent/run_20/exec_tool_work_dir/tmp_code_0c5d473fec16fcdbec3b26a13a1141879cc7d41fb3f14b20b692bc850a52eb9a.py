code = """import json
import pandas as pd
import re

with open(locals()['var_function-call-7266083921109746468'], 'r') as f:
    books = json.load(f)

with open(locals()['var_function-call-10072965068991537289'], 'r') as f:
    reviews = json.load(f)

df_books = pd.DataFrame(books)
df_reviews = pd.DataFrame(reviews)

df_reviews['book_id'] = df_reviews['purchase_id'].str.replace('purchaseid_', 'bookid_')
df_reviews['rating'] = pd.to_numeric(df_reviews['rating'], errors='coerce')

def extract_year_safe(details):
    if not isinstance(details, str):
        return None
    
    # Try finding explicit date format first: Month Day, Year
    # e.g. January 1, 2004
    matches = re.findall(r'([A-Z][a-z]+ \d{1,2},? (\d{4}))', details)
    for match in matches:
        # match is tuple (full_date, year_str)
        y = int(match[1])
        if 1900 <= y <= 2024:
            return y

    # Fallback: look for year numbers near "published" or "released"
    # Find all 4-digit numbers
    # We look for "published/released ... year"
    # But doing this strictly is hard.
    # Let's find all candidates in the string and pick the one that makes sense contextually or is closest to "published"
    
    # Simple approach: Find all 19XX or 20XX in the string.
    # Exclude if it looks like part of ISBN? ISBNs are usually grouped digits.
    # Safe bet: often the year is mentioned as "on ... 1996" or "in 1996".
    
    candidates = re.findall(r'\b(19\d{2}|20\d{2})\b', details)
    # Filter candidates
    valid_years = [int(y) for y in candidates if 1900 <= int(y) <= 2024]
    
    if valid_years:
        # If multiple, which one?
        # Usually the publication date is early in the string or associated with 'published'.
        # Let's try to locate "published" index.
        pub_idx = details.lower().find('published')
        if pub_idx == -1:
            pub_idx = details.lower().find('released')
            
        if pub_idx != -1:
            # Find the candidate closest to pub_idx after it?
            # Or just take the first one found?
            # In the samples, the date follows "published".
            # The regex `published.*?(\d{4})` was good but needs range check.
            
            # Let's retry the regex with range check.
            m = re.search(r'(?:published|released).*?(\b(19|20)\d{2}\b)', details, re.IGNORECASE)
            if m:
                y = int(m.group(1))
                if 1900 <= y <= 2024:
                    return y
        
        # If no "published" keyword or regex failed, just return the first valid year found?
        # Sample 19: "2013th edition" -> 2013 is valid year.
        return valid_years[0]
        
    return None

df_books['year'] = df_books['details'].apply(extract_year_safe)
books_with_year = df_books.dropna(subset=['year']).copy()
books_with_year['decade'] = (books_with_year['year'] // 10 * 10).astype(int).astype(str) + 's'

merged = pd.merge(df_reviews, books_with_year[['book_id', 'decade']], on='book_id', how='inner')

decade_stats = merged.groupby('decade').agg(
    avg_rating=('rating', 'mean'),
    unique_books=('book_id', 'nunique'),
    review_count=('rating', 'count')
).reset_index()

filtered_decades = decade_stats[decade_stats['unique_books'] >= 10].sort_values('avg_rating', ascending=False)

print("__RESULT__:")
print(json.dumps(filtered_decades.to_dict(orient='records')))"""

env_args = {'var_function-call-3600458308634325854': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'var_function-call-5045419460847510275': [{'count': '200'}], 'var_function-call-6749438513669462977': ['review'], 'var_function-call-14243022033857224439': [{'count(*)': '1833'}], 'var_function-call-7266083921109746468': 'file_storage/function-call-7266083921109746468.json', 'var_function-call-10072965068991537289': 'file_storage/function-call-10072965068991537289.json', 'var_function-call-2225101699388499718': '2020s'}

exec(code, env_args)
