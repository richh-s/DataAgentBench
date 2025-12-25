code = """import json
import re
import pandas as pd

# Load data (reloading to be safe, though could rely on previous state if I kept it, but execute_python is stateless between calls unless I pass vars? No, instructions say "previous tool results are available as variables". So I can't reuse variables from previous execute_python block directly unless I assigned them to result? No, I must reload or use the result of previous call if it returned the data.
# The previous call returned only the final answer JSON. So I must reload/reprocess.)
# To save time, I will assume the logic is correct but just want to see the table.

with open(locals()['var_function-call-9466151329181022833'], 'r') as f:
    books_data = json.load(f)

with open(locals()['var_function-call-17556222483133250874'], 'r') as f:
    reviews_data = json.load(f)

book_years = {}
year_pattern = re.compile(r'(?:published|released)[\w\W]{0,50}?\b(19\d{2}|20\d{2})\b', re.IGNORECASE)
date_pattern = re.compile(r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+(19\d{2}|20\d{2})', re.IGNORECASE)

book_info = []
for b in books_data:
    bid_str = b.get('book_id', '')
    details = b.get('details', '')
    m_id = re.search(r'bookid_(\d+)', bid_str)
    if not m_id: continue
    bid = int(m_id.group(1))
    year = None
    m_year = year_pattern.search(details)
    if m_year: year = int(m_year.group(1))
    else:
        m_date = date_pattern.search(details)
        if m_date: year = int(m_date.group(1))
    if year:
        book_info.append({'id': bid, 'year': year})

df_books = pd.DataFrame(book_info)
if not df_books.empty:
    df_books['decade'] = (df_books['year'] // 10) * 10
    df_books['decade_str'] = df_books['decade'].astype(str) + "s"

review_list = []
for r in reviews_data:
    pid_str = r.get('purchase_id', '')
    rating = r.get('rating')
    m_id = re.search(r'purchaseid_(\d+)', pid_str)
    if not m_id: continue
    pid = int(m_id.group(1))
    if rating is not None:
        try: review_list.append({'id': pid, 'rating': float(rating)})
        except: pass

df_reviews = pd.DataFrame(review_list)

if not df_books.empty and not df_reviews.empty:
    merged = pd.merge(df_reviews, df_books, on='id', how='inner')
    
    # Metrics
    # 1. Macro Average (Average of book averages)
    book_avgs = merged.groupby(['decade_str', 'id'])['rating'].mean().reset_index()
    macro_avg = book_avgs.groupby('decade_str')['rating'].mean().reset_index(name='macro_avg')
    
    # 2. Micro Average (Average of all ratings)
    micro_avg = merged.groupby('decade_str')['rating'].mean().reset_index(name='micro_avg')
    
    # Counts
    counts = merged.groupby('decade_str')['id'].nunique().reset_index(name='book_count')
    
    # Combine
    stats = pd.merge(counts, micro_avg, on='decade_str')
    stats = pd.merge(stats, macro_avg, on='decade_str')
    
    print("__RESULT__:")
    print(stats.to_json(orient='records'))
else:
    print("__RESULT__:")
    print("[]")"""

env_args = {'var_function-call-15143408529647577567': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'var_function-call-5012055095290387125': [{'count': '200'}], 'var_function-call-7860955901802981847': ['review'], 'var_function-call-1642967241088979441': [{'COUNT(*)': '1833'}], 'var_function-call-8003113415507431300': [{'purchase_id': 'purchaseid_186'}, {'purchase_id': 'purchaseid_191'}, {'purchase_id': 'purchaseid_190'}, {'purchase_id': 'purchaseid_8'}, {'purchase_id': 'purchaseid_178'}], 'var_function-call-9466151329181022833': 'file_storage/function-call-9466151329181022833.json', 'var_function-call-17556222483133250874': 'file_storage/function-call-17556222483133250874.json', 'var_function-call-5498374544851489913': {'decade': '2020s', 'avg_rating': 4.663636363636364, 'book_count': 21}}

exec(code, env_args)
