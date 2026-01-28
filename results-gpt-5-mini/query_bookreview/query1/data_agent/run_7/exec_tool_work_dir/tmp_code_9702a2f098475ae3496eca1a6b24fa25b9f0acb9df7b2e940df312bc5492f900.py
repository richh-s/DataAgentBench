code = """import json
import pandas as pd
import re

# Load books data from the provided JSON file path
books_path = var_call_v0GAwjFkl9yD8qYCzVXKjd3L
with open(books_path, 'r', encoding='utf-8') as f:
    books = json.load(f)

# Load reviews data from storage variable
reviews = var_call_BaA5qhZDH38TWzICIaaOqHN3

# Create DataFrames
books_df = pd.DataFrame(books)
reviews_df = pd.DataFrame(reviews)

# Normalize ratings to numeric
reviews_df['rating'] = pd.to_numeric(reviews_df['rating'], errors='coerce')

# Normalize purchase_id to book_id by replacing 'purchaseid_' with 'bookid_'
reviews_df['book_id'] = reviews_df['purchase_id'].astype(str).str.replace(r'^purchaseid_', 'bookid_', regex=True)

# Compute average rating per distinct book
book_avg = reviews_df.groupby('book_id', dropna=True)['rating'].mean().reset_index().rename(columns={'rating': 'avg_rating'})

# Extract publication year from books_df.details using regex (first 4-digit year 1000-2023)
def extract_year(text):
    if not isinstance(text, str):
        return None
    # find all 4-digit numbers
    matches = re.findall(r"\b(1\d{3}|20\d{2})\b", text)
    if not matches:
        return None
    # take the first match and ensure it's <= 2023
    for m in matches:
        try:
            y = int(m)
            if 1000 <= y <= 2023:
                return y
        except:
            continue
    return None

books_df['year'] = books_df['details'].apply(extract_year)

# Drop books without a year
books_with_year = books_df.dropna(subset=['year']).copy()
books_with_year['year'] = books_with_year['year'].astype(int)
books_with_year['decade'] = (books_with_year['year'] // 10 * 10).astype(int).astype(str) + 's'

# Merge book averages with books
merged = pd.merge(book_avg, books_with_year[['book_id', 'year', 'decade']], on='book_id', how='inner')

# Now compute per-decade stats: number of distinct books and average of book average ratings
decade_stats = merged.groupby('decade').agg(num_books=('book_id', 'nunique'), avg_of_book_avgs=('avg_rating', 'mean')).reset_index()

# Filter decades with at least 10 distinct books
eligible = decade_stats[decade_stats['num_books'] >= 10].copy()

# If no eligible decades, result is None
if eligible.empty:
    result = None
else:
    # Find decade with highest average rating
    best = eligible.sort_values(['avg_of_book_avgs', 'decade'], ascending=[False, True]).iloc[0]
    result = best['decade']

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_fF1tJEexv0JMLHDg2pEkXyg5': ['review'], 'var_call_Y743UHD6MqCHjvTbDdz6d0R1': ['books_info'], 'var_call_v0GAwjFkl9yD8qYCzVXKjd3L': 'file_storage/call_v0GAwjFkl9yD8qYCzVXKjd3L.json', 'var_call_BaA5qhZDH38TWzICIaaOqHN3': [{'purchase_id': 'purchaseid_186', 'rating': '4'}, {'purchase_id': 'purchaseid_191', 'rating': '4'}, {'purchase_id': 'purchaseid_190', 'rating': '4'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '4'}, {'purchase_id': 'purchaseid_186', 'rating': '4'}, {'purchase_id': 'purchaseid_76', 'rating': '5'}, {'purchase_id': 'purchaseid_186', 'rating': '4'}, {'purchase_id': 'purchaseid_115', 'rating': '5'}, {'purchase_id': 'purchaseid_167', 'rating': '2'}, {'purchase_id': 'purchaseid_188', 'rating': '1'}, {'purchase_id': 'purchaseid_23', 'rating': '5'}, {'purchase_id': 'purchaseid_196', 'rating': '5'}, {'purchase_id': 'purchaseid_196', 'rating': '5'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_48', 'rating': '5'}, {'purchase_id': 'purchaseid_154', 'rating': '3'}, {'purchase_id': 'purchaseid_99', 'rating': '2'}, {'purchase_id': 'purchaseid_190', 'rating': '5'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_169', 'rating': '5'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_145', 'rating': '5'}, {'purchase_id': 'purchaseid_194', 'rating': '4'}, {'purchase_id': 'purchaseid_81', 'rating': '5'}, {'purchase_id': 'purchaseid_199', 'rating': '1'}, {'purchase_id': 'purchaseid_48', 'rating': '5'}, {'purchase_id': 'purchaseid_96', 'rating': '5'}, {'purchase_id': 'purchaseid_167', 'rating': '4'}, {'purchase_id': 'purchaseid_196', 'rating': '5'}, {'purchase_id': 'purchaseid_196', 'rating': '5'}, {'purchase_id': 'purchaseid_196', 'rating': '4'}, {'purchase_id': 'purchaseid_148', 'rating': '5'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_145', 'rating': '5'}, {'purchase_id': 'purchaseid_200', 'rating': '5'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '1'}, {'purchase_id': 'purchaseid_20', 'rating': '5'}, {'purchase_id': 'purchaseid_52', 'rating': '5'}, {'purchase_id': 'purchaseid_159', 'rating': '2'}, {'purchase_id': 'purchaseid_83', 'rating': '5'}, {'purchase_id': 'purchaseid_67', 'rating': '3'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_58', 'rating': '4'}, {'purchase_id': 'purchaseid_196', 'rating': '4'}, {'purchase_id': 'purchaseid_95', 'rating': '5'}, {'purchase_id': 'purchaseid_76', 'rating': '5'}, {'purchase_id': 'purchaseid_3', 'rating': '3'}, {'purchase_id': 'purchaseid_62', 'rating': '5'}, {'purchase_id': 'purchaseid_136', 'rating': '3'}, {'purchase_id': 'purchaseid_10', 'rating': '5'}, {'purchase_id': 'purchaseid_3', 'rating': '3'}, {'purchase_id': 'purchaseid_10', 'rating': '5'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_186', 'rating': '5'}, {'purchase_id': 'purchaseid_46', 'rating': '5'}, {'purchase_id': 'purchaseid_38', 'rating': '5'}, {'purchase_id': 'purchaseid_145', 'rating': '5'}, {'purchase_id': 'purchaseid_48', 'rating': '5'}, {'purchase_id': 'purchaseid_10', 'rating': '5'}, {'purchase_id': 'purchaseid_31', 'rating': '4'}, {'purchase_id': 'purchaseid_115', 'rating': '5'}, {'purchase_id': 'purchaseid_48', 'rating': '5'}, {'purchase_id': 'purchaseid_196', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_7', 'rating': '5'}, {'purchase_id': 'purchaseid_4', 'rating': '5'}, {'purchase_id': 'purchaseid_104', 'rating': '4'}, {'purchase_id': 'purchaseid_8', 'rating': '4'}, {'purchase_id': 'purchaseid_162', 'rating': '5'}, {'purchase_id': 'purchaseid_145', 'rating': '5'}, {'purchase_id': 'purchaseid_8', 'rating': '4'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_186', 'rating': '5'}, {'purchase_id': 'purchaseid_5', 'rating': '5'}, {'purchase_id': 'purchaseid_20', 'rating': '3'}, {'purchase_id': 'purchaseid_158', 'rating': '3'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_165', 'rating': '3'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_6', 'rating': '5'}, {'purchase_id': 'purchaseid_158', 'rating': '4'}, {'purchase_id': 'purchaseid_196', 'rating': '5'}, {'purchase_id': 'purchaseid_5', 'rating': '5'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_115', 'rating': '5'}, {'purchase_id': 'purchaseid_46', 'rating': '5'}, {'purchase_id': 'purchaseid_83', 'rating': '5'}, {'purchase_id': 'purchaseid_86', 'rating': '5'}, {'purchase_id': 'purchaseid_174', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_48', 'rating': '5'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_177', 'rating': '5'}, {'purchase_id': 'purchaseid_187', 'rating': '5'}, {'purchase_id': 'purchaseid_188', 'rating': '4'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_63', 'rating': '2'}, {'purchase_id': 'purchaseid_33', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '4'}, {'purchase_id': 'purchaseid_62', 'rating': '5'}, {'purchase_id': 'purchaseid_10', 'rating': '5'}, {'purchase_id': 'purchaseid_48', 'rating': '2'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_62', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_32', 'rating': '4'}, {'purchase_id': 'purchaseid_157', 'rating': '5'}, {'purchase_id': 'purchaseid_193', 'rating': '4'}, {'purchase_id': 'purchaseid_196', 'rating': '5'}, {'purchase_id': 'purchaseid_186', 'rating': '4'}, {'purchase_id': 'purchaseid_185', 'rating': '4'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_187', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_196', 'rating': '5'}, {'purchase_id': 'purchaseid_13', 'rating': '5'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_72', 'rating': '4'}, {'purchase_id': 'purchaseid_196', 'rating': '3'}, {'purchase_id': 'purchaseid_42', 'rating': '5'}, {'purchase_id': 'purchaseid_96', 'rating': '5'}, {'purchase_id': 'purchaseid_73', 'rating': '5'}, {'purchase_id': 'purchaseid_188', 'rating': '5'}, {'purchase_id': 'purchaseid_145', 'rating': '4'}, {'purchase_id': 'purchaseid_97', 'rating': '5'}, {'purchase_id': 'purchaseid_59', 'rating': '5'}, {'purchase_id': 'purchaseid_192', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_193', 'rating': '4'}, {'purchase_id': 'purchaseid_8', 'rating': '2'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_109', 'rating': '4'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_99', 'rating': '5'}, {'purchase_id': 'purchaseid_76', 'rating': '5'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_154', 'rating': '4'}, {'purchase_id': 'purchaseid_148', 'rating': '4'}, {'purchase_id': 'purchaseid_178', 'rating': '4'}, {'purchase_id': 'purchaseid_163', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_52', 'rating': '5'}, {'purchase_id': 'purchaseid_109', 'rating': '4'}, {'purchase_id': 'purchaseid_196', 'rating': '5'}, {'purchase_id': 'purchaseid_196', 'rating': '5'}, {'purchase_id': 'purchaseid_106', 'rating': '5'}, {'purchase_id': 'purchaseid_130', 'rating': '5'}, {'purchase_id': 'purchaseid_118', 'rating': '5'}, {'purchase_id': 'purchaseid_167', 'rating': '5'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_103', 'rating': '1'}, {'purchase_id': 'purchaseid_8', 'rating': '4'}, {'purchase_id': 'purchaseid_5', 'rating': '5'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_103', 'rating': '4'}, {'purchase_id': 'purchaseid_5', 'rating': '4'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_20', 'rating': '4'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_8', 'rating': '2'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_115', 'rating': '5'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_154', 'rating': '5'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_154', 'rating': '2'}, {'purchase_id': 'purchaseid_32', 'rating': '5'}, {'purchase_id': 'purchaseid_186', 'rating': '5'}, {'purchase_id': 'purchaseid_161', 'rating': '4'}, {'purchase_id': 'purchaseid_41', 'rating': '5'}, {'purchase_id': 'purchaseid_36', 'rating': '5'}, {'purchase_id': 'purchaseid_145', 'rating': '5'}, {'purchase_id': 'purchaseid_196', 'rating': '5'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_145', 'rating': '5'}, {'purchase_id': 'purchaseid_20', 'rating': '4'}, {'purchase_id': 'purchaseid_124', 'rating': '5'}, {'purchase_id': 'purchaseid_48', 'rating': '5'}, {'purchase_id': 'purchaseid_32', 'rating': '5'}, {'purchase_id': 'purchaseid_196', 'rating': '5'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_148', 'rating': '5'}, {'purchase_id': 'purchaseid_196', 'rating': '3'}, {'purchase_id': 'purchaseid_197', 'rating': '5'}, {'purchase_id': 'purchaseid_196', 'rating': '5'}, {'purchase_id': 'purchaseid_41', 'rating': '5'}]}

exec(code, env_args)
