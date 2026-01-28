code = """import json
import pandas as pd

# Load aggregated reviews (has purchase_id, avg_rating, n_reviews)
reviews = var_call_VKRCAVhoTv4NYS8RpJ1bcwsj
df_reviews = pd.DataFrame(reviews)
# create book_id column by replacing prefix
if 'purchase_id' in df_reviews.columns:
    df_reviews['book_id'] = df_reviews['purchase_id'].astype(str).str.replace('purchaseid_', 'bookid_')
# convert avg_rating and n_reviews to numeric
df_reviews['avg_rating'] = pd.to_numeric(df_reviews['avg_rating'], errors='coerce')
df_reviews['n_reviews'] = pd.to_numeric(df_reviews['n_reviews'], errors='coerce')

# Load books data from file path
books_file = var_call_IoTVAXJ4lNGBJ2lwygMwIsbg
with open(books_file, 'r', encoding='utf-8') as f:
    books = json.load(f)

df_books = pd.DataFrame(books)

# Helper functions
import re

def is_english(text):
    if not isinstance(text, str):
        return False
    t = text.lower()
    return ('written in english' in t) or ('available in english' in t) or (' in english' in t)

def has_lit_fic(cat, details):
    # check categories string
    if isinstance(cat, str):
        if 'literature & fiction' in cat.lower():
            return True
        # also handle if both words present separately
        if 'literature' in cat.lower() and 'fiction' in cat.lower():
            return True
    # check details as fallback
    if isinstance(details, str):
        if 'literature & fiction' in details.lower():
            return True
        if 'literature' in details.lower() and 'fiction' in details.lower():
            return True
    return False

# Apply filters
df_books['is_english'] = df_books['details'].apply(is_english)
df_books['has_lit_fic'] = df_books.apply(lambda r: has_lit_fic(r.get('categories'), r.get('details')), axis=1)

# Filtered books
df_books_filtered = df_books[(df_books['is_english']) & (df_books['has_lit_fic'])].copy()

# Merge with reviews on book_id
merged = pd.merge(df_books_filtered, df_reviews, left_on='book_id', right_on='book_id', how='inner')

# Keep only those with avg_rating == 5.0
merged = merged[merged['avg_rating'] == 5.0]

# Prepare output
out = []
for _, row in merged.iterrows():
    # extract author name if possible
    author_field = row.get('author')
    author_name = None
    if isinstance(author_field, str):
        try:
            parsed = json.loads(author_field)
            if isinstance(parsed, dict) and 'name' in parsed:
                author_name = parsed.get('name')
            else:
                author_name = author_field
        except Exception:
            author_name = author_field
    else:
        author_name = str(author_field)
    out.append({
        'book_id': row.get('book_id'),
        'title': row.get('title'),
        'author': author_name,
        'avg_rating': float(row.get('avg_rating')) if pd.notnull(row.get('avg_rating')) else None,
        'n_reviews': int(row.get('n_reviews')) if pd.notnull(row.get('n_reviews')) else None,
        'categories': row.get('categories'),
        'details': row.get('details')
    })

# Sort output by title
out = sorted(out, key=lambda x: (x.get('title') or '').lower())

print("__RESULT__:")
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_BdVryd7fheLdTEx5lbkxW6NU': ['books_info'], 'var_call_pMrHlCLHGMFNGiTmQexN4gDr': ['review'], 'var_call_VKRCAVhoTv4NYS8RpJ1bcwsj': [{'purchase_id': 'purchaseid_101', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_105', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_108', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_110', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_114', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_116', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_117', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_118', 'avg_rating': '5.0', 'n_reviews': '6'}, {'purchase_id': 'purchaseid_12', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_121', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_122', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_123', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_124', 'avg_rating': '5.0', 'n_reviews': '4'}, {'purchase_id': 'purchaseid_126', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_127', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_128', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_130', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_132', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_133', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_134', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_14', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_143', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_144', 'avg_rating': '5.0', 'n_reviews': '6'}, {'purchase_id': 'purchaseid_146', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_150', 'avg_rating': '5.0', 'n_reviews': '11'}, {'purchase_id': 'purchaseid_151', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_152', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_153', 'avg_rating': '5.0', 'n_reviews': '15'}, {'purchase_id': 'purchaseid_156', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_16', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_160', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_163', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_166', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_168', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_170', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_171', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_172', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_174', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_177', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_180', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_181', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_182', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_184', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_192', 'avg_rating': '5.0', 'n_reviews': '6'}, {'purchase_id': 'purchaseid_195', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_197', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_2', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_21', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_24', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_26', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_28', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_29', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_33', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_34', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_38', 'avg_rating': '5.0', 'n_reviews': '4'}, {'purchase_id': 'purchaseid_39', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_40', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_41', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_42', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_47', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_54', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_56', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_57', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_59', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_6', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_60', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_64', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_7', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_71', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_73', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_74', 'avg_rating': '5.0', 'n_reviews': '8'}, {'purchase_id': 'purchaseid_75', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_79', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_80', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_82', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_83', 'avg_rating': '5.0', 'n_reviews': '14'}, {'purchase_id': 'purchaseid_84', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_88', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_9', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_90', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_91', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_97', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_98', 'avg_rating': '5.0', 'n_reviews': '1'}], 'var_call_1ZJeOqxVn0Q1gk0scZCJGfki': 'file_storage/call_1ZJeOqxVn0Q1gk0scZCJGfki.json', 'var_call_vx8HpvQeOOtGq28O3oUiABnf': 'file_storage/call_vx8HpvQeOOtGq28O3oUiABnf.json', 'var_call_w28mY3Y7SlZBtlWD3ZVCJySb': [{'book_id': 'bookid_101'}, {'book_id': 'bookid_105'}, {'book_id': 'bookid_108'}, {'book_id': 'bookid_110'}, {'book_id': 'bookid_114'}, {'book_id': 'bookid_116'}, {'book_id': 'bookid_117'}, {'book_id': 'bookid_118'}, {'book_id': 'bookid_12'}, {'book_id': 'bookid_121'}, {'book_id': 'bookid_122'}, {'book_id': 'bookid_123'}, {'book_id': 'bookid_124'}, {'book_id': 'bookid_126'}, {'book_id': 'bookid_127'}, {'book_id': 'bookid_128'}, {'book_id': 'bookid_130'}, {'book_id': 'bookid_132'}, {'book_id': 'bookid_133'}, {'book_id': 'bookid_134'}, {'book_id': 'bookid_14'}, {'book_id': 'bookid_143'}, {'book_id': 'bookid_144'}, {'book_id': 'bookid_146'}, {'book_id': 'bookid_150'}, {'book_id': 'bookid_151'}, {'book_id': 'bookid_152'}, {'book_id': 'bookid_153'}, {'book_id': 'bookid_156'}, {'book_id': 'bookid_16'}, {'book_id': 'bookid_160'}, {'book_id': 'bookid_163'}, {'book_id': 'bookid_166'}, {'book_id': 'bookid_168'}, {'book_id': 'bookid_170'}, {'book_id': 'bookid_171'}, {'book_id': 'bookid_172'}, {'book_id': 'bookid_174'}, {'book_id': 'bookid_177'}, {'book_id': 'bookid_180'}, {'book_id': 'bookid_181'}, {'book_id': 'bookid_182'}, {'book_id': 'bookid_184'}, {'book_id': 'bookid_192'}, {'book_id': 'bookid_195'}, {'book_id': 'bookid_197'}, {'book_id': 'bookid_2'}, {'book_id': 'bookid_21'}, {'book_id': 'bookid_24'}, {'book_id': 'bookid_26'}, {'book_id': 'bookid_28'}, {'book_id': 'bookid_29'}, {'book_id': 'bookid_33'}, {'book_id': 'bookid_34'}, {'book_id': 'bookid_38'}, {'book_id': 'bookid_39'}, {'book_id': 'bookid_40'}, {'book_id': 'bookid_41'}, {'book_id': 'bookid_42'}, {'book_id': 'bookid_47'}, {'book_id': 'bookid_54'}, {'book_id': 'bookid_56'}, {'book_id': 'bookid_57'}, {'book_id': 'bookid_59'}, {'book_id': 'bookid_6'}, {'book_id': 'bookid_60'}, {'book_id': 'bookid_64'}, {'book_id': 'bookid_7'}, {'book_id': 'bookid_71'}, {'book_id': 'bookid_73'}, {'book_id': 'bookid_74'}, {'book_id': 'bookid_75'}, {'book_id': 'bookid_79'}, {'book_id': 'bookid_80'}, {'book_id': 'bookid_82'}, {'book_id': 'bookid_83'}, {'book_id': 'bookid_84'}, {'book_id': 'bookid_88'}, {'book_id': 'bookid_9'}, {'book_id': 'bookid_90'}, {'book_id': 'bookid_91'}, {'book_id': 'bookid_97'}, {'book_id': 'bookid_98'}], 'var_call_IoTVAXJ4lNGBJ2lwygMwIsbg': 'file_storage/call_IoTVAXJ4lNGBJ2lwygMwIsbg.json'}

exec(code, env_args)
