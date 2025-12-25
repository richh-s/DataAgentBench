code = """import pandas as pd
import json

# Load books
books = pd.DataFrame(locals()['var_function-call-4381061741710512179'])

# Load reviews
with open(locals()['var_function-call-138004503251038692'], 'r') as f:
    reviews_data = json.load(f)
reviews = pd.DataFrame(reviews_data)

# Normalize IDs
# books['id_num'] = books['book_id'].str.extract(r'(\d+)').astype(int) # Extract number. 
# But let's be safer. Maybe replace prefix.
# book_id format: bookid_X
# purchase_id format: purchaseid_X

books['common_id'] = books['book_id'].str.replace('bookid_', '', regex=False)
reviews['common_id'] = reviews['purchase_id'].str.replace('purchaseid_', '', regex=False)

# Filter valid common_ids if needed? 
# The join will handle it.

# Calculate average rating
# Reviews are already filtered for date >= 2020-01-01
reviews['rating'] = pd.to_numeric(reviews['rating'])
avg_ratings = reviews.groupby('common_id')['rating'].mean().reset_index()
avg_ratings.rename(columns={'rating': 'avg_rating'}, inplace=True)

# Filter avg rating >= 4.5
high_rated = avg_ratings[avg_ratings['avg_rating'] >= 4.5]

# Join with books
result = pd.merge(books, high_rated, on='common_id', how='inner')

# Get titles
titles = result['title'].tolist()

print("__RESULT__:")
print(json.dumps(titles))"""

env_args = {'var_function-call-17917719245279300943': ['review'], 'var_function-call-2480433560858932637': [{'review_time': '2012-11-24 18:52:00'}, {'review_time': '2015-12-31 13:35:00'}, {'review_time': '2013-05-05 10:47:00'}, {'review_time': '2020-08-12 11:06:00'}, {'review_time': '2014-11-13 18:55:00'}], 'var_function-call-17054912306449305661': ['books_info'], 'var_function-call-4381061741710512179': [{'book_id': 'bookid_4', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still'}, {'book_id': 'bookid_14', 'title': 'The Old Man and the Pirate Princess'}, {'book_id': 'bookid_32', 'title': 'The Very Hungry Caterpillar (English and Arabic Edition)'}, {'book_id': 'bookid_40', 'title': 'Egypt (Enchantment of the World)'}, {'book_id': 'bookid_48', 'title': 'Clark the Shark: Tooth Trouble, No. 1'}, {'book_id': 'bookid_52', 'title': "I Hadn't Meant to Tell You This"}, {'book_id': 'bookid_54', 'title': 'Favorite Thorton W. Burgess Stories: 6 Books'}, {'book_id': 'bookid_55', 'title': 'Behind the Wheel (Choose Your Own Adventure #35)(Paperback/Revised)'}, {'book_id': 'bookid_57', 'title': "Goodnight Riley and the Moon, It's Almost Bedtime: Personalized Children’s Books, Personalized Gifts, and Bedtime Stories (A Magnificent Me! estorytime.com Series)"}, {'book_id': 'bookid_96', 'title': 'Cheer Up, Ben Franklin! (Young Historians)'}, {'book_id': 'bookid_99', 'title': 'Buddy the Soldier Bear'}, {'book_id': 'bookid_108', 'title': 'The Library Book'}, {'book_id': 'bookid_111', 'title': 'Can You Buy Me The Wind?'}, {'book_id': 'bookid_116', 'title': 'From the Earth to the Moon by Jules Verne, Fiction, Fantasy & Magic'}, {'book_id': 'bookid_120', 'title': "Caroline's Color Dreams: Los Sueños Coloridos De Carolina : Babl Children's Books in Spanish and English"}, {'book_id': 'bookid_124', 'title': 'Skeleton Play: A Fun, Rhyming Halloween Book for Kids! (1)'}, {'book_id': 'bookid_130', 'title': "Benny Goes To The Moon: The great new book from Top Children's entertainer Gerry Ogilvie (1)"}, {'book_id': 'bookid_132', 'title': 'Mae and Jane in the Rain'}, {'book_id': 'bookid_145', 'title': 'Kirsten: An American Girl : 1854 (The American Girls Collection/Boxed Set)'}, {'book_id': 'bookid_146', 'title': 'LunaLu the Llamacorn'}, {'book_id': 'bookid_149', 'title': 'Trouble in the CTC!: The Terra Prime Adventures Book 2'}, {'book_id': 'bookid_152', 'title': 'Around the World Mazes'}, {'book_id': 'bookid_158', 'title': 'Cleo Porter and the Body Electric'}, {'book_id': 'bookid_163', 'title': 'Monster Kisses'}, {'book_id': 'bookid_170', 'title': 'Pokémon: Sun & Moon, Vol. 8 (8)'}], 'var_function-call-138004503251038692': 'file_storage/function-call-138004503251038692.json'}

exec(code, env_args)
