code = """import json, pandas as pd

# load reviews (may be file path)
rev_src = var_call_odDcAEd423pb3ZElwhMT1H2s
if isinstance(rev_src, str):
    with open(rev_src, 'r', encoding='utf-8') as f:
        reviews = json.load(f)
else:
    reviews = rev_src

books = var_call_KhwL9HUTHkZjsaEwaqX0xJfN

rev_df = pd.DataFrame(reviews)
# ratings stored as strings sometimes
rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')

# map purchaseid_x -> bookid_x by suffix after last underscore
rev_df['suffix'] = rev_df['purchase_id'].astype(str).str.extract(r'_(\d+)$')[0]
rev_df['book_id'] = 'bookid_' + rev_df['suffix'].astype(str)

# keep only books in children's list
books_df = pd.DataFrame(books)
child_ids = set(books_df['book_id'].astype(str))
rev_df = rev_df[rev_df['book_id'].isin(child_ids)]

agg = rev_df.groupby('book_id').agg(avg_rating=('rating','mean'), review_count=('rating','size')).reset_index()
agg = agg[agg['avg_rating'] >= 4.5]

out = agg.merge(books_df[['book_id','title','categories']], on='book_id', how='left')
out = out.sort_values(['avg_rating','review_count','title'], ascending=[False, False, True])

# format
out['avg_rating'] = out['avg_rating'].round(3)
result = out.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_KhwL9HUTHkZjsaEwaqX0xJfN': [{'book_id': 'bookid_4', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_14', 'title': 'The Old Man and the Pirate Princess', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_32', 'title': 'The Very Hungry Caterpillar (English and Arabic Edition)', 'categories': '["Books", "Children\'s Books", "Early Learning"]'}, {'book_id': 'bookid_40', 'title': 'Egypt (Enchantment of the World)', 'categories': '["Books", "Children\'s Books", "Geography & Cultures"]'}, {'book_id': 'bookid_48', 'title': 'Clark the Shark: Tooth Trouble, No. 1', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_52', 'title': "I Hadn't Meant to Tell You This", 'categories': '["Books", "Children\'s Books", "Geography & Cultures"]'}, {'book_id': 'bookid_54', 'title': 'Favorite Thorton W. Burgess Stories: 6 Books', 'categories': '["Books", "Children\'s Books", "Animals"]'}, {'book_id': 'bookid_55', 'title': 'Behind the Wheel (Choose Your Own Adventure #35)(Paperback/Revised)', 'categories': '["Books", "Children\'s Books", "Literature & Fiction"]'}, {'book_id': 'bookid_57', 'title': "Goodnight Riley and the Moon, It's Almost Bedtime: Personalized Children’s Books, Personalized Gifts, and Bedtime Stories (A Magnificent Me! estorytime.com Series)", 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_96', 'title': 'Cheer Up, Ben Franklin! (Young Historians)', 'categories': '["Books", "Children\'s Books", "History"]'}, {'book_id': 'bookid_99', 'title': 'Buddy the Soldier Bear', 'categories': '["Books", "Children\'s Books", "Literature & Fiction"]'}, {'book_id': 'bookid_108', 'title': 'The Library Book', 'categories': '["Books", "Children\'s Books", "Education & Reference"]'}, {'book_id': 'bookid_111', 'title': 'Can You Buy Me The Wind?', 'categories': '["Books", "Children\'s Books", "Literature & Fiction"]'}, {'book_id': 'bookid_116', 'title': 'From the Earth to the Moon by Jules Verne, Fiction, Fantasy & Magic', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_120', 'title': "Caroline's Color Dreams: Los Sueños Coloridos De Carolina : Babl Children's Books in Spanish and English", 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_124', 'title': 'Skeleton Play: A Fun, Rhyming Halloween Book for Kids! (1)', 'categories': '["Books", "Children\'s Books", "Holidays & Celebrations"]'}, {'book_id': 'bookid_130', 'title': "Benny Goes To The Moon: The great new book from Top Children's entertainer Gerry Ogilvie (1)", 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_132', 'title': 'Mae and Jane in the Rain', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_145', 'title': 'Kirsten: An American Girl : 1854 (The American Girls Collection/Boxed Set)', 'categories': '["Books", "Boxed Sets", "Children\'s Books"]'}, {'book_id': 'bookid_146', 'title': 'LunaLu the Llamacorn', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_149', 'title': 'Trouble in the CTC!: The Terra Prime Adventures Book 2', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_152', 'title': 'Around the World Mazes', 'categories': '["Books", "Children\'s Books", "Activities, Crafts & Games"]'}, {'book_id': 'bookid_158', 'title': 'Cleo Porter and the Body Electric', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_163', 'title': 'Monster Kisses', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_170', 'title': 'Pokémon: Sun & Moon, Vol. 8 (8)', 'categories': '["Books", "Children\'s Books", "Comics & Graphic Novels"]'}], 'var_call_6ScO0piauBjzi7zzVLMXNZQG': ['review'], 'var_call_odDcAEd423pb3ZElwhMT1H2s': 'file_storage/call_odDcAEd423pb3ZElwhMT1H2s.json'}

exec(code, env_args)
