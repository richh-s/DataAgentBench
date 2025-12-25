code = """import json
import pandas as pd

# Load books
books_data = locals()['var_function-call-1006204491700562562']
# books_data is a list of dicts

# Load reviews from file
with open(locals()['var_function-call-8558563509388130664'], 'r') as f:
    reviews_data = json.load(f)

# Process books
# Create a dict mapping id_number -> title
book_map = {}
for b in books_data:
    # book_id format: bookid_123
    bid_str = b['book_id']
    if '_' in bid_str:
        bid_num = bid_str.split('_')[1]
        book_map[bid_num] = b['title']

# Process reviews
# Aggregate ratings by id_number
review_sums = {} # id -> sum
review_counts = {} # id -> count

for r in reviews_data:
    pid_str = r['purchase_id']
    rating = float(r['rating'])
    
    if '_' in pid_str:
        pid_num = pid_str.split('_')[1]
        
        # Only consider reviews for books we are interested in
        if pid_num in book_map:
            if pid_num not in review_sums:
                review_sums[pid_num] = 0.0
                review_counts[pid_num] = 0
            review_sums[pid_num] += rating
            review_counts[pid_num] += 1

# Calculate averages and filter
result_titles = []
for pid, total_rating in review_sums.items():
    avg = total_rating / review_counts[pid]
    if avg >= 4.5:
        result_titles.append(book_map[pid])

print("__RESULT__:")
print(json.dumps(result_titles))"""

env_args = {'var_function-call-10280435781581349453': ['books_info'], 'var_function-call-10280435781581350898': ['review'], 'var_function-call-606093380639525263': [{'book_id': 'bookid_1', 'title': 'Chaucer', 'categories': '["Books", "Literature & Fiction", "History & Criticism"]'}, {'book_id': 'bookid_2', 'title': 'Notes from a Kidwatcher', 'categories': '["Books", "Reference", "Words, Language & Grammar"]'}, {'book_id': 'bookid_3', 'title': 'Service: A Navy SEAL at War', 'categories': '["Books", "Biographies & Memoirs", "Leaders & Notable People"]'}, {'book_id': 'bookid_4', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_5', 'title': 'Parker & Knight', 'categories': '["Books", "Mystery, Thriller & Suspense", "Thrillers & Suspense"]'}], 'var_function-call-606093380639524084': [{'purchase_id': 'purchaseid_186', 'rating': '4', 'review_time': '2012-11-24 18:52:00'}, {'purchase_id': 'purchaseid_191', 'rating': '4', 'review_time': '2015-12-31 13:35:00'}, {'purchase_id': 'purchaseid_190', 'rating': '4', 'review_time': '2013-05-05 10:47:00'}, {'purchase_id': 'purchaseid_8', 'rating': '5', 'review_time': '2020-08-12 11:06:00'}, {'purchase_id': 'purchaseid_178', 'rating': '4', 'review_time': '2014-11-13 18:55:00'}], 'var_function-call-3473943008655070961': [{'purchase_id': 'purchaseid_186', 'title': 'Ha! On me!  I thought this was a cookbook!', 'rating': '4'}, {'purchase_id': 'purchaseid_191', 'title': 'Four Stars', 'rating': '4'}, {'purchase_id': 'purchaseid_190', 'title': 'A wonderful adventure in France', 'rating': '4'}, {'purchase_id': 'purchaseid_8', 'title': 'Best beginner book.  Been looking for something like this for a long time.', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'title': 'Referance Guide', 'rating': '4'}], 'var_function-call-3757535306578115343': [{'cid': '0', 'name': 'rating', 'type': 'INTEGER', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '1', 'name': 'title', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'text', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'review_time', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '4', 'name': 'helpful_vote', 'type': 'INTEGER', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '5', 'name': 'verified_purchase', 'type': 'INTEGER', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '6', 'name': 'purchase_id', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}], 'var_function-call-12655655248820785477': [{'count': '25'}], 'var_function-call-12655655248820788466': [{'count(*)': '329'}], 'var_function-call-1006204491700562562': [{'book_id': 'bookid_4', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still'}, {'book_id': 'bookid_14', 'title': 'The Old Man and the Pirate Princess'}, {'book_id': 'bookid_32', 'title': 'The Very Hungry Caterpillar (English and Arabic Edition)'}, {'book_id': 'bookid_40', 'title': 'Egypt (Enchantment of the World)'}, {'book_id': 'bookid_48', 'title': 'Clark the Shark: Tooth Trouble, No. 1'}, {'book_id': 'bookid_52', 'title': "I Hadn't Meant to Tell You This"}, {'book_id': 'bookid_54', 'title': 'Favorite Thorton W. Burgess Stories: 6 Books'}, {'book_id': 'bookid_55', 'title': 'Behind the Wheel (Choose Your Own Adventure #35)(Paperback/Revised)'}, {'book_id': 'bookid_57', 'title': "Goodnight Riley and the Moon, It's Almost Bedtime: Personalized Children’s Books, Personalized Gifts, and Bedtime Stories (A Magnificent Me! estorytime.com Series)"}, {'book_id': 'bookid_96', 'title': 'Cheer Up, Ben Franklin! (Young Historians)'}, {'book_id': 'bookid_99', 'title': 'Buddy the Soldier Bear'}, {'book_id': 'bookid_108', 'title': 'The Library Book'}, {'book_id': 'bookid_111', 'title': 'Can You Buy Me The Wind?'}, {'book_id': 'bookid_116', 'title': 'From the Earth to the Moon by Jules Verne, Fiction, Fantasy & Magic'}, {'book_id': 'bookid_120', 'title': "Caroline's Color Dreams: Los Sueños Coloridos De Carolina : Babl Children's Books in Spanish and English"}, {'book_id': 'bookid_124', 'title': 'Skeleton Play: A Fun, Rhyming Halloween Book for Kids! (1)'}, {'book_id': 'bookid_130', 'title': "Benny Goes To The Moon: The great new book from Top Children's entertainer Gerry Ogilvie (1)"}, {'book_id': 'bookid_132', 'title': 'Mae and Jane in the Rain'}, {'book_id': 'bookid_145', 'title': 'Kirsten: An American Girl : 1854 (The American Girls Collection/Boxed Set)'}, {'book_id': 'bookid_146', 'title': 'LunaLu the Llamacorn'}, {'book_id': 'bookid_149', 'title': 'Trouble in the CTC!: The Terra Prime Adventures Book 2'}, {'book_id': 'bookid_152', 'title': 'Around the World Mazes'}, {'book_id': 'bookid_158', 'title': 'Cleo Porter and the Body Electric'}, {'book_id': 'bookid_163', 'title': 'Monster Kisses'}, {'book_id': 'bookid_170', 'title': 'Pokémon: Sun & Moon, Vol. 8 (8)'}], 'var_function-call-8558563509388130664': 'file_storage/function-call-8558563509388130664.json'}

exec(code, env_args)
