code = """import json
import re
import pandas as pd

books_path = locals()['var_function-call-7229594273416415337']
reviews_path = locals()['var_function-call-18367235769688117238']

with open(books_path, 'r') as f:
    books = json.load(f)
with open(reviews_path, 'r') as f:
    reviews = json.load(f)

def get_id(s):
    if not isinstance(s, str): return None
    m = re.search(r'(\d+)$', s)
    if m:
        return int(m.group(1))
    return None

book_data = []
for b in books:
    bid = get_id(b.get('book_id'))
    details = b.get('details', '')
    # Regex without \b, finding all years
    years = re.findall(r'19\d{2}|20\d{2}', details)
    year = None
    if years:
        # Check if year is valid (e.g. <= 2025) just in case
        valid_years = [int(y) for y in years if 1900 <= int(y) <= 2025]
        if valid_years:
            year = valid_years[0]
    
    if bid is not None and year is not None:
        book_data.append({'id': bid, 'year': year})

df_books = pd.DataFrame(book_data)
if df_books.empty:
    df_books = pd.DataFrame(columns=['id', 'year'])
# Drop duplicates if any
df_books = df_books.drop_duplicates(subset=['id'])

review_data = []
for r in reviews:
    pid = get_id(r.get('purchase_id'))
    if pid is not None:
        try:
            rating = float(r['rating'])
            review_data.append({'id': pid, 'rating': rating})
        except:
            pass

df_reviews = pd.DataFrame(review_data)
if df_reviews.empty:
    df_reviews = pd.DataFrame(columns=['id', 'rating'])

if not df_reviews.empty and not df_books.empty:
    # Average rating per book
    book_stats = df_reviews.groupby('id')['rating'].agg(['mean', 'count']).reset_index()
    book_stats.rename(columns={'mean': 'avg_rating', 'count': 'num_reviews'}, inplace=True)
    
    # Merge with publication years
    merged = pd.merge(df_books, book_stats, on='id', how='inner')
    
    # Decade
    merged['decade'] = (merged['year'] // 10) * 10
    
    # Group by decade
    decade_stats = merged.groupby('decade').agg(
        num_books=('id', 'count'),
        avg_rating_decade=('avg_rating', 'mean')
    ).reset_index()
    
    # Format decade as "1980s"
    decade_stats['decade_str'] = decade_stats['decade'].astype(str) + 's'
    
    # Filter: >= 10 distinct books
    filtered = decade_stats[decade_stats['num_books'] >= 10].sort_values('avg_rating_decade', ascending=False)
    
    print("__RESULT__:")
    print(filtered.to_json(orient='records'))
else:
    print("__RESULT__:")
    print("[]")"""

env_args = {'var_function-call-5381900575935500103': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'var_function-call-1146212370315976145': [{'count': '200'}], 'var_function-call-17812567415089105343': ['review'], 'var_function-call-8183095380455942288': [{'count(*)': '1833'}], 'var_function-call-7229594273416415337': 'file_storage/function-call-7229594273416415337.json', 'var_function-call-18367235769688117238': 'file_storage/function-call-18367235769688117238.json', 'var_function-call-4350415323415926900': [], 'var_function-call-10789004458578406465': [], 'var_function-call-70921821608659599': [], 'var_function-call-9267436205315548389': {'book_ids_sample': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'review_ids_sample': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'intersection_count': 200, 'book_count': 200, 'review_count': 200}, 'var_function-call-9130816285809475045': [{'id': 'bookid_1', 'extracted': None, 'details_snippet': 'Published by Chatto & Windus, the first edition of'}, {'id': 'bookid_2', 'extracted': None, 'details_snippet': 'This book, published by Heinemann in its first edi'}, {'id': 'bookid_3', 'extracted': None, 'details_snippet': 'This book, published by Little, Brown and Company '}, {'id': 'bookid_4', 'extracted': None, 'details_snippet': 'This book, published by Scholastic Paperbacks in a'}, {'id': 'bookid_5', 'extracted': None, 'details_snippet': 'The book was published on May 18, 2014, and is ava'}, {'id': 'bookid_6', 'extracted': None, 'details_snippet': 'This book, published independently on December 30,'}, {'id': 'bookid_7', 'extracted': None, 'details_snippet': 'The book, published by Guilford in its second edit'}, {'id': 'bookid_8', 'extracted': None, 'details_snippet': 'This book, published by Make Community, LLC, in it'}, {'id': 'bookid_9', 'extracted': None, 'details_snippet': 'This book, published independently on September 25'}, {'id': 'bookid_10', 'extracted': None, 'details_snippet': 'This book, published by WallBuilder Press in its f'}, {'id': 'bookid_11', 'extracted': None, 'details_snippet': 'Published by Caxton Press on January 1, 1993, this'}, {'id': 'bookid_12', 'extracted': None, 'details_snippet': 'This book, published by Lisette Marshall on May 29'}, {'id': 'bookid_13', 'extracted': None, 'details_snippet': 'The book, published by Central Avenue Publishing o'}, {'id': 'bookid_14', 'extracted': None, 'details_snippet': 'The book, published by Jessica Mathews, LLC on Nov'}, {'id': 'bookid_15', 'extracted': None, 'details_snippet': 'The book is published by Kegan Paul and is a first'}, {'id': 'bookid_16', 'extracted': None, 'details_snippet': 'This book is published by Prentice Hall College Di'}, {'id': 'bookid_17', 'extracted': None, 'details_snippet': 'This book, published by Edelsa Grupo Didascalia in'}, {'id': 'bookid_18', 'extracted': None, 'details_snippet': 'The book, published by Gale, Sabin Americana on Fe'}, {'id': 'bookid_19', 'extracted': None, 'details_snippet': 'The book, published by Foundation Press in its 201'}, {'id': 'bookid_20', 'extracted': None, 'details_snippet': 'The book, published by Soho Crime in a revised edi'}], 'var_function-call-7339627946722146529': {'matches': []}, 'var_function-call-6329305157012130548': ['2004']}

exec(code, env_args)
