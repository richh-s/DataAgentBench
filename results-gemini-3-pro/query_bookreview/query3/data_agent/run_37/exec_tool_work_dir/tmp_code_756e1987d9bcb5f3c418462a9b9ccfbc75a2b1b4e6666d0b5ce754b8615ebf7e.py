code = """import json
import pandas as pd

# Load books
books = pd.DataFrame(locals()['var_function-call-2079776850602896211'])

# Load reviews
# The reviews result is in a file
with open(locals()['var_function-call-15646119665625311226'], 'r') as f:
    reviews_data = json.load(f)
reviews = pd.DataFrame(reviews_data)

# Process IDs to enable join
# Extract number from book_id ("bookid_X" -> X)
# Extract number from purchase_id ("purchaseid_X" -> X)

def extract_id(s):
    if pd.isna(s):
        return None
    # Assuming format prefix_number
    parts = s.split('_')
    if len(parts) > 1:
        return parts[1]
    return s

books['join_id'] = books['book_id'].apply(extract_id)
reviews['join_id'] = reviews['purchase_id'].apply(extract_id)

# Filter reviews to include only those for the books we identified
# Merge books and reviews on join_id
merged = pd.merge(reviews, books[['book_id', 'title', 'join_id']], on='join_id', how='inner')

# Convert rating to numeric
merged['rating'] = pd.to_numeric(merged['rating'])

# Calculate average rating per book
avg_ratings = merged.groupby(['title']).agg({'rating': 'mean'}).reset_index()

# Filter for avg rating >= 4.5
high_rated = avg_ratings[avg_ratings['rating'] >= 4.5]

# Get the list of titles
result_titles = high_rated['title'].tolist()

print("__RESULT__:")
print(json.dumps(result_titles))"""

env_args = {'var_function-call-17955488222720705615': ['books_info'], 'var_function-call-6020207434960262783': [{'book_id': 'bookid_1', 'title': 'Chaucer', 'categories': '["Books", "Literature & Fiction", "History & Criticism"]'}, {'book_id': 'bookid_2', 'title': 'Notes from a Kidwatcher', 'categories': '["Books", "Reference", "Words, Language & Grammar"]'}, {'book_id': 'bookid_3', 'title': 'Service: A Navy SEAL at War', 'categories': '["Books", "Biographies & Memoirs", "Leaders & Notable People"]'}, {'book_id': 'bookid_4', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_5', 'title': 'Parker & Knight', 'categories': '["Books", "Mystery, Thriller & Suspense", "Thrillers & Suspense"]'}], 'var_function-call-18171913182711343567': ['review'], 'var_function-call-17618932210033204233': [{'rating': '4', 'purchase_id': 'purchaseid_186', 'review_time': '2012-11-24 18:52:00'}, {'rating': '4', 'purchase_id': 'purchaseid_191', 'review_time': '2015-12-31 13:35:00'}, {'rating': '4', 'purchase_id': 'purchaseid_190', 'review_time': '2013-05-05 10:47:00'}, {'rating': '5', 'purchase_id': 'purchaseid_8', 'review_time': '2020-08-12 11:06:00'}, {'rating': '4', 'purchase_id': 'purchaseid_178', 'review_time': '2014-11-13 18:55:00'}], 'var_function-call-2079776850602896211': [{'book_id': 'bookid_4', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still'}, {'book_id': 'bookid_14', 'title': 'The Old Man and the Pirate Princess'}, {'book_id': 'bookid_32', 'title': 'The Very Hungry Caterpillar (English and Arabic Edition)'}, {'book_id': 'bookid_40', 'title': 'Egypt (Enchantment of the World)'}, {'book_id': 'bookid_48', 'title': 'Clark the Shark: Tooth Trouble, No. 1'}, {'book_id': 'bookid_52', 'title': "I Hadn't Meant to Tell You This"}, {'book_id': 'bookid_54', 'title': 'Favorite Thorton W. Burgess Stories: 6 Books'}, {'book_id': 'bookid_55', 'title': 'Behind the Wheel (Choose Your Own Adventure #35)(Paperback/Revised)'}, {'book_id': 'bookid_57', 'title': "Goodnight Riley and the Moon, It's Almost Bedtime: Personalized Children’s Books, Personalized Gifts, and Bedtime Stories (A Magnificent Me! estorytime.com Series)"}, {'book_id': 'bookid_96', 'title': 'Cheer Up, Ben Franklin! (Young Historians)'}, {'book_id': 'bookid_99', 'title': 'Buddy the Soldier Bear'}, {'book_id': 'bookid_108', 'title': 'The Library Book'}, {'book_id': 'bookid_111', 'title': 'Can You Buy Me The Wind?'}, {'book_id': 'bookid_116', 'title': 'From the Earth to the Moon by Jules Verne, Fiction, Fantasy & Magic'}, {'book_id': 'bookid_120', 'title': "Caroline's Color Dreams: Los Sueños Coloridos De Carolina : Babl Children's Books in Spanish and English"}, {'book_id': 'bookid_124', 'title': 'Skeleton Play: A Fun, Rhyming Halloween Book for Kids! (1)'}, {'book_id': 'bookid_130', 'title': "Benny Goes To The Moon: The great new book from Top Children's entertainer Gerry Ogilvie (1)"}, {'book_id': 'bookid_132', 'title': 'Mae and Jane in the Rain'}, {'book_id': 'bookid_145', 'title': 'Kirsten: An American Girl : 1854 (The American Girls Collection/Boxed Set)'}, {'book_id': 'bookid_146', 'title': 'LunaLu the Llamacorn'}, {'book_id': 'bookid_149', 'title': 'Trouble in the CTC!: The Terra Prime Adventures Book 2'}, {'book_id': 'bookid_152', 'title': 'Around the World Mazes'}, {'book_id': 'bookid_158', 'title': 'Cleo Porter and the Body Electric'}, {'book_id': 'bookid_163', 'title': 'Monster Kisses'}, {'book_id': 'bookid_170', 'title': 'Pokémon: Sun & Moon, Vol. 8 (8)'}], 'var_function-call-15646119665625311226': 'file_storage/function-call-15646119665625311226.json'}

exec(code, env_args)
