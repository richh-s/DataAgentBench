code = """import json
import pandas as pd

# Read the literature & fiction books data
books_file = var_functions.query_db:16
with open(books_file, 'r') as f:
    books_data = json.load(f)

# Read the reviews data
reviews_file = var_functions.query_db:14
with open(reviews_file, 'r') as f:
    reviews_data = json.load(f)

# Create DataFrames
books_df = pd.DataFrame(books_data)
reviews_df = pd.DataFrame(reviews_data)

# Convert rating to numeric
reviews_df['rating'] = pd.to_numeric(reviews_df['rating'])

# Extract book ID numbers for comparison
books_df['book_id_num'] = books_df['book_id'].str.extract('(\d+)').astype(int)
reviews_df['purchase_id_num'] = reviews_df['purchase_id'].str.extract('(\d+)').astype(int)

# Join DataFrames
merged_df = reviews_df.merge(books_df, left_on='purchase_id_num', right_on='book_id_num', how='inner')

# Calculate average rating per book
avg_ratings = merged_df.groupby(['book_id', 'title', 'categories']).agg({'rating': ['mean', 'count']}).reset_index()
avg_ratings.columns = ['book_id', 'title', 'categories', 'avg_rating', 'review_count']

# Filter for perfect 5.0 average rating
perfect_books = avg_ratings[avg_ratings['avg_rating'] == 5.0]

# Get full book details for perfect rating books
perfect_book_ids = perfect_books['book_id'].tolist()
perfect_book_details = books_df[books_df['book_id'].isin(perfect_book_ids)][['book_id', 'title', 'categories']]

# Add rating info
result = perfect_book_details.merge(perfect_books[['book_id', 'avg_rating', 'review_count']], on='book_id')

# Sort by review count (descending) to show books with most reviews first
result = result.sort_values('review_count', ascending=False)

# Convert to JSON and print
result_json = result.to_json(orient='records', indent=2)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['books_info'], 'var_functions.list_db:2': ['review'], 'var_functions.query_db:4': [{'book_id': 'bookid_1', 'title': 'Chaucer', 'categories': '["Books", "Literature & Fiction", "History & Criticism"]'}, {'book_id': 'bookid_9', 'title': 'Reunion: The Children of Lauderdale Park', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]'}, {'book_id': 'bookid_13', 'title': 'Girl Made of Glass', 'categories': '["Books", "Literature & Fiction", "Poetry"]'}, {'book_id': 'bookid_30', 'title': 'Sugary Sweets (A Taste of Love Series)', 'categories': '["Books", "Literature & Fiction", "Humor & Satire"]'}, {'book_id': 'bookid_36', 'title': 'Therapy Mammals', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]'}, {'book_id': 'bookid_37', 'title': "A Most Dangerous Book: Tacitus's Germania from the Roman Empire to the Third Reich", 'categories': '["Books", "Literature & Fiction", "History & Criticism"]'}, {'book_id': 'bookid_38', 'title': 'The Prophet: With Original 1923 Illustrations by the Author', 'categories': '["Books", "Literature & Fiction", "Poetry"]'}, {'book_id': 'bookid_39', 'title': 'The Melancholy Strumpet Master', 'categories': '["Books", "Literature & Fiction", "Humor & Satire"]'}, {'book_id': 'bookid_44', 'title': 'Reptilian', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]'}, {'book_id': 'bookid_49', 'title': 'Primeval: A Journal of the Uncanny - Issue #1', 'categories': '["Books", "Literature & Fiction", "History & Criticism"]'}], 'var_functions.query_db:6': [{'purchase_id': 'purchaseid_186', 'title': 'Ha! On me!  I thought this was a cookbook!', 'rating': '4'}, {'purchase_id': 'purchaseid_191', 'title': 'Four Stars', 'rating': '4'}, {'purchase_id': 'purchaseid_190', 'title': 'A wonderful adventure in France', 'rating': '4'}, {'purchase_id': 'purchaseid_8', 'title': 'Best beginner book.  Been looking for something like this for a long time.', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'title': 'Referance Guide', 'rating': '4'}, {'purchase_id': 'purchaseid_186', 'title': 'A Good read for Meat Eaters, and Veggie Heads as well', 'rating': '4'}, {'purchase_id': 'purchaseid_76', 'title': 'Greet book', 'rating': '5'}, {'purchase_id': 'purchaseid_186', 'title': 'For anyone except avid non-hunters.', 'rating': '4'}, {'purchase_id': 'purchaseid_115', 'title': 'Highly recommend this book if you love history of Mid Atlantic wrestling...', 'rating': '5'}, {'purchase_id': 'purchaseid_167', 'title': 'Heroine blames others for things & feels her bad behavior is justified', 'rating': '2'}], 'var_functions.query_db:12': [{'book_id': 'bookid_1', 'title': 'Chaucer', 'categories': '["Books", "Literature & Fiction", "History & Criticism"]'}, {'book_id': 'bookid_9', 'title': 'Reunion: The Children of Lauderdale Park', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]'}, {'book_id': 'bookid_13', 'title': 'Girl Made of Glass', 'categories': '["Books", "Literature & Fiction", "Poetry"]'}, {'book_id': 'bookid_30', 'title': 'Sugary Sweets (A Taste of Love Series)', 'categories': '["Books", "Literature & Fiction", "Humor & Satire"]'}, {'book_id': 'bookid_36', 'title': 'Therapy Mammals', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]'}, {'book_id': 'bookid_37', 'title': "A Most Dangerous Book: Tacitus's Germania from the Roman Empire to the Third Reich", 'categories': '["Books", "Literature & Fiction", "History & Criticism"]'}, {'book_id': 'bookid_38', 'title': 'The Prophet: With Original 1923 Illustrations by the Author', 'categories': '["Books", "Literature & Fiction", "Poetry"]'}, {'book_id': 'bookid_39', 'title': 'The Melancholy Strumpet Master', 'categories': '["Books", "Literature & Fiction", "Humor & Satire"]'}, {'book_id': 'bookid_44', 'title': 'Reptilian', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]'}, {'book_id': 'bookid_49', 'title': 'Primeval: A Journal of the Uncanny - Issue #1', 'categories': '["Books", "Literature & Fiction", "History & Criticism"]'}, {'book_id': 'bookid_55', 'title': 'Behind the Wheel (Choose Your Own Adventure #35)(Paperback/Revised)', 'categories': '["Books", "Children\'s Books", "Literature & Fiction"]'}, {'book_id': 'bookid_69', 'title': 'Out of Sheer Rage: Wrestling with D. H. Lawrence', 'categories': '["Books", "Literature & Fiction", "History & Criticism"]'}, {'book_id': 'bookid_70', 'title': 'Polly and the Shadow Goblin: Book 2, Mother of Witches', 'categories': '["Books", "Literature & Fiction", "Mythology & Folk Tales"]'}, {'book_id': 'bookid_74', 'title': 'Child Of The King A Journey of Hope Book 1: Earthly Story With A Heavenly Message', 'categories': '["Books", "Literature & Fiction"]'}, {'book_id': 'bookid_77', 'title': 'One September Morning', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]'}, {'book_id': 'bookid_82', 'title': 'Fire Cracker', 'categories': '["Books", "Literature & Fiction", "United States"]'}, {'book_id': 'bookid_84', 'title': 'Local Honey', 'categories': '["Books", "Literature & Fiction"]'}, {'book_id': 'bookid_89', 'title': "I'll Ride For My Hood: A Salty Love Story", 'categories': '["Books", "Literature & Fiction", "Dramas & Plays"]'}, {'book_id': 'bookid_92', 'title': 'Outage', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]'}, {'book_id': 'bookid_93', 'title': 'Simantov', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]'}, {'book_id': 'bookid_98', 'title': 'Hollywood Confessions: Hollywood Headlines Book #3 (Hollywood Headlines Mysteries)', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]'}, {'book_id': 'bookid_99', 'title': 'Buddy the Soldier Bear', 'categories': '["Books", "Children\'s Books", "Literature & Fiction"]'}, {'book_id': 'bookid_101', 'title': 'Knowing When To Die: Uncollected Stories', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]'}, {'book_id': 'bookid_106', 'title': 'Looking for Peyton Place: A Novel', 'categories': '["Books", "Literature & Fiction", "Contemporary"]'}, {'book_id': 'bookid_109', 'title': 'All the Way to the Gallows', 'categories': '["Books", "Literature & Fiction", "Short Stories & Anthologies"]'}, {'book_id': 'bookid_111', 'title': 'Can You Buy Me The Wind?', 'categories': '["Books", "Children\'s Books", "Literature & Fiction"]'}, {'book_id': 'bookid_122', 'title': 'Childe Harold of Dysna', 'categories': '["Books", "Literature & Fiction", "History & Criticism"]'}, {'book_id': 'bookid_137', 'title': 'Oligarchy', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]'}, {'book_id': 'bookid_142', 'title': 'The Jordan Tracks', 'categories': '["Books", "Literature & Fiction", "Contemporary"]'}, {'book_id': 'bookid_144', 'title': 'Forged in Blood (Freehold)', 'categories': '["Books", "Literature & Fiction", "Short Stories & Anthologies"]'}, {'book_id': 'bookid_161', 'title': "Time's Demon: BOOK II OF THE ISLEVALE CYCLE", 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]'}, {'book_id': 'bookid_167', 'title': 'Dead Silence', 'categories': '["Books", "Christian Books & Bibles", "Literature & Fiction"]'}, {'book_id': 'bookid_171', 'title': 'Exits, Desires, & Slow Fires', 'categories': '["Books", "Literature & Fiction", "Poetry"]'}, {'book_id': 'bookid_177', 'title': 'Kennebago Moments', 'categories': '["Books", "Literature & Fiction", "Poetry"]'}, {'book_id': 'bookid_179', 'title': 'A Cherry Cola Christmas (A Cherry Cola Book Club Novel)', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]'}, {'book_id': 'bookid_180', 'title': 'The Sludge', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]'}, {'book_id': 'bookid_182', 'title': 'Liza of Lambeth', 'categories': '["Books", "Literature & Fiction", "Classics"]'}, {'book_id': 'bookid_187', 'title': 'Consort (A Dark(ish) Faerie Tale Book 3)', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]'}, {'book_id': 'bookid_188', 'title': "The Vampyre and Other Tales of the Macabre (Oxford World's Classics)", 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]'}, {'book_id': 'bookid_195', 'title': 'Something That Feels Like Truth (Switchgrass Books)', 'categories': '["Books", "Literature & Fiction", "Short Stories & Anthologies"]'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
