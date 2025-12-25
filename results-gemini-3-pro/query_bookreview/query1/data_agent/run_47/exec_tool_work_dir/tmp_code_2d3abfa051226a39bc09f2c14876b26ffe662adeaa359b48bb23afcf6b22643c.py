code = """import json
import re
import pandas as pd

# Load data
with open('var_function-call-7229594273416415337.json', 'r') as f:
    books = json.load(f)

with open('var_function-call-18367235769688117238.json', 'r') as f:
    reviews = json.load(f)

# Helper to normalize ID
def get_id(s):
    # s is like "bookid_1" or "purchaseid_186"
    # Extract the number
    m = re.search(r'(\d+)$', s)
    if m:
        return int(m.group(1))
    return None

# Process books
book_data = []
for b in books:
    bid = get_id(b['book_id'])
    details = b['details']
    # Extract year: look for 4 digits 19xx or 20xx
    # Regex: \b(19\d{2}|20\d{2})\b
    # There might be multiple years. Usually the first one is publication.
    years = re.findall(r'\b(19\d{2}|20\d{2})\b', details)
    year = None
    if years:
        # Convert to ints and pick the one that seems to be publication year.
        # Often the first one.
        year = int(years[0])
    
    if bid is not None and year is not None:
        book_data.append({'id': bid, 'year': year})

df_books = pd.DataFrame(book_data)

# Process reviews
review_data = []
for r in reviews:
    pid = get_id(r['purchase_id'])
    if pid is not None:
        try:
            rating = float(r['rating'])
            review_data.append({'id': pid, 'rating': rating})
        except:
            pass

df_reviews = pd.DataFrame(review_data)

# Calculate average rating per book
book_stats = df_reviews.groupby('id')['rating'].agg(['mean', 'count']).reset_index()
book_stats.rename(columns={'mean': 'avg_rating', 'count': 'num_reviews'}, inplace=True)

# Merge
merged = pd.merge(df_books, book_stats, on='id', how='inner') # Inner join: only books with ratings

# Add decade
merged['decade'] = (merged['year'] // 10) * 10

# Group by decade
decade_stats = merged.groupby('decade').agg(
    num_books=('id', 'count'), # count distinct books (ids are unique in df_books? yes, usually)
    avg_rating_decade=('avg_rating', 'mean')
).reset_index()

# Filter decades with >= 10 books
filtered_decades = decade_stats[decade_stats['num_books'] >= 10].copy()

# Sort by avg rating
result = filtered_decades.sort_values(by='avg_rating_decade', ascending=False)

print("__RESULT__:")
print(result.to_json(orient='records'))"""

env_args = {'var_function-call-5381900575935500103': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'var_function-call-1146212370315976145': [{'count': '200'}], 'var_function-call-17812567415089105343': ['review'], 'var_function-call-8183095380455942288': [{'count(*)': '1833'}], 'var_function-call-7229594273416415337': 'file_storage/function-call-7229594273416415337.json', 'var_function-call-18367235769688117238': 'file_storage/function-call-18367235769688117238.json'}

exec(code, env_args)
