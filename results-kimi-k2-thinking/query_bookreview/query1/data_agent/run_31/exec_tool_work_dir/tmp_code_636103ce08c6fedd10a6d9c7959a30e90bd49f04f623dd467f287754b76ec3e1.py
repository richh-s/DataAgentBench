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
    matches = re.findall(year_pattern, details_str)
    if matches:
        return int(matches[0])
    return None

# Create mapping of book_id to year
book_years = {}
for book in books:
    book_id = book['book_id']
    details = book.get('details', '')
    year = extract_year(details)
    book_years[book_id] = year

# Create mapping of purchase_id to book_id
# purchase_id format like "purchaseid_186" maps to "bookid_..."
# We need to see if there's a pattern - let's check actual IDs
purchase_to_book = {}

# First, let's see what rating_number represents and if it helps
# It seems to be total number of ratings - not useful for joining

# Let's try to understand the mapping better by looking at sample data
sample_books = books[:10]
print("__RESULT__:")
print(json.dumps({
    "book_years_sample": {b['book_id']: book_years[b['book_id']] for b in sample_books},
    "reviews_sample": reviews[:5],
    "purchase_ids_sample": [r['purchase_id'] for r in reviews[:10]]
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'reviews_type': "<class 'str'>", 'books_type': "<class 'str'>", 'reviews_sample': 'Not a list', 'books_sample': 'Not a list', 'total_reviews': 'N/A', 'total_books': 'N/A'}, 'var_functions.execute_python:12': {'reviews_sample': [{'purchase_id': 'purchaseid_186', 'rating': '4'}, {'purchase_id': 'purchaseid_191', 'rating': '4'}, {'purchase_id': 'purchaseid_190', 'rating': '4'}], 'books_sample': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.', 'rating_number': '29'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.', 'rating_number': '1'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.', 'rating_number': '3421'}], 'total_reviews': 1833, 'total_books': 200}}

exec(code, env_args)
