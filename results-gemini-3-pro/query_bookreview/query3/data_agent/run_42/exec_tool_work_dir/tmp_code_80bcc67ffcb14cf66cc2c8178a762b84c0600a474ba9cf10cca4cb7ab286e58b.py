code = """import json
import pandas as pd

# Load books
books = locals()['var_function-call-7197889921205200491']

# Load reviews
reviews_path = locals()['var_function-call-7197889921205198904']
with open(reviews_path, 'r') as f:
    reviews = json.load(f)

# Create a set of valid book_ids (Children's books) and a map to titles
valid_books = {}
for b in books:
    # Double check category parsing if needed, but the SQL filter was likely sufficient.
    # We will trust the SQL filter but can verify if strictness is required.
    # The prompt implies strict categorization, so let's verify if 'Children\'s Books' is in the list.
    try:
        cats = json.loads(b['categories'])
        if "Children's Books" in cats:
            valid_books[b['book_id']] = b['title']
    except:
        # If parsing fails or not in list, skip (though SQL LIKE matched it)
        # For safety, if SQL matched, it's likely correct.
        pass

# Aggregate ratings
book_ratings = {} # {book_id: [ratings]}

for r in reviews:
    pid = r['purchase_id']
    # Convert purchaseid_X to bookid_X
    # Assuming the format is strictly purchaseid_...
    if pid.startswith('purchaseid_'):
        bid = 'bookid_' + pid.split('_')[1]
    else:
        continue # Should not happen based on inspection
    
    if bid in valid_books:
        rating = float(r['rating'])
        if bid not in book_ratings:
            book_ratings[bid] = []
        book_ratings[bid].append(rating)

# Calculate averages and filter
result_titles = []
for bid, ratings in book_ratings.items():
    avg_rating = sum(ratings) / len(ratings)
    if avg_rating >= 4.5:
        result_titles.append(valid_books[bid])

# Sort for consistency
result_titles.sort()

print("__RESULT__:")
print(json.dumps(result_titles))"""

env_args = {'var_function-call-2983286535059599678': [{'book_id': 'bookid_1', 'title': 'Chaucer', 'categories': '["Books", "Literature & Fiction", "History & Criticism"]'}, {'book_id': 'bookid_2', 'title': 'Notes from a Kidwatcher', 'categories': '["Books", "Reference", "Words, Language & Grammar"]'}, {'book_id': 'bookid_3', 'title': 'Service: A Navy SEAL at War', 'categories': '["Books", "Biographies & Memoirs", "Leaders & Notable People"]'}, {'book_id': 'bookid_4', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_5', 'title': 'Parker & Knight', 'categories': '["Books", "Mystery, Thriller & Suspense", "Thrillers & Suspense"]'}], 'var_function-call-9293573632542790989': ['review'], 'var_function-call-5759485024286686657': [{'purchase_id': 'purchaseid_186', 'rating': '4', 'review_time': '2012-11-24 18:52:00'}, {'purchase_id': 'purchaseid_191', 'rating': '4', 'review_time': '2015-12-31 13:35:00'}, {'purchase_id': 'purchaseid_190', 'rating': '4', 'review_time': '2013-05-05 10:47:00'}, {'purchase_id': 'purchaseid_8', 'rating': '5', 'review_time': '2020-08-12 11:06:00'}, {'purchase_id': 'purchaseid_178', 'rating': '4', 'review_time': '2014-11-13 18:55:00'}], 'var_function-call-7197889921205200491': [{'book_id': 'bookid_4', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still'}, {'book_id': 'bookid_14', 'title': 'The Old Man and the Pirate Princess'}, {'book_id': 'bookid_32', 'title': 'The Very Hungry Caterpillar (English and Arabic Edition)'}, {'book_id': 'bookid_40', 'title': 'Egypt (Enchantment of the World)'}, {'book_id': 'bookid_48', 'title': 'Clark the Shark: Tooth Trouble, No. 1'}, {'book_id': 'bookid_52', 'title': "I Hadn't Meant to Tell You This"}, {'book_id': 'bookid_54', 'title': 'Favorite Thorton W. Burgess Stories: 6 Books'}, {'book_id': 'bookid_55', 'title': 'Behind the Wheel (Choose Your Own Adventure #35)(Paperback/Revised)'}, {'book_id': 'bookid_57', 'title': "Goodnight Riley and the Moon, It's Almost Bedtime: Personalized Children’s Books, Personalized Gifts, and Bedtime Stories (A Magnificent Me! estorytime.com Series)"}, {'book_id': 'bookid_96', 'title': 'Cheer Up, Ben Franklin! (Young Historians)'}, {'book_id': 'bookid_99', 'title': 'Buddy the Soldier Bear'}, {'book_id': 'bookid_108', 'title': 'The Library Book'}, {'book_id': 'bookid_111', 'title': 'Can You Buy Me The Wind?'}, {'book_id': 'bookid_116', 'title': 'From the Earth to the Moon by Jules Verne, Fiction, Fantasy & Magic'}, {'book_id': 'bookid_120', 'title': "Caroline's Color Dreams: Los Sueños Coloridos De Carolina : Babl Children's Books in Spanish and English"}, {'book_id': 'bookid_124', 'title': 'Skeleton Play: A Fun, Rhyming Halloween Book for Kids! (1)'}, {'book_id': 'bookid_130', 'title': "Benny Goes To The Moon: The great new book from Top Children's entertainer Gerry Ogilvie (1)"}, {'book_id': 'bookid_132', 'title': 'Mae and Jane in the Rain'}, {'book_id': 'bookid_145', 'title': 'Kirsten: An American Girl : 1854 (The American Girls Collection/Boxed Set)'}, {'book_id': 'bookid_146', 'title': 'LunaLu the Llamacorn'}, {'book_id': 'bookid_149', 'title': 'Trouble in the CTC!: The Terra Prime Adventures Book 2'}, {'book_id': 'bookid_152', 'title': 'Around the World Mazes'}, {'book_id': 'bookid_158', 'title': 'Cleo Porter and the Body Electric'}, {'book_id': 'bookid_163', 'title': 'Monster Kisses'}, {'book_id': 'bookid_170', 'title': 'Pokémon: Sun & Moon, Vol. 8 (8)'}], 'var_function-call-7197889921205198904': 'file_storage/function-call-7197889921205198904.json'}

exec(code, env_args)
