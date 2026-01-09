code = """import json, pandas as pd

# load reviews (may be a file path)
rev_src = var_call_plGYVJ8hCpPziEiTIh9rhXKl
if isinstance(rev_src, str):
    with open(rev_src, 'r') as f:
        reviews = json.load(f)
else:
    reviews = rev_src

books = var_call_inETAxSnOzwnOFJr4HaxO7pk

df_books = pd.DataFrame(books)
df_rev = pd.DataFrame(reviews)

# normalize ids: purchaseid_123 -> 123 ; bookid_123 -> 123
for col in ['book_id']:
    df_books[col] = df_books[col].astype(str)
df_rev['purchase_id'] = df_rev['purchase_id'].astype(str)

df_books['id_num'] = df_books['book_id'].str.extract(r'(\d+)').astype(int)
df_rev['id_num'] = df_rev['purchase_id'].str.extract(r'(\d+)').astype(int)

# ratings to float
# ratings in sqlite appear as strings
if 'rating' in df_rev.columns:
    df_rev['rating'] = pd.to_numeric(df_rev['rating'], errors='coerce')

# aggregate from 2020 onwards already filtered
agg = df_rev.groupby('id_num', as_index=False).agg(avg_rating=('rating','mean'), review_count=('rating','count'))

merged = pd.merge(df_books, agg, on='id_num', how='inner')
res = merged[merged['avg_rating'] >= 4.5].copy()
res = res.sort_values(['avg_rating','review_count','title'], ascending=[False, False, True])

out = res[['title','book_id','avg_rating','review_count']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_inETAxSnOzwnOFJr4HaxO7pk': [{'book_id': 'bookid_4', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_14', 'title': 'The Old Man and the Pirate Princess', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_32', 'title': 'The Very Hungry Caterpillar (English and Arabic Edition)', 'categories': '["Books", "Children\'s Books", "Early Learning"]'}, {'book_id': 'bookid_40', 'title': 'Egypt (Enchantment of the World)', 'categories': '["Books", "Children\'s Books", "Geography & Cultures"]'}, {'book_id': 'bookid_48', 'title': 'Clark the Shark: Tooth Trouble, No. 1', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_52', 'title': "I Hadn't Meant to Tell You This", 'categories': '["Books", "Children\'s Books", "Geography & Cultures"]'}, {'book_id': 'bookid_54', 'title': 'Favorite Thorton W. Burgess Stories: 6 Books', 'categories': '["Books", "Children\'s Books", "Animals"]'}, {'book_id': 'bookid_55', 'title': 'Behind the Wheel (Choose Your Own Adventure #35)(Paperback/Revised)', 'categories': '["Books", "Children\'s Books", "Literature & Fiction"]'}, {'book_id': 'bookid_57', 'title': "Goodnight Riley and the Moon, It's Almost Bedtime: Personalized Children’s Books, Personalized Gifts, and Bedtime Stories (A Magnificent Me! estorytime.com Series)", 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_96', 'title': 'Cheer Up, Ben Franklin! (Young Historians)', 'categories': '["Books", "Children\'s Books", "History"]'}, {'book_id': 'bookid_99', 'title': 'Buddy the Soldier Bear', 'categories': '["Books", "Children\'s Books", "Literature & Fiction"]'}, {'book_id': 'bookid_108', 'title': 'The Library Book', 'categories': '["Books", "Children\'s Books", "Education & Reference"]'}, {'book_id': 'bookid_111', 'title': 'Can You Buy Me The Wind?', 'categories': '["Books", "Children\'s Books", "Literature & Fiction"]'}, {'book_id': 'bookid_116', 'title': 'From the Earth to the Moon by Jules Verne, Fiction, Fantasy & Magic', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_120', 'title': "Caroline's Color Dreams: Los Sueños Coloridos De Carolina : Babl Children's Books in Spanish and English", 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_124', 'title': 'Skeleton Play: A Fun, Rhyming Halloween Book for Kids! (1)', 'categories': '["Books", "Children\'s Books", "Holidays & Celebrations"]'}, {'book_id': 'bookid_130', 'title': "Benny Goes To The Moon: The great new book from Top Children's entertainer Gerry Ogilvie (1)", 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_132', 'title': 'Mae and Jane in the Rain', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_145', 'title': 'Kirsten: An American Girl : 1854 (The American Girls Collection/Boxed Set)', 'categories': '["Books", "Boxed Sets", "Children\'s Books"]'}, {'book_id': 'bookid_146', 'title': 'LunaLu the Llamacorn', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_149', 'title': 'Trouble in the CTC!: The Terra Prime Adventures Book 2', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_152', 'title': 'Around the World Mazes', 'categories': '["Books", "Children\'s Books", "Activities, Crafts & Games"]'}, {'book_id': 'bookid_158', 'title': 'Cleo Porter and the Body Electric', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_163', 'title': 'Monster Kisses', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_170', 'title': 'Pokémon: Sun & Moon, Vol. 8 (8)', 'categories': '["Books", "Children\'s Books", "Comics & Graphic Novels"]'}], 'var_call_blIjoLpwD2DMDBPWqUZmVhsg': ['review'], 'var_call_plGYVJ8hCpPziEiTIh9rhXKl': 'file_storage/call_plGYVJ8hCpPziEiTIh9rhXKl.json'}

exec(code, env_args)
