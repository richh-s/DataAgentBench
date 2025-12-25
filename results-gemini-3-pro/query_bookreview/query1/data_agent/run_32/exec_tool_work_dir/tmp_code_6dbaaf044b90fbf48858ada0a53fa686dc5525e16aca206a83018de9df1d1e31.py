code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-8173574687529658226'], 'r') as f:
    books_data = json.load(f)

print("Books data count:", len(books_data))
if len(books_data) > 0:
    print("Sample book:", books_data[0])

books_list = []
for b in books_data:
    b_id_str = b.get('book_id', '')
    num_match = re.search(r'\d+', b_id_str)
    if not num_match:
        continue
    book_id = int(num_match.group(0))
    
    details = b.get('details', '')
    if not details:
        continue
        
    years = re.findall(r'\b(19\d{2}|20[0-2]\d)\b', details)
    if years:
        year = int(years[0])
        decade = (year // 10) * 10
        decade_str = f"{decade}s"
        books_list.append({'book_id': book_id, 'year': year, 'decade': decade_str})

print("Parsed books count:", len(books_list))
if len(books_list) > 0:
    print("Sample parsed book:", books_list[0])

df_books = pd.DataFrame(books_list)
if df_books.empty:
    print("df_books is empty!")
else:
    print("df_books columns:", df_books.columns)

# Reviews
with open(locals()['var_function-call-8173574687529659941'], 'r') as f:
    reviews_data = json.load(f)
    
print("Reviews data count:", len(reviews_data))

reviews_list = []
for r in reviews_data:
    p_id_str = r.get('purchase_id', '')
    num_match = re.search(r'\d+', p_id_str)
    if not num_match:
        continue
    book_id = int(num_match.group(0))
    rating = r.get('rating')
    if rating is None:
        continue
    reviews_list.append({'book_id': book_id, 'rating': float(rating)})

df_reviews = pd.DataFrame(reviews_list)
print("Parsed reviews count:", len(reviews_list))
if df_reviews.empty:
    print("df_reviews is empty!")

# Merge
if not df_books.empty and not df_reviews.empty:
    merged = pd.merge(df_reviews, df_books, on='book_id', how='inner')
    
    decade_stats = merged.groupby('decade').agg(
        distinct_books=('book_id', 'nunique'),
        avg_rating=('rating', 'mean')
    ).reset_index()

    print("Decade stats:")
    print(decade_stats)

    filtered = decade_stats[decade_stats['distinct_books'] >= 10].copy()
    
    if not filtered.empty:
        best = filtered.sort_values('avg_rating', ascending=False).iloc[0]
        print("__RESULT__:")
        print(json.dumps({'decade': best['decade'], 'average_rating': best['avg_rating']}))
    else:
        print("__RESULT__:")
        print(json.dumps("No suitable decade"))
else:
    print("Cannot merge, empty DFs")
    print("__RESULT__:")
    print(json.dumps("Empty dataframes"))"""

env_args = {'var_function-call-10920357629305558601': ['books_info'], 'var_function-call-10920357629305557698': ['review'], 'var_function-call-3393905740280943849': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'var_function-call-3654176990585613679': [{'purchase_id': 'purchaseid_186', 'rating': '4'}, {'purchase_id': 'purchaseid_191', 'rating': '4'}, {'purchase_id': 'purchaseid_190', 'rating': '4'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '4'}], 'var_function-call-2387096001916786856': [{'count': '200'}], 'var_function-call-2387096001916785173': [{'COUNT(*)': '1833'}], 'var_function-call-8173574687529658226': 'file_storage/function-call-8173574687529658226.json', 'var_function-call-8173574687529659941': 'file_storage/function-call-8173574687529659941.json'}

exec(code, env_args)
