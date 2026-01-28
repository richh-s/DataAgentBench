code = """import json, re
import pandas as pd

with open(var_call_V2Ub7kWMd06b7DMRBz5xaSBj, 'r', encoding='utf-8') as f:
    books = json.load(f)
with open(var_call_7WJPf7muozLZut10OuOdjvFo, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

df_books = pd.DataFrame(books)
df_reviews = pd.DataFrame(reviews)

# extract numeric id
def extract_num(s):
    if pd.isna(s):
        return None
    m = re.search(r"(\d+)", str(s))
    return int(m.group(1)) if m else None

# extract year using broader pattern
def extract_year(s):
    if pd.isna(s):
        return None
    s = str(s)
    # search for 4-digit year between 1000 and 2029
    m = re.search(r"\b(1[0-9]{3}|20[0-2][0-9])\b", s)
    if m:
        return int(m.group(0))
    # fallback: any 4-digit between 1000-2099
    m = re.search(r"\b(1[0-9]{3}|20[0-9]{2})\b", s)
    if m:
        return int(m.group(0))
    # fallback: common 19xx/20xx
    m = re.search(r"(19|20)\d{2}", s)
    if m:
        return int(m.group(0))
    return None

# apply
if 'book_id' in df_books.columns:
    df_books['num_id'] = df_books['book_id'].apply(extract_num)
else:
    df_books['num_id'] = None

if 'purchase_id' in df_reviews.columns:
    df_reviews['num_id'] = df_reviews['purchase_id'].apply(extract_num)
else:
    df_reviews['num_id'] = None

# convert ratings
if 'rating' in df_reviews.columns:
    df_reviews['rating'] = pd.to_numeric(df_reviews['rating'], errors='coerce')
else:
    df_reviews['rating'] = None

# extract year
if 'details' in df_books.columns:
    df_books['year'] = df_books['details'].apply(extract_year)
else:
    df_books['year'] = None

# merge
books_clean = df_books.dropna(subset=['num_id']).copy()
reviews_clean = df_reviews.dropna(subset=['num_id']).copy()
merged = pd.merge(reviews_clean, books_clean, on='num_id', how='inner', suffixes=('_rev','_book'))

# keep valid year and rating
merged = merged.dropna(subset=['year','rating']).copy()
merged['year'] = merged['year'].astype(int)
merged['decade_start'] = (merged['year']//10)*10
merged['decade'] = merged['decade_start'].astype(str) + 's'

# aggregate: distinct books per decade and average rating across all reviews
agg = merged.groupby('decade').agg(book_count = ('book_id', lambda x: x.nunique()), avg_rating = ('rating', 'mean')).reset_index()

# filter decades with at least 10 distinct books
agg_filtered = agg[agg['book_count'] >= 10].copy()

best = None
if not agg_filtered.empty:
    best_row = agg_filtered.sort_values('avg_rating', ascending=False).iloc[0]
    best = {'decade': best_row['decade'], 'average_rating': round(float(best_row['avg_rating']),4), 'book_count': int(best_row['book_count'])}
else:
    best = {'decade': None, 'average_rating': None, 'book_count': 0}

print('__RESULT__:')
print(json.dumps(best))"""

env_args = {'var_call_y1Tx7d5jbxthUjoKbarSZn6t': 'file_storage/call_y1Tx7d5jbxthUjoKbarSZn6t.json', 'var_call_AoGVRqzQ10M2wVo911ReA77F': ['review'], 'var_call_7WJPf7muozLZut10OuOdjvFo': 'file_storage/call_7WJPf7muozLZut10OuOdjvFo.json', 'var_call_YMgkOmecrFWpmUbJ3KAaY39G': {'decade': None, 'average_rating': None, 'book_count': 0}, 'var_call_V2Ub7kWMd06b7DMRBz5xaSBj': 'file_storage/call_V2Ub7kWMd06b7DMRBz5xaSBj.json', 'var_call_ZvB85hPDWJ0e3PtS7yvZS3Nb': {'books_total': 200, 'books_with_num': 200, 'books_with_year': 0, 'reviews_total': 1833, 'reviews_with_num': 1833, 'intersect_count': 200, 'year_counts_in_intersect_sample': {'None': 200}, 'sample_missing_year_in_intersect': [{'book_id': 'bookid_1', 'title': 'Chaucer', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.', 'num_id': 1, 'year': None}, {'book_id': 'bookid_2', 'title': 'Notes from a Kidwatcher', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.', 'num_id': 2, 'year': None}, {'book_id': 'bookid_3', 'title': 'Service: A Navy SEAL at War', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.', 'num_id': 3, 'year': None}, {'book_id': 'bookid_4', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.', 'num_id': 4, 'year': None}, {'book_id': 'bookid_5', 'title': 'Parker & Knight', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.', 'num_id': 5, 'year': None}, {'book_id': 'bookid_6', 'title': 'Writings from a Black Woman Living in the Land of the "Free": Strength, Power, Resilience', 'details': 'This book, published independently on December 30, 2021, is written in English and consists of 24 pages. It has an ISBN 13 of 979-8528537702 and weighs 3.2 ounces. The dimensions of the book are 7 x 0.06 x 9 inches.', 'num_id': 6, 'year': None}, {'book_id': 'bookid_7', 'title': "Child Development: A Practitioner's Guide:2nd (Second) edition", 'details': 'The book, published by Guilford in its second edition in January 2004, is also noted as the 8082nd edition from January 1, 1994. It has a remarkably light item weight of just 0.01 ounces.', 'num_id': 7, 'year': None}, {'book_id': 'bookid_8', 'title': 'Make: Electronics: Learning Through Discovery', 'details': 'This book, published by Make Community, LLC, in its second edition on September 22, 2015, is available in English and spans 352 pages in paperback format. It has an ISBN of 9781680450262 for the 10-digit version and 978-1680450262 for the 13-digit version. The content is suitable for readers aged 11 to 17 years. The book weighs 2.91 pounds and its dimensions are 8 inches in width, 0.5 inches in thickness, and 10 inches in height.', 'num_id': 8, 'year': None}, {'book_id': 'bookid_9', 'title': 'Reunion: The Children of Lauderdale Park', 'details': 'This book, published independently on September 25, 2019, is written in English and spans 367 pages. It is available in paperback format and has an ISBN-10 of 1694621731 and an ISBN-13 of 978-1694621733. The item weighs 1.38 pounds and measures 6 x 0.92 x 9 inches.', 'num_id': 9, 'year': None}, {'book_id': 'bookid_10', 'title': 'Four Centuries of American Education', 'details': 'This book, published by WallBuilder Press in its first edition on November 8, 2004, is available in English and comprises 51 pages in paperback format. It has an ISBN-10 of 1932225323 and an ISBN-13 of 978-1932225327, with a total item weight of 3.52 ounces.', 'num_id': 10, 'year': None}], 'agg_top_decades_all': [], 'agg_filtered': [], 'best': None}, 'var_call_lkzsgnhvuOH0PWovTcxdS5oE': 'file_storage/call_lkzsgnhvuOH0PWovTcxdS5oE.json'}

exec(code, env_args)
