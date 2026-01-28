code = """import json
import pandas as pd
import re
import ast

# load data from storage
reviews = var_call_fAGceu7CCWvNrTH5pPwSAzzM
books_json_path = var_call_ZGZgRJuyZZFuB23e3hWDIh4F

# create DataFrame for reviews
df_reviews = pd.DataFrame(reviews)
# convert types
if not df_reviews.empty:
    df_reviews['avg_rating'] = df_reviews['avg_rating'].astype(float)
    df_reviews['review_count'] = df_reviews['review_count'].astype(int)
    # extract numeric id from purchase_id
    df_reviews['num'] = df_reviews['purchase_id'].astype(str).str.extract(r'(\d+)')
    df_reviews['book_id'] = 'bookid_' + df_reviews['num']
else:
    df_reviews['book_id'] = []

# load books data from file
with open(books_json_path, 'r') as f:
    books = json.load(f)

df_books = pd.DataFrame(books)

# parse categories string into list
def parse_categories(s):
    if not isinstance(s, str):
        return []
    try:
        return json.loads(s)
    except Exception:
        try:
            return ast.literal_eval(s)
        except Exception:
            return []

if 'categories' in df_books.columns:
    df_books['categories_list'] = df_books['categories'].apply(parse_categories)
else:
    df_books['categories_list'] = [[] for _ in range(len(df_books))]

# mark if book is in Children's Books category
def is_children_cat(lst):
    if not isinstance(lst, list):
        return False
    for item in lst:
        if isinstance(item, str) and "Children" in item:
            return True
    return False

df_books['is_children'] = df_books['categories_list'].apply(is_children_cat)

# merge on book_id
merged = pd.merge(df_reviews, df_books, on='book_id', how='left')

# filter to children's books
children_books = merged[merged['is_children'] == True].copy()

# prepare output
out = []
for _, row in children_books.iterrows():
    out.append({
        'book_id': row.get('book_id'),
        'title': row.get('title'),
        'avg_rating': float(row.get('avg_rating')) if pd.notna(row.get('avg_rating')) else None,
        'review_count': int(row.get('review_count')) if pd.notna(row.get('review_count')) else None,
        'categories': row.get('categories_list')
    })

# sort by title
out = sorted(out, key=lambda x: (x['title'] or '').lower())

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_24o8BzoaTijvUaht59pOdVNw': ['review'], 'var_call_fAGceu7CCWvNrTH5pPwSAzzM': [{'purchase_id': 'purchaseid_10', 'avg_rating': '5.0', 'review_count': '4'}, {'purchase_id': 'purchaseid_105', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_108', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_110', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_115', 'avg_rating': '4.75', 'review_count': '8'}, {'purchase_id': 'purchaseid_118', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_12', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_122', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_126', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_129', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_13', 'avg_rating': '4.923076923076923', 'review_count': '13'}, {'purchase_id': 'purchaseid_130', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_14', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_144', 'avg_rating': '5.0', 'review_count': '4'}, {'purchase_id': 'purchaseid_146', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_149', 'avg_rating': '4.9', 'review_count': '10'}, {'purchase_id': 'purchaseid_152', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_154', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_158', 'avg_rating': '4.708333333333333', 'review_count': '24'}, {'purchase_id': 'purchaseid_161', 'avg_rating': '4.5', 'review_count': '2'}, {'purchase_id': 'purchaseid_169', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_170', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_172', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_178', 'avg_rating': '4.795918367346939', 'review_count': '49'}, {'purchase_id': 'purchaseid_182', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_184', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_185', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_187', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_192', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_196', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_198', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_200', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_22', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_23', 'avg_rating': '4.5', 'review_count': '2'}, {'purchase_id': 'purchaseid_3', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_33', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_37', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_38', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_39', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_4', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_40', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_41', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_46', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_48', 'avg_rating': '4.75', 'review_count': '4'}, {'purchase_id': 'purchaseid_50', 'avg_rating': '4.5', 'review_count': '2'}, {'purchase_id': 'purchaseid_54', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_55', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_6', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_60', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_66', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_72', 'avg_rating': '4.5', 'review_count': '2'}, {'purchase_id': 'purchaseid_74', 'avg_rating': '5.0', 'review_count': '8'}, {'purchase_id': 'purchaseid_76', 'avg_rating': '4.75', 'review_count': '4'}, {'purchase_id': 'purchaseid_8', 'avg_rating': '4.709677419354839', 'review_count': '31'}, {'purchase_id': 'purchaseid_80', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_83', 'avg_rating': '5.0', 'review_count': '14'}, {'purchase_id': 'purchaseid_88', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_94', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_96', 'avg_rating': '5.0', 'review_count': '1'}], 'var_call_koQXOfAyMfY754hP5nA5L8XG': ['books_info'], 'var_call_ZGZgRJuyZZFuB23e3hWDIh4F': 'file_storage/call_ZGZgRJuyZZFuB23e3hWDIh4F.json'}

exec(code, env_args)
