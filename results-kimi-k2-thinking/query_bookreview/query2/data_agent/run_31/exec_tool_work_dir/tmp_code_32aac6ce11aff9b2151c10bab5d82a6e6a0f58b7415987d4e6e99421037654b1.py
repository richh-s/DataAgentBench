code = """import json

# Load the review data from file
review_file_path = locals()['var_functions.query_db:15']
with open(review_file_path, 'r') as f:
    review_data = json.load(f)

# Load the literature books data
literature_books = locals()['var_functions.query_db:14']

# Extract book IDs from literature books
literature_book_ids = [book['book_id'] for book in literature_books]
print('Total Literature & Fiction books: ' + str(len(literature_book_ids)))

# Process review data
# Extract numeric part from purchase_id and match with book_id
from collections import defaultdict

# Create mapping from purchase_id (numeric suffix) to book_id
book_id_mapping = {}
for book_id in literature_book_ids:
    # Extract numeric part from book_id
    num_part = book_id.replace('bookid_', '')
    book_id_mapping[num_part] = book_id

# Group reviews by book and calculate average rating
book_reviews = defaultdict(list)
for review in review_data:
    purchase_id = review['purchase_id']
    # Extract numeric part from purchase_id
    num_part = purchase_id.replace('purchaseid_', '')
    
    # Check if this book_id exists in our literature books
    if num_part in book_id_mapping:
        book_id = book_id_mapping[num_part]
        book_reviews[book_id].append(float(review['rating']))

print('Books with reviews: ' + str(len(book_reviews)))

# Find books with perfect 5.0 average rating
perfect_books = []
for book_id, ratings in book_reviews.items():
    if len(ratings) > 0 and all(r == 5.0 for r in ratings):
        # Get book details
        book_details = next((b for b in literature_books if b['book_id'] == book_id), None)
        if book_details:
            perfect_books.append({
                'book_id': book_id,
                'title': book_details['title'],
                'rating_number': book_details['rating_number'],
                'categories': book_details['categories'],
                'review_count': len(ratings)
            })

print('Books with perfect 5.0 rating: ' + str(len(perfect_books)))

# Format result
result = perfect_books

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:1': ['books_info'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:14': [{'book_id': 'bookid_1', 'title': 'Chaucer', 'categories': '["Books", "Literature & Fiction", "History & Criticism"]', 'rating_number': '29'}, {'book_id': 'bookid_9', 'title': 'Reunion: The Children of Lauderdale Park', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]', 'rating_number': '12'}, {'book_id': 'bookid_13', 'title': 'Girl Made of Glass', 'categories': '["Books", "Literature & Fiction", "Poetry"]', 'rating_number': '117'}, {'book_id': 'bookid_30', 'title': 'Sugary Sweets (A Taste of Love Series)', 'categories': '["Books", "Literature & Fiction", "Humor & Satire"]', 'rating_number': '119'}, {'book_id': 'bookid_36', 'title': 'Therapy Mammals', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]', 'rating_number': '24'}, {'book_id': 'bookid_37', 'title': "A Most Dangerous Book: Tacitus's Germania from the Roman Empire to the Third Reich", 'categories': '["Books", "Literature & Fiction", "History & Criticism"]', 'rating_number': '110'}, {'book_id': 'bookid_38', 'title': 'The Prophet: With Original 1923 Illustrations by the Author', 'categories': '["Books", "Literature & Fiction", "Poetry"]', 'rating_number': '1367'}, {'book_id': 'bookid_39', 'title': 'The Melancholy Strumpet Master', 'categories': '["Books", "Literature & Fiction", "Humor & Satire"]', 'rating_number': '14'}, {'book_id': 'bookid_44', 'title': 'Reptilian', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]', 'rating_number': '162'}, {'book_id': 'bookid_49', 'title': 'Primeval: A Journal of the Uncanny - Issue #1', 'categories': '["Books", "Literature & Fiction", "History & Criticism"]', 'rating_number': '10'}, {'book_id': 'bookid_55', 'title': 'Behind the Wheel (Choose Your Own Adventure #35)(Paperback/Revised)', 'categories': '["Books", "Children\'s Books", "Literature & Fiction"]', 'rating_number': '12'}, {'book_id': 'bookid_69', 'title': 'Out of Sheer Rage: Wrestling with D. H. Lawrence', 'categories': '["Books", "Literature & Fiction", "History & Criticism"]', 'rating_number': '243'}, {'book_id': 'bookid_70', 'title': 'Polly and the Shadow Goblin: Book 2, Mother of Witches', 'categories': '["Books", "Literature & Fiction", "Mythology & Folk Tales"]', 'rating_number': '1'}, {'book_id': 'bookid_74', 'title': 'Child Of The King A Journey of Hope Book 1: Earthly Story With A Heavenly Message', 'categories': '["Books", "Literature & Fiction"]', 'rating_number': '51'}, {'book_id': 'bookid_77', 'title': 'One September Morning', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]', 'rating_number': '95'}, {'book_id': 'bookid_82', 'title': 'Fire Cracker', 'categories': '["Books", "Literature & Fiction", "United States"]', 'rating_number': '3'}, {'book_id': 'bookid_84', 'title': 'Local Honey', 'categories': '["Books", "Literature & Fiction"]', 'rating_number': '4'}, {'book_id': 'bookid_89', 'title': "I'll Ride For My Hood: A Salty Love Story", 'categories': '["Books", "Literature & Fiction", "Dramas & Plays"]', 'rating_number': '122'}, {'book_id': 'bookid_92', 'title': 'Outage', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]', 'rating_number': '5'}, {'book_id': 'bookid_93', 'title': 'Simantov', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]', 'rating_number': '16'}, {'book_id': 'bookid_98', 'title': 'Hollywood Confessions: Hollywood Headlines Book #3 (Hollywood Headlines Mysteries)', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]', 'rating_number': '167'}, {'book_id': 'bookid_99', 'title': 'Buddy the Soldier Bear', 'categories': '["Books", "Children\'s Books", "Literature & Fiction"]', 'rating_number': '100'}, {'book_id': 'bookid_101', 'title': 'Knowing When To Die: Uncollected Stories', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]', 'rating_number': '10'}, {'book_id': 'bookid_106', 'title': 'Looking for Peyton Place: A Novel', 'categories': '["Books", "Literature & Fiction", "Contemporary"]', 'rating_number': '976'}, {'book_id': 'bookid_109', 'title': 'All the Way to the Gallows', 'categories': '["Books", "Literature & Fiction", "Short Stories & Anthologies"]', 'rating_number': '35'}, {'book_id': 'bookid_111', 'title': 'Can You Buy Me The Wind?', 'categories': '["Books", "Children\'s Books", "Literature & Fiction"]', 'rating_number': '17'}, {'book_id': 'bookid_122', 'title': 'Childe Harold of Dysna', 'categories': '["Books", "Literature & Fiction", "History & Criticism"]', 'rating_number': '2'}, {'book_id': 'bookid_137', 'title': 'Oligarchy', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]', 'rating_number': '166'}, {'book_id': 'bookid_142', 'title': 'The Jordan Tracks', 'categories': '["Books", "Literature & Fiction", "Contemporary"]', 'rating_number': '7'}, {'book_id': 'bookid_144', 'title': 'Forged in Blood (Freehold)', 'categories': '["Books", "Literature & Fiction", "Short Stories & Anthologies"]', 'rating_number': '395'}, {'book_id': 'bookid_161', 'title': "Time's Demon: BOOK II OF THE ISLEVALE CYCLE", 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]', 'rating_number': '26'}, {'book_id': 'bookid_167', 'title': 'Dead Silence', 'categories': '["Books", "Christian Books & Bibles", "Literature & Fiction"]', 'rating_number': '406'}, {'book_id': 'bookid_171', 'title': 'Exits, Desires, & Slow Fires', 'categories': '["Books", "Literature & Fiction", "Poetry"]', 'rating_number': '83'}, {'book_id': 'bookid_177', 'title': 'Kennebago Moments', 'categories': '["Books", "Literature & Fiction", "Poetry"]', 'rating_number': '1'}, {'book_id': 'bookid_179', 'title': 'A Cherry Cola Christmas (A Cherry Cola Book Club Novel)', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]', 'rating_number': '64'}, {'book_id': 'bookid_180', 'title': 'The Sludge', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]', 'rating_number': '12'}, {'book_id': 'bookid_182', 'title': 'Liza of Lambeth', 'categories': '["Books", "Literature & Fiction", "Classics"]', 'rating_number': '252'}, {'book_id': 'bookid_187', 'title': 'Consort (A Dark(ish) Faerie Tale Book 3)', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]', 'rating_number': '47'}, {'book_id': 'bookid_188', 'title': "The Vampyre and Other Tales of the Macabre (Oxford World's Classics)", 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]', 'rating_number': '162'}, {'book_id': 'bookid_195', 'title': 'Something That Feels Like Truth (Switchgrass Books)', 'categories': '["Books", "Literature & Fiction", "Short Stories & Anthologies"]', 'rating_number': '3'}], 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json'}

exec(code, env_args)
