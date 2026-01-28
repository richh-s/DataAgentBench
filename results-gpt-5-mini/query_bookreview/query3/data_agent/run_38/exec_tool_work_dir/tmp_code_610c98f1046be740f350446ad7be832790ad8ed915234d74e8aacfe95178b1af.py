code = """import pandas as pd
import json
import re

# Load original query results
reviews = var_call_MOotSShOsXtEQfpwSzpv9XdZ
with open(var_call_T02kR0buOTzYLhzSmuCOWsiV, 'r') as f:
    books = json.load(f)

# Create DataFrames
df_reviews = pd.DataFrame(reviews)
df_books = pd.DataFrame(books)

# Convert types
df_reviews['avg_rating'] = df_reviews['avg_rating'].astype(float)
df_reviews['review_count'] = df_reviews['review_count'].astype(int)

# Extract numeric id helper
def extract_num(s):
    if pd.isna(s):
        return None
    m = re.search(r'_(\d+)$', s)
    return int(m.group(1)) if m else None

# Add numeric ids
df_reviews['num_id'] = df_reviews['purchase_id'].apply(extract_num)
df_books['num_id'] = df_books['book_id'].apply(extract_num)

# Merge
df_merged = pd.merge(df_reviews, df_books, on='num_id', how='inner')

# Ensure title column comes from books table
if 'title_y' in df_merged.columns:
    df_merged['book_title'] = df_merged['title_y']
elif 'title' in df_merged.columns:
    # if only one title column exists, prefer the books' title when available
    df_merged['book_title'] = df_merged['title']
else:
    df_merged['book_title'] = None

# Filter for Children's Books and avg_rating >= 4.5
mask_children = df_merged['categories'].fillna('').str.contains("Children's Books")
mask_rating = df_merged['avg_rating'] >= 4.5
result_df = df_merged[mask_children & mask_rating].copy()

# Build plain-text answer
if not result_df.empty:
    lines = []
    for _, row in result_df.iterrows():
        title = row.get('book_title')
        book_id = row.get('book_id')
        avg = row.get('avg_rating')
        cnt = row.get('review_count')
        lines.append(f"{title} (book_id: {book_id}): avg_rating={avg}, reviews={cnt}")
    answer_text = "\n".join(lines)
else:
    answer_text = "No Children's Books found with average rating >= 4.5 since 2020."

print("__RESULT__:")
print(json.dumps(answer_text))"""

