code = """import json
import pandas as pd
import re

# Load data
with open(var_call_TUvJXKQeqJ37mMHR2spm3ift, 'r', encoding='utf-8') as f:
    books = json.load(f)
with open(var_call_Nx0j5IGC14Xr8U35jHcX9nVS, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

books_df = pd.DataFrame(books)
reviews_df = pd.DataFrame(reviews)

# normalize ratings
reviews_df['rating'] = pd.to_numeric(reviews_df['rating'], errors='coerce')

# extract numeric id
import math

def extract_num_id(s):
    if not isinstance(s, str):
        return None
    m = re.search(r'_(\d+)$', s)
    if m:
        return m.group(1)
    m2 = re.search(r'(\d+)', s)
    return m2.group(1) if m2 else None

books_df['num_id'] = books_df['book_id'].apply(extract_num_id)
reviews_df['num_id'] = reviews_df['purchase_id'].apply(extract_num_id)
reviews_df['book_id'] = reviews_df['num_id'].apply(lambda x: f'bookid_{x}' if pd.notnull(x) else None)

# Merge reviews with books
merged = reviews_df.merge(books_df[['book_id','details']], on='book_id', how='left')

# Extract year from details by finding all 4-digit numbers and selecting first in 1500-2023

def extract_year_from_details(details):
    if not isinstance(details, str):
        return None
    matches = re.findall(r"\d{4}", details)
    for m in matches:
        try:
            y = int(m)
        except:
            continue
        if 1500 <= y <= 2023:
            return y
    return None

# Build book-year mapping from books_df details
books_df['year'] = books_df['details'].apply(extract_year_from_details)

# Now merge book-year into per-book averages
# Compute per-book average rating and ensure book has a year
book_ratings = merged.groupby('book_id', dropna=True)['rating'].mean().reset_index().rename(columns={'rating':'avg_rating'})
# join with books_df to get year
book_ratings = book_ratings.merge(books_df[['book_id','year']], on='book_id', how='left')
# keep only books with year
book_ratings = book_ratings[book_ratings['year'].notnull()].copy()
book_ratings['year'] = book_ratings['year'].astype(int)
book_ratings['decade_start'] = (book_ratings['year'] // 10) * 10
book_ratings['decade'] = book_ratings['decade_start'].astype(str) + 's'

# Per-decade stats: average of book avg_ratings and distinct book counts
decade_stats = book_ratings.groupby('decade').agg(distinct_books=('book_id','nunique'), avg_rating=('avg_rating','mean')).reset_index()

# Filter decades with at least 10 distinct books
valid = decade_stats[decade_stats['distinct_books'] >= 10]

best_decade = None
if not valid.empty:
    # select highest avg_rating, tie-breaker smaller decade string
    valid_sorted = valid.sort_values(['avg_rating','decade'], ascending=[False, True])
    best_decade = valid_sorted.iloc[0]['decade']

# Prepare output
print('__RESULT__:')
print(json.dumps(best_decade))"""

