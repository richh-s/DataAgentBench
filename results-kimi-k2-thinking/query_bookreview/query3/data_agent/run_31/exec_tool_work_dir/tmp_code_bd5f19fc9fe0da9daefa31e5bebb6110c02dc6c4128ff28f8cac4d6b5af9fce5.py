code = """import json
import pandas as pd
from pathlib import Path

# Read children's books data
children_books_data = locals()['var_functions.query_db:14']
df_children_books = pd.DataFrame(children_books_data)
print(f"Found {len(df_children_books)} children's books")

# Read review data from file
review_data_file = locals()['var_functions.query_db:16']
with open(review_data_file, 'r') as f:
    review_data = json.load(f)

df_reviews = pd.DataFrame(review_data)
print(f"Total reviews: {len(df_reviews)}")

# Filter reviews from 2020 onwards and convert data types
df_reviews['review_time'] = pd.to_datetime(df_reviews['review_time'])
df_reviews['rating'] = df_reviews['rating'].astype(float)
df_reviews_2020 = df_reviews[df_reviews['review_time'] >= '2020-01-01']
print(f"Reviews from 2020 onwards: {len(df_reviews_2020)}")

# Extract numeric IDs for joining
df_children_books['book_num_id'] = df_children_books['book_id'].str.extract('(\d+)').astype(int)
df_reviews_2020['purchase_num_id'] = df_reviews_2020['purchase_id'].str.extract('(\d+)').astype(int)

# Show a few examples of the IDs to verify the pattern
print("\nSample book IDs:")
print(df_children_books[['book_id', 'book_num_id']].head())
print("\nSample purchase IDs:")
print(df_reviews_2020[['purchase_id', 'purchase_num_id']].head())

# Merge the dataframes on numeric IDs
df_merged = pd.merge(df_children_books, df_reviews_2020, left_on='book_num_id', right_on='purchase_num_id', how='inner')
print(f"\nMerged reviews with children's books: {len(df_merged)}")

# Calculate average rating per book
df_avg_ratings = df_merged.groupby(['book_id', 'title']).agg({
    'rating': ['mean', 'count']
}).round(2)

df_avg_ratings.columns = ['avg_rating', 'review_count']
df_avg_ratings = df_avg_ratings.reset_index()

# Filter books with average rating >= 4.5
books_with_high_rating = df_avg_ratings[df_avg_ratings['avg_rating'] >= 4.5]
print(f"Books with avg rating >= 4.5: {len(books_with_high_rating)}")

# Format result and print books with no matches for debugging
if len(books_with_high_rating) == 0:
    print("\nNo books found with average rating >= 4.5")
    print("\nBooks with any reviews from 2020:")
    df_any_reviews = df_avg_ratings[df_avg_ratings['review_count'] > 0]
    print(df_any_reviews.head(10))
    
    # Check if there are any children's books with reviews at all
    print(f"\nTotal children's books with reviews from 2020: {len(df_avg_ratings)}")
else:
    result = books_with_high_rating.sort_values('avg_rating', ascending=False)
    result_data = result.to_dict('records')
    
    # Print result in the required format
    print('__RESULT__:')
    print(json.dumps(result_data, default=str))"""

