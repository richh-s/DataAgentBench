code = """import pandas as pd
import json

book_ids_with_titles = locals()['var_function-call-11767778878811922875']
review_data_path = locals()['var_function-call-11382397401168780903']

with open(review_data_path, 'r') as f:
    review_data = json.load(f)

df_books = pd.DataFrame(book_ids_with_titles)
df_reviews = pd.DataFrame(review_data)

df_reviews['rating'] = pd.to_numeric(df_reviews['rating'])
df_reviews['review_time'] = pd.to_datetime(df_reviews['review_time'])

# Filter reviews from 2020 onwards
df_reviews_filtered_time = df_reviews[df_reviews['review_time'].dt.year >= 2020]

# Filter reviews for books categorized as 'Children\'s Books'
df_reviews_children = df_reviews_filtered_time[df_reviews_filtered_time['purchase_id'].isin(df_books['book_id'])]

# Calculate average rating for each book
df_avg_ratings = df_reviews_children.groupby('purchase_id')['rating'].mean().reset_index()

# Filter for books with average rating >= 4.5
df_highly_rated_children = df_avg_ratings[df_avg_ratings['rating'] >= 4.5]

# Join with books_info to get the titles
result = pd.merge(df_highly_rated_children, df_books, left_on='purchase_id', right_on='book_id')

print("__RESULT__:")
print(result['title'].tolist())"""

env_args = {'var_function-call-10905855161344533246': ['books_info'], 'var_function-call-823286447514667173': [{'book_id': 'bookid_4'}, {'book_id': 'bookid_14'}, {'book_id': 'bookid_32'}, {'book_id': 'bookid_40'}, {'book_id': 'bookid_48'}, {'book_id': 'bookid_52'}, {'book_id': 'bookid_54'}, {'book_id': 'bookid_55'}, {'book_id': 'bookid_57'}, {'book_id': 'bookid_96'}, {'book_id': 'bookid_99'}, {'book_id': 'bookid_108'}, {'book_id': 'bookid_111'}, {'book_id': 'bookid_116'}, {'book_id': 'bookid_120'}, {'book_id': 'bookid_124'}, {'book_id': 'bookid_130'}, {'book_id': 'bookid_132'}, {'book_id': 'bookid_145'}, {'book_id': 'bookid_146'}, {'book_id': 'bookid_149'}, {'book_id': 'bookid_152'}, {'book_id': 'bookid_158'}, {'book_id': 'bookid_163'}, {'book_id': 'bookid_170'}], 'var_function-call-18359033879084326006': ['review'], 'var_function-call-11620096789899722257': [], 'var_function-call-11767778878811922875': [{'book_id': 'bookid_4', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still'}, {'book_id': 'bookid_14', 'title': 'The Old Man and the Pirate Princess'}, {'book_id': 'bookid_32', 'title': 'The Very Hungry Caterpillar (English and Arabic Edition)'}, {'book_id': 'bookid_40', 'title': 'Egypt (Enchantment of the World)'}, {'book_id': 'bookid_48', 'title': 'Clark the Shark: Tooth Trouble, No. 1'}, {'book_id': 'bookid_52', 'title': "I Hadn't Meant to Tell You This"}, {'book_id': 'bookid_54', 'title': 'Favorite Thorton W. Burgess Stories: 6 Books'}, {'book_id': 'bookid_55', 'title': 'Behind the Wheel (Choose Your Own Adventure #35)(Paperback/Revised)'}, {'book_id': 'bookid_57', 'title': "Goodnight Riley and the Moon, It's Almost Bedtime: Personalized Children’s Books, Personalized Gifts, and Bedtime Stories (A Magnificent Me! estorytime.com Series)"}, {'book_id': 'bookid_96', 'title': 'Cheer Up, Ben Franklin! (Young Historians)'}, {'book_id': 'bookid_99', 'title': 'Buddy the Soldier Bear'}, {'book_id': 'bookid_108', 'title': 'The Library Book'}, {'book_id': 'bookid_111', 'title': 'Can You Buy Me The Wind?'}, {'book_id': 'bookid_116', 'title': 'From the Earth to the Moon by Jules Verne, Fiction, Fantasy & Magic'}, {'book_id': 'bookid_120', 'title': "Caroline's Color Dreams: Los Sueños Coloridos De Carolina : Babl Children's Books in Spanish and English"}, {'book_id': 'bookid_124', 'title': 'Skeleton Play: A Fun, Rhyming Halloween Book for Kids! (1)'}, {'book_id': 'bookid_130', 'title': "Benny Goes To The Moon: The great new book from Top Children's entertainer Gerry Ogilvie (1)"}, {'book_id': 'bookid_132', 'title': 'Mae and Jane in the Rain'}, {'book_id': 'bookid_145', 'title': 'Kirsten: An American Girl : 1854 (The American Girls Collection/Boxed Set)'}, {'book_id': 'bookid_146', 'title': 'LunaLu the Llamacorn'}, {'book_id': 'bookid_149', 'title': 'Trouble in the CTC!: The Terra Prime Adventures Book 2'}, {'book_id': 'bookid_152', 'title': 'Around the World Mazes'}, {'book_id': 'bookid_158', 'title': 'Cleo Porter and the Body Electric'}, {'book_id': 'bookid_163', 'title': 'Monster Kisses'}, {'book_id': 'bookid_170', 'title': 'Pokémon: Sun & Moon, Vol. 8 (8)'}], 'var_function-call-8045795041171620258': "'bookid_4', 'bookid_14', 'bookid_32', 'bookid_40', 'bookid_48', 'bookid_52', 'bookid_54', 'bookid_55', 'bookid_57', 'bookid_96', 'bookid_99', 'bookid_108', 'bookid_111', 'bookid_116', 'bookid_120', 'bookid_124', 'bookid_130', 'bookid_132', 'bookid_145', 'bookid_146', 'bookid_149', 'bookid_152', 'bookid_158', 'bookid_163', 'bookid_170'", 'var_function-call-1587689907002152480': [], 'var_function-call-11382397401168780903': 'file_storage/function-call-11382397401168780903.json'}

exec(code, env_args)
