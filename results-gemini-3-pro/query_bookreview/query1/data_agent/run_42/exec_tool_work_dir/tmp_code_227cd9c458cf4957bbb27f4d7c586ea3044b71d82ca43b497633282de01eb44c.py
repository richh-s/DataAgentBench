code = """import json
import re
import pandas as pd

# Load data
with open(locals()['var_function-call-11873734450374781457'], 'r') as f:
    books_data = json.load(f)
with open(locals()['var_function-call-12960266777265457397'], 'r') as f:
    reviews_data = json.load(f)

# Process Books
def extract_year(details):
    match = re.search(r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+(?:\d{1,2},\s+)?(\d{4})', details)
    if match:
        return int(match.group(1))
    return None

books = []
for b in books_data:
    bid_str = b['book_id']
    try:
        bid_num = int(bid_str.split('_')[1])
    except:
        continue
    year = extract_year(b['details'])
    if year:
        books.append({'id': bid_num, 'year': year, 'decade': (year // 10) * 10})

df_books = pd.DataFrame(books)

# Process Reviews
reviews = []
for r in reviews_data:
    pid_str = r['purchase_id']
    try:
        pid_num = int(pid_str.split('_')[1])
        rating = float(r['rating'])
        reviews.append({'id': pid_num, 'rating': rating})
    except:
        continue

df_reviews = pd.DataFrame(reviews)

book_ratings = df_reviews.groupby('id')['rating'].mean().reset_index()
book_ratings.columns = ['id', 'avg_rating']
merged = pd.merge(df_books, book_ratings, on='id')

decade_stats = merged.groupby('decade').agg(
    book_count=('id', 'count'),
    decade_avg_rating=('avg_rating', 'mean')
).reset_index()

print("__RESULT__:")
print(decade_stats.to_json(orient='records'))"""

env_args = {'var_function-call-1918891154920008115': ['books_info'], 'var_function-call-4779394784672551508': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'var_function-call-4232704316358836999': [{'count': '200'}], 'var_function-call-9922110301894938185': ['review'], 'var_function-call-9575717848918279717': [{'count(*)': '1833'}], 'var_function-call-6905681582815727663': [{'purchase_id': 'purchaseid_186', 'rating': '4'}, {'purchase_id': 'purchaseid_191', 'rating': '4'}, {'purchase_id': 'purchaseid_190', 'rating': '4'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '4'}], 'var_function-call-11873734450374781457': 'file_storage/function-call-11873734450374781457.json', 'var_function-call-12960266777265457397': 'file_storage/function-call-12960266777265457397.json', 'var_function-call-6099026701102176886': {'decade': '1980s', 'average_rating': 4.5481993851559075, 'book_count': 11}}

exec(code, env_args)
