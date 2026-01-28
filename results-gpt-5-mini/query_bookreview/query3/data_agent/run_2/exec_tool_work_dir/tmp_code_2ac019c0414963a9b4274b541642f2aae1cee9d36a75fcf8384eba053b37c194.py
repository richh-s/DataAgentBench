code = """import json
import pandas as pd

# Load previous query results available as variables
reviews = var_call_mG8DAvpKMhtFmu44PxH3TFqY
books_file = var_call_C4IU0s60XXzdiTLH1QLtxZUF

# Load full books data from file
with open(books_file, 'r', encoding='utf-8') as f:
    books = json.load(f)

# Create DataFrames
df_reviews = pd.DataFrame(reviews)
# Convert avg_rating and num_reviews to numeric types
df_reviews['avg_rating'] = pd.to_numeric(df_reviews['avg_rating'], errors='coerce')
df_reviews['num_reviews'] = pd.to_numeric(df_reviews['num_reviews'], errors='coerce')

df_books = pd.DataFrame(books)

# Extract numeric suffix to perform fuzzy join: purchaseid_10 -> bookid_10
df_reviews['key'] = df_reviews['purchase_id'].astype(str).apply(lambda x: x.split('_')[-1])
df_books['key'] = df_books['book_id'].astype(str).apply(lambda x: x.split('_')[-1])

# Merge on key
merged = pd.merge(df_reviews, df_books, on='key', how='left', suffixes=('_rev', '_book'))

# Filter for Children's Books in categories
# Some categories may be None; ensure string
merged['categories'] = merged['categories'].fillna('')
mask = merged['categories'].str.contains("Children's Books")
res = merged[mask]

# Prepare output list with title, book_id, avg_rating, num_reviews, categories
output = []
for _, row in res.iterrows():
    output.append({
        'book_id': row['book_id'],
        'title': row['title'],
        'avg_rating': float(row['avg_rating']) if not pd.isna(row['avg_rating']) else None,
        'num_reviews': int(row['num_reviews']) if not pd.isna(row['num_reviews']) else None,
        'categories': row['categories']
    })

# Remove possible duplicates (same book may appear multiple times) by book_id, keep highest avg_rating record
unique = {}
for item in output:
    bid = item['book_id']
    if bid not in unique or (item['avg_rating'] is not None and item['avg_rating'] > unique[bid]['avg_rating']):
        unique[bid] = item

final_list = list(unique.values())

# Sort by avg_rating desc, then num_reviews desc
final_list.sort(key=lambda x: ((-x['avg_rating']) if x['avg_rating'] is not None else 0, -x['num_reviews'] if x['num_reviews'] is not None else 0))

print("__RESULT__:")
print(json.dumps(final_list))"""

env_args = {'var_call_11QdljHhSEMSizzX48C8LvPE': ['review'], 'var_call_mG8DAvpKMhtFmu44PxH3TFqY': [{'purchase_id': 'purchaseid_10', 'avg_rating': '5.0', 'num_reviews': '4'}, {'purchase_id': 'purchaseid_105', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_108', 'avg_rating': '5.0', 'num_reviews': '3'}, {'purchase_id': 'purchaseid_110', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_115', 'avg_rating': '4.75', 'num_reviews': '8'}, {'purchase_id': 'purchaseid_118', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_12', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_122', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_126', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_129', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_13', 'avg_rating': '4.923076923076923', 'num_reviews': '13'}, {'purchase_id': 'purchaseid_130', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_14', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_144', 'avg_rating': '5.0', 'num_reviews': '4'}, {'purchase_id': 'purchaseid_146', 'avg_rating': '5.0', 'num_reviews': '3'}, {'purchase_id': 'purchaseid_149', 'avg_rating': '4.9', 'num_reviews': '10'}, {'purchase_id': 'purchaseid_152', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_154', 'avg_rating': '5.0', 'num_reviews': '3'}, {'purchase_id': 'purchaseid_158', 'avg_rating': '4.708333333333333', 'num_reviews': '24'}, {'purchase_id': 'purchaseid_161', 'avg_rating': '4.5', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_169', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_170', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_172', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_178', 'avg_rating': '4.795918367346939', 'num_reviews': '49'}, {'purchase_id': 'purchaseid_182', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_184', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_185', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_187', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_192', 'avg_rating': '5.0', 'num_reviews': '3'}, {'purchase_id': 'purchaseid_196', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_198', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_200', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_22', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_23', 'avg_rating': '4.5', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_3', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_33', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_37', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_38', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_39', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_4', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_40', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_41', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_46', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_48', 'avg_rating': '4.75', 'num_reviews': '4'}, {'purchase_id': 'purchaseid_50', 'avg_rating': '4.5', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_54', 'avg_rating': '5.0', 'num_reviews': '3'}, {'purchase_id': 'purchaseid_55', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_6', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_60', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_66', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_72', 'avg_rating': '4.5', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_74', 'avg_rating': '5.0', 'num_reviews': '8'}, {'purchase_id': 'purchaseid_76', 'avg_rating': '4.75', 'num_reviews': '4'}, {'purchase_id': 'purchaseid_8', 'avg_rating': '4.709677419354839', 'num_reviews': '31'}, {'purchase_id': 'purchaseid_80', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_83', 'avg_rating': '5.0', 'num_reviews': '14'}, {'purchase_id': 'purchaseid_88', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_94', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_96', 'avg_rating': '5.0', 'num_reviews': '1'}], 'var_call_sQOoxTY35PE7RzfI6wqIlWBg': ['books_info'], 'var_call_C4IU0s60XXzdiTLH1QLtxZUF': 'file_storage/call_C4IU0s60XXzdiTLH1QLtxZUF.json'}

exec(code, env_args)
