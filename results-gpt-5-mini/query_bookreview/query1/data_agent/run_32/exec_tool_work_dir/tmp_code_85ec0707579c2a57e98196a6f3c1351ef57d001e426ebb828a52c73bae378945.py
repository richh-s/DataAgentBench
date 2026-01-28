code = """import json, re
import pandas as pd
with open(var_call_uoQBgM6xZLvCULtDUAjY1i45,'r',encoding='utf-8') as f:
    books = json.load(f)
with open(var_call_3TFu4u2EsLD3NZx9UVOjCJLb,'r',encoding='utf-8') as f:
    reviews = json.load(f)

df_books = pd.DataFrame(books)
df_reviews = pd.DataFrame(reviews)

# normalize rating
if 'rating' in df_reviews.columns:
    df_reviews['rating'] = pd.to_numeric(df_reviews['rating'], errors='coerce')
# map ids
df_reviews['book_id'] = df_reviews['purchase_id'].astype(str).str.replace('purchaseid_', 'bookid_', regex=False)

# extract year by finding any 4-digit sequence
def extract_year_all(detail):
    if not isinstance(detail, str):
        return None
    m = re.findall(r"(\d{4})", detail)
    if not m:
        return None
    # pick the most plausible year: any between 1000 and 2099, prefer first that looks like a publication year (>= 1500?)
    for grp in m:
        try:
            y = int(grp)
            if 1000 <= y <= 2099:
                return y
        except:
            continue
    return None

if 'details' in df_books.columns:
    df_books['year'] = df_books['details'].apply(extract_year_all)
else:
    df_books['year'] = None

# merge reviews with books
merged = pd.merge(df_reviews, df_books[['book_id','year']], on='book_id', how='inner')
# keep only rows with valid year and rating
merged = merged[merged['year'].notna() & merged['rating'].notna()].copy()
if merged.empty:
    out = {'decade': None, 'average_rating': None, 'distinct_books_in_decade_with_ratings': None}
    print('__RESULT__:')
    print(json.dumps(out))
else:
    merged['decade_start'] = (merged['year'].astype(int) // 10) * 10
    merged['decade'] = merged['decade_start'].astype(int).astype(str) + 's'
    # per-book mean rating
    book_means = merged.groupby(['book_id','decade']).agg(book_avg_rating=('rating','mean')).reset_index()
    # per-decade aggregate: number of distinct books and mean of book averages
    decade_grp = book_means.groupby('decade').agg(distinct_books=('book_id','nunique'), decade_avg_rating=('book_avg_rating','mean')).reset_index()
    # filter decades with at least 10 distinct books
    decade_filtered = decade_grp[decade_grp['distinct_books'] >= 10].copy()
    if decade_filtered.empty:
        out = {'decade': None, 'average_rating': None, 'distinct_books_in_decade_with_ratings': None}
        print('__RESULT__:')
        print(json.dumps(out))
    else:
        # pick highest average rating; break ties by more books then earliest decade
        decade_filtered = decade_filtered.sort_values(by=['decade_avg_rating','distinct_books','decade'], ascending=[False, False, True]).reset_index(drop=True)
        top = decade_filtered.iloc[0]
        out = {'decade': top['decade'], 'average_rating': round(float(top['decade_avg_rating']),4), 'distinct_books_in_decade_with_ratings': int(top['distinct_books'])}
        print('__RESULT__:')
        print(json.dumps(out))"""

