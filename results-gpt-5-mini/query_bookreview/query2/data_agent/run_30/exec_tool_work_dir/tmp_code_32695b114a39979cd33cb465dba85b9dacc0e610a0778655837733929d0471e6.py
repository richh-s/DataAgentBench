code = """import json
import pandas as pd

# Load previous tool results from storage
# var_call_emAiPJ99rDNV133FzuoYEImT contains the review aggregates (list of dicts)
# var_call_PiKPba5jna0o1jV5SALYtsEE contains the path to a JSON file with the books query result

reviews = var_call_emAiPJ99rDNV133FzuoYEImT

# Load the large books result from the file path
books_file_path = var_call_PiKPba5jna0o1jV5SALYtsEE
with open(books_file_path, 'r', encoding='utf-8') as f:
    books = json.load(f)

# Create DataFrames
df_reviews = pd.DataFrame(reviews)
# Normalize numeric fields
if not df_reviews.empty:
    df_reviews['avg_rating'] = df_reviews['avg_rating'].astype(float)
    df_reviews['n_reviews'] = df_reviews['n_reviews'].astype(int)

# Map purchase_id to book_id by replacing prefix
if not df_reviews.empty:
    df_reviews['book_id'] = df_reviews['purchase_id'].str.replace('purchaseid_', 'bookid_', regex=False)

# Books DataFrame
df_books = pd.DataFrame(books)

# Ensure categories and details are strings
df_books['categories'] = df_books['categories'].astype(str)
df_books['details'] = df_books['details'].astype(str)

# Filter books that have 'Literature & Fiction' in categories (case-insensitive)
mask_lit = df_books['categories'].str.contains('Literature & Fiction', case=False, na=False)
df_books_lit = df_books[mask_lit].copy()

# Further filter to English-language by checking 'English' in details (simple heuristic)
mask_english = df_books_lit['details'].str.contains('English', case=False, na=False)
df_books_lit_en = df_books_lit[mask_english].copy()

# Merge with reviews that have perfect 5.0 average
# First filter reviews to avg_rating == 5.0 (allow small float tolerance)
if not df_reviews.empty:
    df_reviews_5 = df_reviews[abs(df_reviews['avg_rating'] - 5.0) < 1e-9].copy()
else:
    df_reviews_5 = pd.DataFrame(columns=['book_id'])

# Merge on book_id
merged = pd.merge(df_books_lit_en, df_reviews_5, on='book_id', how='inner')

# Prepare output list of dicts
output = []
for _, row in merged.iterrows():
    output.append({
        'book_id': row['book_id'],
        'title': row.get('title'),
        'author': row.get('author'),
        'categories': row.get('categories'),
        'details': row.get('details'),
        'avg_rating': float(row.get('avg_rating')) if pd.notna(row.get('avg_rating')) else None,
        'n_reviews': int(row.get('n_reviews')) if pd.notna(row.get('n_reviews')) else None
    })

# Print result in required format as JSON string
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_PiKPba5jna0o1jV5SALYtsEE': 'file_storage/call_PiKPba5jna0o1jV5SALYtsEE.json', 'var_call_jDjl8WSdzwtNiuAweQa3giIy': ['review'], 'var_call_emAiPJ99rDNV133FzuoYEImT': [{'purchase_id': 'purchaseid_101', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_105', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_108', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_110', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_114', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_116', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_117', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_118', 'avg_rating': '5.0', 'n_reviews': '6'}, {'purchase_id': 'purchaseid_12', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_121', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_122', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_123', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_124', 'avg_rating': '5.0', 'n_reviews': '4'}, {'purchase_id': 'purchaseid_126', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_127', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_128', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_130', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_132', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_133', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_134', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_14', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_143', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_144', 'avg_rating': '5.0', 'n_reviews': '6'}, {'purchase_id': 'purchaseid_146', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_150', 'avg_rating': '5.0', 'n_reviews': '11'}, {'purchase_id': 'purchaseid_151', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_152', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_153', 'avg_rating': '5.0', 'n_reviews': '15'}, {'purchase_id': 'purchaseid_156', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_16', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_160', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_163', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_166', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_168', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_170', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_171', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_172', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_174', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_177', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_180', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_181', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_182', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_184', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_192', 'avg_rating': '5.0', 'n_reviews': '6'}, {'purchase_id': 'purchaseid_195', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_197', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_2', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_21', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_24', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_26', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_28', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_29', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_33', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_34', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_38', 'avg_rating': '5.0', 'n_reviews': '4'}, {'purchase_id': 'purchaseid_39', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_40', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_41', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_42', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_47', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_54', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_56', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_57', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_59', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_6', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_60', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_64', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_7', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_71', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_73', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_74', 'avg_rating': '5.0', 'n_reviews': '8'}, {'purchase_id': 'purchaseid_75', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_79', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_80', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_82', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_83', 'avg_rating': '5.0', 'n_reviews': '14'}, {'purchase_id': 'purchaseid_84', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_88', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_9', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_90', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_91', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_97', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_98', 'avg_rating': '5.0', 'n_reviews': '1'}]}

exec(code, env_args)
