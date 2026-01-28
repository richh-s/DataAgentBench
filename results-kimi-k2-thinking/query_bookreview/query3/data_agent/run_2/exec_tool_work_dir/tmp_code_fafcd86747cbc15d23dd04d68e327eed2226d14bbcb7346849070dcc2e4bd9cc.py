code = """import json
import pandas as pd

# Load the review data from file (it's stored as a JSON file path)
review_file_path = locals()['var_functions.query_db:14']
with open(review_file_path, 'r') as f:
    reviews_data = json.load(f)

# Load the books data from file
books_file_path = locals()['var_functions.query_db:6']
with open(books_file_path, 'r') as f:
    books_data = json.load(f)

# Convert to DataFrames
reviews_df = pd.DataFrame(reviews_data)
books_df = pd.DataFrame(books_data)

# Filter books that are in 'Children's Books' category
childrens_books_df = books_df[books_df['categories'].str.contains("Children's Books", na=False)]

# Extract numeric ID from purchase_id and book_id for joining
reviews_df['book_numeric_id'] = reviews_df['purchase_id'].str.extract(r'purchaseid_(\d+)')
childrens_books_df['book_numeric_id'] = childrens_books_df['book_id'].str.extract(r'bookid_(\d+)')

# Merge reviews with children's books
merged_df = pd.merge(reviews_df, childrens_books_df, on='book_numeric_id', how='inner', suffixes=('_review', '_book'))

# Convert rating to float
merged_df['rating'] = merged_df['rating'].astype(float)

# Calculate average rating per book
# Group by the actual book_id from books_df (which is the _book suffix after merge)
book_ratings = merged_df.groupby('book_id').agg({
    'rating': ['mean', 'count'],
    'title': 'first',  # title from books_df
    'categories': 'first'
}).reset_index()

# Flatten column names
book_ratings.columns = ['book_id', 'average_rating', 'review_count', 'title', 'categories']

# Filter books with average rating >= 4.5 and at least 1 review
result_df = book_ratings[(book_ratings['average_rating'] >= 4.5) & (book_ratings['review_count'] >= 1)]

# Sort by average rating descending
result_df = result_df.sort_values('average_rating', ascending=False)

# Convert to JSON string for output
result_json = result_df.to_json(orient='records', indent=2)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'columns': ['purchase_id', 'title_review', 'rating', 'review_time', 'book_numeric_id', 'book_id', 'title_book', 'categories']}, 'var_functions.execute_python:12': [{'book_id': 'bookid_108', 'average_rating': 5.0, 'review_count': 3, 'title': 'The Library Book', 'categories': '["Books", "Children\'s Books", "Education & Reference"]'}, {'book_id': 'bookid_130', 'average_rating': 5.0, 'review_count': 1, 'title': "Benny Goes To The Moon: The great new book from Top Children's entertainer Gerry Ogilvie (1)", 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_14', 'average_rating': 5.0, 'review_count': 1, 'title': 'The Old Man and the Pirate Princess', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_146', 'average_rating': 5.0, 'review_count': 3, 'title': 'LunaLu the Llamacorn', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_152', 'average_rating': 5.0, 'review_count': 1, 'title': 'Around the World Mazes', 'categories': '["Books", "Children\'s Books", "Activities, Crafts & Games"]'}, {'book_id': 'bookid_170', 'average_rating': 5.0, 'review_count': 1, 'title': 'Pokémon: Sun & Moon, Vol. 8 (8)', 'categories': '["Books", "Children\'s Books", "Comics & Graphic Novels"]'}, {'book_id': 'bookid_96', 'average_rating': 5.0, 'review_count': 1, 'title': 'Cheer Up, Ben Franklin! (Young Historians)', 'categories': '["Books", "Children\'s Books", "History"]'}, {'book_id': 'bookid_4', 'average_rating': 5.0, 'review_count': 1, 'title': 'Monstrous Stories #4: The Day the Mice Stood Still', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_40', 'average_rating': 5.0, 'review_count': 1, 'title': 'Egypt (Enchantment of the World)', 'categories': '["Books", "Children\'s Books", "Geography & Cultures"]'}, {'book_id': 'bookid_54', 'average_rating': 5.0, 'review_count': 3, 'title': 'Favorite Thorton W. Burgess Stories: 6 Books', 'categories': '["Books", "Children\'s Books", "Animals"]'}, {'book_id': 'bookid_55', 'average_rating': 5.0, 'review_count': 1, 'title': 'Behind the Wheel (Choose Your Own Adventure #35)(Paperback/Revised)', 'categories': '["Books", "Children\'s Books", "Literature & Fiction"]'}, {'book_id': 'bookid_149', 'average_rating': 4.9, 'review_count': 10, 'title': 'Trouble in the CTC!: The Terra Prime Adventures Book 2', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_48', 'average_rating': 4.75, 'review_count': 4, 'title': 'Clark the Shark: Tooth Trouble, No. 1', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_158', 'average_rating': 4.7083333333, 'review_count': 24, 'title': 'Cleo Porter and the Body Electric', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