env_args = {'var_call_TmxbjPq0NdaugFpHVwIbt13H': ['books_info'], 'var_call_qtfordLX0oPiqP3bTJAZLsTQ': ['review'], 'var_call_uoQBgM6xZLvCULtDUAjY1i45': 'file_storage/call_uoQBgM6xZLvCULtDUAjY1i45.json', 'var_call_3TFu4u2EsLD3NZx9UVOjCJLb': 'file_storage/call_3TFu4u2EsLD3NZx9UVOjCJLb.json', 'var_call_gbfV8WSCwCdXgmhfDxEEK8nr': {'decade': None, 'average_rating': None, 'distinct_books_in_decade_with_ratings': None}, 'var_call_lpBSqG0FRTwOdTlteXvQtyr1': {'stats': {'num_books_rows': 200, 'num_reviews_rows': 1833, 'num_unique_books_in_books': 200, 'num_unique_books_in_reviews': 200, 'num_books_with_year': 0, 'merged_rows': 1833, 'unique_books_in_merged': 200, 'unique_years_in_merged': []}, 'book_year_counts': [], 'decade_groups': []}, 'var_call_hBruTaN68MYu7K1h23VSTrxB': [{'index': 0, 'book_id': 'bookid_1', 'details_preview': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of', 'year_found': None}, {'index': 1, 'book_id': 'bookid_2', 'details_preview': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN', 'year_found': None}, {'index': 2, 'book_id': 'bookid_3', 'details_preview': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363', 'year_found': None}, {'index': 3, 'book_id': 'bookid_4', 'details_preview': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575', 'year_found': None}, {'index': 4, 'book_id': 'bookid_5', 'details_preview': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it s', 'year_found': None}, {'index': 5, 'book_id': 'bookid_6', 'details_preview': 'This book, published independently on December 30, 2021, is written in English and consists of 24 pages. It has an ISBN 13 of 979-8528537702 and weighs 3.2 ounces. The dimensions of the book are 7 x 0', 'year_found': None}, {'index': 6, 'book_id': 'bookid_7', 'details_preview': 'The book, published by Guilford in its second edition in January 2004, is also noted as the 8082nd edition from January 1, 1994. It has a remarkably light item weight of just 0.01 ounces.', 'year_found': None}, {'index': 7, 'book_id': 'bookid_8', 'details_preview': 'This book, published by Make Community, LLC, in its second edition on September 22, 2015, is available in English and spans 352 pages in paperback format. It has an ISBN of 9781680450262 for the 10-di', 'year_found': None}, {'index': 8, 'book_id': 'bookid_9', 'details_preview': 'This book, published independently on September 25, 2019, is written in English and spans 367 pages. It is available in paperback format and has an ISBN-10 of 1694621731 and an ISBN-13 of 978-16946217', 'year_found': None}, {'index': 9, 'book_id': 'bookid_10', 'details_preview': 'This book, published by WallBuilder Press in its first edition on November 8, 2004, is available in English and comprises 51 pages in paperback format. It has an ISBN-10 of 1932225323 and an ISBN-13 o', 'year_found': None}, {'index': 10, 'book_id': 'bookid_11', 'details_preview': 'Published by Caxton Press on January 1, 1993, this book is available in English and spans 407 pages. It has an ISBN-10 of 0893011673 and an ISBN-13 of 978-0893011673. Weighing 1.51 pounds, the book me', 'year_found': None}, {'index': 11, 'book_id': 'bookid_12', 'details_preview': 'This book, published by Lisette Marshall on May 29, 2022, is written in English and is available in paperback, comprising 215 pages. It has an ISBN 10 number of 9083256898 and an ISBN 13 number of 978', 'year_found': None}, {'index': 12, 'book_id': 'bookid_13', 'details_preview': 'The book, published by Central Avenue Publishing on January 24, 2023, is available in English and comes in paperback format, consisting of 144 pages. It has an ISBN-10 number of 1771682760 and an ISBN', 'year_found': None}, {'index': 13, 'book_id': 'bookid_14', 'details_preview': 'The book, published by Jessica Mathews, LLC on November 13, 2019, is written in English and features a paperback format comprising 26 pages. It has an ISBN-10 of 1087848539 and an ISBN-13 of 978-10878', 'year_found': None}, {'index': 14, 'book_id': 'bookid_15', 'details_preview': 'The book is published by Kegan Paul and is a first edition released on November 15, 2000. It is written in English and is available in hardcover, comprising 348 pages. The ISBN-10 for this edition is ', 'year_found': None}, {'index': 15, 'book_id': 'bookid_16', 'details_preview': 'This book is published by Prentice Hall College Division and is in its third edition, released on January 1, 1997. It is written in English and is available in paperback, consisting of 390 pages. The ', 'year_found': None}, {'index': 16, 'book_id': 'bookid_17', 'details_preview': 'This book, published by Edelsa Grupo Didascalia in a September 1, 1987 edition, is written in Spanish and consists of 44 pages. It has an ISBN-10 number of 8477110190 and an ISBN-13 number of 978-8477', 'year_found': None}, {'index': 17, 'book_id': 'bookid_18', 'details_preview': 'The book, published by Gale, Sabin Americana on February 21, 2012, is written in English and is available in paperback format, comprising 26 pages. It has an ISBN-10 of 1275627234 and an ISBN-13 of 97', 'year_found': None}, {'index': 18, 'book_id': 'bookid_19', 'details_preview': 'The book, published by Foundation Press in its 2013th edition on March 22, 2013, is available in English and spans 355 pages. It has an ISBN-10 number of 1609303687 and an ISBN-13 number of 978-160930', 'year_found': None}, {'index': 19, 'book_id': 'bookid_20', 'details_preview': 'The book, published by Soho Crime in a revised edition on July 1, 2003, is available in English and has a total print length of 372 pages. It has a file size of 2295 KB and supports various features s', 'year_found': None}]}

exec(code, env_args)
