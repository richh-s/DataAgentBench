code = """import json
import re

# Load data
with open(locals()['var_function-call-11592929828767818440'], 'r') as f:
    books = json.load(f)

with open(locals()['var_function-call-8472064431398200047'], 'r') as f:
    reviews = json.load(f)

# Regex for date: Month (DD, )? YYYY
# Matches: "January 1, 2004", "May 20, 1996", "January 2004"
date_pattern = re.compile(r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+(?:\d{1,2},?\s+)?(\d{4})')

book_decade = {}

for b in books:
    # Parse book_id: "bookid_1" -> 1
    bid_str = b.get('book_id')
    if not bid_str:
        continue
    try:
        bid_num = int(bid_str.split('_')[1])
    except IndexError:
        continue
        
    details = b.get('details')
    if not details:
        continue
        
    # Find year
    match = date_pattern.search(details)
    if match:
        year = int(match.group(1))
        # Determine decade
        decade = (year // 10) * 10
        decade_str = f"{decade}s"
        book_decade[bid_num] = decade_str

# Process reviews
decade_stats = {} # decade -> {'total_rating': 0, 'count': 0, 'book_ids': set()}

for r in reviews:
    pid_str = r.get('purchase_id')
    if not pid_str:
        continue
    try:
        pid_num = int(pid_str.split('_')[1])
    except IndexError:
        continue
        
    rating_val = r.get('rating')
    if rating_val is None:
        continue
    rating = float(rating_val)
    
    if pid_num in book_decade:
        dec = book_decade[pid_num]
        if dec not in decade_stats:
            decade_stats[dec] = {'total_rating': 0.0, 'count': 0, 'book_ids': set()}
            
        decade_stats[dec]['total_rating'] += rating
        decade_stats[dec]['count'] += 1
        decade_stats[dec]['book_ids'].add(pid_num)

# Find result
best_decade = None
highest_avg = -1.0

results_debug = []

for dec, stats in decade_stats.items():
    unique_books = len(stats['book_ids'])
    if unique_books >= 10:
        avg_rating = stats['total_rating'] / stats['count']
        results_debug.append((dec, avg_rating, unique_books))
        if avg_rating > highest_avg:
            highest_avg = avg_rating
            best_decade = dec

print("__RESULT__:")
print(json.dumps(best_decade))"""

env_args = {'var_function-call-12709362354578298012': ['books_info'], 'var_function-call-808595993560139342': ['review'], 'var_function-call-9566370790292574227': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'var_function-call-16423280322374248516': [{'purchase_id': 'purchaseid_186', 'rating': '4'}, {'purchase_id': 'purchaseid_191', 'rating': '4'}, {'purchase_id': 'purchaseid_190', 'rating': '4'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '4'}], 'var_function-call-2578811916176776378': [{'Count(*)': '1833'}], 'var_function-call-11389927933067722346': [{'count': '200'}], 'var_function-call-11592929828767818440': 'file_storage/function-call-11592929828767818440.json', 'var_function-call-8472064431398200047': 'file_storage/function-call-8472064431398200047.json'}

exec(code, env_args)
