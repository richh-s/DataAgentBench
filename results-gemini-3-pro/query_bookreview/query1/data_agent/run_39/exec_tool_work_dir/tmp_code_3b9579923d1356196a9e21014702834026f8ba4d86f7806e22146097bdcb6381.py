code = """import json
import re
import pandas as pd

# Load ratings
with open(locals()['var_function-call-5178717517229536386'], 'r') as f:
    ratings_data = json.load(f)

# Load books
with open(locals()['var_function-call-12618321796913413905'], 'r') as f:
    books_data = json.load(f)

# Convert ratings to dict: purchase_id -> avg_rating
# Normalize purchase_id: "purchaseid_1" -> "1"
rating_map = {}
for r in ratings_data:
    pid = r['purchase_id']
    if not pid: continue
    # extract number
    m = re.search(r'(\d+)$', pid)
    if m:
        key = m.group(1)
        rating_map[key] = float(r['avg_rating'])

# Process books
book_years = []
year_regex = re.compile(r'(?:published|released).*?(\d{4})', re.IGNORECASE)

for b in books_data:
    bid = b['book_id']
    details = b['details']
    
    # extract number from book_id
    m_id = re.search(r'(\d+)$', bid)
    if not m_id:
        continue
    key = m_id.group(1)
    
    if key in rating_map:
        # Extract year
        if details:
            # Clean details to avoid newlines breaking regex sometimes?
            # Standard regex works on multiline if not using dot matches newline, but here . matches everything except newline. 
            # Details seem to be single strings.
            m_year = year_regex.search(details)
            if m_year:
                year = int(m_year.group(1))
                # Reasonable year check
                if 1900 <= year <= 2024:
                    book_years.append({
                        'year': year,
                        'rating': rating_map[key],
                        'book_id': bid
                    })

# Create DataFrame
df = pd.DataFrame(book_years)

if df.empty:
    print('__RESULT__:')
    print(json.dumps("No data found"))
else:
    # Assign decade
    df['decade'] = (df['year'] // 10) * 10
    
    # Group by decade
    decade_stats = df.groupby('decade').agg(
        avg_rating=('rating', 'mean'),
        book_count=('book_id', 'nunique')
    ).reset_index()
    
    # Filter >= 10 books
    filtered = decade_stats[decade_stats['book_count'] >= 10]
    
    # Find max avg_rating
    if filtered.empty:
         print('__RESULT__:')
         print(json.dumps("No decade with >= 10 books"))
    else:
        best = filtered.loc[filtered['avg_rating'].idxmax()]
        result_decade = str(int(best['decade'])) + 's'
        print('__RESULT__:')
        print(json.dumps(result_decade))"""

env_args = {'var_function-call-940676870274130036': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'var_function-call-9231060360200983024': ['review'], 'var_function-call-5178717517229536386': 'file_storage/function-call-5178717517229536386.json', 'var_function-call-12618321796913413905': 'file_storage/function-call-12618321796913413905.json'}

exec(code, env_args)
