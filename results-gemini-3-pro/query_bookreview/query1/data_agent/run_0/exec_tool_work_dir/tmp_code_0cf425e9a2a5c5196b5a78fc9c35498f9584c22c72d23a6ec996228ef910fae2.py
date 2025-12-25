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
    
    matches = re.findall(r'([12]\d{3})', details)
    year = None
    if matches:
        valid_years = [int(m) for m in matches if 1900 <= int(m) <= 2024]
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

merged = pd.merge(df_reviews, df_books, on='id', how='inner')
merged['decade'] = (merged['year'] // 10) * 10
merged['decade_str'] = merged['decade'].astype(str) + "s"

# Method 1: Global Average
g1 = merged.groupby('decade_str').agg(
    distinct_books=('id', 'nunique'),
    avg_rating_global=('rating', 'mean')
).reset_index()

# Method 2: Average of Book Averages
book_avgs = merged.groupby(['decade_str', 'id'])['rating'].mean().reset_index()
g2 = book_avgs.groupby('decade_str')['rating'].mean().reset_index().rename(columns={'rating': 'avg_rating_per_book'})

final = pd.merge(g1, g2, on='decade_str')
final = final[final['distinct_books'] >= 10]
print("__RESULT__:")
print(final.to_json(orient='records'))"""

env_args = {'var_function-call-4644691029107538022': 'file_storage/function-call-4644691029107538022.json', 'var_function-call-16058013232113512935': ['review'], 'var_function-call-2272556202224259319': [{'COUNT(*)': '1833'}], 'var_function-call-15315810567359206872': [{'count': '200'}], 'var_function-call-12909927237427682117': [{'purchase_id': 'purchaseid_186'}, {'purchase_id': 'purchaseid_191'}, {'purchase_id': 'purchaseid_190'}, {'purchase_id': 'purchaseid_8'}, {'purchase_id': 'purchaseid_178'}], 'var_function-call-5847662609626649812': 'file_storage/function-call-5847662609626649812.json', 'var_function-call-10489614112549282405': 'file_storage/function-call-10489614112549282405.json', 'var_function-call-1543764841573784033': [], 'var_function-call-2513143424708080617': {'result': [], 'debug': {'books_count': 0, 'total_books_raw': 200, 'book_ids_example': [1, 2, 3, 4, 5], 'reviews_count': 1833, 'total_reviews_raw': 1833, 'review_ids_example': [1, 2, 3, 4, 5]}}, 'var_function-call-10281650635427195667': {'sample_book': {'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.', 'years_found': [], 'type_details': "<class 'str'>"}, 'var_function-call-10870574930865302821': {'years_simple': ['2004']}, 'var_function-call-15899302473534940159': [{'decade_str': '2020s', 'distinct_books': 21, 'avg_rating': 4.6636363636}, {'decade_str': '2010s', 'distinct_books': 88, 'avg_rating': 4.6085918854}, {'decade_str': '2000s', 'distinct_books': 47, 'avg_rating': 4.2762237762}, {'decade_str': '1980s', 'distinct_books': 11, 'avg_rating': 4.2083333333}, {'decade_str': '1990s', 'distinct_books': 16, 'avg_rating': 3.8208955224}]}

exec(code, env_args)