env_args = {'var_call_25XrTT1v8MA76LlhO9Ah0Qpu': ['review'], 'var_call_CaaMHIphba5mhsgrjOW70AAl': ['books_info'], 'var_call_ahSeu74lplrW2uWVFYFbYKof': 'file_storage/call_ahSeu74lplrW2uWVFYFbYKof.json', 'var_call_t8s9j3CLGS3oQRddFrBguw0a': 'file_storage/call_t8s9j3CLGS3oQRddFrBguw0a.json', 'var_call_AnPCoO6KSaGRcg5jGKCGL4Nx': None, 'var_call_o2VX8jZXpeJ7U4MZ3xWm2fnA': [], 'var_call_TUvJXKQeqJ37mMHR2spm3ift': 'file_storage/call_TUvJXKQeqJ37mMHR2spm3ift.json', 'var_call_Nx0j5IGC14Xr8U35jHcX9nVS': 'file_storage/call_Nx0j5IGC14Xr8U35jHcX9nVS.json', 'var_call_O5RsHGoXv8ot6FPveUYIK5TK': {'books_count': 200, 'reviews_count': 1833, 'merged_rows': 1833, 'rows_with_details': 1833, 'rows_without_details': 0, 'rows_with_year': 0, 'unique_books_with_year': 0, 'decade_stats': [], 'valid_decades': [], 'best_decade': None}, 'var_call_6t101iyHVg7Fe3HYMMtBXFCF': {'sample_books': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}, {'book_id': 'bookid_6', 'details': 'This book, published independently on December 30, 2021, is written in English and consists of 24 pages. It has an ISBN 13 of 979-8528537702 and weighs 3.2 ounces. The dimensions of the book are 7 x 0.06 x 9 inches.'}, {'book_id': 'bookid_7', 'details': 'The book, published by Guilford in its second edition in January 2004, is also noted as the 8082nd edition from January 1, 1994. It has a remarkably light item weight of just 0.01 ounces.'}, {'book_id': 'bookid_8', 'details': 'This book, published by Make Community, LLC, in its second edition on September 22, 2015, is available in English and spans 352 pages in paperback format. It has an ISBN of 9781680450262 for the 10-digit version and 978-1680450262 for the 13-digit version. The content is suitable for readers aged 11 to 17 years. The book weighs 2.91 pounds and its dimensions are 8 inches in width, 0.5 inches in thickness, and 10 inches in height.'}, {'book_id': 'bookid_9', 'details': 'This book, published independently on September 25, 2019, is written in English and spans 367 pages. It is available in paperback format and has an ISBN-10 of 1694621731 and an ISBN-13 of 978-1694621733. The item weighs 1.38 pounds and measures 6 x 0.92 x 9 inches.'}, {'book_id': 'bookid_10', 'details': 'This book, published by WallBuilder Press in its first edition on November 8, 2004, is available in English and comprises 51 pages in paperback format. It has an ISBN-10 of 1932225323 and an ISBN-13 of 978-1932225327, with a total item weight of 3.52 ounces.'}, {'book_id': 'bookid_11', 'details': 'Published by Caxton Press on January 1, 1993, this book is available in English and spans 407 pages. It has an ISBN-10 of 0893011673 and an ISBN-13 of 978-0893011673. Weighing 1.51 pounds, the book measures 6.05 inches in width, 1.14 inches in depth, and 9.03 inches in height.'}, {'book_id': 'bookid_12', 'details': 'This book, published by Lisette Marshall on May 29, 2022, is written in English and is available in paperback, comprising 215 pages. It has an ISBN 10 number of 9083256898 and an ISBN 13 number of 978-9083256894. The item weighs 11.4 ounces and has dimensions of 6 x 0.54 x 9 inches.'}, {'book_id': 'bookid_13', 'details': 'The book, published by Central Avenue Publishing on January 24, 2023, is available in English and comes in paperback format, consisting of 144 pages. It has an ISBN-10 number of 1771682760 and an ISBN-13 number of 978-1771682763. The item weighs 5.1 ounces and has dimensions of 5.25 x 0.4 x 8 inches.'}, {'book_id': 'bookid_14', 'details': 'The book, published by Jessica Mathews, LLC on November 13, 2019, is written in English and features a paperback format comprising 26 pages. It has an ISBN-10 of 1087848539 and an ISBN-13 of 978-1087848532. Suitable for readers aged 3 to 8 years, it is appropriate for students in Kindergarten through 3rd grade. The item weighs 3.03 ounces and has dimensions of 8.5 x 0.05 x 11 inches.'}, {'book_id': 'bookid_15', 'details': 'The book is published by Kegan Paul and is a first edition released on November 15, 2000. It is written in English and is available in hardcover, comprising 348 pages. The ISBN-10 for this edition is 0710306911, while the ISBN-13 is 978-0710306913. The item weighs 2.23 pounds and has dimensions of 5.5 x 1.25 x 8.5 inches.'}, {'book_id': 'bookid_16', 'details': 'This book is published by Prentice Hall College Division and is in its third edition, released on January 1, 1997. It is written in English and is available in paperback, consisting of 390 pages. The ISBN-10 for this book is 0130840963, while the ISBN-13 is 978-0130840967. The item weighs 1.3 pounds and has dimensions of 7.01 x 0.67 x 9.17 inches.'}, {'book_id': 'bookid_17', 'details': 'This book, published by Edelsa Grupo Didascalia in a September 1, 1987 edition, is written in Spanish and consists of 44 pages. It has an ISBN-10 number of 8477110190 and an ISBN-13 number of 978-8477110194. The item weighs 2.05 ounces and has dimensions of 5.12 x 0.16 x 7.48 inches.'}, {'book_id': 'bookid_18', 'details': 'The book, published by Gale, Sabin Americana on February 21, 2012, is written in English and is available in paperback format, comprising 26 pages. It has an ISBN-10 of 1275627234 and an ISBN-13 of 978-1275627239. The item weighs 2.4 ounces and has dimensions of 7.44 x 0.05 x 9.69 inches.'}, {'book_id': 'bookid_19', 'details': "The book, published by Foundation Press in its 2013th edition on March 22, 2013, is available in English and spans 355 pages. It has an ISBN-10 number of 1609303687 and an ISBN-13 number of 978-1609303686. Weighing 1.5 pounds, the book's dimensions are 7 inches in width, 0.5 inches in thickness, and 9.75 inches in height."}, {'book_id': 'bookid_20', 'details': 'The book, published by Soho Crime in a revised edition on July 1, 2003, is available in English and has a total print length of 372 pages. It has a file size of 2295 KB and supports various features such as Text to Speech, a screen reader, enhanced typesetting, X-Ray, Word Wise, and sticky notes on Kindle Scribe.'}], 'regex_results': [{'book_id': 'bookid_1', 'matches': []}, {'book_id': 'bookid_2', 'matches': []}, {'book_id': 'bookid_3', 'matches': []}, {'book_id': 'bookid_4', 'matches': []}, {'book_id': 'bookid_5', 'matches': []}, {'book_id': 'bookid_6', 'matches': []}, {'book_id': 'bookid_7', 'matches': []}, {'book_id': 'bookid_8', 'matches': []}, {'book_id': 'bookid_9', 'matches': []}, {'book_id': 'bookid_10', 'matches': []}, {'book_id': 'bookid_11', 'matches': []}, {'book_id': 'bookid_12', 'matches': []}, {'book_id': 'bookid_13', 'matches': []}, {'book_id': 'bookid_14', 'matches': []}, {'book_id': 'bookid_15', 'matches': []}, {'book_id': 'bookid_16', 'matches': []}, {'book_id': 'bookid_17', 'matches': []}, {'book_id': 'bookid_18', 'matches': []}, {'book_id': 'bookid_19', 'matches': []}, {'book_id': 'bookid_20', 'matches': []}], 'num_books': 200, 'num_reviews': 1833}, 'var_call_TjHaKFVNblOHggcSTLxJjp56': 'file_storage/call_TjHaKFVNblOHggcSTLxJjp56.json'}

exec(code, env_args)