env_args = {'var_functions.list_db:0': ['books_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['review'], 'var_functions.query_db:8': [{'book_id': 'bookid_4', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_14', 'title': 'The Old Man and the Pirate Princess', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_32', 'title': 'The Very Hungry Caterpillar (English and Arabic Edition)', 'categories': '["Books", "Children\'s Books", "Early Learning"]'}, {'book_id': 'bookid_40', 'title': 'Egypt (Enchantment of the World)', 'categories': '["Books", "Children\'s Books", "Geography & Cultures"]'}, {'book_id': 'bookid_48', 'title': 'Clark the Shark: Tooth Trouble, No. 1', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_52', 'title': "I Hadn't Meant to Tell You This", 'categories': '["Books", "Children\'s Books", "Geography & Cultures"]'}, {'book_id': 'bookid_54', 'title': 'Favorite Thorton W. Burgess Stories: 6 Books', 'categories': '["Books", "Children\'s Books", "Animals"]'}, {'book_id': 'bookid_55', 'title': 'Behind the Wheel (Choose Your Own Adventure #35)(Paperback/Revised)', 'categories': '["Books", "Children\'s Books", "Literature & Fiction"]'}, {'book_id': 'bookid_57', 'title': "Goodnight Riley and the Moon, It's Almost Bedtime: Personalized Children’s Books, Personalized Gifts, and Bedtime Stories (A Magnificent Me! estorytime.com Series)", 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_96', 'title': 'Cheer Up, Ben Franklin! (Young Historians)', 'categories': '["Books", "Children\'s Books", "History"]'}, {'book_id': 'bookid_99', 'title': 'Buddy the Soldier Bear', 'categories': '["Books", "Children\'s Books", "Literature & Fiction"]'}, {'book_id': 'bookid_108', 'title': 'The Library Book', 'categories': '["Books", "Children\'s Books", "Education & Reference"]'}, {'book_id': 'bookid_111', 'title': 'Can You Buy Me The Wind?', 'categories': '["Books", "Children\'s Books", "Literature & Fiction"]'}, {'book_id': 'bookid_116', 'title': 'From the Earth to the Moon by Jules Verne, Fiction, Fantasy & Magic', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_120', 'title': "Caroline's Color Dreams: Los Sueños Coloridos De Carolina : Babl Children's Books in Spanish and English", 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_124', 'title': 'Skeleton Play: A Fun, Rhyming Halloween Book for Kids! (1)', 'categories': '["Books", "Children\'s Books", "Holidays & Celebrations"]'}, {'book_id': 'bookid_130', 'title': "Benny Goes To The Moon: The great new book from Top Children's entertainer Gerry Ogilvie (1)", 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_132', 'title': 'Mae and Jane in the Rain', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_145', 'title': 'Kirsten: An American Girl : 1854 (The American Girls Collection/Boxed Set)', 'categories': '["Books", "Boxed Sets", "Children\'s Books"]'}, {'book_id': 'bookid_146', 'title': 'LunaLu the Llamacorn', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_149', 'title': 'Trouble in the CTC!: The Terra Prime Adventures Book 2', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_152', 'title': 'Around the World Mazes', 'categories': '["Books", "Children\'s Books", "Activities, Crafts & Games"]'}, {'book_id': 'bookid_158', 'title': 'Cleo Porter and the Body Electric', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_163', 'title': 'Monster Kisses', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_170', 'title': 'Pokémon: Sun & Moon, Vol. 8 (8)', 'categories': '["Books", "Children\'s Books", "Comics & Graphic Novels"]'}], 'var_functions.query_db:10': [{'review_time': '2012-11-24 18:52:00', 'rating': '4', 'purchase_id': 'purchaseid_186'}, {'review_time': '2015-12-31 13:35:00', 'rating': '4', 'purchase_id': 'purchaseid_191'}, {'review_time': '2013-05-05 10:47:00', 'rating': '4', 'purchase_id': 'purchaseid_190'}, {'review_time': '2020-08-12 11:06:00', 'rating': '5', 'purchase_id': 'purchaseid_8'}, {'review_time': '2014-11-13 18:55:00', 'rating': '4', 'purchase_id': 'purchaseid_178'}], 'var_functions.query_db:12': [{'review_time': '2023-06-14 09:29:00', 'rating': '5', 'purchase_id': 'purchaseid_178'}, {'review_time': '2023-05-28 10:53:00', 'rating': '5', 'purchase_id': 'purchaseid_83'}, {'review_time': '2023-05-16 17:49:00', 'rating': '5', 'purchase_id': 'purchaseid_13'}, {'review_time': '2023-05-02 06:16:00', 'rating': '1', 'purchase_id': 'purchaseid_85'}, {'review_time': '2023-04-26 11:55:00', 'rating': '5', 'purchase_id': 'purchaseid_149'}, {'review_time': '2023-04-25 19:47:00', 'rating': '5', 'purchase_id': 'purchaseid_13'}, {'review_time': '2023-04-25 15:15:00', 'rating': '5', 'purchase_id': 'purchaseid_74'}, {'review_time': '2023-04-19 04:29:00', 'rating': '5', 'purchase_id': 'purchaseid_85'}, {'review_time': '2023-04-06 08:24:38', 'rating': '5', 'purchase_id': 'purchaseid_13'}, {'review_time': '2023-04-05 05:02:00', 'rating': '5', 'purchase_id': 'purchaseid_13'}], 'var_functions.query_db:14': [{'book_id': 'bookid_4', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_14', 'title': 'The Old Man and the Pirate Princess', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_32', 'title': 'The Very Hungry Caterpillar (English and Arabic Edition)', 'categories': '["Books", "Children\'s Books", "Early Learning"]'}, {'book_id': 'bookid_40', 'title': 'Egypt (Enchantment of the World)', 'categories': '["Books", "Children\'s Books", "Geography & Cultures"]'}, {'book_id': 'bookid_48', 'title': 'Clark the Shark: Tooth Trouble, No. 1', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_52', 'title': "I Hadn't Meant to Tell You This", 'categories': '["Books", "Children\'s Books", "Geography & Cultures"]'}, {'book_id': 'bookid_54', 'title': 'Favorite Thorton W. Burgess Stories: 6 Books', 'categories': '["Books", "Children\'s Books", "Animals"]'}, {'book_id': 'bookid_55', 'title': 'Behind the Wheel (Choose Your Own Adventure #35)(Paperback/Revised)', 'categories': '["Books", "Children\'s Books", "Literature & Fiction"]'}, {'book_id': 'bookid_57', 'title': "Goodnight Riley and the Moon, It's Almost Bedtime: Personalized Children’s Books, Personalized Gifts, and Bedtime Stories (A Magnificent Me! estorytime.com Series)", 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_96', 'title': 'Cheer Up, Ben Franklin! (Young Historians)', 'categories': '["Books", "Children\'s Books", "History"]'}, {'book_id': 'bookid_99', 'title': 'Buddy the Soldier Bear', 'categories': '["Books", "Children\'s Books", "Literature & Fiction"]'}, {'book_id': 'bookid_108', 'title': 'The Library Book', 'categories': '["Books", "Children\'s Books", "Education & Reference"]'}, {'book_id': 'bookid_111', 'title': 'Can You Buy Me The Wind?', 'categories': '["Books", "Children\'s Books", "Literature & Fiction"]'}, {'book_id': 'bookid_116', 'title': 'From the Earth to the Moon by Jules Verne, Fiction, Fantasy & Magic', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_120', 'title': "Caroline's Color Dreams: Los Sueños Coloridos De Carolina : Babl Children's Books in Spanish and English", 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_124', 'title': 'Skeleton Play: A Fun, Rhyming Halloween Book for Kids! (1)', 'categories': '["Books", "Children\'s Books", "Holidays & Celebrations"]'}, {'book_id': 'bookid_130', 'title': "Benny Goes To The Moon: The great new book from Top Children's entertainer Gerry Ogilvie (1)", 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_132', 'title': 'Mae and Jane in the Rain', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_145', 'title': 'Kirsten: An American Girl : 1854 (The American Girls Collection/Boxed Set)', 'categories': '["Books", "Boxed Sets", "Children\'s Books"]'}, {'book_id': 'bookid_146', 'title': 'LunaLu the Llamacorn', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_149', 'title': 'Trouble in the CTC!: The Terra Prime Adventures Book 2', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_152', 'title': 'Around the World Mazes', 'categories': '["Books", "Children\'s Books", "Activities, Crafts & Games"]'}, {'book_id': 'bookid_158', 'title': 'Cleo Porter and the Body Electric', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_163', 'title': 'Monster Kisses', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_170', 'title': 'Pokémon: Sun & Moon, Vol. 8 (8)', 'categories': '["Books", "Children\'s Books", "Comics & Graphic Novels"]'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
