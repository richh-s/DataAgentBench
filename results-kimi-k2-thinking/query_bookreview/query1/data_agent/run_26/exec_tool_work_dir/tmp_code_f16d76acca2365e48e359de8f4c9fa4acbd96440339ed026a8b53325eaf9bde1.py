code = """import json, re, os

# Load data from stored file paths
books_path = locals()['var_functions.query_db:128']
reviews_path = locals()['var_functions.query_db:129']

# Read files and parse JSON
with open(books_path, 'r') as f:
    books_data = json.load(f)

with open(reviews_path, 'r') as f:
    reviews_data = json.load(f)

print('Loaded {} books and {} reviews'.format(len(books_data), len(reviews_data)))

# Extract publication year from book details using regex
def extract_publication_year(details_str):
    if not details_str or not isinstance(details_str, str):
        return None
    
    # Pattern 1: "released on January 1, 2004" or "on May 20, 1996"
    pattern1 = r'(?:released\s+)?(?:on\s+)?(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+(\d{4})'
    match = re.search(pattern1, details_str, re.IGNORECASE)
    if match:
        year = int(match.group(1))
        if 1900 <= year <= 2025:
            return year
    
    # Pattern 2: Any year between 1900-2025
    pattern2 = r'\b(19\d{2}|20[0-2]\d)\b'
    match = re.search(pattern2, details_str)
    if match:
        year = int(match.group(1))
        if 1900 <= year <= 2025:
            return year
    
    return None

# Map numeric book IDs to publication decades
book_id_to_decade = {}
successful_extractions = 0

for book in books_data:
    numeric_id = book.get('num_id')
    if numeric_id:
        try:
            numeric_id = int(numeric_id)
            details = book.get('details', '')
            year = extract_publication_year(details)
            
            if year:
                decade = '{}s'.format((year // 10) * 10)
                book_id_to_decade[numeric_id] = decade
                successful_extractions += 1
        except (ValueError, TypeError):
            continue

print('Successfully extracted publication years for {} books'.format(successful_extractions))
print('Sample mapping (numeric_id -> decade):', list(book_id_to_decade.items())[:10])

# Group reviews by decade
from collections import defaultdict
decade_stats = defaultdict(lambda: {'books': set(), 'sum_ratings': 0.0, 'review_count': 0})
processed_reviews = 0

for review in reviews_data:
    try:
        numeric_id = int(review.get('num_id', 0))
        rating = float(review.get('rating', 0))
        
        if numeric_id and numeric_id in book_id_to_decade:
            decade = book_id_to_decade[numeric_id]
            
            decade_stats[decade]['books'].add(numeric_id)
            decade_stats[decade]['sum_ratings'] += rating
            decade_stats[decade]['review_count'] += 1
            processed_reviews += 1
    except (ValueError, TypeError):
        continue

print('Matched {} reviews to books with publication years'.format(processed_reviews))
print('Decades with reviews:', list(decade_stats.keys()))

# Calculate average ratings for each decade and filter for >= 10 distinct books
decade_averages = []
for decade, stats in decade_stats.items():
    distinct_books = len(stats['books'])
    if distinct_books >= 10:
        avg_rating = stats['sum_ratings'] / stats['review_count']
        decade_averages.append((decade, avg_rating, distinct_books, stats['review_count']))

# Sort by average rating descending
decade_averages.sort(key=lambda x: x[1], reverse=True)

print('\nDecades with >= 10 distinct books: {}'.format(len(decade_averages)))
for i, (decade, avg_rating, books, reviews) in enumerate(decade_averages, 1):
    print('{}. {}: avg_rating={:.3f}, {} books, {} reviews'.format(i, decade, avg_rating, books, reviews))

# Get the decade with the highest average rating
top_decade = decade_averages[0][0] if decade_averages else None
print('\nTop decade:', top_decade)

print('__RESULT__:')
print(json.dumps(top_decade))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'books_with_years': 0, 'total_reviews': 10, 'books_with_reviews': 8, 'books_with_both': 0, 'sample_books': []}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': [{'book_count': '200'}], 'var_functions.execute_python:34': None, 'var_functions.execute_python:56': None, 'var_functions.execute_python:58': {'status': 'debug_done'}, 'var_functions.execute_python:66': None, 'var_functions.execute_python:68': None, 'var_functions.execute_python:70': 'No decade found with at least 10 distinct books', 'var_functions.execute_python:74': None, 'var_functions.query_db:76': [{'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}], 'var_functions.query_db:80': [{'total_reviews': '1833'}], 'var_functions.execute_python:82': None, 'var_functions.execute_python:86': None, 'var_functions.query_db:88': [{'purchase_id': 'purchaseid_186'}, {'purchase_id': 'purchaseid_191'}, {'purchase_id': 'purchaseid_190'}, {'purchase_id': 'purchaseid_8'}, {'purchase_id': 'purchaseid_178'}, {'purchase_id': 'purchaseid_76'}, {'purchase_id': 'purchaseid_115'}, {'purchase_id': 'purchaseid_167'}, {'purchase_id': 'purchaseid_188'}, {'purchase_id': 'purchaseid_23'}, {'purchase_id': 'purchaseid_196'}, {'purchase_id': 'purchaseid_3'}, {'purchase_id': 'purchaseid_48'}, {'purchase_id': 'purchaseid_154'}, {'purchase_id': 'purchaseid_99'}, {'purchase_id': 'purchaseid_169'}, {'purchase_id': 'purchaseid_145'}, {'purchase_id': 'purchaseid_194'}, {'purchase_id': 'purchaseid_81'}, {'purchase_id': 'purchaseid_199'}], 'var_functions.execute_python:90': None, 'var_functions.execute_python:92': None, 'var_functions.execute_python:96': None, 'var_functions.query_db:98': [{'title': 'Ha! On me!  I thought this was a cookbook!', 'purchase_id': 'purchaseid_186', 'rating': '4'}, {'title': 'Four Stars', 'purchase_id': 'purchaseid_191', 'rating': '4'}, {'title': 'A wonderful adventure in France', 'purchase_id': 'purchaseid_190', 'rating': '4'}, {'title': 'Best beginner book.  Been looking for something like this for a long time.', 'purchase_id': 'purchaseid_8', 'rating': '5'}, {'title': 'Referance Guide', 'purchase_id': 'purchaseid_178', 'rating': '4'}], 'var_functions.list_db:102': ['review'], 'var_functions.list_db:103': ['books_info'], 'var_functions.query_db:106': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}, {'book_id': 'bookid_6', 'details': 'This book, published independently on December 30, 2021, is written in English and consists of 24 pages. It has an ISBN 13 of 979-8528537702 and weighs 3.2 ounces. The dimensions of the book are 7 x 0.06 x 9 inches.'}, {'book_id': 'bookid_7', 'details': 'The book, published by Guilford in its second edition in January 2004, is also noted as the 8082nd edition from January 1, 1994. It has a remarkably light item weight of just 0.01 ounces.'}, {'book_id': 'bookid_8', 'details': 'This book, published by Make Community, LLC, in its second edition on September 22, 2015, is available in English and spans 352 pages in paperback format. It has an ISBN of 9781680450262 for the 10-digit version and 978-1680450262 for the 13-digit version. The content is suitable for readers aged 11 to 17 years. The book weighs 2.91 pounds and its dimensions are 8 inches in width, 0.5 inches in thickness, and 10 inches in height.'}, {'book_id': 'bookid_9', 'details': 'This book, published independently on September 25, 2019, is written in English and spans 367 pages. It is available in paperback format and has an ISBN-10 of 1694621731 and an ISBN-13 of 978-1694621733. The item weighs 1.38 pounds and measures 6 x 0.92 x 9 inches.'}, {'book_id': 'bookid_10', 'details': 'This book, published by WallBuilder Press in its first edition on November 8, 2004, is available in English and comprises 51 pages in paperback format. It has an ISBN-10 of 1932225323 and an ISBN-13 of 978-1932225327, with a total item weight of 3.52 ounces.'}], 'var_functions.query_db:107': [{'purchase_id': 'purchaseid_186', 'rating': '4'}, {'purchase_id': 'purchaseid_191', 'rating': '4'}, {'purchase_id': 'purchaseid_190', 'rating': '4'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '4'}, {'purchase_id': 'purchaseid_186', 'rating': '4'}, {'purchase_id': 'purchaseid_76', 'rating': '5'}, {'purchase_id': 'purchaseid_186', 'rating': '4'}, {'purchase_id': 'purchaseid_115', 'rating': '5'}, {'purchase_id': 'purchaseid_167', 'rating': '2'}], 'var_functions.execute_python:110': None, 'var_functions.query_db:112': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.', 'title': 'Chaucer'}, {'book_id': 'bookid_10', 'details': 'This book, published by WallBuilder Press in its first edition on November 8, 2004, is available in English and comprises 51 pages in paperback format. It has an ISBN-10 of 1932225323 and an ISBN-13 of 978-1932225327, with a total item weight of 3.52 ounces.', 'title': 'Four Centuries of American Education'}], 'var_functions.query_db:113': 'file_storage/functions.query_db:113.json', 'var_functions.execute_python:118': None, 'var_functions.execute_python:122': None, 'var_functions.query_db:124': 'file_storage/functions.query_db:124.json', 'var_functions.query_db:128': 'file_storage/functions.query_db:128.json', 'var_functions.query_db:129': 'file_storage/functions.query_db:129.json'}

exec(code, env_args)
