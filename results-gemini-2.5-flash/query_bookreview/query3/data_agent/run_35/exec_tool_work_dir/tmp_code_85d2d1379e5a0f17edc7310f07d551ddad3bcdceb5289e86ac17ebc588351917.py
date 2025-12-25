code = """import pandas as pd
import json

# Load results from previous steps
rated_books_data = locals()['var_function-call-10185438723085380796']
all_books_categories_filepath = locals()['var_function-call-2370334891330516969']

# Load all book categories from the file
with open(all_books_categories_filepath, 'r') as f:
    all_books_categories_data = json.load(f)

# Convert to pandas DataFrames
df_rated_books = pd.DataFrame(rated_books_data)
df_all_books_categories = pd.DataFrame(all_books_categories_data)

# Rename 'purchase_id' to 'book_id' in df_rated_books for merging
df_rated_books = df_rated_books.rename(columns={'purchase_id': 'book_id'})

# Merge the two DataFrames to combine ratings with categories
df_merged = pd.merge(df_rated_books, df_all_books_categories, on='book_id', how='inner')

# Function to safely parse the categories string and check for 'Children\'s Books'
def is_childrens_book(categories_str):
    try:
        # The categories are stored as a string representation of a list
        categories_list = json.loads(categories_str)
        return 'Children\'s Books' in categories_list
    except (json.JSONDecodeError, TypeError):
        return False

# Filter for 'Children\'s Books' using the function
df_childrens_books_with_ratings = df_merged[df_merged['categories'].apply(is_childrens_book)]

# Filter for average rating of at least 4.5
df_highly_rated_childrens_books = df_childrens_books_with_ratings[df_childrens_books_with_ratings['average_rating'].astype(float) >= 4.5]

# Get unique titles
result_titles = df_highly_rated_childrens_books['title'].unique().tolist()

print("__RESULT__:")
print(json.dumps(result_titles))"""

env_args = {'var_function-call-1884334617205654098': ['review'], 'var_function-call-10185438723085380796': [{'purchase_id': 'purchaseid_10', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_105', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_108', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_110', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_115', 'average_rating': '4.75'}, {'purchase_id': 'purchaseid_118', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_12', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_122', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_126', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_129', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_13', 'average_rating': '4.923076923076923'}, {'purchase_id': 'purchaseid_130', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_14', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_144', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_146', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_149', 'average_rating': '4.9'}, {'purchase_id': 'purchaseid_152', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_154', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_158', 'average_rating': '4.708333333333333'}, {'purchase_id': 'purchaseid_161', 'average_rating': '4.5'}, {'purchase_id': 'purchaseid_169', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_170', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_172', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_178', 'average_rating': '4.795918367346939'}, {'purchase_id': 'purchaseid_182', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_184', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_185', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_187', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_192', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_196', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_198', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_200', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_22', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_23', 'average_rating': '4.5'}, {'purchase_id': 'purchaseid_3', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_33', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_37', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_38', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_39', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_4', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_40', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_41', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_46', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_48', 'average_rating': '4.75'}, {'purchase_id': 'purchaseid_50', 'average_rating': '4.5'}, {'purchase_id': 'purchaseid_54', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_55', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_6', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_60', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_66', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_72', 'average_rating': '4.5'}, {'purchase_id': 'purchaseid_74', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_76', 'average_rating': '4.75'}, {'purchase_id': 'purchaseid_8', 'average_rating': '4.709677419354839'}, {'purchase_id': 'purchaseid_80', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_83', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_88', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_94', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_96', 'average_rating': '5.0'}], 'var_function-call-2950507770111326093': [], 'var_function-call-14097176335515958841': [{'categories': '["Books", "Literature & Fiction", "History & Criticism"]'}, {'categories': '["Books", "Reference", "Words, Language & Grammar"]'}, {'categories': '["Books", "Biographies & Memoirs", "Leaders & Notable People"]'}, {'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'categories': '["Books", "Mystery, Thriller & Suspense", "Thrillers & Suspense"]'}], 'var_function-call-13530770549879954071': [], 'var_function-call-16706620510636819682': [{'book_id': 'bookid_4', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still'}, {'book_id': 'bookid_14', 'title': 'The Old Man and the Pirate Princess'}, {'book_id': 'bookid_32', 'title': 'The Very Hungry Caterpillar (English and Arabic Edition)'}, {'book_id': 'bookid_40', 'title': 'Egypt (Enchantment of the World)'}, {'book_id': 'bookid_48', 'title': 'Clark the Shark: Tooth Trouble, No. 1'}, {'book_id': 'bookid_52', 'title': "I Hadn't Meant to Tell You This"}, {'book_id': 'bookid_54', 'title': 'Favorite Thorton W. Burgess Stories: 6 Books'}, {'book_id': 'bookid_55', 'title': 'Behind the Wheel (Choose Your Own Adventure #35)(Paperback/Revised)'}, {'book_id': 'bookid_57', 'title': "Goodnight Riley and the Moon, It's Almost Bedtime: Personalized Children’s Books, Personalized Gifts, and Bedtime Stories (A Magnificent Me! estorytime.com Series)"}, {'book_id': 'bookid_96', 'title': 'Cheer Up, Ben Franklin! (Young Historians)'}, {'book_id': 'bookid_99', 'title': 'Buddy the Soldier Bear'}, {'book_id': 'bookid_108', 'title': 'The Library Book'}, {'book_id': 'bookid_111', 'title': 'Can You Buy Me The Wind?'}, {'book_id': 'bookid_116', 'title': 'From the Earth to the Moon by Jules Verne, Fiction, Fantasy & Magic'}, {'book_id': 'bookid_120', 'title': "Caroline's Color Dreams: Los Sueños Coloridos De Carolina : Babl Children's Books in Spanish and English"}, {'book_id': 'bookid_124', 'title': 'Skeleton Play: A Fun, Rhyming Halloween Book for Kids! (1)'}, {'book_id': 'bookid_130', 'title': "Benny Goes To The Moon: The great new book from Top Children's entertainer Gerry Ogilvie (1)"}, {'book_id': 'bookid_132', 'title': 'Mae and Jane in the Rain'}, {'book_id': 'bookid_145', 'title': 'Kirsten: An American Girl : 1854 (The American Girls Collection/Boxed Set)'}, {'book_id': 'bookid_146', 'title': 'LunaLu the Llamacorn'}, {'book_id': 'bookid_149', 'title': 'Trouble in the CTC!: The Terra Prime Adventures Book 2'}, {'book_id': 'bookid_152', 'title': 'Around the World Mazes'}, {'book_id': 'bookid_158', 'title': 'Cleo Porter and the Body Electric'}, {'book_id': 'bookid_163', 'title': 'Monster Kisses'}, {'book_id': 'bookid_170', 'title': 'Pokémon: Sun & Moon, Vol. 8 (8)'}], 'var_function-call-9036476929188257927': [], 'var_function-call-2370334891330516969': 'file_storage/function-call-2370334891330516969.json'}

exec(code, env_args)
