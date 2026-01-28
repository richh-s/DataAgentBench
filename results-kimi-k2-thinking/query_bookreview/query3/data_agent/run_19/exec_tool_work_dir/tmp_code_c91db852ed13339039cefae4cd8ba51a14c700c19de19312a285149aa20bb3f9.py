code = """import json
import pandas as pd

# Load children's books data
children_books = locals()['var_functions.query_db:0']
children_books_df = pd.DataFrame(children_books)

# Load review data from file
review_file_path = locals()['var_functions.query_db:8']
with open(review_file_path, 'r') as f:
    review_data = json.load(f)
    
review_df = pd.DataFrame(review_data)

print('Children books found:', len(children_books_df))
print('Reviews from 2020 onwards found:', len(review_df))

# Extract numeric IDs for matching
children_books_df['numeric_id'] = children_books_df['book_id'].str.extract('(\d+)').astype(int)
review_df['numeric_id'] = review_df['purchase_id'].str.extract('(\d+)').astype(int)
print('Data prepared for joining')

result = 'Data loading complete'
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'book_id': 'bookid_4', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still'}, {'book_id': 'bookid_14', 'title': 'The Old Man and the Pirate Princess'}, {'book_id': 'bookid_32', 'title': 'The Very Hungry Caterpillar (English and Arabic Edition)'}, {'book_id': 'bookid_40', 'title': 'Egypt (Enchantment of the World)'}, {'book_id': 'bookid_48', 'title': 'Clark the Shark: Tooth Trouble, No. 1'}, {'book_id': 'bookid_52', 'title': "I Hadn't Meant to Tell You This"}, {'book_id': 'bookid_54', 'title': 'Favorite Thorton W. Burgess Stories: 6 Books'}, {'book_id': 'bookid_55', 'title': 'Behind the Wheel (Choose Your Own Adventure #35)(Paperback/Revised)'}, {'book_id': 'bookid_57', 'title': "Goodnight Riley and the Moon, It's Almost Bedtime: Personalized Children’s Books, Personalized Gifts, and Bedtime Stories (A Magnificent Me! estorytime.com Series)"}, {'book_id': 'bookid_96', 'title': 'Cheer Up, Ben Franklin! (Young Historians)'}, {'book_id': 'bookid_99', 'title': 'Buddy the Soldier Bear'}, {'book_id': 'bookid_108', 'title': 'The Library Book'}, {'book_id': 'bookid_111', 'title': 'Can You Buy Me The Wind?'}, {'book_id': 'bookid_116', 'title': 'From the Earth to the Moon by Jules Verne, Fiction, Fantasy & Magic'}, {'book_id': 'bookid_120', 'title': "Caroline's Color Dreams: Los Sueños Coloridos De Carolina : Babl Children's Books in Spanish and English"}, {'book_id': 'bookid_124', 'title': 'Skeleton Play: A Fun, Rhyming Halloween Book for Kids! (1)'}, {'book_id': 'bookid_130', 'title': "Benny Goes To The Moon: The great new book from Top Children's entertainer Gerry Ogilvie (1)"}, {'book_id': 'bookid_132', 'title': 'Mae and Jane in the Rain'}, {'book_id': 'bookid_145', 'title': 'Kirsten: An American Girl : 1854 (The American Girls Collection/Boxed Set)'}, {'book_id': 'bookid_146', 'title': 'LunaLu the Llamacorn'}, {'book_id': 'bookid_149', 'title': 'Trouble in the CTC!: The Terra Prime Adventures Book 2'}, {'book_id': 'bookid_152', 'title': 'Around the World Mazes'}, {'book_id': 'bookid_158', 'title': 'Cleo Porter and the Body Electric'}, {'book_id': 'bookid_163', 'title': 'Monster Kisses'}, {'book_id': 'bookid_170', 'title': 'Pokémon: Sun & Moon, Vol. 8 (8)'}], 'var_functions.execute_python:5': ['bookid_4', 'bookid_14', 'bookid_32', 'bookid_40', 'bookid_48', 'bookid_52', 'bookid_54', 'bookid_55', 'bookid_57', 'bookid_96', 'bookid_99', 'bookid_108', 'bookid_111', 'bookid_116', 'bookid_120', 'bookid_124', 'bookid_130', 'bookid_132', 'bookid_145', 'bookid_146', 'bookid_149', 'bookid_152', 'bookid_158', 'bookid_163', 'bookid_170'], 'var_functions.list_db:6': ['review'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
