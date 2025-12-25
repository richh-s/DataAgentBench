code = """import json, re, pandas as pd

# Load full results from files
with open(var_call_SlzEIRv3C3ReLz2m9DRwahOW, 'r') as f:
    books = json.load(f)
with open(var_call_q4iI8hR8Emf9RFkQNRXxHufq, 'r') as f:
    reviews = json.load(f)

books_df = pd.DataFrame(books)
reviews_df = pd.DataFrame(reviews)

# extract year from details using regex like 'on <Month> <d>, <yyyy>' or 'on January 1, 2004' or 'on 2004'
year_pattern = re.compile(r'(19|20)\d{2}')

books_df['year'] = books_df['details'].apply(lambda x: int(year_pattern.search(x).group()) if isinstance(x,str) and year_pattern.search(x) else None)

# compute decade label, e.g. 1980s
books_df['decade'] = books_df['year'].apply(lambda y: f"{int(y//10*10)}s" if pd.notnull(y) else None)

# join reviews with books on purchase_id == book_id (exact, not fuzzy, since ids look aligned)
merged = reviews_df.merge(books_df[['book_id','decade']], left_on='purchase_id', right_on='book_id', how='inner')

# coerce rating to float
merged['rating'] = merged['rating'].astype(float)

# aggregate: per book_id and decade, average rating (book-level), then per decade average across distinct books
book_decade_avg = merged.groupby(['book_id','decade'])['rating'].mean().reset_index(name='book_avg_rating')

# filter decades with at least 10 distinct books
decade_counts = book_decade_avg.groupby('decade')['book_id'].nunique().reset_index(name='n_books')
eligible_decades = decade_counts[decade_counts['n_books']>=10]['decade']

eligible_book_avgs = book_decade_avg[book_decade_avg['decade'].isin(eligible_decades)]

decade_avg = eligible_book_avgs.groupby('decade')['book_avg_rating'].mean().reset_index(name='decade_avg_rating')

# get decade with highest average rating
if len(decade_avg)==0:
    result = None
else:
    top_row = decade_avg.sort_values(['decade_avg_rating','decade'], ascending=[False, True]).iloc[0]
    result = top_row['decade']

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_SlzEIRv3C3ReLz2m9DRwahOW': 'file_storage/call_SlzEIRv3C3ReLz2m9DRwahOW.json', 'var_call_VMknwabqSF1edSVWblH0nloU': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'var_call_MErw9QT1ku4PRTcwnh8e1qvu': ['review'], 'var_call_q4iI8hR8Emf9RFkQNRXxHufq': 'file_storage/call_q4iI8hR8Emf9RFkQNRXxHufq.json'}

exec(code, env_args)
