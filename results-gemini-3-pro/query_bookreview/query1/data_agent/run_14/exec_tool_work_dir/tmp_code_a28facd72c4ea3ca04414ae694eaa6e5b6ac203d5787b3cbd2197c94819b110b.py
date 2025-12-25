code = """import json
import re
import pandas as pd

# Load data
with open(locals()['var_function-call-13891406088243492122']) as f:
    books = json.load(f)
with open(locals()['var_function-call-13891406088243492623']) as f:
    reviews = json.load(f)

# Process books
book_data = []
for b in books:
    bid_str = b.get('book_id', '')
    details = b.get('details', '')
    
    # Extract ID
    match = re.search(r'bookid_(\d+)', bid_str)
    if not match:
        continue
    bid = int(match.group(1))
    
    # Extract Year
    # Pattern: Month (Day,) Year
    # e.g. January 1, 2004 or January 2004
    year_match = re.search(r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+(?:\d{1,2},?\s+)?(\d{4})', details)
    if year_match:
        year = int(year_match.group(1))
        book_data.append({'id': bid, 'year': year})

df_books = pd.DataFrame(book_data)

# Process reviews
review_data = []
for r in reviews:
    pid_str = r.get('purchase_id', '')
    rating_val = r.get('rating', '0')
    try:
        rating = float(rating_val)
    except:
        continue
        
    match = re.search(r'purchaseid_(\d+)', pid_str)
    if not match:
        continue
    pid = int(match.group(1))
    review_data.append({'id': pid, 'rating': rating})

df_reviews = pd.DataFrame(review_data)

# Calculate average rating per book
df_book_ratings = df_reviews.groupby('id')['rating'].mean().reset_index()
df_book_ratings.columns = ['id', 'avg_book_rating']

# Merge
df_merged = pd.merge(df_books, df_book_ratings, on='id')

# Add decade
df_merged['decade'] = (df_merged['year'] // 10) * 10

# Group by decade
stats = df_merged.groupby('decade').agg(
    book_count=('id', 'nunique'),
    decade_avg_rating=('avg_book_rating', 'mean')
).reset_index()

# Filter
filtered = stats[stats['book_count'] >= 10].copy()

# Sort
filtered = filtered.sort_values('decade_avg_rating', ascending=False)

result_list = filtered.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result_list))"""

env_args = {'var_function-call-15304440070204199737': ['books_info'], 'var_function-call-15304440070204199270': ['review'], 'var_function-call-18229384358160094794': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.', 'title': 'Chaucer'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.', 'title': 'Notes from a Kidwatcher'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.', 'title': 'Service: A Navy SEAL at War'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.', 'title': 'Parker & Knight'}], 'var_function-call-18229384358160096831': [{'purchase_id': 'purchaseid_186', 'rating': '4'}, {'purchase_id': 'purchaseid_191', 'rating': '4'}, {'purchase_id': 'purchaseid_190', 'rating': '4'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '4'}], 'var_function-call-16257558540972431529': [{'book_id': 'bookid_1'}, {'book_id': 'bookid_2'}, {'book_id': 'bookid_3'}, {'book_id': 'bookid_4'}, {'book_id': 'bookid_5'}, {'book_id': 'bookid_6'}, {'book_id': 'bookid_7'}, {'book_id': 'bookid_8'}, {'book_id': 'bookid_9'}, {'book_id': 'bookid_10'}], 'var_function-call-16257558540972429796': [{'purchase_id': 'purchaseid_186'}, {'purchase_id': 'purchaseid_191'}, {'purchase_id': 'purchaseid_190'}, {'purchase_id': 'purchaseid_8'}, {'purchase_id': 'purchaseid_178'}, {'purchase_id': 'purchaseid_186'}, {'purchase_id': 'purchaseid_76'}, {'purchase_id': 'purchaseid_186'}, {'purchase_id': 'purchaseid_115'}, {'purchase_id': 'purchaseid_167'}], 'var_function-call-11746651272559848608': [{'count': '200'}], 'var_function-call-11746651272559848043': [{'COUNT(*)': '1833'}], 'var_function-call-13891406088243492122': 'file_storage/function-call-13891406088243492122.json', 'var_function-call-13891406088243492623': 'file_storage/function-call-13891406088243492623.json'}

exec(code, env_args)
