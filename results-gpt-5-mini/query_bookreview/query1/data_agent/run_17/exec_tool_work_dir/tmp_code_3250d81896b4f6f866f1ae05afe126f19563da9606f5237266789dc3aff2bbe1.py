code = """import json, re, pandas as pd
with open(var_call_XTvE2u4u8fNfAT70SyBtj3lO, 'r') as f:
    reviews = json.load(f)
with open(var_call_WgirpVXkL6BEgT2yzTQt6Ktv, 'r') as f:
    books = json.load(f)

# DataFrames
df_rev = pd.DataFrame(reviews)
# ensure avg_rating float
df_rev['avg_rating'] = df_rev['avg_rating'].astype(float)

# map purchase_id like purchaseid_123 -> bookid_123
import math

def purchase_to_book(pid):
    m = re.search(r"(\d+)", pid)
    return f"bookid_{m.group(1)}" if m else None

df_rev['book_id'] = df_rev['purchase_id'].apply(purchase_to_book)

# books df
df_books = pd.DataFrame(books)

# robust year extraction: look for 18xx-2099 but ensure not adjacent to digits
year_re = re.compile(r'(?<!\d)(18\d{2}|19\d{2}|20\d{2})(?!\d)')

def extract_year(details):
    if not isinstance(details, str):
        return None
    m = year_re.search(details)
    if m:
        y = int(m.group(1))
        if 1500 <= y <= 2025:
            return y
    return None

df_books['pub_year'] = df_books['details'].apply(extract_year) if 'details' in df_books.columns else None

# drop books without pub_year
df_books_year = df_books.dropna(subset=['pub_year']).copy()
if not df_books_year.empty:
    df_books_year['pub_year'] = df_books_year['pub_year'].astype(int)
    df_books_year['decade'] = df_books_year['pub_year'].apply(lambda y: f"{(y//10)*10}s")
else:
    df_books_year['decade'] = []

# Merge per-book avg ratings with books by book_id
merged = pd.merge(df_rev, df_books_year[['book_id','decade']], on='book_id', how='inner')

# Group by decade: count distinct books and average the per-book avg_rating
if merged.empty:
    result = {'best_decade': None, 'avg_rating': None, 'n_books': 0, 'decades': []}
else:
    grp = merged.groupby('decade').agg(n_books=('book_id','nunique'), avg_rating=('avg_rating','mean')).reset_index()
    grp_filtered = grp[grp['n_books'] >= 10].copy()
    if grp_filtered.empty:
        result = {'best_decade': None, 'avg_rating': None, 'n_books': 0, 'decades': []}
    else:
        # choose highest avg_rating, tiebreaker by n_books desc, then decade lexicographically
        grp_filtered = grp_filtered.sort_values(by=['avg_rating','n_books','decade'], ascending=[False,False,True])
        best = grp_filtered.iloc[0]
        decades_list = []
        for _, r in grp_filtered.sort_values('decade').iterrows():
            decades_list.append({'decade': r['decade'], 'avg_rating': round(float(r['avg_rating']),4), 'n_books': int(r['n_books'])})
        result = {'best_decade': best['decade'], 'avg_rating': round(float(best['avg_rating']),4), 'n_books': int(best['n_books']), 'decades': decades_list}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_HMpLhDV5JN6U08VwosCXQpgv': ['review'], 'var_call_tm06RGmquUHZ4WBzlNs8BZRv': ['books_info'], 'var_call_XTvE2u4u8fNfAT70SyBtj3lO': 'file_storage/call_XTvE2u4u8fNfAT70SyBtj3lO.json', 'var_call_WgirpVXkL6BEgT2yzTQt6Ktv': 'file_storage/call_WgirpVXkL6BEgT2yzTQt6Ktv.json', 'var_call_RdSLEQzUUDJbC5EcyEKWN7Ms': {'best_decade': None, 'avg_rating': None, 'n_books': 0, 'decades': []}, 'var_call_L6UkvxvMuj7Va4rSfw4VdNYI': {'total_books': 200, 'books_with_year': 0, 'sample_with_year': [], 'sample_without_year': [{'book_id': 'bookid_1', 'title': 'Chaucer', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.', 'categories': '["Books", "Literature & Fiction", "History & Criticism"]', 'pub_year': None}, {'book_id': 'bookid_2', 'title': 'Notes from a Kidwatcher', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.', 'categories': '["Books", "Reference", "Words, Language & Grammar"]', 'pub_year': None}, {'book_id': 'bookid_3', 'title': 'Service: A Navy SEAL at War', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.', 'categories': '["Books", "Biographies & Memoirs", "Leaders & Notable People"]', 'pub_year': None}, {'book_id': 'bookid_4', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]', 'pub_year': None}, {'book_id': 'bookid_5', 'title': 'Parker & Knight', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.', 'categories': '["Books", "Mystery, Thriller & Suspense", "Thrillers & Suspense"]', 'pub_year': None}, {'book_id': 'bookid_6', 'title': 'Writings from a Black Woman Living in the Land of the "Free": Strength, Power, Resilience', 'details': 'This book, published independently on December 30, 2021, is written in English and consists of 24 pages. It has an ISBN 13 of 979-8528537702 and weighs 3.2 ounces. The dimensions of the book are 7 x 0.06 x 9 inches.', 'categories': '["Books", "Arts & Photography", "History & Criticism"]', 'pub_year': None}, {'book_id': 'bookid_7', 'title': "Child Development: A Practitioner's Guide:2nd (Second) edition", 'details': 'The book, published by Guilford in its second edition in January 2004, is also noted as the 8082nd edition from January 1, 1994. It has a remarkably light item weight of just 0.01 ounces.', 'categories': '["Books", "Parenting & Relationships", "Parenting"]', 'pub_year': None}, {'book_id': 'bookid_8', 'title': 'Make: Electronics: Learning Through Discovery', 'details': 'This book, published by Make Community, LLC, in its second edition on September 22, 2015, is available in English and spans 352 pages in paperback format. It has an ISBN of 9781680450262 for the 10-digit version and 978-1680450262 for the 13-digit version. The content is suitable for readers aged 11 to 17 years. The book weighs 2.91 pounds and its dimensions are 8 inches in width, 0.5 inches in thickness, and 10 inches in height.', 'categories': '["Books", "Engineering & Transportation", "Engineering"]', 'pub_year': None}, {'book_id': 'bookid_9', 'title': 'Reunion: The Children of Lauderdale Park', 'details': 'This book, published independently on September 25, 2019, is written in English and spans 367 pages. It is available in paperback format and has an ISBN-10 of 1694621731 and an ISBN-13 of 978-1694621733. The item weighs 1.38 pounds and measures 6 x 0.92 x 9 inches.', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]', 'pub_year': None}, {'book_id': 'bookid_10', 'title': 'Four Centuries of American Education', 'details': 'This book, published by WallBuilder Press in its first edition on November 8, 2004, is available in English and comprises 51 pages in paperback format. It has an ISBN-10 of 1932225323 and an ISBN-13 of 978-1932225327, with a total item weight of 3.52 ounces.', 'categories': '["Books", "Education & Teaching", "Schools & Teaching"]', 'pub_year': None}], 'num_purchase_ids': 200, 'purchase_id_min': 1, 'purchase_id_max': 200, 'book_id_min': 1, 'book_id_max': 200, 'merged_count': 200, 'merged_unique_books': 200}, 'var_call_LOaDYgPuhsLVKnTvDFYdeGl7': 'file_storage/call_LOaDYgPuhsLVKnTvDFYdeGl7.json'}

exec(code, env_args)
