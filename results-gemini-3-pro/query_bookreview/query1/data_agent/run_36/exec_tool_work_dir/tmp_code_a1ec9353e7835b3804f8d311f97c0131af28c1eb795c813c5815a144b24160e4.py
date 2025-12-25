code = """import json
import re
import pandas as pd

# Load data
with open(locals()['var_function-call-9466151329181022833'], 'r') as f:
    books_data = json.load(f)

with open(locals()['var_function-call-17556222483133250874'], 'r') as f:
    reviews_data = json.load(f)

# Process Books
book_years = {}
year_pattern = re.compile(r'(?:published|released)[\w\W]{0,50}?\b(19\d{2}|20\d{2})\b', re.IGNORECASE)
# Fallback pattern: look for date like "Month Day, Year"
date_pattern = re.compile(r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+(19\d{2}|20\d{2})', re.IGNORECASE)

# ID mapping
# bookid_X -> X
# purchaseid_X -> X

book_info = []
for b in books_data:
    bid_str = b.get('book_id', '')
    details = b.get('details', '')
    
    # Extract ID
    # assume format bookid_(\d+)
    m_id = re.search(r'bookid_(\d+)', bid_str)
    if not m_id:
        continue
    bid = int(m_id.group(1))
    
    # Extract Year
    year = None
    # Try patterns
    m_year = year_pattern.search(details)
    if m_year:
        year = int(m_year.group(1))
    else:
        m_date = date_pattern.search(details)
        if m_date:
            year = int(m_date.group(1))
    
    if year:
        book_info.append({'id': bid, 'year': year})

# Create DataFrame for books
df_books = pd.DataFrame(book_info)
if not df_books.empty:
    df_books['decade'] = (df_books['year'] // 10) * 10
    df_books['decade_str'] = df_books['decade'].astype(str) + "s"

# Process Reviews
review_list = []
for r in reviews_data:
    pid_str = r.get('purchase_id', '')
    rating = r.get('rating')
    
    # Extract ID
    m_id = re.search(r'purchaseid_(\d+)', pid_str)
    if not m_id:
        continue
    pid = int(m_id.group(1))
    
    if rating is not None:
        try:
            rating = float(rating)
            review_list.append({'id': pid, 'rating': rating})
        except:
            pass

df_reviews = pd.DataFrame(review_list)

# Join
# We need distinct books rated count
# And average rating
if not df_books.empty and not df_reviews.empty:
    # Merge
    merged = pd.merge(df_reviews, df_books, on='id', how='inner')
    
    # Group by decade
    # 1. Count distinct books
    distinct_books = merged.groupby('decade_str')['id'].nunique().reset_index(name='book_count')
    
    # 2. Average rating (average of all ratings in that decade)
    avg_rating = merged.groupby('decade_str')['rating'].mean().reset_index(name='avg_rating')
    
    # Combine
    stats = pd.merge(distinct_books, avg_rating, on='decade_str')
    
    # Filter >= 10 books
    filtered = stats[stats['book_count'] >= 10].copy()
    
    # Find max
    if not filtered.empty:
        best_decade = filtered.sort_values('avg_rating', ascending=False).iloc[0]
        result = {
            'decade': best_decade['decade_str'],
            'avg_rating': best_decade['avg_rating'],
            'book_count': int(best_decade['book_count'])
        }
    else:
        result = "No decade met criteria"
        
    print("__RESULT__:")
    print(json.dumps(result))
else:
    print("__RESULT__:")
    print(json.dumps("Empty data"))"""

env_args = {'var_function-call-15143408529647577567': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'var_function-call-5012055095290387125': [{'count': '200'}], 'var_function-call-7860955901802981847': ['review'], 'var_function-call-1642967241088979441': [{'COUNT(*)': '1833'}], 'var_function-call-8003113415507431300': [{'purchase_id': 'purchaseid_186'}, {'purchase_id': 'purchaseid_191'}, {'purchase_id': 'purchaseid_190'}, {'purchase_id': 'purchaseid_8'}, {'purchase_id': 'purchaseid_178'}], 'var_function-call-9466151329181022833': 'file_storage/function-call-9466151329181022833.json', 'var_function-call-17556222483133250874': 'file_storage/function-call-17556222483133250874.json'}

exec(code, env_args)
