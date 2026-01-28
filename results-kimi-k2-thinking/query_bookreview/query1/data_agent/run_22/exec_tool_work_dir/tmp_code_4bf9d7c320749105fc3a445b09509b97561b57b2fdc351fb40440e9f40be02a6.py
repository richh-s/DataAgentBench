code = """import json
import re
from collections import defaultdict
import pandas as pd

# Load the full data from files
books_file = locals()['var_functions.query_db:18']
reviews_file = locals()['var_functions.query_db:10']

books_data = []
with open(books_file, 'r') as f:
    for line in f:
        books_data.extend(json.loads(line))

reviews_data = []
with open(reviews_file, 'r') as f:
    for line in f:
        reviews_data.extend(json.loads(line))

# Extract year from details
year_pattern = r'\d{4}'
books_with_year = []
for book in books_data:
    details = book.get('details', '')
    match = re.search(year_pattern, details)
    if match:
        year = int(match.group())
        book['publication_year'] = year
        books_with_year.append(book)

# Create mappings
book_id_to_year = {book['book_id']: book['publication_year'] for book in books_with_year}

# Get reviews with ratings and purchase_id
valid_reviews = []
for review in reviews_data:
    if 'rating' in review and 'purchase_id' in review:
        try:
            rating = float(review['rating'])
            purchase_id = review['purchase_id']
            # Extract book_id from purchase_id (format: purchaseid_XXX)
            match = re.search(r'purchaseid_(\d+)', purchase_id)
            if match:
                book_num = match.group(1)
                book_id = f'bookid_{book_num}'
                if book_id in book_id_to_year:
                    valid_reviews.append({
                        'book_id': book_id,
                        'rating': rating,
                        'year': book_id_to_year[book_id]
                    })
        except (ValueError, TypeError):
            continue

# Group by decade
decade_stats = defaultdict(lambda: {'ratings': [], 'books': set()})
for review in valid_reviews:
    decade = (review['year'] // 10) * 10
    decade_stats[decade]['ratings'].append(review['rating'])
    decade_stats[decade]['books'].add(review['book_id'])

# Calculate average ratings for decades with at least 10 distinct books
decade_averages = []
for decade, stats in decade_stats.items():
    if len(stats['books']) >= 10:
        avg_rating = sum(stats['ratings']) / len(stats['ratings'])
        decade_averages.append({
            'decade': decade,
            'avg_rating': avg_rating,
            'num_books': len(stats['books']),
            'num_ratings': len(stats['ratings'])
        })

# Sort by average rating descending
decade_averages.sort(key=lambda x: x['avg_rating'], reverse=True)

print('__RESULT__:')
print(json.dumps({
    'total_books_with_year': len(books_with_year),
    'total_valid_reviews': len(valid_reviews),
    'decades': decade_averages[:10]  # Show top 10 decades
}))"""

env_args = {'var_functions.list_db:0': ['books_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['review'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
