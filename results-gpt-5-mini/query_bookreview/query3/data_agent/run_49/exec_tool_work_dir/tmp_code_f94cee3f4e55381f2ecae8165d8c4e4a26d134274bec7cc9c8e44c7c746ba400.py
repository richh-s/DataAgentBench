code = """import json
import pandas as pd
import re

# Load reviews from the large JSON file path stored in var_call_wHIPNvFNUcXarRUteQy34elq
with open(var_call_wHIPNvFNUcXarRUteQy34elq, 'r') as f:
    reviews = json.load(f)

books = var_call_GyStwmLqdJKm6NamO9Nave99

# Create DataFrames
rv = pd.DataFrame(reviews)
books_df = pd.DataFrame(books)

# Normalize types
rv['rating'] = pd.to_numeric(rv['rating'], errors='coerce')
rv['review_time'] = pd.to_datetime(rv['review_time'], errors='coerce')

# Extract numeric id from purchase_id and book_id
rv['numeric_id'] = rv['purchase_id'].astype(str).str.extract(r'(\d+)').astype(float)
books_df['numeric_id'] = books_df['book_id'].astype(str).str.extract(r'(\d+)').astype(float)

# Keep only reviews from 2020 onwards - the initial query already filtered, but ensure again
rv = rv[rv['review_time'] >= pd.to_datetime('2020-01-01')]

# Filter reviews to only those whose numeric_id is in the children's books list
child_ids = books_df['numeric_id'].unique().tolist()
rv_children = rv[rv['numeric_id'].isin(child_ids)].copy()

# Compute average rating per numeric_id
agg = rv_children.groupby('numeric_id').agg(average_rating=('rating', 'mean'), review_count=('rating', 'count')).reset_index()

# Merge with books titles
agg = agg.merge(books_df[['numeric_id','book_id','title']], on='numeric_id', how='left')

# Filter average_rating >= 4.5
agg = agg[agg['average_rating'] >= 4.5]

# Round average_rating to 3 decimals
agg['average_rating'] = agg['average_rating'].round(3)

# Prepare result list
result = []
for _, row in agg.sort_values(['average_rating','review_count'], ascending=[False, False]).iterrows():
    result.append({
        'book_id': row['book_id'],
        'title': row['title'],
        'average_rating': float(row['average_rating']),
        'review_count': int(row['review_count'])
    })

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_aEPYOcO6FXNPrLRAGr6jUZ0z': ['review'], 'var_call_VkpwuqNy0NhGVp5vUBSB6CUd': ['books_info'], 'var_call_wHIPNvFNUcXarRUteQy34elq': 'file_storage/call_wHIPNvFNUcXarRUteQy34elq.json', 'var_call_GyStwmLqdJKm6NamO9Nave99': [{'book_id': 'bookid_4', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_14', 'title': 'The Old Man and the Pirate Princess', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_32', 'title': 'The Very Hungry Caterpillar (English and Arabic Edition)', 'categories': '["Books", "Children\'s Books", "Early Learning"]'}, {'book_id': 'bookid_40', 'title': 'Egypt (Enchantment of the World)', 'categories': '["Books", "Children\'s Books", "Geography & Cultures"]'}, {'book_id': 'bookid_48', 'title': 'Clark the Shark: Tooth Trouble, No. 1', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_52', 'title': "I Hadn't Meant to Tell You This", 'categories': '["Books", "Children\'s Books", "Geography & Cultures"]'}, {'book_id': 'bookid_54', 'title': 'Favorite Thorton W. Burgess Stories: 6 Books', 'categories': '["Books", "Children\'s Books", "Animals"]'}, {'book_id': 'bookid_55', 'title': 'Behind the Wheel (Choose Your Own Adventure #35)(Paperback/Revised)', 'categories': '["Books", "Children\'s Books", "Literature & Fiction"]'}, {'book_id': 'bookid_57', 'title': "Goodnight Riley and the Moon, It's Almost Bedtime: Personalized Children’s Books, Personalized Gifts, and Bedtime Stories (A Magnificent Me! estorytime.com Series)", 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_96', 'title': 'Cheer Up, Ben Franklin! (Young Historians)', 'categories': '["Books", "Children\'s Books", "History"]'}, {'book_id': 'bookid_99', 'title': 'Buddy the Soldier Bear', 'categories': '["Books", "Children\'s Books", "Literature & Fiction"]'}, {'book_id': 'bookid_108', 'title': 'The Library Book', 'categories': '["Books", "Children\'s Books", "Education & Reference"]'}, {'book_id': 'bookid_111', 'title': 'Can You Buy Me The Wind?', 'categories': '["Books", "Children\'s Books", "Literature & Fiction"]'}, {'book_id': 'bookid_116', 'title': 'From the Earth to the Moon by Jules Verne, Fiction, Fantasy & Magic', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_120', 'title': "Caroline's Color Dreams: Los Sueños Coloridos De Carolina : Babl Children's Books in Spanish and English", 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_124', 'title': 'Skeleton Play: A Fun, Rhyming Halloween Book for Kids! (1)', 'categories': '["Books", "Children\'s Books", "Holidays & Celebrations"]'}, {'book_id': 'bookid_130', 'title': "Benny Goes To The Moon: The great new book from Top Children's entertainer Gerry Ogilvie (1)", 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_132', 'title': 'Mae and Jane in the Rain', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_145', 'title': 'Kirsten: An American Girl : 1854 (The American Girls Collection/Boxed Set)', 'categories': '["Books", "Boxed Sets", "Children\'s Books"]'}, {'book_id': 'bookid_146', 'title': 'LunaLu the Llamacorn', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_149', 'title': 'Trouble in the CTC!: The Terra Prime Adventures Book 2', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_152', 'title': 'Around the World Mazes', 'categories': '["Books", "Children\'s Books", "Activities, Crafts & Games"]'}, {'book_id': 'bookid_158', 'title': 'Cleo Porter and the Body Electric', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_163', 'title': 'Monster Kisses', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_170', 'title': 'Pokémon: Sun & Moon, Vol. 8 (8)', 'categories': '["Books", "Children\'s Books", "Comics & Graphic Novels"]'}]}

exec(code, env_args)
