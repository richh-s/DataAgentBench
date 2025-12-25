code = """import json
import re
import pandas as pd

# Load data
with open(locals()['var_function-call-5847662609626649812'], 'r') as f:
    reviews = json.load(f)

with open(locals()['var_function-call-10489614112549282405'], 'r') as f:
    books = json.load(f)

# Process Books
book_data = []
for b in books:
    b_id_str = b.get('book_id', '')
    details = b.get('details', '')
    
    m_id = re.search(r'bookid_(\d+)', b_id_str)
    if not m_id:
        continue
    b_id = int(m_id.group(1))
    
    years = re.findall(r'\b(19\d{2}|20\d{2})\b', details)
    
    year = None
    if years:
        valid_years = [int(y) for y in years if 1900 <= int(y) <= 2024]
        if valid_years:
            year = valid_years[0]
            
    if year:
        book_data.append({'id': b_id, 'year': year})

df_books = pd.DataFrame(book_data)
print("Books columns:", df_books.columns)
print("Books count:", len(df_books))

# Process Reviews
review_data = []
for r in reviews:
    p_id_str = r.get('purchase_id', '')
    rating_str = r.get('rating', '0')
    
    m_id = re.search(r'purchaseid_(\d+)', p_id_str)
    if not m_id:
        continue
    p_id = int(m_id.group(1))
    
    try:
        rating = float(rating_str)
    except:
        continue
        
    review_data.append({'id': p_id, 'rating': rating})

df_reviews = pd.DataFrame(review_data)
print("Reviews columns:", df_reviews.columns)
print("Reviews count:", len(df_reviews))

if not df_books.empty and not df_reviews.empty:
    merged = pd.merge(df_reviews, df_books, on='id', how='inner')
    print("Merged count:", len(merged))
    
    # Calculate Decade
    merged['decade'] = (merged['year'] // 10) * 10
    merged['decade_str'] = merged['decade'].astype(str) + "s"

    grouped = merged.groupby('decade_str').agg(
        distinct_books=('id', 'nunique'),
        avg_rating=('rating', 'mean')
    ).reset_index()
    
    print("Grouped:")
    print(grouped)

    filtered = grouped[grouped['distinct_books'] >= 10].copy()
    filtered = filtered.sort_values(by='avg_rating', ascending=False)
    
    print("__RESULT__:")
    print(filtered.to_json(orient='records'))
else:
    print("__RESULT__:")
    print("[]")"""

env_args = {'var_function-call-4644691029107538022': 'file_storage/function-call-4644691029107538022.json', 'var_function-call-16058013232113512935': ['review'], 'var_function-call-2272556202224259319': [{'COUNT(*)': '1833'}], 'var_function-call-15315810567359206872': [{'count': '200'}], 'var_function-call-12909927237427682117': [{'purchase_id': 'purchaseid_186'}, {'purchase_id': 'purchaseid_191'}, {'purchase_id': 'purchaseid_190'}, {'purchase_id': 'purchaseid_8'}, {'purchase_id': 'purchaseid_178'}], 'var_function-call-5847662609626649812': 'file_storage/function-call-5847662609626649812.json', 'var_function-call-10489614112549282405': 'file_storage/function-call-10489614112549282405.json'}

exec(code, env_args)
