code = """import json
import pandas as pd
# load the two query results from storage
books_path = var_call_htm5br0RNgZMNaHQdwzHJ5z3
reviews_path = var_call_hm1RRcvfp0u53zbK8DxXp5bc

books = pd.read_json(books_path)
reviews = pd.read_json(reviews_path)

# Normalize ids: books.book_id like 'bookid_1' corresponds to review.purchase_id like 'purchaseid_1'
# We'll extract the numeric suffix and match

def extract_num_id(s):
    if pd.isna(s):
        return None
    parts = s.split('_')
    if len(parts) >= 2:
        return parts[-1]
    return None

books['id_num'] = books['book_id'].apply(extract_num_id)
reviews['id_num'] = reviews['purchase_id'].apply(extract_num_id)

# filter reviews to avg_rating == 5.0 (float), allow small float tolerance
reviews['avg_rating'] = reviews['avg_rating'].astype(float)
perfect = reviews[reviews['avg_rating'] == 5.0]

# merge with books on id_num and ensure English-language and category contains 'Literature & Fiction'
merged = perfect.merge(books, on='id_num', suffixes=('_rev','_book'))

# filter English-language: look in details for 'available in English' or 'is written in English' or 'available in English'
eng_mask = merged['details'].str.contains('English', case=False, na=False)
cat_mask = merged['categories'].str.contains('Literature & Fiction', case=False, na=False)
final = merged[eng_mask & cat_mask]

# prepare output: return book_id, title, author if present, avg_rating, review_count, categories, details
out = final[['book_id','title','avg_rating','review_count','categories','details']].copy()
# ensure serializable
out_records = out.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(out_records))"""

env_args = {'var_call_htm5br0RNgZMNaHQdwzHJ5z3': 'file_storage/call_htm5br0RNgZMNaHQdwzHJ5z3.json', 'var_call_TsgFwy1PQyoesRQCXgFrJaMF': ['review'], 'var_call_hm1RRcvfp0u53zbK8DxXp5bc': 'file_storage/call_hm1RRcvfp0u53zbK8DxXp5bc.json'}

exec(code, env_args)
