code = """import json
import re
from collections import defaultdict

# Read the books data file
books_file = locals()['var_functions.query_db:18']
with open(books_file, 'r') as f:
    books_content = f.read()
books_data = json.loads(books_content)

# Read the reviews data file  
reviews_file = locals()['var_functions.query_db:10']
with open(reviews_file, 'r') as f:
    reviews_content = f.read()
reviews_data = json.loads(reviews_content)

# Extract publication year from details
year_pattern = r'\d{4}'
book_id_to_year = {}
for book in books_data:
    details = book.get('details', '')
    match = re.search(year_pattern, details)
    if match:
        year = int(match.group())
        book_id_to_year[book['book_id']] = year

# Map purchase_id to book_id and collect ratings
purchase_to_book = {}
decade_stats = defaultdict(lambda: {'ratings': [], 'books': set()})

for review in reviews_data:
    if 'rating' in review and 'purchase_id' in review:
        try:
            rating = float(review['rating'])
            purchase_id = review['purchase_id']
            # Match purchase_id format: purchaseid_XXX
            match = re.match(r'purchaseid_(\d+)', purchase_id)
            if match:
                book_num = match.group(1)
                book_id = f'bookid_{book_num}'
                if book_id in book_id_to_year:
                    year = book_id_to_year[book_id]
                    decade = (year // 10) * 10
                    decade_stats[decade]['ratings'].append(rating)
                    decade_stats[decade]['books'].add(book_id)
        except (ValueError, TypeError):
            continue

# Calculate averages for decades with at least 10 distinct books
decade_averages = []
for decade, stats in decade_stats.items():
    num_books = len(stats['books'])
    if num_books >= 10:
        avg_rating = sum(stats['ratings']) / len(stats['ratings'])
        decade_averages.append({
            'decade': f"{decade}s",
            'avg_rating': round(avg_rating, 3),
            'num_books': num_books,
            'num_ratings': len(stats['ratings'])
        })

# Sort by average rating descending
decade_averages.sort(key=lambda x: x['avg_rating'], reverse=True)

result = {
    'total_books_with_year': len(book_id_to_year),
    'total_reviews_matched': sum(len(stats['ratings']) for stats in decade_stats.values()),
    'decades_analyzed': len(decade_averages),
    'top_decades': decade_averages[:5]
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['books_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['review'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
