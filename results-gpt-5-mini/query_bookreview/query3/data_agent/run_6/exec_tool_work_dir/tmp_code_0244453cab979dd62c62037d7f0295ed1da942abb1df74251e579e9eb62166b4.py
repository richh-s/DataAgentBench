code = """import json
import pandas as pd
import re
import ast

# Load review aggregates from storage
reviews = var_call_nC5DfcA3KTJeIcgIIBRjeC5T

# Load books data from file path stored in var_call_TQEJqJJ7UgfazlLOSLDrs1Yl
books_file_path = var_call_TQEJqJJ7UgfazlLOSLDrs1Yl
with open(books_file_path, 'r', encoding='utf-8') as f:
    books = json.load(f)

# Normalize reviews into DataFrame
df_rev = pd.DataFrame(reviews)
# Convert types
df_rev['avg_rating'] = df_rev['avg_rating'].astype(float)
try:
    df_rev['review_count'] = df_rev['review_count'].astype(int)
except Exception:
    df_rev['review_count'] = df_rev['review_count'].apply(lambda x: int(x) if x is not None and x != '' else 0)

# Extract numeric id and map to book_id
def purchase_to_bookid(purchase_id):
    m = re.search(r"(\\d+)$", str(purchase_id))
    if m:
        return 'bookid_' + m.group(1)
    return None

df_rev['book_id'] = df_rev['purchase_id'].apply(purchase_to_bookid)

# Normalize books into DataFrame
df_books = pd.DataFrame(books)

# Parse categories string into list
def parse_categories(cat_str):
    if cat_str is None:
        return []
    if isinstance(cat_str, list):
        return cat_str
    s = cat_str.strip()
    if s == '':
        return []
    try:
        return json.loads(s)
    except Exception:
        try:
            return ast.literal_eval(s)
        except Exception:
            return [s]

df_books['categories_list'] = df_books['categories'].apply(parse_categories)

# Merge on book_id
df_merged = pd.merge(df_rev, df_books, on='book_id', how='left')

# Filter: categories contains "Children's Books" and avg_rating >= 4.5
def has_children_cats(cats):
    if not isinstance(cats, list):
        return False
    return "Children's Books" in cats

filtered = df_merged[df_merged['categories_list'].apply(has_children_cats) & (df_merged['avg_rating'] >= 4.5)].copy()

# Prepare output records
output_records = []
for _, row in filtered.iterrows():
    output_records.append({
        'book_id': row.get('book_id'),
        'title': row.get('title'),
        'avg_rating': float(round(row.get('avg_rating', 0), 6)),
        'review_count': int(row.get('review_count', 0)),
        'categories': row.get('categories_list')
    })

# Prepare plain text answer listing titles
titles = [r['title'] for r in output_records if r.get('title')]
if len(titles) == 0:
    plain_text = 'No Children\'s Books have an average rating of at least 4.5 from 2020 onwards in the data.'
else:
    plain_text = 'Books (Children\'s Books) with avg rating >= 4.5 from 2020 onwards:\n' + '\n'.join([f"- {t}" for t in titles])

result = {'matches': output_records, 'plain_text': plain_text}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_8sjVu1btoN6NrvyoeUOWqkvO': ['review'], 'var_call_iR312fU5tdUT9Rq8lzzg4jah': ['books_info'], 'var_call_nC5DfcA3KTJeIcgIIBRjeC5T': [{'purchase_id': 'purchaseid_96', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_94', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_88', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_83', 'avg_rating': '5.0', 'review_count': '14'}, {'purchase_id': 'purchaseid_80', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_74', 'avg_rating': '5.0', 'review_count': '8'}, {'purchase_id': 'purchaseid_66', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_60', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_6', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_55', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_54', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_46', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_41', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_40', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_4', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_39', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_38', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_37', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_33', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_3', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_22', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_200', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_198', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_196', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_192', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_187', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_185', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_184', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_182', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_172', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_170', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_169', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_154', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_152', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_146', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_144', 'avg_rating': '5.0', 'review_count': '4'}, {'purchase_id': 'purchaseid_14', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_130', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_129', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_126', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_122', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_12', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_118', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_110', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_108', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_105', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_10', 'avg_rating': '5.0', 'review_count': '4'}, {'purchase_id': 'purchaseid_13', 'avg_rating': '4.923076923076923', 'review_count': '13'}, {'purchase_id': 'purchaseid_149', 'avg_rating': '4.9', 'review_count': '10'}, {'purchase_id': 'purchaseid_178', 'avg_rating': '4.795918367346939', 'review_count': '49'}, {'purchase_id': 'purchaseid_76', 'avg_rating': '4.75', 'review_count': '4'}, {'purchase_id': 'purchaseid_48', 'avg_rating': '4.75', 'review_count': '4'}, {'purchase_id': 'purchaseid_115', 'avg_rating': '4.75', 'review_count': '8'}, {'purchase_id': 'purchaseid_8', 'avg_rating': '4.709677419354839', 'review_count': '31'}, {'purchase_id': 'purchaseid_158', 'avg_rating': '4.708333333333333', 'review_count': '24'}, {'purchase_id': 'purchaseid_72', 'avg_rating': '4.5', 'review_count': '2'}, {'purchase_id': 'purchaseid_50', 'avg_rating': '4.5', 'review_count': '2'}, {'purchase_id': 'purchaseid_23', 'avg_rating': '4.5', 'review_count': '2'}, {'purchase_id': 'purchaseid_161', 'avg_rating': '4.5', 'review_count': '2'}, {'purchase_id': 'purchaseid_99', 'avg_rating': '4.4', 'review_count': '5'}, {'purchase_id': 'purchaseid_62', 'avg_rating': '4.0', 'review_count': '6'}, {'purchase_id': 'purchaseid_45', 'avg_rating': '4.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_31', 'avg_rating': '4.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_25', 'avg_rating': '4.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_193', 'avg_rating': '4.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_167', 'avg_rating': '4.0', 'review_count': '12'}, {'purchase_id': 'purchaseid_145', 'avg_rating': '4.0', 'review_count': '5'}, {'purchase_id': 'purchaseid_140', 'avg_rating': '4.0', 'review_count': '4'}, {'purchase_id': 'purchaseid_137', 'avg_rating': '4.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_11', 'avg_rating': '4.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_107', 'avg_rating': '4.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_20', 'avg_rating': '3.875', 'review_count': '16'}, {'purchase_id': 'purchaseid_85', 'avg_rating': '3.8333333333333335', 'review_count': '12'}, {'purchase_id': 'purchaseid_5', 'avg_rating': '3.75', 'review_count': '4'}, {'purchase_id': 'purchaseid_32', 'avg_rating': '3.5714285714285716', 'review_count': '7'}, {'purchase_id': 'purchaseid_93', 'avg_rating': '3.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_67', 'avg_rating': '3.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_189', 'avg_rating': '2.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_155', 'avg_rating': '1.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_109', 'avg_rating': '1.0', 'review_count': '2'}], 'var_call_TQEJqJJ7UgfazlLOSLDrs1Yl': 'file_storage/call_TQEJqJJ7UgfazlLOSLDrs1Yl.json', 'var_call_XQaqicjdfgWYq18k9Cvfc0uu': {'reviews_count': 80, 'books_file_path': 'file_storage/call_TQEJqJJ7UgfazlLOSLDrs1Yl.json'}}

exec(code, env_args)
