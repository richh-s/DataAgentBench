code = """import json

# Load books
books = locals()['var_function-call-7197889921205200491']
# Load reviews
reviews_path = locals()['var_function-call-7197889921205198904']
with open(reviews_path, 'r') as f:
    reviews = json.load(f)

print("Total books fetched:", len(books))
print("Total reviews fetched:", len(reviews))

# Check book parsing
valid_books = {}
parsed_count = 0
for b in books:
    try:
        cats = json.loads(b['categories'])
        if "Children's Books" in cats:
            valid_books[b['book_id']] = b['title']
            parsed_count += 1
    except Exception as e:
        print(f"Error parsing categories for {b['book_id']}: {e}")

print("Books with 'Children's Books' category:", parsed_count)
print("Sample valid_books keys:", list(valid_books.keys())[:5])

# Check ID mapping
review_ids = set()
mapped_ids = set()
for r in reviews[:100]:
    pid = r['purchase_id']
    review_ids.add(pid)
    if pid.startswith('purchaseid_'):
        bid = 'bookid_' + pid.split('_')[1]
        mapped_ids.add(bid)

print("Sample review purchase_ids:", list(review_ids)[:5])
print("Sample mapped book_ids:", list(mapped_ids)[:5])

# Check intersection
common_ids = set(valid_books.keys()).intersection(mapped_ids)
print("Intersection in sample:", len(common_ids))

# Check intersection on full set
all_mapped_ids = set()
for r in reviews:
    pid = r['purchase_id']
    if pid.startswith('purchaseid_'):
        bid = 'bookid_' + pid.split('_')[1]
        all_mapped_ids.add(bid)

full_intersection = set(valid_books.keys()).intersection(all_mapped_ids)
print("Full intersection count:", len(full_intersection))

# If intersection is small, maybe list some intersecting IDs
if full_intersection:
    print("Sample intersecting ID:", list(full_intersection)[0])
    
print("__RESULT__:")
print(json.dumps("Debug done"))"""

env_args = {'var_function-call-2983286535059599678': [{'book_id': 'bookid_1', 'title': 'Chaucer', 'categories': '["Books", "Literature & Fiction", "History & Criticism"]'}, {'book_id': 'bookid_2', 'title': 'Notes from a Kidwatcher', 'categories': '["Books", "Reference", "Words, Language & Grammar"]'}, {'book_id': 'bookid_3', 'title': 'Service: A Navy SEAL at War', 'categories': '["Books", "Biographies & Memoirs", "Leaders & Notable People"]'}, {'book_id': 'bookid_4', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_5', 'title': 'Parker & Knight', 'categories': '["Books", "Mystery, Thriller & Suspense", "Thrillers & Suspense"]'}], 'var_function-call-9293573632542790989': ['review'], 'var_function-call-5759485024286686657': [{'purchase_id': 'purchaseid_186', 'rating': '4', 'review_time': '2012-11-24 18:52:00'}, {'purchase_id': 'purchaseid_191', 'rating': '4', 'review_time': '2015-12-31 13:35:00'}, {'purchase_id': 'purchaseid_190', 'rating': '4', 'review_time': '2013-05-05 10:47:00'}, {'purchase_id': 'purchaseid_8', 'rating': '5', 'review_time': '2020-08-12 11:06:00'}, {'purchase_id': 'purchaseid_178', 'rating': '4', 'review_time': '2014-11-13 18:55:00'}], 'var_function-call-7197889921205200491': [{'book_id': 'bookid_4', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still'}, {'book_id': 'bookid_14', 'title': 'The Old Man and the Pirate Princess'}, {'book_id': 'bookid_32', 'title': 'The Very Hungry Caterpillar (English and Arabic Edition)'}, {'book_id': 'bookid_40', 'title': 'Egypt (Enchantment of the World)'}, {'book_id': 'bookid_48', 'title': 'Clark the Shark: Tooth Trouble, No. 1'}, {'book_id': 'bookid_52', 'title': "I Hadn't Meant to Tell You This"}, {'book_id': 'bookid_54', 'title': 'Favorite Thorton W. Burgess Stories: 6 Books'}, {'book_id': 'bookid_55', 'title': 'Behind the Wheel (Choose Your Own Adventure #35)(Paperback/Revised)'}, {'book_id': 'bookid_57', 'title': "Goodnight Riley and the Moon, It's Almost Bedtime: Personalized Children’s Books, Personalized Gifts, and Bedtime Stories (A Magnificent Me! estorytime.com Series)"}, {'book_id': 'bookid_96', 'title': 'Cheer Up, Ben Franklin! (Young Historians)'}, {'book_id': 'bookid_99', 'title': 'Buddy the Soldier Bear'}, {'book_id': 'bookid_108', 'title': 'The Library Book'}, {'book_id': 'bookid_111', 'title': 'Can You Buy Me The Wind?'}, {'book_id': 'bookid_116', 'title': 'From the Earth to the Moon by Jules Verne, Fiction, Fantasy & Magic'}, {'book_id': 'bookid_120', 'title': "Caroline's Color Dreams: Los Sueños Coloridos De Carolina : Babl Children's Books in Spanish and English"}, {'book_id': 'bookid_124', 'title': 'Skeleton Play: A Fun, Rhyming Halloween Book for Kids! (1)'}, {'book_id': 'bookid_130', 'title': "Benny Goes To The Moon: The great new book from Top Children's entertainer Gerry Ogilvie (1)"}, {'book_id': 'bookid_132', 'title': 'Mae and Jane in the Rain'}, {'book_id': 'bookid_145', 'title': 'Kirsten: An American Girl : 1854 (The American Girls Collection/Boxed Set)'}, {'book_id': 'bookid_146', 'title': 'LunaLu the Llamacorn'}, {'book_id': 'bookid_149', 'title': 'Trouble in the CTC!: The Terra Prime Adventures Book 2'}, {'book_id': 'bookid_152', 'title': 'Around the World Mazes'}, {'book_id': 'bookid_158', 'title': 'Cleo Porter and the Body Electric'}, {'book_id': 'bookid_163', 'title': 'Monster Kisses'}, {'book_id': 'bookid_170', 'title': 'Pokémon: Sun & Moon, Vol. 8 (8)'}], 'var_function-call-7197889921205198904': 'file_storage/function-call-7197889921205198904.json', 'var_function-call-18095803638518684143': []}

exec(code, env_args)
