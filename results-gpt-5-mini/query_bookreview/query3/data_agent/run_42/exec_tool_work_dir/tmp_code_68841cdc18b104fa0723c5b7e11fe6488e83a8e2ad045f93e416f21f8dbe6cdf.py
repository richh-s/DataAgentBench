code = """import json
import pandas as pd
import re

with open(var_call_bmIgUAXKjX8yjxSfPgATyeTy, 'r') as f:
    reviews = json.load(f)
with open(var_call_PqDutk8xXQUKu7IuHjYHFlrN, 'r') as f:
    books = json.load(f)

# DataFrames
df_r = pd.DataFrame(reviews)
df_b = pd.DataFrame(books)

# Clean ratings and times
if 'rating' in df_r.columns:
    df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
else:
    df_r['rating'] = pd.Series(dtype=float)
if 'review_time' in df_r.columns:
    df_r['review_time'] = pd.to_datetime(df_r['review_time'], errors='coerce')
else:
    df_r['review_time'] = pd.Series(pd.NaT)

# Filter reviews from 2020 onwards
df_r = df_r[df_r['review_time'] >= pd.Timestamp('2020-01-01')].copy()

# Map purchase_id to book_id
def to_bookid(pid):
    if pd.isna(pid):
        return None
    m = re.search(r"(\d+)", str(pid))
    if m:
        return 'bookid_' + m.group(1)
    return None

if 'purchase_id' in df_r.columns:
    df_r['book_id'] = df_r['purchase_id'].apply(to_bookid)
else:
    df_r['book_id'] = None

# Drop rows without book_id or rating
df_r = df_r.dropna(subset=['book_id', 'rating'])

# Aggregate average rating per book_id
if not df_r.empty:
    agg = df_r.groupby('book_id').agg(avg_rating=('rating', 'mean'), review_count=('rating', 'count')).reset_index()
    agg['avg_rating'] = agg['avg_rating'].round(3)
else:
    agg = pd.DataFrame(columns=['book_id', 'avg_rating', 'review_count'])

# Identify children's books in df_b
if 'categories' in df_b.columns:
    df_b['is_children'] = df_b['categories'].astype(str).str.contains("Children's Books", na=False)
else:
    df_b['is_children'] = False
children_books = df_b[df_b['is_children']].copy()

# Join agg with children_books on book_id
res = pd.merge(agg, children_books[['book_id', 'title']], on='book_id', how='inner')

# Filter avg_rating >= 4.5
res = res[res['avg_rating'] >= 4.5].sort_values(['avg_rating', 'review_count'], ascending=[False, False])

result = res[['book_id', 'title', 'avg_rating', 'review_count']].to_dict(orient='records')

# Ensure types JSON serializable
for r in result:
    r['avg_rating'] = float(r['avg_rating'])
    r['review_count'] = int(r['review_count'])

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_V4Ay7XT6DZjxMcFI1xYIrbr3': ['review'], 'var_call_xjSOnwYTFge2cGaFGNaZqfAm': ['books_info'], 'var_call_bmIgUAXKjX8yjxSfPgATyeTy': 'file_storage/call_bmIgUAXKjX8yjxSfPgATyeTy.json', 'var_call_PqDutk8xXQUKu7IuHjYHFlrN': 'file_storage/call_PqDutk8xXQUKu7IuHjYHFlrN.json', 'var_call_1xNuphlCke72czMqZ5Vtt7iF': {'review_columns': ['purchase_id', 'rating', 'review_time', 'title'], 'books_columns': ['book_id', 'title', 'categories', 'details'], 'review_len': 100, 'books_len': 200, 'review_head': [{'purchase_id': 'purchaseid_186', 'rating': '4', 'review_time': '2012-11-24 18:52:00', 'title': 'Ha! On me!  I thought this was a cookbook!'}, {'purchase_id': 'purchaseid_191', 'rating': '4', 'review_time': '2015-12-31 13:35:00', 'title': 'Four Stars'}, {'purchase_id': 'purchaseid_190', 'rating': '4', 'review_time': '2013-05-05 10:47:00', 'title': 'A wonderful adventure in France'}], 'books_head': [{'book_id': 'bookid_1', 'title': 'Chaucer', 'categories': '["Books", "Literature & Fiction", "History & Criticism"]', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'title': 'Notes from a Kidwatcher', 'categories': '["Books", "Reference", "Words, Language & Grammar"]', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'title': 'Service: A Navy SEAL at War', 'categories': '["Books", "Biographies & Memoirs", "Leaders & Notable People"]', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}]}, 'var_call_grbz42XNAWTdWlTzAP9gLFwr': {'df_r_columns': ['purchase_id', 'rating', 'review_time', 'title'], 'df_b_columns': ['book_id', 'title', 'categories', 'details'], 'df_r_sample': [{'purchase_id': 'purchaseid_186', 'rating': '4', 'review_time': '2012-11-24 18:52:00', 'title': 'Ha! On me!  I thought this was a cookbook!'}, {'purchase_id': 'purchaseid_191', 'rating': '4', 'review_time': '2015-12-31 13:35:00', 'title': 'Four Stars'}, {'purchase_id': 'purchaseid_190', 'rating': '4', 'review_time': '2013-05-05 10:47:00', 'title': 'A wonderful adventure in France'}, {'purchase_id': 'purchaseid_8', 'rating': '5', 'review_time': '2020-08-12 11:06:00', 'title': 'Best beginner book.  Been looking for something like this for a long time.'}, {'purchase_id': 'purchaseid_178', 'rating': '4', 'review_time': '2014-11-13 18:55:00', 'title': 'Referance Guide'}], 'df_b_sample': [{'book_id': 'bookid_1', 'title': 'Chaucer', 'categories': '["Books", "Literature & Fiction", "History & Criticism"]', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'title': 'Notes from a Kidwatcher', 'categories': '["Books", "Reference", "Words, Language & Grammar"]', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'title': 'Service: A Navy SEAL at War', 'categories': '["Books", "Biographies & Memoirs", "Leaders & Notable People"]', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'title': 'Parker & Knight', 'categories': '["Books", "Mystery, Thriller & Suspense", "Thrillers & Suspense"]', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'mapped_bookids_sample': [{'purchase_id': 'purchaseid_186', 'book_id': 'bookid_186'}, {'purchase_id': 'purchaseid_191', 'book_id': 'bookid_191'}, {'purchase_id': 'purchaseid_190', 'book_id': 'bookid_190'}, {'purchase_id': 'purchaseid_8', 'book_id': 'bookid_8'}, {'purchase_id': 'purchaseid_178', 'book_id': 'bookid_178'}, {'purchase_id': 'purchaseid_186', 'book_id': 'bookid_186'}, {'purchase_id': 'purchaseid_76', 'book_id': 'bookid_76'}, {'purchase_id': 'purchaseid_186', 'book_id': 'bookid_186'}, {'purchase_id': 'purchaseid_115', 'book_id': 'bookid_115'}, {'purchase_id': 'purchaseid_167', 'book_id': 'bookid_167'}, {'purchase_id': 'purchaseid_188', 'book_id': 'bookid_188'}, {'purchase_id': 'purchaseid_23', 'book_id': 'bookid_23'}, {'purchase_id': 'purchaseid_196', 'book_id': 'bookid_196'}, {'purchase_id': 'purchaseid_196', 'book_id': 'bookid_196'}, {'purchase_id': 'purchaseid_3', 'book_id': 'bookid_3'}, {'purchase_id': 'purchaseid_48', 'book_id': 'bookid_48'}, {'purchase_id': 'purchaseid_154', 'book_id': 'bookid_154'}, {'purchase_id': 'purchaseid_99', 'book_id': 'bookid_99'}, {'purchase_id': 'purchaseid_190', 'book_id': 'bookid_190'}, {'purchase_id': 'purchaseid_3', 'book_id': 'bookid_3'}], 'children_count': 25, 'children_sample': [{'book_id': 'bookid_4', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.', 'is_children': True}, {'book_id': 'bookid_14', 'title': 'The Old Man and the Pirate Princess', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]', 'details': 'The book, published by Jessica Mathews, LLC on November 13, 2019, is written in English and features a paperback format comprising 26 pages. It has an ISBN-10 of 1087848539 and an ISBN-13 of 978-1087848532. Suitable for readers aged 3 to 8 years, it is appropriate for students in Kindergarten through 3rd grade. The item weighs 3.03 ounces and has dimensions of 8.5 x 0.05 x 11 inches.', 'is_children': True}, {'book_id': 'bookid_32', 'title': 'The Very Hungry Caterpillar (English and Arabic Edition)', 'categories': '["Books", "Children\'s Books", "Early Learning"]', 'details': 'This book, published by Mantra Lingua / Tsai Fong on January 1, 1998, is available in both English and Arabic. It has an ISBN of 1852691247 for the 10-digit version and 978-1852691240 for the 13-digit version. Suitable for children aged 2 to 4 years, the book weighs 4.3 ounces and has dimensions of 10.75 x 0.25 x 7.25 inches.', 'is_children': True}, {'book_id': 'bookid_40', 'title': 'Egypt (Enchantment of the World)', 'categories': '["Books", "Children\'s Books", "Geography & Cultures"]', 'details': "Published by Children's Press in a library edition on January 11, 2012, this book is available in English and features a hardcover format with a total of 144 pages. It has an ISBN-10 of 9780531253090 and an ISBN-13 of 978-0531253090. The reading age for this book is targeted at children between 10 to 14 years, with a Lexile measure of 940L, making it suitable for students in grades 5 to 9. The book weighs 1.2 pounds and has dimensions of 8.25 by 0.5 by 9.5 inches.", 'is_children': True}, {'book_id': 'bookid_48', 'title': 'Clark the Shark: Tooth Trouble, No. 1', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]', 'details': 'This illustrated edition of the book, published by HarperCollins on December 30, 2014, is available in English and features a total of 32 pages. It is suitable for children aged 4 to 8 years, with a grade level ranging from preschool to 3. The book has an item weight of 2.82 ounces and its dimensions are 6 inches in width, 0.12 inches in thickness, and 9 inches in height. The ISBN numbers for this edition are 9780062279064 (ISBN 10) and 978-0062279064 (ISBN 13).', 'is_children': True}], 'children_has_title': True, 'children_columns': ['book_id', 'title', 'categories', 'details', 'is_children']}}

exec(code, env_args)
