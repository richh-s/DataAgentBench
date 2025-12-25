code = """import json, re, pandas as pd

# Load full review data
with open(var_call_HVbc9Ommixd3LjEzm7Gub1CT, 'r') as f:
    reviews = json.load(f)

# Load full books data
with open(var_call_D2DwWRhZSS5tIAU2HRxFisPJ, 'r') as f:
    books = json.load(f)

# Build mapping from purchase_id to decade using exact join to book_id
# Extract year from details text
year_pattern = re.compile(r'(19|20)\d{2}')
book_years = {}
for b in books:
    details = b.get('details') or ''
    m = year_pattern.search(details)
    if not m:
        continue
    year = int(m.group(0))
    decade = (year // 10) * 10
    book_years[b['book_id'].replace('bookid_', 'purchaseid_')] = decade

# Aggregate ratings per book (purchase_id)
book_ratings = {}
for r in reviews:
    pid = r['purchase_id']
    if pid not in book_years:
        continue
    rating = float(r['rating'])
    book_ratings.setdefault(pid, []).append(rating)

# Compute per-book average and decade
records = []
for pid, rs in book_ratings.items():
    decade = book_years.get(pid)
    if decade is None:
        continue
    avg_rating = sum(rs)/len(rs)
    records.append({'purchase_id': pid, 'decade': decade, 'avg_rating': avg_rating})

if not records:
    result = None
else:
    df = pd.DataFrame(records)
    # Count distinct books per decade
    counts = df.groupby('decade')['purchase_id'].nunique()
    valid_decades = counts[counts >= 10].index
    if len(valid_decades) == 0:
        result = None
    else:
        df_valid = df[df['decade'].isin(valid_decades)]
        decade_avg = df_valid.groupby('decade')['avg_rating'].mean()
        best_decade = decade_avg.idxmax()
        result = f"{best_decade}s"

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_M2FPatJmFNbQKh8iOELxyuFP': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'var_call_4pRXIWrsbTXGvYQ5I2gxW7j5': ['review'], 'var_call_HVbc9Ommixd3LjEzm7Gub1CT': 'file_storage/call_HVbc9Ommixd3LjEzm7Gub1CT.json', 'var_call_D2DwWRhZSS5tIAU2HRxFisPJ': 'file_storage/call_D2DwWRhZSS5tIAU2HRxFisPJ.json'}

exec(code, env_args)
