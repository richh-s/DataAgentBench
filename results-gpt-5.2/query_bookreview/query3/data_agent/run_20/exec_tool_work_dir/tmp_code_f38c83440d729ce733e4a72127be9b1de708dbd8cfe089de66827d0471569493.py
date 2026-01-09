code = """import json, pandas as pd

# books list
books = pd.DataFrame(var_call_udhVCPrLPWOaF3yK2Ap4qce6)

# reviews large file
path = var_call_uTp9FJE2iywVBzD9Ezaav0AD
with open(path, 'r', encoding='utf-8') as f:
    reviews_data = json.load(f)
reviews = pd.DataFrame(reviews_data)

# normalize ids: purchaseid_XX vs bookid_XX => extract numeric suffix
books['id_num'] = books['book_id'].str.extract(r'(\d+)$').astype('Int64')
reviews['id_num'] = reviews['purchase_id'].str.extract(r'(\d+)$').astype('Int64')

# ratings to float
reviews['rating'] = pd.to_numeric(reviews['rating'], errors='coerce')

# filter only reviews that match these children books
child_ids = set(books['id_num'].dropna().astype(int).tolist())
rev_child = reviews[reviews['id_num'].isin(child_ids)].copy()

agg = (rev_child.groupby('id_num')
       .agg(avg_rating=('rating','mean'), review_count=('rating','count'))
       .reset_index())

# join back to books
res = books.merge(agg, on='id_num', how='left')
res = res[res['review_count'].fillna(0) > 0]
res = res[res['avg_rating'] >= 4.5].copy()
res = res.sort_values(['avg_rating','review_count','title'], ascending=[False, False, True])

out = res[['title','book_id','avg_rating','review_count']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_udhVCPrLPWOaF3yK2Ap4qce6': [{'book_id': 'bookid_4', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_14', 'title': 'The Old Man and the Pirate Princess', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_32', 'title': 'The Very Hungry Caterpillar (English and Arabic Edition)', 'categories': '["Books", "Children\'s Books", "Early Learning"]'}, {'book_id': 'bookid_40', 'title': 'Egypt (Enchantment of the World)', 'categories': '["Books", "Children\'s Books", "Geography & Cultures"]'}, {'book_id': 'bookid_48', 'title': 'Clark the Shark: Tooth Trouble, No. 1', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_52', 'title': "I Hadn't Meant to Tell You This", 'categories': '["Books", "Children\'s Books", "Geography & Cultures"]'}, {'book_id': 'bookid_54', 'title': 'Favorite Thorton W. Burgess Stories: 6 Books', 'categories': '["Books", "Children\'s Books", "Animals"]'}, {'book_id': 'bookid_55', 'title': 'Behind the Wheel (Choose Your Own Adventure #35)(Paperback/Revised)', 'categories': '["Books", "Children\'s Books", "Literature & Fiction"]'}, {'book_id': 'bookid_57', 'title': "Goodnight Riley and the Moon, It's Almost Bedtime: Personalized Children’s Books, Personalized Gifts, and Bedtime Stories (A Magnificent Me! estorytime.com Series)", 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_96', 'title': 'Cheer Up, Ben Franklin! (Young Historians)', 'categories': '["Books", "Children\'s Books", "History"]'}, {'book_id': 'bookid_99', 'title': 'Buddy the Soldier Bear', 'categories': '["Books", "Children\'s Books", "Literature & Fiction"]'}, {'book_id': 'bookid_108', 'title': 'The Library Book', 'categories': '["Books", "Children\'s Books", "Education & Reference"]'}, {'book_id': 'bookid_111', 'title': 'Can You Buy Me The Wind?', 'categories': '["Books", "Children\'s Books", "Literature & Fiction"]'}, {'book_id': 'bookid_116', 'title': 'From the Earth to the Moon by Jules Verne, Fiction, Fantasy & Magic', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_120', 'title': "Caroline's Color Dreams: Los Sueños Coloridos De Carolina : Babl Children's Books in Spanish and English", 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_124', 'title': 'Skeleton Play: A Fun, Rhyming Halloween Book for Kids! (1)', 'categories': '["Books", "Children\'s Books", "Holidays & Celebrations"]'}, {'book_id': 'bookid_130', 'title': "Benny Goes To The Moon: The great new book from Top Children's entertainer Gerry Ogilvie (1)", 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_132', 'title': 'Mae and Jane in the Rain', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_145', 'title': 'Kirsten: An American Girl : 1854 (The American Girls Collection/Boxed Set)', 'categories': '["Books", "Boxed Sets", "Children\'s Books"]'}, {'book_id': 'bookid_146', 'title': 'LunaLu the Llamacorn', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_149', 'title': 'Trouble in the CTC!: The Terra Prime Adventures Book 2', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_152', 'title': 'Around the World Mazes', 'categories': '["Books", "Children\'s Books", "Activities, Crafts & Games"]'}, {'book_id': 'bookid_158', 'title': 'Cleo Porter and the Body Electric', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_163', 'title': 'Monster Kisses', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_170', 'title': 'Pokémon: Sun & Moon, Vol. 8 (8)', 'categories': '["Books", "Children\'s Books", "Comics & Graphic Novels"]'}], 'var_call_Z8MNuCvVNTz5KGKV2ZcMFiU5': ['review'], 'var_call_uTp9FJE2iywVBzD9Ezaav0AD': 'file_storage/call_uTp9FJE2iywVBzD9Ezaav0AD.json'}

exec(code, env_args)
