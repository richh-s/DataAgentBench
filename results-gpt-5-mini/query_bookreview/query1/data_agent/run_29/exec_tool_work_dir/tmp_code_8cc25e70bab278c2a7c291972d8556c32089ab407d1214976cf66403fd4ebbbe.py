code = """import json
import pandas as pd
import re

# Load data from storage variables (they may be lists or file paths)
# Variables available: var_call_lNXh3CF221wiuRrQoEfXUgzO (books), var_call_N4RobalkF1OUF98FVqTaLdsK (reviews)

def load_var(v):
    if isinstance(v, str):
        # it's a filepath
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return v

books = load_var(var_call_lNXh3CF221wiuRrQoEfXUgzO)
reviews = load_var(var_call_N4RobalkF1OUF98FVqTaLdsK)

df_books = pd.DataFrame(books)
df_reviews = pd.DataFrame(reviews)

# Normalize ratings
if 'rating' in df_reviews.columns:
    df_reviews['rating'] = pd.to_numeric(df_reviews['rating'], errors='coerce')

# Map purchase_id -> book_id by replacing prefix
if 'purchase_id' in df_reviews.columns:
    df_reviews['book_id'] = df_reviews['purchase_id'].astype(str).str.replace(r'^purchaseid_', 'bookid_', regex=True)

# Extract year from books.details or maybe other fields
def extract_year(s):
    if not isinstance(s, str):
        return None
    # find first 4-digit year between 1000 and 2023
    m = re.search(r'(1[0-9]{3}|20[0-2][0-9]|2023)', s)
    if m:
        try:
            y = int(m.group(0))
            if 1000 <= y <= 2023:
                return y
        except:
            return None
    # if not found, try any 4-digit
    m2 = re.search(r'(\d{4})', s)
    if m2:
        y = int(m2.group(0))
        if 1000 <= y <= 2023:
            return y
    return None

# Apply extraction on details and description and maybe title
df_books['year'] = df_books['details'].fillna('').astype(str).apply(extract_year)
# If no year in details, try description
mask_no_year = df_books['year'].isna()
if mask_no_year.any():
    df_books.loc[mask_no_year, 'year'] = df_books.loc[mask_no_year, 'description'].fillna('').astype(str).apply(extract_year)

# Create decade
def year_to_decade(y):
    if pd.isna(y):
        return None
    try:
        y = int(y)
        decade_start = (y // 10) * 10
        return f"{decade_start}s"
    except:
        return None

df_books['decade'] = df_books['year'].apply(year_to_decade)

# Merge reviews with books on book_id
df_merged = pd.merge(df_reviews, df_books[['book_id', 'year', 'decade']], on='book_id', how='left')

# Keep only rows with valid decade and rating
df_merged = df_merged[df_merged['decade'].notna() & df_merged['rating'].notna()]

# Compute per-book average rating
book_avg = df_merged.groupby(['book_id','decade'], as_index=False)['rating'].mean()
book_avg.rename(columns={'rating':'avg_rating'}, inplace=True)

# For each decade, consider distinct books count and average of book averages
decade_stats = book_avg.groupby('decade').agg(
    books_count = ('book_id','nunique'),
    decade_avg = ('avg_rating','mean')
).reset_index()

# Filter decades with at least 10 distinct books
decade_stats_filtered = decade_stats[decade_stats['books_count'] >= 10]

result_decade = None
if not decade_stats_filtered.empty:
    # get decade with highest decade_avg
    top = decade_stats_filtered.sort_values(['decade_avg','decade'], ascending=[False, True]).iloc[0]
    result_decade = top['decade']

# Prepare output
out = result_decade if result_decade is not None else None
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_LFBnXqciVpmVjotAprHigqAR': ['review'], 'var_call_49RqLyyE8dsXdunNGsPWg8cp': ['books_info'], 'var_call_vTzwoc4DpMxhuW0qJY2Jm5Vf': [{'purchase_id': 'purchaseid_186', 'rating': '4', 'title': 'Ha! On me!  I thought this was a cookbook!', 'review_time': '2012-11-24 18:52:00'}, {'purchase_id': 'purchaseid_191', 'rating': '4', 'title': 'Four Stars', 'review_time': '2015-12-31 13:35:00'}, {'purchase_id': 'purchaseid_190', 'rating': '4', 'title': 'A wonderful adventure in France', 'review_time': '2013-05-05 10:47:00'}, {'purchase_id': 'purchaseid_8', 'rating': '5', 'title': 'Best beginner book.  Been looking for something like this for a long time.', 'review_time': '2020-08-12 11:06:00'}, {'purchase_id': 'purchaseid_178', 'rating': '4', 'title': 'Referance Guide', 'review_time': '2014-11-13 18:55:00'}, {'purchase_id': 'purchaseid_186', 'rating': '4', 'title': 'A Good read for Meat Eaters, and Veggie Heads as well', 'review_time': '2013-02-20 16:09:00'}, {'purchase_id': 'purchaseid_76', 'rating': '5', 'title': 'Greet book', 'review_time': '2020-02-27 05:11:00'}, {'purchase_id': 'purchaseid_186', 'rating': '4', 'title': 'For anyone except avid non-hunters.', 'review_time': '2013-01-06 07:52:00'}, {'purchase_id': 'purchaseid_115', 'rating': '5', 'title': 'Highly recommend this book if you love history of Mid Atlantic wrestling...', 'review_time': '2019-07-24 13:29:00'}, {'purchase_id': 'purchaseid_167', 'rating': '2', 'title': 'Heroine blames others for things & feels her bad behavior is justified', 'review_time': '2020-06-01 07:33:00'}, {'purchase_id': 'purchaseid_188', 'rating': '1', 'title': 'Kindle version listed is not the book offered', 'review_time': '2016-01-25 19:03:00'}, {'purchase_id': 'purchaseid_23', 'rating': '5', 'title': 'Book of Love series', 'review_time': '2021-07-31 18:34:00'}, {'purchase_id': 'purchaseid_196', 'rating': '5', 'title': 'Fascinating Read!', 'review_time': '2013-05-21 13:42:00'}, {'purchase_id': 'purchaseid_196', 'rating': '5', 'title': 'Excellent Merchandise', 'review_time': '2013-02-27 19:49:00'}, {'purchase_id': 'purchaseid_3', 'rating': '5', 'title': 'Five Stars', 'review_time': '2014-10-24 10:52:00'}, {'purchase_id': 'purchaseid_48', 'rating': '5', 'title': 'Adorable book that my daughter has fallen in love with', 'review_time': '2015-11-10 10:51:00'}, {'purchase_id': 'purchaseid_154', 'rating': '3', 'title': 'Good story', 'review_time': '2018-09-04 11:04:00'}, {'purchase_id': 'purchaseid_99', 'rating': '2', 'title': 'Overpriced for the size', 'review_time': '2021-01-27 07:08:00'}, {'purchase_id': 'purchaseid_190', 'rating': '5', 'title': "An insider's view///", 'review_time': '2013-02-05 06:53:00'}, {'purchase_id': 'purchaseid_3', 'rating': '5', 'title': 'Service:', 'review_time': '2013-02-18 04:04:00'}, {'purchase_id': 'purchaseid_169', 'rating': '5', 'title': 'Great shape and good condition', 'review_time': '2014-07-12 19:16:00'}, {'purchase_id': 'purchaseid_3', 'rating': '5', 'title': 'Five Stars', 'review_time': '2015-03-07 04:30:00'}, {'purchase_id': 'purchaseid_145', 'rating': '5', 'title': 'but they made a little girl happy on her birthday', 'review_time': '2015-12-18 05:07:00'}, {'purchase_id': 'purchaseid_194', 'rating': '4', 'title': 'A real eye opener.', 'review_time': '2017-08-24 14:29:00'}, {'purchase_id': 'purchaseid_81', 'rating': '5', 'title': 'Fast shipping', 'review_time': '2018-12-19 14:40:00'}, {'purchase_id': 'purchaseid_199', 'rating': '1', 'title': 'Falsedades y mentiras del totalitarismo cubano', 'review_time': '2019-09-09 10:16:00'}, {'purchase_id': 'purchaseid_48', 'rating': '5', 'title': 'Five Stars', 'review_time': '2016-03-10 20:11:00'}, {'purchase_id': 'purchaseid_96', 'rating': '5', 'title': 'Adorable', 'review_time': '2018-12-22 04:31:00'}, {'purchase_id': 'purchaseid_167', 'rating': '4', 'title': 'Murder, Kidnapping, and Prayers', 'review_time': '2020-06-14 11:52:00'}, {'purchase_id': 'purchaseid_196', 'rating': '5', 'title': 'Amazing and true', 'review_time': '2019-04-27 18:20:00'}, {'purchase_id': 'purchaseid_196', 'rating': '5', 'title': 'Wonderful book', 'review_time': '2019-03-27 13:46:00'}, {'purchase_id': 'purchaseid_196', 'rating': '4', 'title': 'Powerful and Compelling with a Couple Flaws - Thus Thoroughly Human!', 'review_time': '2017-02-08 09:44:00'}, {'purchase_id': 'purchaseid_148', 'rating': '5', 'title': 'Winning in Fatherhood', 'review_time': '2012-06-25 09:52:00'}, {'purchase_id': 'purchaseid_8', 'rating': '5', 'title': 'Excellent !', 'review_time': '2017-03-13 20:33:04'}, {'purchase_id': 'purchaseid_145', 'rating': '5', 'title': 'Five Stars', 'review_time': '2016-08-06 10:31:00'}, {'purchase_id': 'purchaseid_200', 'rating': '5', 'title': 'DEAR COLEMAN...PLEASE PUBLISH A NEW EDITION...THIS DIRECTORY IS GREAT!!', 'review_time': '2015-11-28 11:40:00'}, {'purchase_id': 'purchaseid_8', 'rating': '5', 'title': 'This is a great book for learning entry-level electronics', 'review_time': '2017-11-07 10:11:54'}, {'purchase_id': 'purchaseid_178', 'rating': '1', 'title': 'One Star', 'review_time': '2015-06-27 14:34:00'}, {'purchase_id': 'purchaseid_20', 'rating': '5', 'title': 'A Most Entertaining and enjoyable book.', 'review_time': '2021-10-31 19:46:00'}, {'purchase_id': 'purchaseid_52', 'rating': '5', 'title': 'Very Good Well Written', 'review_time': '2019-12-05 14:52:00'}, {'purchase_id': 'purchaseid_159', 'rating': '2', 'title': 'It is too expensive for the people to be able to read it.', 'review_time': '2018-04-28 14:09:00'}, {'purchase_id': 'purchaseid_83', 'rating': '5', 'title': 'Gift Recipient LOVES this book', 'review_time': '2021-06-22 12:04:00'}, {'purchase_id': 'purchaseid_67', 'rating': '3', 'title': 'Rare Pics', 'review_time': '2021-02-10 16:28:00'}, {'purchase_id': 'purchaseid_3', 'rating': '5', 'title': 'Five Stars', 'review_time': '2017-02-02 06:42:00'}, {'purchase_id': 'purchaseid_58', 'rating': '4', 'title': 'Four Stars', 'review_time': '2018-04-21 01:04:00'}, {'purchase_id': 'purchaseid_196', 'rating': '4', 'title': 'an important read', 'review_time': '2014-05-28 09:10:00'}, {'purchase_id': 'purchaseid_95', 'rating': '5', 'title': 'Book', 'review_time': '2019-08-02 19:18:00'}, {'purchase_id': 'purchaseid_76', 'rating': '5', 'title': 'Five Stars', 'review_time': '2015-01-09 10:37:00'}, {'purchase_id': 'purchaseid_3', 'rating': '3', 'title': 'Not my type of book', 'review_time': '2012-08-09 07:16:00'}, {'purchase_id': 'purchaseid_62', 'rating': '5', 'title': 'Great how to book for the beginner and advanced photographers', 'review_time': '2020-04-16 04:41:00'}], 'var_call_lNXh3CF221wiuRrQoEfXUgzO': 'file_storage/call_lNXh3CF221wiuRrQoEfXUgzO.json', 'var_call_N4RobalkF1OUF98FVqTaLdsK': 'file_storage/call_N4RobalkF1OUF98FVqTaLdsK.json'}

exec(code, env_args)
