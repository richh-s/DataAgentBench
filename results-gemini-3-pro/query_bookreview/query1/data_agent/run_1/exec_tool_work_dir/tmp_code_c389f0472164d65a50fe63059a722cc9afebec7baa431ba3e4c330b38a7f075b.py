code = """import json
import re
import pandas as pd

# Load data
with open(locals()['var_function-call-6823915072745218246'], 'r') as f:
    books_data = json.load(f)

with open(locals()['var_function-call-4571223686527832889'], 'r') as f:
    reviews_data = json.load(f)

# Process Books
book_years = []
for b in books_data:
    bid_str = b.get('book_id', '')
    # Extract ID number
    match_id = re.search(r'bookid_(\d+)', bid_str)
    if not match_id:
        continue
    bid = int(match_id.group(1))
    
    details = b.get('details', '')
    # Extract year. 
    # Patterns: "published ... on ... YYYY", "released on ... YYYY", "YYYYth edition" (risky)
    # Safest: Look for 4 digits in 1900-2023 range, appearing after "published" or "released" or as a date.
    # Simple regex for year finding in the text.
    # Note: Details often contain dimensions, ISBNs. ISBNs are 10 or 13 digits.
    # Dimensions like 5.5 x 8.5.
    # Year is usually 4 digits.
    # Regex: `\b(19\d{2}|20\d{2})\b`. 
    # But ISBN parts could match. 
    # Let's try to match date context: `(?:January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}, (\d{4})`
    # Or `\d{4}` provided it's not part of ISBN.
    
    # Try explicit date format first
    year = None
    date_match = re.search(r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+(\d{4})', details)
    if date_match:
        year = int(date_match.group(1))
    else:
        # Fallback: look for "YYYY" that is likely a year.
        # Avoid ISBNs (usually labeled).
        # Find all 4-digit numbers.
        candidates = re.findall(r'\b(19\d{2}|20[0-2]\d)\b', details)
        # Filter candidates. If multiple, maybe pick the first one? Or the one after "published"?
        # Usually "published ... YYYY".
        # Let's look at the text snippets in thought trace. 
        # "released on January 1, 2004" (Matched by date regex)
        # "published ... on May 20, 1996" (Matched by date regex)
        # "published independently on December 30, 2021" (Matched by date regex)
        # "released on November 15, 2000" (Matched by date regex)
        # "published ... in a September 1, 1987 edition" (Matched by date regex)
        pass
        
    if year:
        book_years.append({'id': bid, 'year': year})

books_df = pd.DataFrame(book_years)
books_df['decade'] = (books_df['year'] // 10) * 10
books_df['decade_str'] = books_df['decade'].astype(str) + 's'

# Process Reviews
review_list = []
for r in reviews_data:
    pid_str = r.get('purchase_id', '')
    match_id = re.search(r'purchaseid_(\d+)', pid_str)
    if not match_id:
        continue
    pid = int(match_id.group(1))
    
    try:
        rating = float(r.get('rating', 0))
    except:
        continue
        
    review_list.append({'id': pid, 'rating': rating})

reviews_df = pd.DataFrame(review_list)

# Join
merged = pd.merge(reviews_df, books_df, on='id', how='inner')

# Aggregation
# Group by decade
grouped = merged.groupby('decade_str')

results = []
for decade, group in grouped:
    # distinct books
    distinct_books = group['id'].nunique()
    if distinct_books >= 10:
        avg_rating = group['rating'].mean() # Average of all ratings
        avg_book_rating = group.groupby('id')['rating'].mean().mean() # Average of book averages
        results.append({
            'decade': decade,
            'distinct_books': distinct_books,
            'avg_rating': avg_rating,
            'avg_book_rating': avg_book_rating
        })

results_df = pd.DataFrame(results)
# Sort by avg_rating
results_df_sorted = results_df.sort_values('avg_rating', ascending=False)

print("__RESULT__:")
print(results_df_sorted.to_json(orient='records'))"""

env_args = {'var_function-call-6917719738639545908': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'var_function-call-5788727384283848552': ['review'], 'var_function-call-3525897299712882466': [{'count(*)': '1833'}], 'var_function-call-6885967342009570214': [{'count': '200'}], 'var_function-call-6823915072745218246': 'file_storage/function-call-6823915072745218246.json', 'var_function-call-4571223686527832889': 'file_storage/function-call-4571223686527832889.json'}

exec(code, env_args)
