code = """import json
import pandas as pd

# Get the file path from the variable
file_path = locals()['var_function-call-15893569364720928727']

# Load reviews from the file
with open(file_path, 'r') as f:
    reviews = json.load(f)

# Load books from the previous result
books = locals()['var_function-call-15893569364720927594']

# Create DataFrames
df_reviews = pd.DataFrame(reviews)
df_books = pd.DataFrame(books)

# Ensure numeric types for rating
df_reviews['rating'] = pd.to_numeric(df_reviews['rating'])

# Calculate average rating per purchase_id
avg_ratings = df_reviews.groupby('purchase_id')['rating'].mean().reset_index()

# Filter for avg rating >= 4.5
high_rated = avg_ratings[avg_ratings['rating'] >= 4.5].copy()

# Extract numeric ID from purchase_id (format "purchaseid_123")
high_rated['id_num'] = high_rated['purchase_id'].str.extract(r'(\d+)$').astype(int)

# Extract numeric ID from book_id (format "bookid_123")
df_books['id_num'] = df_books['book_id'].str.extract(r'(\d+)$').astype(int)

# Merge
result_df = pd.merge(df_books, high_rated, on='id_num', how='inner')

# Get titles
titles = result_df['title'].tolist()

print("__RESULT__:")
print(json.dumps(titles))"""

env_args = {'var_function-call-2949562448822751565': ['review'], 'var_function-call-2949562448822754756': ['books_info'], 'var_function-call-14634478087371902873': [{'purchase_id': 'purchaseid_186', 'review_time': '2012-11-24 18:52:00', 'rating': '4'}, {'purchase_id': 'purchaseid_191', 'review_time': '2015-12-31 13:35:00', 'rating': '4'}, {'purchase_id': 'purchaseid_190', 'review_time': '2013-05-05 10:47:00', 'rating': '4'}, {'purchase_id': 'purchaseid_8', 'review_time': '2020-08-12 11:06:00', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'review_time': '2014-11-13 18:55:00', 'rating': '4'}], 'var_function-call-14634478087371901334': [{'book_id': 'bookid_1', 'categories': '["Books", "Literature & Fiction", "History & Criticism"]', 'title': 'Chaucer'}, {'book_id': 'bookid_2', 'categories': '["Books", "Reference", "Words, Language & Grammar"]', 'title': 'Notes from a Kidwatcher'}, {'book_id': 'bookid_3', 'categories': '["Books", "Biographies & Memoirs", "Leaders & Notable People"]', 'title': 'Service: A Navy SEAL at War'}, {'book_id': 'bookid_4', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still'}, {'book_id': 'bookid_5', 'categories': '["Books", "Mystery, Thriller & Suspense", "Thrillers & Suspense"]', 'title': 'Parker & Knight'}], 'var_function-call-15893569364720928727': 'file_storage/function-call-15893569364720928727.json', 'var_function-call-15893569364720927594': [{'book_id': 'bookid_4', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still'}, {'book_id': 'bookid_14', 'title': 'The Old Man and the Pirate Princess'}, {'book_id': 'bookid_32', 'title': 'The Very Hungry Caterpillar (English and Arabic Edition)'}, {'book_id': 'bookid_40', 'title': 'Egypt (Enchantment of the World)'}, {'book_id': 'bookid_48', 'title': 'Clark the Shark: Tooth Trouble, No. 1'}, {'book_id': 'bookid_52', 'title': "I Hadn't Meant to Tell You This"}, {'book_id': 'bookid_54', 'title': 'Favorite Thorton W. Burgess Stories: 6 Books'}, {'book_id': 'bookid_55', 'title': 'Behind the Wheel (Choose Your Own Adventure #35)(Paperback/Revised)'}, {'book_id': 'bookid_57', 'title': "Goodnight Riley and the Moon, It's Almost Bedtime: Personalized Children’s Books, Personalized Gifts, and Bedtime Stories (A Magnificent Me! estorytime.com Series)"}, {'book_id': 'bookid_96', 'title': 'Cheer Up, Ben Franklin! (Young Historians)'}, {'book_id': 'bookid_99', 'title': 'Buddy the Soldier Bear'}, {'book_id': 'bookid_108', 'title': 'The Library Book'}, {'book_id': 'bookid_111', 'title': 'Can You Buy Me The Wind?'}, {'book_id': 'bookid_116', 'title': 'From the Earth to the Moon by Jules Verne, Fiction, Fantasy & Magic'}, {'book_id': 'bookid_120', 'title': "Caroline's Color Dreams: Los Sueños Coloridos De Carolina : Babl Children's Books in Spanish and English"}, {'book_id': 'bookid_124', 'title': 'Skeleton Play: A Fun, Rhyming Halloween Book for Kids! (1)'}, {'book_id': 'bookid_130', 'title': "Benny Goes To The Moon: The great new book from Top Children's entertainer Gerry Ogilvie (1)"}, {'book_id': 'bookid_132', 'title': 'Mae and Jane in the Rain'}, {'book_id': 'bookid_145', 'title': 'Kirsten: An American Girl : 1854 (The American Girls Collection/Boxed Set)'}, {'book_id': 'bookid_146', 'title': 'LunaLu the Llamacorn'}, {'book_id': 'bookid_149', 'title': 'Trouble in the CTC!: The Terra Prime Adventures Book 2'}, {'book_id': 'bookid_152', 'title': 'Around the World Mazes'}, {'book_id': 'bookid_158', 'title': 'Cleo Porter and the Body Electric'}, {'book_id': 'bookid_163', 'title': 'Monster Kisses'}, {'book_id': 'bookid_170', 'title': 'Pokémon: Sun & Moon, Vol. 8 (8)'}]}

exec(code, env_args)
