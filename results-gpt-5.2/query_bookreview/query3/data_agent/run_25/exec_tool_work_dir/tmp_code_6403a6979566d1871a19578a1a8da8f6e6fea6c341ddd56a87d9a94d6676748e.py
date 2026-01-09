code = """import json, pandas as pd

# Load books (already in-memory)
books = pd.DataFrame(var_call_AG2OGnxIkTd3tg7kCM51vQXu)

# Load reviews (large) from json file
path = var_call_6azw9jlPyswhfEzVrgtlVJ0a
with open(path, 'r', encoding='utf-8') as f:
    reviews_data = json.load(f)
reviews = pd.DataFrame(reviews_data)

# Clean ratings
reviews['rating'] = pd.to_numeric(reviews['rating'], errors='coerce')

# Fuzzy join rule per hint: purchase_id like 'purchaseid_4' aligns with book_id 'bookid_4' by numeric suffix
# Extract suffix digits
books['suffix'] = books['book_id'].str.extract(r'(\d+)$')[0]
reviews['suffix'] = reviews['purchase_id'].str.extract(r'(\d+)$')[0]

# Keep only reviews whose suffix matches a Children's Books book
child_suffixes = set(books['suffix'].dropna().unique().tolist())
rev_child = reviews[reviews['suffix'].isin(child_suffixes)].copy()

# Compute average rating from 2020 onwards (already filtered by SQL)
avg = rev_child.groupby('suffix', as_index=False).agg(avg_rating=('rating','mean'), review_count=('rating','count'))

# Join back to books
out = books.merge(avg, on='suffix', how='inner')

# Filter avg >= 4.5
out = out[out['avg_rating'] >= 4.5].copy()

# Prepare final list
out = out.sort_values(['avg_rating','review_count','title'], ascending=[False, False, True])
records = out[['title','book_id','avg_rating','review_count']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(records))"""

env_args = {'var_call_AG2OGnxIkTd3tg7kCM51vQXu': [{'book_id': 'bookid_4', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_14', 'title': 'The Old Man and the Pirate Princess', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_32', 'title': 'The Very Hungry Caterpillar (English and Arabic Edition)', 'categories': '["Books", "Children\'s Books", "Early Learning"]'}, {'book_id': 'bookid_40', 'title': 'Egypt (Enchantment of the World)', 'categories': '["Books", "Children\'s Books", "Geography & Cultures"]'}, {'book_id': 'bookid_48', 'title': 'Clark the Shark: Tooth Trouble, No. 1', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_52', 'title': "I Hadn't Meant to Tell You This", 'categories': '["Books", "Children\'s Books", "Geography & Cultures"]'}, {'book_id': 'bookid_54', 'title': 'Favorite Thorton W. Burgess Stories: 6 Books', 'categories': '["Books", "Children\'s Books", "Animals"]'}, {'book_id': 'bookid_55', 'title': 'Behind the Wheel (Choose Your Own Adventure #35)(Paperback/Revised)', 'categories': '["Books", "Children\'s Books", "Literature & Fiction"]'}, {'book_id': 'bookid_57', 'title': "Goodnight Riley and the Moon, It's Almost Bedtime: Personalized Children’s Books, Personalized Gifts, and Bedtime Stories (A Magnificent Me! estorytime.com Series)", 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_96', 'title': 'Cheer Up, Ben Franklin! (Young Historians)', 'categories': '["Books", "Children\'s Books", "History"]'}, {'book_id': 'bookid_99', 'title': 'Buddy the Soldier Bear', 'categories': '["Books", "Children\'s Books", "Literature & Fiction"]'}, {'book_id': 'bookid_108', 'title': 'The Library Book', 'categories': '["Books", "Children\'s Books", "Education & Reference"]'}, {'book_id': 'bookid_111', 'title': 'Can You Buy Me The Wind?', 'categories': '["Books", "Children\'s Books", "Literature & Fiction"]'}, {'book_id': 'bookid_116', 'title': 'From the Earth to the Moon by Jules Verne, Fiction, Fantasy & Magic', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_120', 'title': "Caroline's Color Dreams: Los Sueños Coloridos De Carolina : Babl Children's Books in Spanish and English", 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_124', 'title': 'Skeleton Play: A Fun, Rhyming Halloween Book for Kids! (1)', 'categories': '["Books", "Children\'s Books", "Holidays & Celebrations"]'}, {'book_id': 'bookid_130', 'title': "Benny Goes To The Moon: The great new book from Top Children's entertainer Gerry Ogilvie (1)", 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_132', 'title': 'Mae and Jane in the Rain', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_145', 'title': 'Kirsten: An American Girl : 1854 (The American Girls Collection/Boxed Set)', 'categories': '["Books", "Boxed Sets", "Children\'s Books"]'}, {'book_id': 'bookid_146', 'title': 'LunaLu the Llamacorn', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_149', 'title': 'Trouble in the CTC!: The Terra Prime Adventures Book 2', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_152', 'title': 'Around the World Mazes', 'categories': '["Books", "Children\'s Books", "Activities, Crafts & Games"]'}, {'book_id': 'bookid_158', 'title': 'Cleo Porter and the Body Electric', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_163', 'title': 'Monster Kisses', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_170', 'title': 'Pokémon: Sun & Moon, Vol. 8 (8)', 'categories': '["Books", "Children\'s Books", "Comics & Graphic Novels"]'}], 'var_call_A1SugLySLWhCdvXQdFdxSnNw': ['review'], 'var_call_6azw9jlPyswhfEzVrgtlVJ0a': 'file_storage/call_6azw9jlPyswhfEzVrgtlVJ0a.json'}

exec(code, env_args)
