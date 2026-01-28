code = """import json
import re

# Load the data
books_file = locals()['var_functions.query_db:10']
reviews_file = locals()['var_functions.query_db:12']

with open(books_file, 'r') as f:
    books_data = json.load(f)

with open(reviews_file, 'r') as f:
    reviews_data = json.load(f)

# Create mapping from book_id to decade
book_decades = {}
for book in books_data:
    details = book.get('details', '')
    year_match = re.search(r'(\d{4})', details)
    if year_match:
        year = int(year_match.group(1))
        decade = (year // 10) * 10
        book_decades[book['book_id']] = decade

# Map reviews to books and calculate ratings per decade
# purchase_id format: purchaseid_XXX, book_id format: bookid_XXX
decade_ratings = {}
decade_books = {}

for review in reviews_data:
    purchase_id = review['purchase_id']
    rating = float(review['rating'])
    
    # Extract numeric part from purchase_id
    match = re.search(r'purchaseid_(\d+)', purchase_id)
    if match:
        book_num = match.group(1)
        book_id = f'bookid_{book_num}'
        
        if book_id in book_decades:
            decade = book_decades[book_id]
            
            if decade not in decade_ratings:
                decade_ratings[decade] = []
                decade_books[decade] = set()
            
            decade_ratings[decade].append(rating)
            decade_books[decade].add(book_id)

# Calculate average ratings for decades with at least 10 distinct books
decade_stats = []
for decade in decade_ratings:
    num_books = len(decade_books[decade])
    if num_books >= 10:
        avg_rating = sum(decade_ratings[decade]) / len(decade_ratings[decade])
        decade_stats.append({
            'decade': decade,
            'avg_rating': round(avg_rating, 2),
            'num_books': num_books,
            'total_reviews': len(decade_ratings[decade])
        })

# Sort by average rating descending
decade_stats.sort(key=lambda x: x['avg_rating'], reverse=True)

print('__RESULT__:')
print(json.dumps({
    'decades_analyzed': len(decade_stats),
    'top_decades': decade_stats[:5],
    'all_decades': decade_stats
}))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'book_id': 'bookid_1', 'title': 'Chaucer', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'title': 'Notes from a Kidwatcher', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'title': 'Service: A Navy SEAL at War', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'title': 'Parker & Knight', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}, {'book_id': 'bookid_6', 'title': 'Writings from a Black Woman Living in the Land of the "Free": Strength, Power, Resilience', 'details': 'This book, published independently on December 30, 2021, is written in English and consists of 24 pages. It has an ISBN 13 of 979-8528537702 and weighs 3.2 ounces. The dimensions of the book are 7 x 0.06 x 9 inches.'}, {'book_id': 'bookid_7', 'title': "Child Development: A Practitioner's Guide:2nd (Second) edition", 'details': 'The book, published by Guilford in its second edition in January 2004, is also noted as the 8082nd edition from January 1, 1994. It has a remarkably light item weight of just 0.01 ounces.'}, {'book_id': 'bookid_8', 'title': 'Make: Electronics: Learning Through Discovery', 'details': 'This book, published by Make Community, LLC, in its second edition on September 22, 2015, is available in English and spans 352 pages in paperback format. It has an ISBN of 9781680450262 for the 10-digit version and 978-1680450262 for the 13-digit version. The content is suitable for readers aged 11 to 17 years. The book weighs 2.91 pounds and its dimensions are 8 inches in width, 0.5 inches in thickness, and 10 inches in height.'}, {'book_id': 'bookid_9', 'title': 'Reunion: The Children of Lauderdale Park', 'details': 'This book, published independently on September 25, 2019, is written in English and spans 367 pages. It is available in paperback format and has an ISBN-10 of 1694621731 and an ISBN-13 of 978-1694621733. The item weighs 1.38 pounds and measures 6 x 0.92 x 9 inches.'}, {'book_id': 'bookid_10', 'title': 'Four Centuries of American Education', 'details': 'This book, published by WallBuilder Press in its first edition on November 8, 2004, is available in English and comprises 51 pages in paperback format. It has an ISBN-10 of 1932225323 and an ISBN-13 of 978-1932225327, with a total item weight of 3.52 ounces.'}], 'var_functions.execute_python:8': {'sample_books': [{'book_id': 'bookid_1', 'title': 'Chaucer', 'year': 2004}, {'book_id': 'bookid_2', 'title': 'Notes from a Kidwatcher', 'year': 1996}, {'book_id': 'bookid_3', 'title': 'Service: A Navy SEAL at War', 'year': 2012}, {'book_id': 'bookid_4', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still', 'year': 2013}, {'book_id': 'bookid_5', 'title': 'Parker & Knight', 'year': 2014}], 'year_range': '1996 to 2021', 'total_with_years': 10}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:18': {'total_books': 200, 'total_reviews': 1833, 'books_with_years': 193, 'sample_books': [{'book_id': 'bookid_1', 'title': 'Chaucer', 'year': 2004, 'decade': 2000}, {'book_id': 'bookid_2', 'title': 'Notes from a Kidwatcher', 'year': 1996, 'decade': 1990}, {'book_id': 'bookid_3', 'title': 'Service: A Navy SEAL at War', 'year': 2012, 'decade': 2010}], 'unique_books_rated': 200, 'sample_reviews': [['purchaseid_186', [4.0, 4.0, 4.0, 5.0, 5.0, 4.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 4.0, 5.0, 5.0, 5.0, 4.0, 4.0, 5.0, 5.0, 5.0, 4.0, 5.0, 5.0, 5.0, 5.0, 4.0, 5.0, 4.0, 5.0, 4.0, 4.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 3.0, 5.0, 5.0, 5.0, 4.0, 5.0, 4.0, 5.0, 5.0, 3.0, 5.0, 4.0, 5.0, 4.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 4.0, 4.0, 5.0, 5.0, 2.0, 5.0, 4.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0]], ['purchaseid_191', [4.0, 4.0, 5.0]], ['purchaseid_190', [4.0, 5.0, 5.0, 5.0, 5.0, 4.0, 5.0, 5.0, 5.0, 4.0, 4.0, 5.0, 4.0, 4.0, 5.0, 4.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 2.0, 4.0, 4.0, 4.0, 4.0, 5.0, 4.0, 4.0, 4.0, 5.0, 5.0]]]}}

exec(code, env_args)
