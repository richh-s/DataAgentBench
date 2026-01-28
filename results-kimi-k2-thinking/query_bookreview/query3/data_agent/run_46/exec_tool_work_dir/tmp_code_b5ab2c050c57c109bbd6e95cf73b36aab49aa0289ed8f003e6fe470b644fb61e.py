code = """import json
import pandas as pd

# Load the data
children_books = locals()['var_functions.query_db:2']

# Read reviews from file
review_file_path = locals()['var_functions.query_db:7']
with open(review_file_path, 'r') as f:
    reviews = json.load(f)

# Create DataFrames
df_books = pd.DataFrame(children_books)
df_reviews = pd.DataFrame(reviews)

# Extract IDs from strings
df_books['id_num'] = df_books['book_id'].str.extract(r'(\d+)')
df_reviews['id_num'] = df_reviews['purchase_id'].str.extract(r'(\d+)')

# Convert to string
df_books['id_num'] = df_books['id_num'].astype(str)
df_reviews['id_num'] = df_reviews['id_num'].astype(str)

# Convert rating to float
df_reviews['rating_float'] = df_reviews['rating'].astype(float)

# Join books with reviews
merged = df_books.merge(df_reviews, left_on='id_num', right_on='id_num', how='inner')

# Filter only reviews from 2020 onwards (the data is already filtered for 2020+ queries)
# Group by books and calculate average rating
book_ratings = merged.groupby(['book_id', 'title_x']).agg({
    'rating_float': ['mean', 'count']
}).reset_index()

# Flatten column names
book_ratings.columns = ['book_id', 'title', 'avg_rating', 'review_count']

# Filter books with average rating >= 4.5
high_rated_books = book_ratings[book_ratings['avg_rating'] >= 4.5].copy()

# Round avg_rating to 2 decimal places
high_rated_books['avg_rating'] = high_rated_books['avg_rating'].round(2)

# Sort by rating
high_rated_books = high_rated_books.sort_values('avg_rating', ascending=False)

# Debug info to understand what's happening
print('Total merged reviews:', len(merged))
print('Book ratings calculated:', len(book_ratings))
print('High-rated books count:', len(high_rated_books))
print('\nAll calculated book ratings (for debugging):')
print(book_ratings.to_string())
print('\nHigh-rated books that meet the criteria:')
print(high_rated_books.to_string())

# Create result
result_json = high_rated_books.to_json(orient='records')

print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['books_info'], 'var_functions.query_db:2': [{'book_id': 'bookid_4', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_14', 'title': 'The Old Man and the Pirate Princess', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_32', 'title': 'The Very Hungry Caterpillar (English and Arabic Edition)', 'categories': '["Books", "Children\'s Books", "Early Learning"]'}, {'book_id': 'bookid_40', 'title': 'Egypt (Enchantment of the World)', 'categories': '["Books", "Children\'s Books", "Geography & Cultures"]'}, {'book_id': 'bookid_48', 'title': 'Clark the Shark: Tooth Trouble, No. 1', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_52', 'title': "I Hadn't Meant to Tell You This", 'categories': '["Books", "Children\'s Books", "Geography & Cultures"]'}, {'book_id': 'bookid_54', 'title': 'Favorite Thorton W. Burgess Stories: 6 Books', 'categories': '["Books", "Children\'s Books", "Animals"]'}, {'book_id': 'bookid_55', 'title': 'Behind the Wheel (Choose Your Own Adventure #35)(Paperback/Revised)', 'categories': '["Books", "Children\'s Books", "Literature & Fiction"]'}, {'book_id': 'bookid_57', 'title': "Goodnight Riley and the Moon, It's Almost Bedtime: Personalized Children’s Books, Personalized Gifts, and Bedtime Stories (A Magnificent Me! estorytime.com Series)", 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_96', 'title': 'Cheer Up, Ben Franklin! (Young Historians)', 'categories': '["Books", "Children\'s Books", "History"]'}, {'book_id': 'bookid_99', 'title': 'Buddy the Soldier Bear', 'categories': '["Books", "Children\'s Books", "Literature & Fiction"]'}, {'book_id': 'bookid_108', 'title': 'The Library Book', 'categories': '["Books", "Children\'s Books", "Education & Reference"]'}, {'book_id': 'bookid_111', 'title': 'Can You Buy Me The Wind?', 'categories': '["Books", "Children\'s Books", "Literature & Fiction"]'}, {'book_id': 'bookid_116', 'title': 'From the Earth to the Moon by Jules Verne, Fiction, Fantasy & Magic', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_120', 'title': "Caroline's Color Dreams: Los Sueños Coloridos De Carolina : Babl Children's Books in Spanish and English", 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_124', 'title': 'Skeleton Play: A Fun, Rhyming Halloween Book for Kids! (1)', 'categories': '["Books", "Children\'s Books", "Holidays & Celebrations"]'}, {'book_id': 'bookid_130', 'title': "Benny Goes To The Moon: The great new book from Top Children's entertainer Gerry Ogilvie (1)", 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_132', 'title': 'Mae and Jane in the Rain', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_145', 'title': 'Kirsten: An American Girl : 1854 (The American Girls Collection/Boxed Set)', 'categories': '["Books", "Boxed Sets", "Children\'s Books"]'}, {'book_id': 'bookid_146', 'title': 'LunaLu the Llamacorn', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_149', 'title': 'Trouble in the CTC!: The Terra Prime Adventures Book 2', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_152', 'title': 'Around the World Mazes', 'categories': '["Books", "Children\'s Books", "Activities, Crafts & Games"]'}, {'book_id': 'bookid_158', 'title': 'Cleo Porter and the Body Electric', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_163', 'title': 'Monster Kisses', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_170', 'title': 'Pokémon: Sun & Moon, Vol. 8 (8)', 'categories': '["Books", "Children\'s Books", "Comics & Graphic Novels"]'}], 'var_functions.list_db:4': ['review'], 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:10': {'books_columns': ['book_id', 'title', 'categories'], 'reviews_columns': ['purchase_id', 'title', 'rating', 'review_time']}, 'var_functions.execute_python:14': {'books_count': 25, 'reviews_count': 329, 'books_with_ids': 25, 'reviews_with_ids': 329, 'merged_count': 72}}

exec(code, env_args)
