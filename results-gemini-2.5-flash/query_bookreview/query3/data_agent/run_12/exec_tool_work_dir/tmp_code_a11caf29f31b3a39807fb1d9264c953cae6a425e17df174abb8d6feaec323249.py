code = """import pandas as pd
import json

children_books_full_string = locals()['var_function-call-15249955154798236259']['results'][0]
start_index = children_books_full_string.find('[')
end_index = children_books_full_string.rfind(']') + 1
children_books_json_str = children_books_full_string[start_index:end_index]

children_books = pd.DataFrame(json.loads(children_books_json_str))
reviews = pd.read_json(locals()['var_function-call-12923903255126928998'])

# Rename 'purchase_id' to 'book_id' in reviews for merging
reviews = reviews.rename(columns={'purchase_id': 'book_id'})

# Convert rating to numeric
reviews['rating'] = pd.to_numeric(reviews['rating'])

# Merge the two dataframes
merged_df = pd.merge(children_books, reviews, on='book_id', how='inner')

# Calculate the average rating for each book
average_ratings = merged_df.groupby('title')['rating'].mean().reset_index()

# Filter for books with an average rating of at least 4.5
high_rated_children_books = average_ratings[average_ratings['rating'] >= 4.5]

result = high_rated_children_books['title'].tolist()

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-15249955154798236259': [{'book_id': 'bookid_4', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still'}, {'book_id': 'bookid_14', 'title': 'The Old Man and the Pirate Princess'}, {'book_id': 'bookid_32', 'title': 'The Very Hungry Caterpillar (English and Arabic Edition)'}, {'book_id': 'bookid_40', 'title': 'Egypt (Enchantment of the World)'}, {'book_id': 'bookid_48', 'title': 'Clark the Shark: Tooth Trouble, No. 1'}, {'book_id': 'bookid_52', 'title': "I Hadn't Meant to Tell You This"}, {'book_id': 'bookid_54', 'title': 'Favorite Thorton W. Burgess Stories: 6 Books'}, {'book_id': 'bookid_55', 'title': 'Behind the Wheel (Choose Your Own Adventure #35)(Paperback/Revised)'}, {'book_id': 'bookid_57', 'title': "Goodnight Riley and the Moon, It's Almost Bedtime: Personalized Children’s Books, Personalized Gifts, and Bedtime Stories (A Magnificent Me! estorytime.com Series)"}, {'book_id': 'bookid_96', 'title': 'Cheer Up, Ben Franklin! (Young Historians)'}, {'book_id': 'bookid_99', 'title': 'Buddy the Soldier Bear'}, {'book_id': 'bookid_108', 'title': 'The Library Book'}, {'book_id': 'bookid_111', 'title': 'Can You Buy Me The Wind?'}, {'book_id': 'bookid_116', 'title': 'From the Earth to the Moon by Jules Verne, Fiction, Fantasy & Magic'}, {'book_id': 'bookid_120', 'title': "Caroline's Color Dreams: Los Sueños Coloridos De Carolina : Babl Children's Books in Spanish and English"}, {'book_id': 'bookid_124', 'title': 'Skeleton Play: A Fun, Rhyming Halloween Book for Kids! (1)'}, {'book_id': 'bookid_130', 'title': "Benny Goes To The Moon: The great new book from Top Children's entertainer Gerry Ogilvie (1)"}, {'book_id': 'bookid_132', 'title': 'Mae and Jane in the Rain'}, {'book_id': 'bookid_145', 'title': 'Kirsten: An American Girl : 1854 (The American Girls Collection/Boxed Set)'}, {'book_id': 'bookid_146', 'title': 'LunaLu the Llamacorn'}, {'book_id': 'bookid_149', 'title': 'Trouble in the CTC!: The Terra Prime Adventures Book 2'}, {'book_id': 'bookid_152', 'title': 'Around the World Mazes'}, {'book_id': 'bookid_158', 'title': 'Cleo Porter and the Body Electric'}, {'book_id': 'bookid_163', 'title': 'Monster Kisses'}, {'book_id': 'bookid_170', 'title': 'Pokémon: Sun & Moon, Vol. 8 (8)'}], 'var_function-call-7267196298078259345': ['review'], 'var_function-call-12923903255126928998': 'file_storage/function-call-12923903255126928998.json'}

exec(code, env_args)
