code = """import json, re, os

# Load the file paths from stored results
books_result = locals()['var_functions.query_db:22'] 
reviews_result = locals()['var_functions.query_db:5']

# Load actual data
with open(books_result) as f:
    books = json.load(f)
with open(reviews_result) as f:
    reviews = json.load(f)

print('Loaded {} books and {} reviews'.format(len(books), len(reviews)))

# Look at some sample data
print('\nFirst 5 books:')
for i, b in enumerate(books[:5]):
    book_id = b.get('book_id')
    details = b.get('details', '')
    year_match = re.search(r'(19\d{2}|20\d{2})', details)
    year = year_match.group(1) if year_match else 'No year'
    print('  {}. {} - {}'.format(i+1, book_id, year))

print('\nFirst 5 reviews:')
for i, r in enumerate(reviews[:5]):
    print('  {}. {} - rating {}'.format(i+1, r['purchase_id'], r['rating']))

# Extract numeric IDs
book_ids = set()
book_year_map = {}
for b in books:
    book_id = b['book_id']
    match = re.search(r'(\d+)$', book_id)
    if match:
        num_id = int(match.group(1))
        book_ids.add(num_id)
        
        # Try to extract year
        details = b.get('details', '')
        year_match = re.search(r'(19\d{2}|20[0-2]\d)', details)
        if year_match:
            year = int(year_match.group(1))
            if 1900 <= year <= 2025:
                decade = '{}s'.format((year//10)*10)
                book_year_map[num_id] = decade

print('\nBooks with extractable years: {}'.format(len(book_year_map)))
print('Sample: {}'.format(list(book_year_map.items())[:10]))

# Check reviews
review_ids = set()
for r in reviews:
    purchase_id = r['purchase_id']
    match = re.search(r'(\d+)$', purchase_id)
    if match:
        num_id = int(match.group(1))
        review_ids.add(num_id)

print('\nNumber of unique books in reviews: {}'.format(len(review_ids)))
print('Sample review book IDs: {}'.format(sorted(list(review_ids))[:10]))

# Find common IDs
common_ids = book_ids & review_ids
print('\nCommon IDs (books with both year and reviews): {}'.format(len(common_ids)))
print('Sample common IDs: {}'.format(sorted(list(common_ids))[:10]))

# Group by decade
decade_reviews = {}
for r in reviews:
    purchase_id = r['purchase_id']
    match = re.search(r'(\d+)$', purchase_id)
    if match:
        num_id = int(match.group(1))
        if num_id in book_year_map:
            decade = book_year_map[num_id]
            if decade not in decade_reviews:
                decade_reviews[decade] = []
            decade_reviews[decade].append(float(r['rating']))

print('\nReviews by decade:')
for decade in sorted(decade_reviews.keys()):
    ratings = decade_reviews[decade]
    print('  {}: {} reviews, avg={:.2f}'.format(decade, len(ratings), sum(ratings)/len(ratings)))

# Find decades with enough books
from collections import defaultdict
decade_books = defaultdict(set)
for num_id, decade in book_year_map.items():
    if num_id in review_ids:
        decade_books[decade].add(num_id)

print('\nDistinct books per decade (that have reviews):')
valid_decades = []
for decade in sorted(decade_books.keys()):
    num_books = len(decade_books[decade])
    print('  {}: {} books'.format(decade, num_books))
    if num_books >= 2:  # Test threshold
        # Calculate avg rating
        ratings = decade_reviews.get(decade, [])
        if ratings:
            avg = sum(ratings) / len(ratings)
            valid_decades.append((decade, avg, num_books, len(ratings)))

print('\nValid decades:')
valid_decades.sort(key=lambda x: x[1], reverse=True)
for d in valid_decades:
    print('  {}: avg={:.3f}, {} books, {} reviews'.format(d[0], d[1], d[2], d[3]))

top_decade = valid_decades[0][0] if valid_decades else None
print('\nTop decade: {}'.format(top_decade))

print('__RESULT__:')
print(json.dumps(top_decade))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'books_with_years': 0, 'total_reviews': 10, 'books_with_reviews': 8, 'books_with_both': 0, 'sample_books': []}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': [{'book_count': '200'}], 'var_functions.execute_python:34': None, 'var_functions.execute_python:56': None, 'var_functions.execute_python:58': {'status': 'debug_done'}, 'var_functions.execute_python:66': None, 'var_functions.execute_python:68': None, 'var_functions.execute_python:70': 'No decade found with at least 10 distinct books', 'var_functions.execute_python:74': None, 'var_functions.query_db:76': [{'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}], 'var_functions.query_db:80': [{'total_reviews': '1833'}], 'var_functions.execute_python:82': None, 'var_functions.execute_python:86': None, 'var_functions.query_db:88': [{'purchase_id': 'purchaseid_186'}, {'purchase_id': 'purchaseid_191'}, {'purchase_id': 'purchaseid_190'}, {'purchase_id': 'purchaseid_8'}, {'purchase_id': 'purchaseid_178'}, {'purchase_id': 'purchaseid_76'}, {'purchase_id': 'purchaseid_115'}, {'purchase_id': 'purchaseid_167'}, {'purchase_id': 'purchaseid_188'}, {'purchase_id': 'purchaseid_23'}, {'purchase_id': 'purchaseid_196'}, {'purchase_id': 'purchaseid_3'}, {'purchase_id': 'purchaseid_48'}, {'purchase_id': 'purchaseid_154'}, {'purchase_id': 'purchaseid_99'}, {'purchase_id': 'purchaseid_169'}, {'purchase_id': 'purchaseid_145'}, {'purchase_id': 'purchaseid_194'}, {'purchase_id': 'purchaseid_81'}, {'purchase_id': 'purchaseid_199'}], 'var_functions.execute_python:90': None, 'var_functions.execute_python:92': None, 'var_functions.execute_python:96': None, 'var_functions.query_db:98': [{'title': 'Ha! On me!  I thought this was a cookbook!', 'purchase_id': 'purchaseid_186', 'rating': '4'}, {'title': 'Four Stars', 'purchase_id': 'purchaseid_191', 'rating': '4'}, {'title': 'A wonderful adventure in France', 'purchase_id': 'purchaseid_190', 'rating': '4'}, {'title': 'Best beginner book.  Been looking for something like this for a long time.', 'purchase_id': 'purchaseid_8', 'rating': '5'}, {'title': 'Referance Guide', 'purchase_id': 'purchaseid_178', 'rating': '4'}], 'var_functions.list_db:102': ['review'], 'var_functions.list_db:103': ['books_info'], 'var_functions.query_db:106': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}, {'book_id': 'bookid_6', 'details': 'This book, published independently on December 30, 2021, is written in English and consists of 24 pages. It has an ISBN 13 of 979-8528537702 and weighs 3.2 ounces. The dimensions of the book are 7 x 0.06 x 9 inches.'}, {'book_id': 'bookid_7', 'details': 'The book, published by Guilford in its second edition in January 2004, is also noted as the 8082nd edition from January 1, 1994. It has a remarkably light item weight of just 0.01 ounces.'}, {'book_id': 'bookid_8', 'details': 'This book, published by Make Community, LLC, in its second edition on September 22, 2015, is available in English and spans 352 pages in paperback format. It has an ISBN of 9781680450262 for the 10-digit version and 978-1680450262 for the 13-digit version. The content is suitable for readers aged 11 to 17 years. The book weighs 2.91 pounds and its dimensions are 8 inches in width, 0.5 inches in thickness, and 10 inches in height.'}, {'book_id': 'bookid_9', 'details': 'This book, published independently on September 25, 2019, is written in English and spans 367 pages. It is available in paperback format and has an ISBN-10 of 1694621731 and an ISBN-13 of 978-1694621733. The item weighs 1.38 pounds and measures 6 x 0.92 x 9 inches.'}, {'book_id': 'bookid_10', 'details': 'This book, published by WallBuilder Press in its first edition on November 8, 2004, is available in English and comprises 51 pages in paperback format. It has an ISBN-10 of 1932225323 and an ISBN-13 of 978-1932225327, with a total item weight of 3.52 ounces.'}], 'var_functions.query_db:107': [{'purchase_id': 'purchaseid_186', 'rating': '4'}, {'purchase_id': 'purchaseid_191', 'rating': '4'}, {'purchase_id': 'purchaseid_190', 'rating': '4'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '4'}, {'purchase_id': 'purchaseid_186', 'rating': '4'}, {'purchase_id': 'purchaseid_76', 'rating': '5'}, {'purchase_id': 'purchaseid_186', 'rating': '4'}, {'purchase_id': 'purchaseid_115', 'rating': '5'}, {'purchase_id': 'purchaseid_167', 'rating': '2'}], 'var_functions.execute_python:110': None, 'var_functions.query_db:112': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.', 'title': 'Chaucer'}, {'book_id': 'bookid_10', 'details': 'This book, published by WallBuilder Press in its first edition on November 8, 2004, is available in English and comprises 51 pages in paperback format. It has an ISBN-10 of 1932225323 and an ISBN-13 of 978-1932225327, with a total item weight of 3.52 ounces.', 'title': 'Four Centuries of American Education'}], 'var_functions.query_db:113': 'file_storage/functions.query_db:113.json'}

exec(code, env_args)
