code = """# First, let's examine the structure of our data
import pandas as pd
import json

# Load the data
children_result = locals()['var_functions.query_db:8']
reviews_result = locals()['var_functions.query_db:10']

# Read from files if needed
if isinstance(children_result, str):
    with open(children_result, 'r') as f:
        children_books = json.load(f)
else:
    children_books = children_result

if isinstance(reviews_result, str):
    with open(reviews_result, 'r') as f:
        reviews_2020 = json.load(f)
else:
    reviews_2020 = reviews_result

# Map purchase_id to book_id format
for review in reviews_2020:
    purchase_id = review['purchase_id']
    if purchase_id.startswith('purchaseid_'):
        book_id_num = purchase_id.split('_')[1]
        review['book_id'] = f'bookid_{book_id_num}'

# Create DataFrames
df_children = pd.DataFrame(children_books)
df_reviews = pd.DataFrame(reviews_2020)

print('Children books columns:', df_children.columns.tolist())
print('Reviews columns:', df_reviews.columns.tolist())

# Merge the data
merged = df_children.merge(df_reviews, on='book_id', how='inner')
print('Merged columns:', merged.columns.tolist())
print('Merged rows:', len(merged))

# Show a few merged rows
print('Sample merged data:')
print(merged[['book_id', 'title', 'rating']].head())

# Group by book and calculate average rating
grouped = merged.groupby(['book_id', 'title'])['rating'].agg(['mean', 'count']).reset_index()
grouped.columns = ['book_id', 'title', 'avg_rating', 'review_count']

# Filter for books with average rating >= 4.5
result = grouped[grouped['avg_rating'] >= 4.5]

print(f'Found {len(result)} books with avg rating >= 4.5')
print('Result preview:')
print(result.head())

# Output result in required format
result_json = result.to_json(orient='records')
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['books_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['review'], 'var_functions.query_db:6': [{'rating': '4', 'purchase_id': 'purchaseid_186', 'review_time': '2012-11-24 18:52:00'}, {'rating': '4', 'purchase_id': 'purchaseid_191', 'review_time': '2015-12-31 13:35:00'}, {'rating': '4', 'purchase_id': 'purchaseid_190', 'review_time': '2013-05-05 10:47:00'}, {'rating': '5', 'purchase_id': 'purchaseid_8', 'review_time': '2020-08-12 11:06:00'}, {'rating': '4', 'purchase_id': 'purchaseid_178', 'review_time': '2014-11-13 18:55:00'}], 'var_functions.query_db:8': [{'book_id': 'bookid_4', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_14', 'title': 'The Old Man and the Pirate Princess', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_32', 'title': 'The Very Hungry Caterpillar (English and Arabic Edition)', 'categories': '["Books", "Children\'s Books", "Early Learning"]'}, {'book_id': 'bookid_40', 'title': 'Egypt (Enchantment of the World)', 'categories': '["Books", "Children\'s Books", "Geography & Cultures"]'}, {'book_id': 'bookid_48', 'title': 'Clark the Shark: Tooth Trouble, No. 1', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_52', 'title': "I Hadn't Meant to Tell You This", 'categories': '["Books", "Children\'s Books", "Geography & Cultures"]'}, {'book_id': 'bookid_54', 'title': 'Favorite Thorton W. Burgess Stories: 6 Books', 'categories': '["Books", "Children\'s Books", "Animals"]'}, {'book_id': 'bookid_55', 'title': 'Behind the Wheel (Choose Your Own Adventure #35)(Paperback/Revised)', 'categories': '["Books", "Children\'s Books", "Literature & Fiction"]'}, {'book_id': 'bookid_57', 'title': "Goodnight Riley and the Moon, It's Almost Bedtime: Personalized Children’s Books, Personalized Gifts, and Bedtime Stories (A Magnificent Me! estorytime.com Series)", 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_96', 'title': 'Cheer Up, Ben Franklin! (Young Historians)', 'categories': '["Books", "Children\'s Books", "History"]'}, {'book_id': 'bookid_99', 'title': 'Buddy the Soldier Bear', 'categories': '["Books", "Children\'s Books", "Literature & Fiction"]'}, {'book_id': 'bookid_108', 'title': 'The Library Book', 'categories': '["Books", "Children\'s Books", "Education & Reference"]'}, {'book_id': 'bookid_111', 'title': 'Can You Buy Me The Wind?', 'categories': '["Books", "Children\'s Books", "Literature & Fiction"]'}, {'book_id': 'bookid_116', 'title': 'From the Earth to the Moon by Jules Verne, Fiction, Fantasy & Magic', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_120', 'title': "Caroline's Color Dreams: Los Sueños Coloridos De Carolina : Babl Children's Books in Spanish and English", 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_124', 'title': 'Skeleton Play: A Fun, Rhyming Halloween Book for Kids! (1)', 'categories': '["Books", "Children\'s Books", "Holidays & Celebrations"]'}, {'book_id': 'bookid_130', 'title': "Benny Goes To The Moon: The great new book from Top Children's entertainer Gerry Ogilvie (1)", 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_132', 'title': 'Mae and Jane in the Rain', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_145', 'title': 'Kirsten: An American Girl : 1854 (The American Girls Collection/Boxed Set)', 'categories': '["Books", "Boxed Sets", "Children\'s Books"]'}, {'book_id': 'bookid_146', 'title': 'LunaLu the Llamacorn', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_149', 'title': 'Trouble in the CTC!: The Terra Prime Adventures Book 2', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_152', 'title': 'Around the World Mazes', 'categories': '["Books", "Children\'s Books", "Activities, Crafts & Games"]'}, {'book_id': 'bookid_158', 'title': 'Cleo Porter and the Body Electric', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_163', 'title': 'Monster Kisses', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_170', 'title': 'Pokémon: Sun & Moon, Vol. 8 (8)', 'categories': '["Books", "Children\'s Books", "Comics & Graphic Novels"]'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
