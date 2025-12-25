code = """import pandas as pd
import json

# Load books
books_data = locals()['var_function-call-13100700179920884987']
df_books = pd.DataFrame(books_data)

# Load reviews
reviews_file_path = locals()['var_function-call-4273390651133138039']
with open(reviews_file_path, 'r') as f:
    reviews_data = json.load(f)
df_reviews = pd.DataFrame(reviews_data)

# Convert rating to float
df_reviews['rating'] = df_reviews['rating'].astype(float)

# Merge
# book_id in books corresponds to purchase_id in reviews
merged = pd.merge(df_books, df_reviews, left_on='book_id', right_on='purchase_id', how='inner')

# Calculate average rating
avg_ratings = merged.groupby(['book_id', 'title'])['rating'].mean().reset_index()

# Filter >= 4.5
result_df = avg_ratings[avg_ratings['rating'] >= 4.5]

# Get titles
titles = result_df['title'].tolist()

print("__RESULT__:")
print(json.dumps(titles))"""

env_args = {'var_function-call-9838380601063403326': [{'book_id': 'bookid_1', 'title': 'Chaucer', 'categories': '["Books", "Literature & Fiction", "History & Criticism"]'}, {'book_id': 'bookid_2', 'title': 'Notes from a Kidwatcher', 'categories': '["Books", "Reference", "Words, Language & Grammar"]'}, {'book_id': 'bookid_3', 'title': 'Service: A Navy SEAL at War', 'categories': '["Books", "Biographies & Memoirs", "Leaders & Notable People"]'}, {'book_id': 'bookid_4', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_5', 'title': 'Parker & Knight', 'categories': '["Books", "Mystery, Thriller & Suspense", "Thrillers & Suspense"]'}], 'var_function-call-524553318592950692': ['review'], 'var_function-call-13100700179920886124': [{'rating': '4', 'purchase_id': 'purchaseid_186', 'review_time': '2012-11-24 18:52:00'}, {'rating': '4', 'purchase_id': 'purchaseid_191', 'review_time': '2015-12-31 13:35:00'}, {'rating': '4', 'purchase_id': 'purchaseid_190', 'review_time': '2013-05-05 10:47:00'}, {'rating': '5', 'purchase_id': 'purchaseid_8', 'review_time': '2020-08-12 11:06:00'}, {'rating': '4', 'purchase_id': 'purchaseid_178', 'review_time': '2014-11-13 18:55:00'}], 'var_function-call-13100700179920884987': [{'book_id': 'bookid_4', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still'}, {'book_id': 'bookid_14', 'title': 'The Old Man and the Pirate Princess'}, {'book_id': 'bookid_32', 'title': 'The Very Hungry Caterpillar (English and Arabic Edition)'}, {'book_id': 'bookid_40', 'title': 'Egypt (Enchantment of the World)'}, {'book_id': 'bookid_48', 'title': 'Clark the Shark: Tooth Trouble, No. 1'}, {'book_id': 'bookid_52', 'title': "I Hadn't Meant to Tell You This"}, {'book_id': 'bookid_54', 'title': 'Favorite Thorton W. Burgess Stories: 6 Books'}, {'book_id': 'bookid_55', 'title': 'Behind the Wheel (Choose Your Own Adventure #35)(Paperback/Revised)'}, {'book_id': 'bookid_57', 'title': "Goodnight Riley and the Moon, It's Almost Bedtime: Personalized Children’s Books, Personalized Gifts, and Bedtime Stories (A Magnificent Me! estorytime.com Series)"}, {'book_id': 'bookid_96', 'title': 'Cheer Up, Ben Franklin! (Young Historians)'}, {'book_id': 'bookid_99', 'title': 'Buddy the Soldier Bear'}, {'book_id': 'bookid_108', 'title': 'The Library Book'}, {'book_id': 'bookid_111', 'title': 'Can You Buy Me The Wind?'}, {'book_id': 'bookid_116', 'title': 'From the Earth to the Moon by Jules Verne, Fiction, Fantasy & Magic'}, {'book_id': 'bookid_120', 'title': "Caroline's Color Dreams: Los Sueños Coloridos De Carolina : Babl Children's Books in Spanish and English"}, {'book_id': 'bookid_124', 'title': 'Skeleton Play: A Fun, Rhyming Halloween Book for Kids! (1)'}, {'book_id': 'bookid_130', 'title': "Benny Goes To The Moon: The great new book from Top Children's entertainer Gerry Ogilvie (1)"}, {'book_id': 'bookid_132', 'title': 'Mae and Jane in the Rain'}, {'book_id': 'bookid_145', 'title': 'Kirsten: An American Girl : 1854 (The American Girls Collection/Boxed Set)'}, {'book_id': 'bookid_146', 'title': 'LunaLu the Llamacorn'}, {'book_id': 'bookid_149', 'title': 'Trouble in the CTC!: The Terra Prime Adventures Book 2'}, {'book_id': 'bookid_152', 'title': 'Around the World Mazes'}, {'book_id': 'bookid_158', 'title': 'Cleo Porter and the Body Electric'}, {'book_id': 'bookid_163', 'title': 'Monster Kisses'}, {'book_id': 'bookid_170', 'title': 'Pokémon: Sun & Moon, Vol. 8 (8)'}], 'var_function-call-3294671076964993952': [{'count': '25'}], 'var_function-call-4213605318296194809': [{'COUNT(*)': '329'}], 'var_function-call-4273390651133138039': 'file_storage/function-call-4273390651133138039.json'}

exec(code, env_args)