env_args = {'var_call_nCFaGwXbaMJTqPROrmtDkLbF': ['review'], 'var_call_MOotSShOsXtEQfpwSzpv9XdZ': [{'purchase_id': 'purchaseid_10', 'avg_rating': '5.0', 'review_count': '4'}, {'purchase_id': 'purchaseid_105', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_107', 'avg_rating': '4.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_108', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_109', 'avg_rating': '1.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_11', 'avg_rating': '4.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_110', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_115', 'avg_rating': '4.75', 'review_count': '8'}, {'purchase_id': 'purchaseid_118', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_12', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_122', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_126', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_129', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_13', 'avg_rating': '4.923076923076923', 'review_count': '13'}, {'purchase_id': 'purchaseid_130', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_137', 'avg_rating': '4.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_14', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_140', 'avg_rating': '4.0', 'review_count': '4'}, {'purchase_id': 'purchaseid_144', 'avg_rating': '5.0', 'review_count': '4'}, {'purchase_id': 'purchaseid_145', 'avg_rating': '4.0', 'review_count': '5'}, {'purchase_id': 'purchaseid_146', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_149', 'avg_rating': '4.9', 'review_count': '10'}, {'purchase_id': 'purchaseid_152', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_154', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_155', 'avg_rating': '1.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_158', 'avg_rating': '4.708333333333333', 'review_count': '24'}, {'purchase_id': 'purchaseid_161', 'avg_rating': '4.5', 'review_count': '2'}, {'purchase_id': 'purchaseid_167', 'avg_rating': '4.0', 'review_count': '12'}, {'purchase_id': 'purchaseid_169', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_170', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_172', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_178', 'avg_rating': '4.795918367346939', 'review_count': '49'}, {'purchase_id': 'purchaseid_182', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_184', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_185', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_187', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_189', 'avg_rating': '2.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_192', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_193', 'avg_rating': '4.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_196', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_198', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_20', 'avg_rating': '3.875', 'review_count': '16'}, {'purchase_id': 'purchaseid_200', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_22', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_23', 'avg_rating': '4.5', 'review_count': '2'}, {'purchase_id': 'purchaseid_25', 'avg_rating': '4.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_3', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_31', 'avg_rating': '4.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_32', 'avg_rating': '3.5714285714285716', 'review_count': '7'}, {'purchase_id': 'purchaseid_33', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_37', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_38', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_39', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_4', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_40', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_41', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_45', 'avg_rating': '4.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_46', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_48', 'avg_rating': '4.75', 'review_count': '4'}, {'purchase_id': 'purchaseid_5', 'avg_rating': '3.75', 'review_count': '4'}, {'purchase_id': 'purchaseid_50', 'avg_rating': '4.5', 'review_count': '2'}, {'purchase_id': 'purchaseid_54', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_55', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_6', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_60', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_62', 'avg_rating': '4.0', 'review_count': '6'}, {'purchase_id': 'purchaseid_66', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_67', 'avg_rating': '3.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_72', 'avg_rating': '4.5', 'review_count': '2'}, {'purchase_id': 'purchaseid_74', 'avg_rating': '5.0', 'review_count': '8'}, {'purchase_id': 'purchaseid_76', 'avg_rating': '4.75', 'review_count': '4'}, {'purchase_id': 'purchaseid_8', 'avg_rating': '4.709677419354839', 'review_count': '31'}, {'purchase_id': 'purchaseid_80', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_83', 'avg_rating': '5.0', 'review_count': '14'}, {'purchase_id': 'purchaseid_85', 'avg_rating': '3.8333333333333335', 'review_count': '12'}, {'purchase_id': 'purchaseid_88', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_93', 'avg_rating': '3.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_94', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_96', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_99', 'avg_rating': '4.4', 'review_count': '5'}], 'var_call_cdXwGKcMXS60ugxQBPepKBQ6': ['books_info'], 'var_call_T02kR0buOTzYLhzSmuCOWsiV': 'file_storage/call_T02kR0buOTzYLhzSmuCOWsiV.json', 'var_call_1RNDVDypqTlryYz0vpy74uz4': [{'book_id': 'bookid_108', 'title': 'The Library Book', 'categories': '["Books", "Children\'s Books", "Education & Reference"]', 'avg_rating': 5.0, 'review_count': 3, 'purchase_id': 'purchaseid_108'}, {'book_id': 'bookid_130', 'title': "Benny Goes To The Moon: The great new book from Top Children's entertainer Gerry Ogilvie (1)", 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]', 'avg_rating': 5.0, 'review_count': 1, 'purchase_id': 'purchaseid_130'}, {'book_id': 'bookid_14', 'title': 'The Old Man and the Pirate Princess', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]', 'avg_rating': 5.0, 'review_count': 1, 'purchase_id': 'purchaseid_14'}, {'book_id': 'bookid_146', 'title': 'LunaLu the Llamacorn', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]', 'avg_rating': 5.0, 'review_count': 3, 'purchase_id': 'purchaseid_146'}, {'book_id': 'bookid_149', 'title': 'Trouble in the CTC!: The Terra Prime Adventures Book 2', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]', 'avg_rating': 4.9, 'review_count': 10, 'purchase_id': 'purchaseid_149'}, {'book_id': 'bookid_152', 'title': 'Around the World Mazes', 'categories': '["Books", "Children\'s Books", "Activities, Crafts & Games"]', 'avg_rating': 5.0, 'review_count': 1, 'purchase_id': 'purchaseid_152'}, {'book_id': 'bookid_158', 'title': 'Cleo Porter and the Body Electric', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]', 'avg_rating': 4.708333333333333, 'review_count': 24, 'purchase_id': 'purchaseid_158'}, {'book_id': 'bookid_170', 'title': 'Pokémon: Sun & Moon, Vol. 8 (8)', 'categories': '["Books", "Children\'s Books", "Comics & Graphic Novels"]', 'avg_rating': 5.0, 'review_count': 1, 'purchase_id': 'purchaseid_170'}, {'book_id': 'bookid_4', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]', 'avg_rating': 5.0, 'review_count': 1, 'purchase_id': 'purchaseid_4'}, {'book_id': 'bookid_40', 'title': 'Egypt (Enchantment of the World)', 'categories': '["Books", "Children\'s Books", "Geography & Cultures"]', 'avg_rating': 5.0, 'review_count': 1, 'purchase_id': 'purchaseid_40'}, {'book_id': 'bookid_48', 'title': 'Clark the Shark: Tooth Trouble, No. 1', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]', 'avg_rating': 4.75, 'review_count': 4, 'purchase_id': 'purchaseid_48'}, {'book_id': 'bookid_54', 'title': 'Favorite Thorton W. Burgess Stories: 6 Books', 'categories': '["Books", "Children\'s Books", "Animals"]', 'avg_rating': 5.0, 'review_count': 3, 'purchase_id': 'purchaseid_54'}, {'book_id': 'bookid_55', 'title': 'Behind the Wheel (Choose Your Own Adventure #35)(Paperback/Revised)', 'categories': '["Books", "Children\'s Books", "Literature & Fiction"]', 'avg_rating': 5.0, 'review_count': 1, 'purchase_id': 'purchaseid_55'}, {'book_id': 'bookid_96', 'title': 'Cheer Up, Ben Franklin! (Young Historians)', 'categories': '["Books", "Children\'s Books", "History"]', 'avg_rating': 5.0, 'review_count': 1, 'purchase_id': 'purchaseid_96'}]}

exec(code, env_args)
