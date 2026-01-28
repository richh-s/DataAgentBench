code = """import json
import re

# Access the reviews and books from file paths
reviews_path = locals()['var_functions.query_db:5']
books_path = locals()['var_functions.query_db:6']

with open(reviews_path, 'r') as f:
    reviews = json.load(f)

with open(books_path, 'r') as f:
    books = json.load(f)

# Parse year from book details
year_pattern = r'(?:\b|\D)(1[5-9][0-9]{2}|20[0-3][0-9])(?:\b|\D)'

def extract_year(details_str):
    if not details_str:
        return None
    matches = re.findall(year_pattern, details_str)
    if matches:
        return int(matches[0])
    return None

# Create mapping of book_id to year and decade
book_info = {}
for book in books:
    book_id = book['book_id']
    details = book.get('details', '')
    year = extract_year(details)
    decade = f"{year//10*10}s" if year else None
    
    book_info[book_id] = {
        'year': year,
        'decade': decade
    }

# Create mapping of purchase_id to book_id by extracting the number
purchase_to_book = {}
for review in reviews:
    purchase_id = review['purchase_id']
    # Extract number from purchase_id (e.g., "purchaseid_186" -> 186)
    match = re.search(r'purchaseid_(\d+)', purchase_id)
    if match:
        num = int(match.group(1))
        book_id = f"bookid_{num}"
        if book_id in book_info:
            purchase_to_book[purchase_id] = book_id

# Aggregate ratings by book
book_ratings = {}
for review in reviews:
    purchase_id = review['purchase_id']
    if purchase_id in purchase_to_book:
        book_id = purchase_to_book[purchase_id]
        
        if book_id not in book_ratings:
            book_ratings[book_id] = []
        
        try:
            rating = float(review['rating'])
            book_ratings[book_id].append(rating)
        except (ValueError, TypeError):
            continue

# Calculate average rating per book and aggregate by decade
decade_stats = {}
books_with_decade = 0

for book_id, ratings in book_ratings.items():
    if book_id in book_info and book_info[book_id]['decade']:
        decade = book_info[book_id]['decade']
        year = book_info[book_id]['year']
        
        if decade not in decade_stats:
            decade_stats[decade] = {
                'total_ratings': 0,
                'sum_ratings': 0.0,
                'books': set(),
                'books_with_ratings': 0
            }
        
        avg_rating = sum(ratings) / len(ratings)
        decade_stats[decade]['total_ratings'] += len(ratings)
        decade_stats[decade]['sum_ratings'] += avg_rating * len(ratings)
        decade_stats[decade]['books'].add(book_id)
        decade_stats[decade]['books_with_ratings'] += 1
        books_with_decade += 1

# Filter decades with at least 10 distinct books and calculate average rating
valid_decades = []
for decade, stats in decade_stats.items():
    if stats['books_with_ratings'] >= 10:
        avg_rating = stats['sum_ratings'] / stats['total_ratings']
        valid_decades.append({
            'decade': decade,
            'avg_rating': avg_rating,
            'book_count': stats['books_with_ratings'],
            'total_rating_count': stats['total_ratings']
        })

# Sort by average rating descending
valid_decades.sort(key=lambda x: x['avg_rating'], reverse=True)

print("__RESULT__:")
print(json.dumps({
    "valid_decades": valid_decades,
    "total_books_with_ratings_and_decade": books_with_decade,
    "total_decades_considered": len(valid_decades)
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'reviews_type': "<class 'str'>", 'books_type': "<class 'str'>", 'reviews_sample': 'Not a list', 'books_sample': 'Not a list', 'total_reviews': 'N/A', 'total_books': 'N/A'}, 'var_functions.execute_python:12': {'reviews_sample': [{'purchase_id': 'purchaseid_186', 'rating': '4'}, {'purchase_id': 'purchaseid_191', 'rating': '4'}, {'purchase_id': 'purchaseid_190', 'rating': '4'}], 'books_sample': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.', 'rating_number': '29'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.', 'rating_number': '1'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.', 'rating_number': '3421'}], 'total_reviews': 1833, 'total_books': 200}, 'var_functions.execute_python:14': {'book_years_sample': {'bookid_1': 2004, 'bookid_2': 1996, 'bookid_3': 2012, 'bookid_4': 2013, 'bookid_5': 2014, 'bookid_6': 2021, 'bookid_7': 2004, 'bookid_8': 2015, 'bookid_9': 2019, 'bookid_10': 2004}, 'reviews_sample': [{'purchase_id': 'purchaseid_186', 'rating': '4'}, {'purchase_id': 'purchaseid_191', 'rating': '4'}, {'purchase_id': 'purchaseid_190', 'rating': '4'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '4'}], 'purchase_ids_sample': ['purchaseid_186', 'purchaseid_191', 'purchaseid_190', 'purchaseid_8', 'purchaseid_178', 'purchaseid_186', 'purchaseid_76', 'purchaseid_186', 'purchaseid_115', 'purchaseid_167']}}

exec(code, env_args)
