code = """import json
import pandas as pd
import numpy as np

# Load children's books from previous query
children_books = locals()['var_functions.query_db:2']

# Load reviews from 2020 onwards from the file
review_file_path = locals()['var_functions.query_db:7']
with open(review_file_path, 'r') as f:
    reviews = json.load(f)

# Convert to DataFrames
df_books = pd.DataFrame(children_books)
df_reviews = pd.DataFrame(reviews)

# Print sample data to understand patterns
print('Sample books data:')
for i, book in enumerate(children_books[:3]):
    print(f"  {book['book_id']}: {book['title']}")

print('\nSample reviews data:')
for i, review in enumerate(reviews[:10]):
    print(f"  {review['purchase_id']}: {review['title'][:50]}...")

# Extract numeric IDs
df_books['book_id_num'] = df_books['book_id'].str.extract('(\d+)')
df_reviews['purchase_id_num'] = df_reviews['purchase_id'].str.extract('(\d+)')

# Find matching books
matched_data = []
for _, book in df_books.iterrows():
    book_id = book['book_id_num']
    if book_id in df_reviews['purchase_id_num'].values:
        book_reviews = df_reviews[df_reviews['purchase_id_num'] == book_id]
        avg_rating = book_reviews['rating'].astype(float).mean()
        review_count = len(book_reviews)
        matched_data.append({
            'book_id': book['book_id'],
            'title': book['title'],
            'purchase_id_in_reviews': f'purchaseid_{book_id}',
            'average_rating': round(avg_rating, 2),
            'review_count': review_count,
            'review_years': sorted(set([r['review_time'][:4] for r in reviews if r['purchase_id'] == f'purchaseid_{book_id}']))
        })

print('__RESULT__:')
print(json.dumps({
    'total_children_books': len(children_books),
    'books_with_extracted_ids': len(df_books['book_id_num'].dropna()),
    'reviews_with_extracted_ids': len(df_reviews['purchase_id_num'].dropna()),
    'matched_books_count': len(matched_data),
    'matched_books_sample': matched_data[:5] if matched_data else []
}))"""

env_args = {'var_functions.list_db:0': ['books_info'], 'var_functions.query_db:2': [{'book_id': 'bookid_4', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_14', 'title': 'The Old Man and the Pirate Princess', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_32', 'title': 'The Very Hungry Caterpillar (English and Arabic Edition)', 'categories': '["Books", "Children\'s Books", "Early Learning"]'}, {'book_id': 'bookid_40', 'title': 'Egypt (Enchantment of the World)', 'categories': '["Books", "Children\'s Books", "Geography & Cultures"]'}, {'book_id': 'bookid_48', 'title': 'Clark the Shark: Tooth Trouble, No. 1', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_52', 'title': "I Hadn't Meant to Tell You This", 'categories': '["Books", "Children\'s Books", "Geography & Cultures"]'}, {'book_id': 'bookid_54', 'title': 'Favorite Thorton W. Burgess Stories: 6 Books', 'categories': '["Books", "Children\'s Books", "Animals"]'}, {'book_id': 'bookid_55', 'title': 'Behind the Wheel (Choose Your Own Adventure #35)(Paperback/Revised)', 'categories': '["Books", "Children\'s Books", "Literature & Fiction"]'}, {'book_id': 'bookid_57', 'title': "Goodnight Riley and the Moon, It's Almost Bedtime: Personalized Children’s Books, Personalized Gifts, and Bedtime Stories (A Magnificent Me! estorytime.com Series)", 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_96', 'title': 'Cheer Up, Ben Franklin! (Young Historians)', 'categories': '["Books", "Children\'s Books", "History"]'}, {'book_id': 'bookid_99', 'title': 'Buddy the Soldier Bear', 'categories': '["Books", "Children\'s Books", "Literature & Fiction"]'}, {'book_id': 'bookid_108', 'title': 'The Library Book', 'categories': '["Books", "Children\'s Books", "Education & Reference"]'}, {'book_id': 'bookid_111', 'title': 'Can You Buy Me The Wind?', 'categories': '["Books", "Children\'s Books", "Literature & Fiction"]'}, {'book_id': 'bookid_116', 'title': 'From the Earth to the Moon by Jules Verne, Fiction, Fantasy & Magic', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_120', 'title': "Caroline's Color Dreams: Los Sueños Coloridos De Carolina : Babl Children's Books in Spanish and English", 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_124', 'title': 'Skeleton Play: A Fun, Rhyming Halloween Book for Kids! (1)', 'categories': '["Books", "Children\'s Books", "Holidays & Celebrations"]'}, {'book_id': 'bookid_130', 'title': "Benny Goes To The Moon: The great new book from Top Children's entertainer Gerry Ogilvie (1)", 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_132', 'title': 'Mae and Jane in the Rain', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_145', 'title': 'Kirsten: An American Girl : 1854 (The American Girls Collection/Boxed Set)', 'categories': '["Books", "Boxed Sets", "Children\'s Books"]'}, {'book_id': 'bookid_146', 'title': 'LunaLu the Llamacorn', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_149', 'title': 'Trouble in the CTC!: The Terra Prime Adventures Book 2', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_152', 'title': 'Around the World Mazes', 'categories': '["Books", "Children\'s Books", "Activities, Crafts & Games"]'}, {'book_id': 'bookid_158', 'title': 'Cleo Porter and the Body Electric', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_163', 'title': 'Monster Kisses', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_170', 'title': 'Pokémon: Sun & Moon, Vol. 8 (8)', 'categories': '["Books", "Children\'s Books", "Comics & Graphic Novels"]'}], 'var_functions.list_db:4': ['review'], 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:10': {'books_columns': ['book_id', 'title', 'categories'], 'reviews_columns': ['purchase_id', 'title', 'rating', 'review_time']}}

exec(code, env_args)
