code = """import json
import re

# Access file paths from local variables
books_file = locals()['var_function-call-16964057040556250204']
reviews_file = locals()['var_function-call-970376804958453031']

with open(books_file, 'r') as f:
    books_data = json.load(f)

with open(reviews_file, 'r') as f:
    reviews_data = json.load(f)

# Helper to extract ID number
def get_id_num(s):
    # s is like "bookid_1" or "purchaseid_186"
    m = re.search(r'(\d+)$', s)
    if m:
        return int(m.group(1))
    return None

# Extract years from books
month_pattern = r'(?:January|February|March|April|May|June|July|August|September|October|November|December)'
date_pattern_1 = re.compile(rf'{month_pattern}\s+\d{{1,2}},?\s+(\d{{4}})')
date_pattern_2 = re.compile(rf'{month_pattern}\s+(\d{{4}})')

book_years = {}

for b in books_data:
    bid_num = get_id_num(b['book_id'])
    details = b.get('details', '')
    
    if bid_num is None:
        continue
        
    year = None
    m1 = date_pattern_1.search(details)
    if m1:
        year = int(m1.group(1))
    else:
        m2 = date_pattern_2.search(details)
        if m2:
            year = int(m2.group(1))
            
    if year:
        book_years[bid_num] = year

# Process Reviews
decade_stats = {} 

for r in reviews_data:
    pid_num = get_id_num(r['purchase_id'])
    if pid_num is None:
        continue
    
    if pid_num in book_years:
        year = book_years[pid_num]
        decade = (year // 10) * 10
        decade_str = f"{decade}s"
        
        if decade_str not in decade_stats:
            decade_stats[decade_str] = {'ratings': [], 'book_ids': set()}
        
        try:
            rating = float(r['rating'])
            decade_stats[decade_str]['ratings'].append(rating)
            decade_stats[decade_str]['book_ids'].add(pid_num)
        except ValueError:
            pass

# Analyze results
results = []
for decade, stats in decade_stats.items():
    num_books = len(stats['book_ids'])
    if num_books >= 10:
        avg_rating = sum(stats['ratings']) / len(stats['ratings'])
        results.append({
            'decade': decade,
            'avg_rating': avg_rating,
            'num_books': num_books
        })

# Sort by avg rating descending
results.sort(key=lambda x: x['avg_rating'], reverse=True)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-4226735740055498788': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'var_function-call-1830573000602717874': [{'count': '200'}], 'var_function-call-1827365578464884817': ['review'], 'var_function-call-601489560405955251': [{'COUNT(*)': '1833'}], 'var_function-call-16964057040556250204': 'file_storage/function-call-16964057040556250204.json', 'var_function-call-970376804958453031': 'file_storage/function-call-970376804958453031.json'}

exec(code, env_args)
