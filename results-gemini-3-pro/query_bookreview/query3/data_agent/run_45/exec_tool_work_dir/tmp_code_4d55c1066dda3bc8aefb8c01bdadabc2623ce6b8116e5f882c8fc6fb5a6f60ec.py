code = """import pandas as pd
import json

# Load books
books = locals()['var_function-call-12043537241011522063']
# books is a list of dicts

# Load reviews from file
with open(locals()['var_function-call-18420541154522107887'], 'r') as f:
    reviews = json.load(f)

# Process books
# Create a dictionary mapping numeric_id -> title
book_map = {}
for b in books:
    # book_id format "bookid_X"
    if 'book_id' in b and b['book_id'] and b['book_id'].startswith('bookid_'):
        bid = b['book_id'].split('_')[1]
        book_map[bid] = b['title']

# Process reviews
# We only care about reviews for the books we identified
# And we need to calculate average rating
from collections import defaultdict

ratings_sum = defaultdict(float)
ratings_count = defaultdict(int)

for r in reviews:
    pid = r['purchase_id']
    # purchase_id format "purchaseid_X"
    if pid and pid.startswith('purchaseid_'):
        rid = pid.split('_')[1]
        if rid in book_map:
            try:
                val = float(r['rating'])
                ratings_sum[rid] += val
                ratings_count[rid] += 1
            except:
                pass

# Calculate averages and filter
result_titles = []
for rid, title in book_map.items():
    if ratings_count[rid] > 0:
        avg = ratings_sum[rid] / ratings_count[rid]
        if avg >= 4.5:
            result_titles.append(title)

print("__RESULT__:")
print(json.dumps(result_titles))"""

env_args = {'var_function-call-12043537241011522063': [{'book_id': 'bookid_4', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_14', 'title': 'The Old Man and the Pirate Princess', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_32', 'title': 'The Very Hungry Caterpillar (English and Arabic Edition)', 'categories': '["Books", "Children\'s Books", "Early Learning"]'}, {'book_id': 'bookid_40', 'title': 'Egypt (Enchantment of the World)', 'categories': '["Books", "Children\'s Books", "Geography & Cultures"]'}, {'book_id': 'bookid_48', 'title': 'Clark the Shark: Tooth Trouble, No. 1', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_52', 'title': "I Hadn't Meant to Tell You This", 'categories': '["Books", "Children\'s Books", "Geography & Cultures"]'}, {'book_id': 'bookid_54', 'title': 'Favorite Thorton W. Burgess Stories: 6 Books', 'categories': '["Books", "Children\'s Books", "Animals"]'}, {'book_id': 'bookid_55', 'title': 'Behind the Wheel (Choose Your Own Adventure #35)(Paperback/Revised)', 'categories': '["Books", "Children\'s Books", "Literature & Fiction"]'}, {'book_id': 'bookid_57', 'title': "Goodnight Riley and the Moon, It's Almost Bedtime: Personalized Children’s Books, Personalized Gifts, and Bedtime Stories (A Magnificent Me! estorytime.com Series)", 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_96', 'title': 'Cheer Up, Ben Franklin! (Young Historians)', 'categories': '["Books", "Children\'s Books", "History"]'}, {'book_id': 'bookid_99', 'title': 'Buddy the Soldier Bear', 'categories': '["Books", "Children\'s Books", "Literature & Fiction"]'}, {'book_id': 'bookid_108', 'title': 'The Library Book', 'categories': '["Books", "Children\'s Books", "Education & Reference"]'}, {'book_id': 'bookid_111', 'title': 'Can You Buy Me The Wind?', 'categories': '["Books", "Children\'s Books", "Literature & Fiction"]'}, {'book_id': 'bookid_116', 'title': 'From the Earth to the Moon by Jules Verne, Fiction, Fantasy & Magic', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_120', 'title': "Caroline's Color Dreams: Los Sueños Coloridos De Carolina : Babl Children's Books in Spanish and English", 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_124', 'title': 'Skeleton Play: A Fun, Rhyming Halloween Book for Kids! (1)', 'categories': '["Books", "Children\'s Books", "Holidays & Celebrations"]'}, {'book_id': 'bookid_130', 'title': "Benny Goes To The Moon: The great new book from Top Children's entertainer Gerry Ogilvie (1)", 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_132', 'title': 'Mae and Jane in the Rain', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_145', 'title': 'Kirsten: An American Girl : 1854 (The American Girls Collection/Boxed Set)', 'categories': '["Books", "Boxed Sets", "Children\'s Books"]'}, {'book_id': 'bookid_146', 'title': 'LunaLu the Llamacorn', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_149', 'title': 'Trouble in the CTC!: The Terra Prime Adventures Book 2', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_152', 'title': 'Around the World Mazes', 'categories': '["Books", "Children\'s Books", "Activities, Crafts & Games"]'}, {'book_id': 'bookid_158', 'title': 'Cleo Porter and the Body Electric', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_163', 'title': 'Monster Kisses', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_170', 'title': 'Pokémon: Sun & Moon, Vol. 8 (8)', 'categories': '["Books", "Children\'s Books", "Comics & Graphic Novels"]'}], 'var_function-call-3861160882069560334': ['review'], 'var_function-call-14472722425884511507': [{'purchase_id': 'purchaseid_186', 'review_time': '2012-11-24 18:52:00', 'rating': '4'}, {'purchase_id': 'purchaseid_191', 'review_time': '2015-12-31 13:35:00', 'rating': '4'}, {'purchase_id': 'purchaseid_190', 'review_time': '2013-05-05 10:47:00', 'rating': '4'}, {'purchase_id': 'purchaseid_8', 'review_time': '2020-08-12 11:06:00', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'review_time': '2014-11-13 18:55:00', 'rating': '4'}], 'var_function-call-18420541154522107887': 'file_storage/function-call-18420541154522107887.json'}

exec(code, env_args)
