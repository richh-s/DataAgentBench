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
    
    # Extract ID
    # bookid_1 -> 1
    m_id = re.search(r'bookid_(\d+)', b_id_str)
    if not m_id:
        continue
    b_id = int(m_id.group(1))
    
    # Extract Year
    # Look for 4 digit year 19xx or 20xx
    # We prioritize years that appear in the text.
    # regex matches 1900-2099
    years = re.findall(r'\b(19\d{2}|20\d{2})\b', details)
    
    year = None
    if years:
        # Heuristic: First year mentioned is often the publication year of the edition described.
        # Filter range just in case
        valid_years = [int(y) for y in years if 1900 <= int(y) <= 2024]
        if valid_years:
            year = valid_years[0]
            
    if year:
        book_data.append({'id': b_id, 'year': year})

df_books = pd.DataFrame(book_data)

# Process Reviews
review_data = []
for r in reviews:
    p_id_str = r.get('purchase_id', '')
    rating_str = r.get('rating', '0')
    
    # Extract ID
    # purchaseid_186 -> 186
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

# Merge
# Inner join to keep only rated books with known years
merged = pd.merge(df_reviews, df_books, on='id', how='inner')

# Calculate Decade
merged['decade'] = (merged['year'] // 10) * 10
merged['decade_str'] = merged['decade'].astype(str) + "s"

# Group by Decade
# We need:
# 1. Count of distinct books
# 2. Average rating
grouped = merged.groupby('decade_str').agg(
    distinct_books=('id', 'nunique'),
    avg_rating=('rating', 'mean')
).reset_index()

# Filter
filtered = grouped[grouped['distinct_books'] >= 10].copy()

# Sort by avg_rating desc
filtered = filtered.sort_values(by='avg_rating', ascending=False)

print("__RESULT__:")
print(filtered.to_json(orient='records'))"""

env_args = {'var_function-call-4644691029107538022': 'file_storage/function-call-4644691029107538022.json', 'var_function-call-16058013232113512935': ['review'], 'var_function-call-2272556202224259319': [{'COUNT(*)': '1833'}], 'var_function-call-15315810567359206872': [{'count': '200'}], 'var_function-call-12909927237427682117': [{'purchase_id': 'purchaseid_186'}, {'purchase_id': 'purchaseid_191'}, {'purchase_id': 'purchaseid_190'}, {'purchase_id': 'purchaseid_8'}, {'purchase_id': 'purchaseid_178'}], 'var_function-call-5847662609626649812': 'file_storage/function-call-5847662609626649812.json', 'var_function-call-10489614112549282405': 'file_storage/function-call-10489614112549282405.json'}

exec(code, env_args)
