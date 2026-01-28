code = """import json
import re

# Read the review data from file
review_file = var_functions.query_db:6
with open(review_file, 'r') as f:
    review_data = json.load(f)

# Review data is now in review_data variable
# Let's also load the literature & fiction books data
lit_fiction_books = var_functions.query_db:2

print(f"Total reviews: {len(review_data)}")
print(f"Literature & Fiction books: {len(lit_fiction_books)}")

# Extract book IDs from literature & fiction books
book_ids_lit_fic = [book['book_id'] for book in lit_fiction_books]

# Map purchase_id to book_id (assuming purchaseid_X corresponds to bookid_X)
# Extract numeric part from IDs
book_id_map = {}
for book in lit_fiction_books:
    match = re.search(r'bookid_(\d+)', book['book_id'])
    if match:
        num = int(match.group(1))
        book_id_map[num] = book['book_id']

# Group reviews by book ID
book_reviews = {}
for review in review_data:
    if 'purchase_id' in review and review['purchase_id']:
        match = re.search(r'purchaseid_(\d+)', review['purchase_id'])
        if match:
            purchase_num = int(match.group(1))
            if purchase_num in book_id_map:
                book_id = book_id_map[purchase_num]
                if book_id not in book_reviews:
                    book_reviews[book_id] = []
                book_reviews[book_id].append(float(review['rating']))

# Calculate average ratings for each book
average_ratings = {}
for book_id, ratings in book_reviews.items():
    if ratings:
        avg_rating = sum(ratings) / len(ratings)
        average_ratings[book_id] = {
            'average_rating': avg_rating,
            'review_count': len(ratings),
            'ratings': ratings
        }

# Find books with perfect 5.0 average and at least 1 review
perfect_books = []
for book in lit_fiction_books:
    book_id = book['book_id']
    if book_id in average_ratings:
        avg_info = average_ratings[book_id]
        if avg_info['average_rating'] == 5.0:
            perfect_books.append({
                'book_id': book_id,
                'title': book['title'],
                'categories': book['categories'],
                'review_count': avg_info['review_count']
            })

print(f"Books with perfect 5.0 average rating: {len(perfect_books)}")
for book in perfect_books:
    print(f"  - {book['title']} ({book['book_id']}): {book['review_count']} reviews, avg 5.0")

# Print in required format
result_json = json.dumps(perfect_books, indent=2)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['books_info'], 'var_functions.query_db:2': [{'book_id': 'bookid_1', 'title': 'Chaucer', 'categories': '["Books", "Literature & Fiction", "History & Criticism"]'}, {'book_id': 'bookid_9', 'title': 'Reunion: The Children of Lauderdale Park', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]'}, {'book_id': 'bookid_13', 'title': 'Girl Made of Glass', 'categories': '["Books", "Literature & Fiction", "Poetry"]'}, {'book_id': 'bookid_30', 'title': 'Sugary Sweets (A Taste of Love Series)', 'categories': '["Books", "Literature & Fiction", "Humor & Satire"]'}, {'book_id': 'bookid_36', 'title': 'Therapy Mammals', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]'}, {'book_id': 'bookid_37', 'title': "A Most Dangerous Book: Tacitus's Germania from the Roman Empire to the Third Reich", 'categories': '["Books", "Literature & Fiction", "History & Criticism"]'}, {'book_id': 'bookid_38', 'title': 'The Prophet: With Original 1923 Illustrations by the Author', 'categories': '["Books", "Literature & Fiction", "Poetry"]'}, {'book_id': 'bookid_39', 'title': 'The Melancholy Strumpet Master', 'categories': '["Books", "Literature & Fiction", "Humor & Satire"]'}, {'book_id': 'bookid_44', 'title': 'Reptilian', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]'}, {'book_id': 'bookid_49', 'title': 'Primeval: A Journal of the Uncanny - Issue #1', 'categories': '["Books", "Literature & Fiction", "History & Criticism"]'}, {'book_id': 'bookid_55', 'title': 'Behind the Wheel (Choose Your Own Adventure #35)(Paperback/Revised)', 'categories': '["Books", "Children\'s Books", "Literature & Fiction"]'}, {'book_id': 'bookid_69', 'title': 'Out of Sheer Rage: Wrestling with D. H. Lawrence', 'categories': '["Books", "Literature & Fiction", "History & Criticism"]'}, {'book_id': 'bookid_70', 'title': 'Polly and the Shadow Goblin: Book 2, Mother of Witches', 'categories': '["Books", "Literature & Fiction", "Mythology & Folk Tales"]'}, {'book_id': 'bookid_74', 'title': 'Child Of The King A Journey of Hope Book 1: Earthly Story With A Heavenly Message', 'categories': '["Books", "Literature & Fiction"]'}, {'book_id': 'bookid_77', 'title': 'One September Morning', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]'}, {'book_id': 'bookid_82', 'title': 'Fire Cracker', 'categories': '["Books", "Literature & Fiction", "United States"]'}, {'book_id': 'bookid_84', 'title': 'Local Honey', 'categories': '["Books", "Literature & Fiction"]'}, {'book_id': 'bookid_89', 'title': "I'll Ride For My Hood: A Salty Love Story", 'categories': '["Books", "Literature & Fiction", "Dramas & Plays"]'}, {'book_id': 'bookid_92', 'title': 'Outage', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]'}, {'book_id': 'bookid_93', 'title': 'Simantov', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]'}, {'book_id': 'bookid_98', 'title': 'Hollywood Confessions: Hollywood Headlines Book #3 (Hollywood Headlines Mysteries)', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]'}, {'book_id': 'bookid_99', 'title': 'Buddy the Soldier Bear', 'categories': '["Books", "Children\'s Books", "Literature & Fiction"]'}, {'book_id': 'bookid_101', 'title': 'Knowing When To Die: Uncollected Stories', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]'}, {'book_id': 'bookid_106', 'title': 'Looking for Peyton Place: A Novel', 'categories': '["Books", "Literature & Fiction", "Contemporary"]'}, {'book_id': 'bookid_109', 'title': 'All the Way to the Gallows', 'categories': '["Books", "Literature & Fiction", "Short Stories & Anthologies"]'}, {'book_id': 'bookid_111', 'title': 'Can You Buy Me The Wind?', 'categories': '["Books", "Children\'s Books", "Literature & Fiction"]'}, {'book_id': 'bookid_122', 'title': 'Childe Harold of Dysna', 'categories': '["Books", "Literature & Fiction", "History & Criticism"]'}, {'book_id': 'bookid_137', 'title': 'Oligarchy', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]'}, {'book_id': 'bookid_142', 'title': 'The Jordan Tracks', 'categories': '["Books", "Literature & Fiction", "Contemporary"]'}, {'book_id': 'bookid_144', 'title': 'Forged in Blood (Freehold)', 'categories': '["Books", "Literature & Fiction", "Short Stories & Anthologies"]'}, {'book_id': 'bookid_161', 'title': "Time's Demon: BOOK II OF THE ISLEVALE CYCLE", 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]'}, {'book_id': 'bookid_167', 'title': 'Dead Silence', 'categories': '["Books", "Christian Books & Bibles", "Literature & Fiction"]'}, {'book_id': 'bookid_171', 'title': 'Exits, Desires, & Slow Fires', 'categories': '["Books", "Literature & Fiction", "Poetry"]'}, {'book_id': 'bookid_177', 'title': 'Kennebago Moments', 'categories': '["Books", "Literature & Fiction", "Poetry"]'}, {'book_id': 'bookid_179', 'title': 'A Cherry Cola Christmas (A Cherry Cola Book Club Novel)', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]'}, {'book_id': 'bookid_180', 'title': 'The Sludge', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]'}, {'book_id': 'bookid_182', 'title': 'Liza of Lambeth', 'categories': '["Books", "Literature & Fiction", "Classics"]'}, {'book_id': 'bookid_187', 'title': 'Consort (A Dark(ish) Faerie Tale Book 3)', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]'}, {'book_id': 'bookid_188', 'title': "The Vampyre and Other Tales of the Macabre (Oxford World's Classics)", 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]'}, {'book_id': 'bookid_195', 'title': 'Something That Feels Like Truth (Switchgrass Books)', 'categories': '["Books", "Literature & Fiction", "Short Stories & Anthologies"]'}], 'var_functions.list_db:4': ['review'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
