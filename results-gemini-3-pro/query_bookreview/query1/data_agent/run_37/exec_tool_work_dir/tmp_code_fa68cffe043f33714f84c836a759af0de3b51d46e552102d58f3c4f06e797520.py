code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-4085971081807944351'], 'r') as f:
    books_data = json.load(f)

with open(locals()['var_function-call-2549186950145988470'], 'r') as f:
    reviews_data = json.load(f)

books_list = []
for b in books_data:
    b_id_str = b.get('book_id')
    details = b.get('details', '')
    
    m_id = re.search(r'bookid_(\d+)', b_id_str)
    if not m_id:
        continue
    b_id = int(m_id.group(1))
    
    # Find first year-like number
    match = re.search(r'(19\d{2}|20\d{2})', details)
    if match:
        year = int(match.group(1))
        books_list.append({'id': b_id, 'year': year})

df_books = pd.DataFrame(books_list)
if df_books.empty:
    print("__RESULT__:")
    print(json.dumps({"error": "No books with years found"}))
else:
    df_books['decade'] = (df_books['year'] // 10) * 10
    df_books['decade_str'] = df_books['decade'].astype(str) + 's'

    reviews_list = []
    for r in reviews_data:
        p_id_str = r.get('purchase_id')
        avg_rating = float(r.get('avg_rating'))
        review_count = int(r.get('review_count'))
        
        m_id = re.search(r'purchaseid_(\d+)', p_id_str)
        if not m_id:
            continue
        p_id = int(m_id.group(1))
        
        reviews_list.append({'id': p_id, 'avg_rating': avg_rating, 'review_count': review_count})

    df_reviews = pd.DataFrame(reviews_list)
    
    # Merge
    df_merged = pd.merge(df_books, df_reviews, on='id', how='inner')
    
    # Stats
    decade_stats = df_merged.groupby('decade_str').agg(
        num_books=('id', 'nunique'),
        macro_avg_rating=('avg_rating', 'mean'),
        weighted_sum=('avg_rating', lambda x: (x * df_merged.loc[x.index, 'review_count']).sum()),
        total_reviews=('review_count', 'sum')
    ).reset_index()

    decade_stats['micro_avg_rating'] = decade_stats['weighted_sum'] / decade_stats['total_reviews']

    # Filter
    df_filtered = decade_stats[decade_stats['num_books'] >= 10].copy()
    
    # Sort
    df_filtered = df_filtered.sort_values(by='micro_avg_rating', ascending=False)
    
    print("__RESULT__:")
    print(json.dumps({
        'stats': df_filtered[['decade_str', 'num_books', 'macro_avg_rating', 'micro_avg_rating']].to_dict(orient='records')
    }))"""

env_args = {'var_function-call-16219580158143234846': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'var_function-call-15084204797040615940': [{'count': '200'}], 'var_function-call-7190096270945092360': ['review'], 'var_function-call-8445870022034454807': [{'COUNT(*)': '1833'}], 'var_function-call-6451088586545664160': [{'purchase_id': 'purchaseid_186'}, {'purchase_id': 'purchaseid_191'}, {'purchase_id': 'purchaseid_190'}, {'purchase_id': 'purchaseid_8'}, {'purchase_id': 'purchaseid_178'}], 'var_function-call-4085971081807944351': 'file_storage/function-call-4085971081807944351.json', 'var_function-call-2549186950145988470': 'file_storage/function-call-2549186950145988470.json', 'var_function-call-9198154057629967878': {'error': 'No books parsed'}, 'var_function-call-12965972204696762320': [{'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is ', 'candidates': []}, {'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is', 'candidates': []}, {'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available ', 'candidates': []}, {'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written i', 'candidates': []}, {'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB a', 'candidates': []}], 'var_function-call-8521974568885738716': [{'type': "<class 'str'>", 'repr': "'Published by Chatto & Windus, the first edition of'", 'digits_sample': ['1', '2004', '196', '10', '0701169850'], 'has_2004': True}, {'type': "<class 'str'>", 'repr': "'This book, published by Heinemann in its first edi'", 'digits_sample': ['20', '1996', '316', '10', '0435088688'], 'has_2004': False}, {'type': "<class 'str'>", 'repr': "'This book, published by Little, Brown and Company '", 'digits_sample': ['8', '2012', '384', '10', '9780316185363'], 'has_2004': False}]}

exec(code, env_args)
