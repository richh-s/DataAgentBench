code = """import json
import re
import pandas as pd

# Load data
with open(locals()['var_function-call-5847662609626649812'], 'r') as f:
    reviews = json.load(f)

with open(locals()['var_function-call-10489614112549282405'], 'r') as f:
    books = json.load(f)

debug_info = {}

# Process Books
book_data = []
book_ids_seen = set()
for b in books:
    b_id_str = b.get('book_id', '')
    details = b.get('details', '')
    
    m_id = re.search(r'bookid_(\d+)', b_id_str)
    if not m_id:
        continue
    b_id = int(m_id.group(1))
    book_ids_seen.add(b_id)
    
    years = re.findall(r'\b(19\d{2}|20\d{2})\b', details)
    year = None
    if years:
        valid_years = [int(y) for y in years if 1900 <= int(y) <= 2024]
        if valid_years:
            year = valid_years[0]
            
    if year:
        book_data.append({'id': b_id, 'year': year})

df_books = pd.DataFrame(book_data)
debug_info['books_count'] = len(df_books)
debug_info['total_books_raw'] = len(books)
debug_info['book_ids_example'] = list(book_ids_seen)[:5]

# Process Reviews
review_data = []
review_ids_seen = set()
for r in reviews:
    p_id_str = r.get('purchase_id', '')
    rating_str = r.get('rating', '0')
    
    m_id = re.search(r'purchaseid_(\d+)', p_id_str)
    if not m_id:
        continue
    p_id = int(m_id.group(1))
    review_ids_seen.add(p_id)
    
    try:
        rating = float(rating_str)
    except:
        continue
        
    review_data.append({'id': p_id, 'rating': rating})

df_reviews = pd.DataFrame(review_data)
debug_info['reviews_count'] = len(df_reviews)
debug_info['total_reviews_raw'] = len(reviews)
debug_info['review_ids_example'] = list(review_ids_seen)[:5]

final_res = []

if not df_books.empty and not df_reviews.empty:
    merged = pd.merge(df_reviews, df_books, on='id', how='inner')
    debug_info['merged_count'] = len(merged)
    
    if not merged.empty:
        merged['decade'] = (merged['year'] // 10) * 10
        merged['decade_str'] = merged['decade'].astype(str) + "s"

        grouped = merged.groupby('decade_str').agg(
            distinct_books=('id', 'nunique'),
            avg_rating=('rating', 'mean')
        ).reset_index()
        
        debug_info['grouped_data'] = grouped.to_dict(orient='records')

        filtered = grouped[grouped['distinct_books'] >= 10].copy()
        filtered = filtered.sort_values(by='avg_rating', ascending=False)
        final_res = filtered.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps({"result": final_res, "debug": debug_info}))"""

env_args = {'var_function-call-4644691029107538022': 'file_storage/function-call-4644691029107538022.json', 'var_function-call-16058013232113512935': ['review'], 'var_function-call-2272556202224259319': [{'COUNT(*)': '1833'}], 'var_function-call-15315810567359206872': [{'count': '200'}], 'var_function-call-12909927237427682117': [{'purchase_id': 'purchaseid_186'}, {'purchase_id': 'purchaseid_191'}, {'purchase_id': 'purchaseid_190'}, {'purchase_id': 'purchaseid_8'}, {'purchase_id': 'purchaseid_178'}], 'var_function-call-5847662609626649812': 'file_storage/function-call-5847662609626649812.json', 'var_function-call-10489614112549282405': 'file_storage/function-call-10489614112549282405.json', 'var_function-call-1543764841573784033': []}

exec(code, env_args)
