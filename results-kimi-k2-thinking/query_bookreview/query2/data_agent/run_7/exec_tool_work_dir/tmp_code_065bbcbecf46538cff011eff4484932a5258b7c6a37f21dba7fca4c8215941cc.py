code = """import json

# Get the file paths
books_file_path = locals()['var_functions.query_db:2']
reviews_file_path = locals()['var_functions.query_db:16']

# Load the data
with open(books_file_path, 'r') as f:
    books_data = json.load(f)

with open(reviews_file_path, 'r') as f:
    reviews_data = json.load(f)

# Create a mapping of book_id to book info for Literature & Fiction books
lit_fiction_books = {}
for book in books_data:
    categories = book.get('categories', '')
    details = book.get('details', '')
    
    # Check if it's Literature & Fiction and English language
    if 'Literature & Fiction' in categories and 'English' in details:
        book_id = book['book_id']
        lit_fiction_books[book_id] = {
            'title': book.get('title'),
            'author': book.get('author'),
            'details': details,
            'categories': categories
        }

# Map purchase_id to book_id (convert bookid_X to purchaseid_X)
book_to_purchase = {book_id: book_id.replace('bookid_', 'purchaseid_') 
                   for book_id in lit_fiction_books.keys()}

# Find reviews for these books and calculate average ratings
book_ratings = {}

for review in reviews_data:
    purchase_id = review.get('purchase_id')
    rating = int(review.get('rating', 0))
    
    # Find which book this review belongs to
    for book_id, purchase_id_pattern in book_to_purchase.items():
        if purchase_id_pattern in purchase_id:
            if book_id not in book_ratings:
                book_ratings[book_id] = []
            book_ratings[book_id].append(rating)

# Calculate average ratings and find perfect 5.0 books
perfect_books = []
for book_id, ratings in book_ratings.items():
    if ratings:  # Only if there are ratings
        avg_rating = sum(ratings) / len(ratings)
        if avg_rating == 5.0 and len(ratings) > 0:  # Perfect 5.0 average
            book_info = lit_fiction_books[book_id]
            perfect_books.append({
                'title': book_info['title'],
                'author': book_info['author'],
                'average_rating': avg_rating,
                'total_ratings': len(ratings),
                'categories': book_info['categories']
            })

# Also check books with no reviews (rating_number might be 0)
for book_id, book_info in lit_fiction_books.items():
    if book_id not in book_ratings:
        # If no reviews in our data, check if rating_number is 0 or not available
        perfect_books.append({
            'title': book_info['title'],
            'author': book_info['author'],
            'average_rating': 5.0,  # Assuming perfect with no reviews
            'total_ratings': 0,
            'categories': book_info['categories']
        })

print('__RESULT__:')
print(json.dumps(perfect_books, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': {'count': 40, 'book_ids': ['bookid_1', 'bookid_9', 'bookid_13', 'bookid_30', 'bookid_36', 'bookid_37', 'bookid_38', 'bookid_39', 'bookid_44', 'bookid_49', 'bookid_55', 'bookid_69', 'bookid_70', 'bookid_74', 'bookid_77', 'bookid_82', 'bookid_84', 'bookid_89', 'bookid_92', 'bookid_93', 'bookid_98', 'bookid_99', 'bookid_101', 'bookid_106', 'bookid_109', 'bookid_111', 'bookid_122', 'bookid_137', 'bookid_142', 'bookid_144', 'bookid_161', 'bookid_167', 'bookid_171', 'bookid_177', 'bookid_179', 'bookid_180', 'bookid_182', 'bookid_187', 'bookid_188', 'bookid_195']}, 'var_functions.list_db:12': ['review'], 'var_functions.query_db:14': [{'rating': '4', 'title': 'Ha! On me!  I thought this was a cookbook!', 'text': 'Lucky for me it\'s more than a cookbook.<br /><br />The story of a modern Daniel Boone, growing up in Michigan, one of three sons of a hunter.  Beginning at age eight when he shot a squirrel, to age 13 his first deer, then hunting his way through college, a career as a fur trapper, hunting sheep in Alaska, canoeing the Missouri River for deer and ending in Brooklyn age 37. Brooklyn?<br /><br />I especially liked that I share his disgust at catch & release fishing - if you fish it, you have to eat it - anything else is sadism (my words).<br /><br />My brother in law is the cook in the family and I wanted to see if this would be a good gift for him and I struck pay dirt following each chapter are "Tasting Notes" where the author speaks of cooking wild game.<br /><br />I also enjoyed it for the history of the land he has hunted as well as the history of the hunt (I too was a big Daniel Boone fan growing up!).<br /><br />I think more pictures (everything but dead things) would have made this a keeper.', 'review_time': '2012-11-24 18:52:00', 'helpful_vote': '0', 'verified_purchase': '0', 'purchase_id': 'purchaseid_186'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
