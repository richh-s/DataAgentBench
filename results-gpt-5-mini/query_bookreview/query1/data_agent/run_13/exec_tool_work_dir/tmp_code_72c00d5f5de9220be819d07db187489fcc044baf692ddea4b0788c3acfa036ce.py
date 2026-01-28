code = """import json
import pandas as pd
import re

books_path = var_call_pRLFf1uGnd9sIAK58vrpRrTd
reviews_path = var_call_bWD8aiXmknR4yB0zMqClK4JE
with open(books_path, 'r', encoding='utf-8') as f:
    books = json.load(f)
with open(reviews_path, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

books_df = pd.DataFrame(books)
reviews_df = pd.DataFrame(reviews)

reviews_df['rating'] = pd.to_numeric(reviews_df['rating'], errors='coerce')
reviews_df['book_id'] = reviews_df['purchase_id'].astype(str).str.replace('purchaseid_', 'bookid_', regex=False)

# simpler regex
four_re = re.compile(r"\b(\d{4})\b")

def extract_year_simple(detail):
    if not isinstance(detail, str):
        return None
    for m in four_re.findall(detail):
        try:
            y = int(m)
            if 1000 <= y <= 2023:
                return y
        except:
            continue
    return None

books_df['pub_year'] = books_df['details'].apply(extract_year_simple)
books_with_year = books_df.dropna(subset=['pub_year']).copy()
books_with_year['pub_year'] = books_with_year['pub_year'].astype(int)
books_with_year['decade'] = (books_with_year['pub_year'] // 10 * 10).astype(int).astype(str) + 's'

merged = pd.merge(reviews_df, books_with_year[['book_id','decade']], on='book_id', how='inner')

# per-book average rating
book_avg = merged.groupby('book_id', as_index=False).agg({'rating':'mean', 'decade':'first'})
book_avg.rename(columns={'rating':'avg_rating'}, inplace=True)

# per-decade stats
decade_stats = book_avg.groupby('decade').agg(book_count=('book_id','nunique'), decade_avg_rating=('avg_rating','mean')).reset_index()
# filter >=10
decade_stats_filtered = decade_stats[decade_stats['book_count'] >= 10].copy()

if decade_stats_filtered.empty:
    out = {'decade_with_highest_avg': None, 'reason': 'no decade has at least 10 distinct rated books', 'decade_stats': decade_stats.to_dict(orient='records')}
else:
    top = decade_stats_filtered.sort_values(by=['decade_avg_rating','book_count','decade'], ascending=[False, False, True]).iloc[0]
    out = {'decade_with_highest_avg': top['decade'], 'avg_rating': round(float(top['decade_avg_rating']),4), 'book_count': int(top['book_count']), 'decade_stats': decade_stats_filtered.to_dict(orient='records')}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_HjCwp3kP57Wi9qGfmIhDYN3p': ['books_info'], 'var_call_pRLFf1uGnd9sIAK58vrpRrTd': 'file_storage/call_pRLFf1uGnd9sIAK58vrpRrTd.json', 'var_call_6OqtxT8HeK3FLZ5u4gMbPLp4': ['review'], 'var_call_bWD8aiXmknR4yB0zMqClK4JE': 'file_storage/call_bWD8aiXmknR4yB0zMqClK4JE.json', 'var_call_4rVGdv08NLfl4bToC7WwgqbT': {'decade': None, 'avg_rating': None, 'book_count': 0}, 'var_call_2VUlZqlAGCWekiBjZqCGkLA7': {'total_books_in_books_db': 200, 'books_with_extracted_year': 0, 'decade_counts_in_books_with_year': {}, 'unique_books_in_reviews_joined_with_books': 0, 'unique_books_per_decade_in_merged': {}, 'sample_books_with_no_year': [{'book_id': 'bookid_1', 'title': 'Chaucer', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'title': 'Notes from a Kidwatcher', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'title': 'Service: A Navy SEAL at War', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'title': 'Parker & Knight', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}]}, 'var_call_RSEdhgrJ4MBIfkSRAfzopnBo': {'first_10_books': [{'book_id': 'bookid_1', 'title': 'Chaucer', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.', 'categories': '["Books", "Literature & Fiction", "History & Criticism"]'}, {'book_id': 'bookid_2', 'title': 'Notes from a Kidwatcher', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.', 'categories': '["Books", "Reference", "Words, Language & Grammar"]'}, {'book_id': 'bookid_3', 'title': 'Service: A Navy SEAL at War', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.', 'categories': '["Books", "Biographies & Memoirs", "Leaders & Notable People"]'}, {'book_id': 'bookid_4', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_5', 'title': 'Parker & Knight', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.', 'categories': '["Books", "Mystery, Thriller & Suspense", "Thrillers & Suspense"]'}, {'book_id': 'bookid_6', 'title': 'Writings from a Black Woman Living in the Land of the "Free": Strength, Power, Resilience', 'details': 'This book, published independently on December 30, 2021, is written in English and consists of 24 pages. It has an ISBN 13 of 979-8528537702 and weighs 3.2 ounces. The dimensions of the book are 7 x 0.06 x 9 inches.', 'categories': '["Books", "Arts & Photography", "History & Criticism"]'}, {'book_id': 'bookid_7', 'title': "Child Development: A Practitioner's Guide:2nd (Second) edition", 'details': 'The book, published by Guilford in its second edition in January 2004, is also noted as the 8082nd edition from January 1, 1994. It has a remarkably light item weight of just 0.01 ounces.', 'categories': '["Books", "Parenting & Relationships", "Parenting"]'}, {'book_id': 'bookid_8', 'title': 'Make: Electronics: Learning Through Discovery', 'details': 'This book, published by Make Community, LLC, in its second edition on September 22, 2015, is available in English and spans 352 pages in paperback format. It has an ISBN of 9781680450262 for the 10-digit version and 978-1680450262 for the 13-digit version. The content is suitable for readers aged 11 to 17 years. The book weighs 2.91 pounds and its dimensions are 8 inches in width, 0.5 inches in thickness, and 10 inches in height.', 'categories': '["Books", "Engineering & Transportation", "Engineering"]'}, {'book_id': 'bookid_9', 'title': 'Reunion: The Children of Lauderdale Park', 'details': 'This book, published independently on September 25, 2019, is written in English and spans 367 pages. It is available in paperback format and has an ISBN-10 of 1694621731 and an ISBN-13 of 978-1694621733. The item weighs 1.38 pounds and measures 6 x 0.92 x 9 inches.', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]'}, {'book_id': 'bookid_10', 'title': 'Four Centuries of American Education', 'details': 'This book, published by WallBuilder Press in its first edition on November 8, 2004, is available in English and comprises 51 pages in paperback format. It has an ISBN-10 of 1932225323 and an ISBN-13 of 978-1932225327, with a total item weight of 3.52 ounces.', 'categories': '["Books", "Education & Teaching", "Schools & Teaching"]'}], 'first_10_reviews': [{'rating': '4', 'purchase_id': 'purchaseid_186', 'review_time': '2012-11-24 18:52:00'}, {'rating': '4', 'purchase_id': 'purchaseid_191', 'review_time': '2015-12-31 13:35:00'}, {'rating': '4', 'purchase_id': 'purchaseid_190', 'review_time': '2013-05-05 10:47:00'}, {'rating': '5', 'purchase_id': 'purchaseid_8', 'review_time': '2020-08-12 11:06:00'}, {'rating': '4', 'purchase_id': 'purchaseid_178', 'review_time': '2014-11-13 18:55:00'}, {'rating': '4', 'purchase_id': 'purchaseid_186', 'review_time': '2013-02-20 16:09:00'}, {'rating': '5', 'purchase_id': 'purchaseid_76', 'review_time': '2020-02-27 05:11:00'}, {'rating': '4', 'purchase_id': 'purchaseid_186', 'review_time': '2013-01-06 07:52:00'}, {'rating': '5', 'purchase_id': 'purchaseid_115', 'review_time': '2019-07-24 13:29:00'}, {'rating': '2', 'purchase_id': 'purchaseid_167', 'review_time': '2020-06-01 07:33:00'}], 'books_keys': ['book_id', 'title', 'details', 'categories'], 'reviews_keys': ['rating', 'purchase_id', 'review_time']}, 'var_call_aiaV1F7CEEGinPTop2vNIQYu': 'file_storage/call_aiaV1F7CEEGinPTop2vNIQYu.json'}

exec(code, env_args)
