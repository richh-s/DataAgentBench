code = """# Step 1: Get the file paths from storage
books_key = 'var_functions.query_db:42'
reviews_key = 'var_functions.query_db:30'

# Check what's available
import json, re
from collections import defaultdict
books_file = books_key
reviews_file = reviews_key

# Load books data
with open(books_file, 'r') as f:
    books_data = json.load(f)

# Load reviews data  
with open(reviews_file, 'r') as f:
    reviews_data = json.load(f)

print(f"Loaded {len(books_data)} books and {len(reviews_data)} reviews")

# Extract publication years from book details
book_years = {}
for book in books_data:
    book_id = book['book_id']
    details = book.get('details', '')
    
    # Try to find publication year using regex patterns
    publication_year = None
    patterns = [
        r'published[^\d]*(\d{4})',
        r'released[^\d]*(\d{4})', 
        r'(?:January|February|March|April|May|June|July|August|September|October|November|December)[^\d]*(\d{4})',
        r'(\d{4})'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, details, re.IGNORECASE)
        if match:
            year = int(match.group(1))
            if 1900 <= year <= 2023:  # Valid publication year range
                publication_year = year
                break
    
    if publication_year:
        book_years[book_id] = publication_year

print(f"Found publication years for {len(book_years)} books")

# Group ratings by book
book_ratings = defaultdict(list)
for review in reviews_data:
    book_id = review['purchase_id']
    try:
        rating = float(review['rating'])
        book_ratings[book_id].append(rating)
    except (ValueError, TypeError):
        continue

print(f"Found ratings for {len(book_ratings)} books")

# Calculate decade statistics
decade_stats = defaultdict(lambda: {'total_rating': 0, 'num_reviews': 0, 'books': set()})

for book_id, year in sorted(book_years.items())[:20]:
    print(f"DEBUG: {book_id} -> {year}")

for book_id, year in book_years.items():
    if book_id in book_ratings:
        decade = (year // 10) * 10
        decade_stats[decade]['total_rating'] += sum(book_ratings[book_id])
        decade_stats[decade]['num_reviews'] += len(book_ratings[book_id])
        decade_stats[decade]['books'].add(book_id)

# Calculate averages and filter for decades with at least 10 books
decade_results = []
for decade, stats in sorted(decade_stats.items(), key=lambda x: x[0]):
    num_books = len(stats['books'])
    num_reviews = stats['num_reviews']
    if num_books >= 3:  # Lower threshold for debugging
        avg_rating = stats['total_rating'] / num_reviews if num_reviews > 0 else 0
        decade_results.append({
            'decade': decade,
            'average_rating': round(avg_rating, 3),
            'num_books': num_books,
            'num_reviews': num_reviews
        })

# Sort by average rating descending
decade_results.sort(key=lambda x: x['average_rating'], reverse=True)

print(f"\nTop decades:")
for result in decade_results[:10]:
    print(f"{result['decade']}s: Avg={result['average_rating']}, Books={result['num_books']}, Reviews={result['num_reviews']}")

# Prepare JSON result
result_json = json.dumps(decade_results, indent=2)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['books_info'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}, {'book_id': 'bookid_6', 'details': 'This book, published independently on December 30, 2021, is written in English and consists of 24 pages. It has an ISBN 13 of 979-8528537702 and weighs 3.2 ounces. The dimensions of the book are 7 x 0.06 x 9 inches.'}, {'book_id': 'bookid_7', 'details': 'The book, published by Guilford in its second edition in January 2004, is also noted as the 8082nd edition from January 1, 1994. It has a remarkably light item weight of just 0.01 ounces.'}, {'book_id': 'bookid_8', 'details': 'This book, published by Make Community, LLC, in its second edition on September 22, 2015, is available in English and spans 352 pages in paperback format. It has an ISBN of 9781680450262 for the 10-digit version and 978-1680450262 for the 13-digit version. The content is suitable for readers aged 11 to 17 years. The book weighs 2.91 pounds and its dimensions are 8 inches in width, 0.5 inches in thickness, and 10 inches in height.'}, {'book_id': 'bookid_9', 'details': 'This book, published independently on September 25, 2019, is written in English and spans 367 pages. It is available in paperback format and has an ISBN-10 of 1694621731 and an ISBN-13 of 978-1694621733. The item weighs 1.38 pounds and measures 6 x 0.92 x 9 inches.'}, {'book_id': 'bookid_10', 'details': 'This book, published by WallBuilder Press in its first edition on November 8, 2004, is available in English and comprises 51 pages in paperback format. It has an ISBN-10 of 1932225323 and an ISBN-13 of 978-1932225327, with a total item weight of 3.52 ounces.'}, {'book_id': 'bookid_12', 'details': 'This book, published by Lisette Marshall on May 29, 2022, is written in English and is available in paperback, comprising 215 pages. It has an ISBN 10 number of 9083256898 and an ISBN 13 number of 978-9083256894. The item weighs 11.4 ounces and has dimensions of 6 x 0.54 x 9 inches.'}, {'book_id': 'bookid_13', 'details': 'The book, published by Central Avenue Publishing on January 24, 2023, is available in English and comes in paperback format, consisting of 144 pages. It has an ISBN-10 number of 1771682760 and an ISBN-13 number of 978-1771682763. The item weighs 5.1 ounces and has dimensions of 5.25 x 0.4 x 8 inches.'}, {'book_id': 'bookid_14', 'details': 'The book, published by Jessica Mathews, LLC on November 13, 2019, is written in English and features a paperback format comprising 26 pages. It has an ISBN-10 of 1087848539 and an ISBN-13 of 978-1087848532. Suitable for readers aged 3 to 8 years, it is appropriate for students in Kindergarten through 3rd grade. The item weighs 3.03 ounces and has dimensions of 8.5 x 0.05 x 11 inches.'}, {'book_id': 'bookid_15', 'details': 'The book is published by Kegan Paul and is a first edition released on November 15, 2000. It is written in English and is available in hardcover, comprising 348 pages. The ISBN-10 for this edition is 0710306911, while the ISBN-13 is 978-0710306913. The item weighs 2.23 pounds and has dimensions of 5.5 x 1.25 x 8.5 inches.'}, {'book_id': 'bookid_16', 'details': 'This book is published by Prentice Hall College Division and is in its third edition, released on January 1, 1997. It is written in English and is available in paperback, consisting of 390 pages. The ISBN-10 for this book is 0130840963, while the ISBN-13 is 978-0130840967. The item weighs 1.3 pounds and has dimensions of 7.01 x 0.67 x 9.17 inches.'}, {'book_id': 'bookid_17', 'details': 'This book, published by Edelsa Grupo Didascalia in a September 1, 1987 edition, is written in Spanish and consists of 44 pages. It has an ISBN-10 number of 8477110190 and an ISBN-13 number of 978-8477110194. The item weighs 2.05 ounces and has dimensions of 5.12 x 0.16 x 7.48 inches.'}, {'book_id': 'bookid_18', 'details': 'The book, published by Gale, Sabin Americana on February 21, 2012, is written in English and is available in paperback format, comprising 26 pages. It has an ISBN-10 of 1275627234 and an ISBN-13 of 978-1275627239. The item weighs 2.4 ounces and has dimensions of 7.44 x 0.05 x 9.69 inches.'}, {'book_id': 'bookid_19', 'details': "The book, published by Foundation Press in its 2013th edition on March 22, 2013, is available in English and spans 355 pages. It has an ISBN-10 number of 1609303687 and an ISBN-13 number of 978-1609303686. Weighing 1.5 pounds, the book's dimensions are 7 inches in width, 0.5 inches in thickness, and 9.75 inches in height."}, {'book_id': 'bookid_20', 'details': 'The book, published by Soho Crime in a revised edition on July 1, 2003, is available in English and has a total print length of 372 pages. It has a file size of 2295 KB and supports various features such as Text to Speech, a screen reader, enhanced typesetting, X-Ray, Word Wise, and sticky notes on Kindle Scribe.'}, {'book_id': 'bookid_21', 'details': 'The book, published by Random House in its first edition on January 1, 1945, is written in English and weighs 12 ounces.'}], 'var_functions.query_db:11': [{'purchase_id': 'purchaseid_186'}, {'purchase_id': 'purchaseid_191'}, {'purchase_id': 'purchaseid_190'}, {'purchase_id': 'purchaseid_8'}, {'purchase_id': 'purchaseid_178'}, {'purchase_id': 'purchaseid_186'}, {'purchase_id': 'purchaseid_76'}, {'purchase_id': 'purchaseid_186'}, {'purchase_id': 'purchaseid_115'}, {'purchase_id': 'purchaseid_167'}, {'purchase_id': 'purchaseid_188'}, {'purchase_id': 'purchaseid_23'}, {'purchase_id': 'purchaseid_196'}, {'purchase_id': 'purchaseid_196'}, {'purchase_id': 'purchaseid_3'}, {'purchase_id': 'purchaseid_48'}, {'purchase_id': 'purchaseid_154'}, {'purchase_id': 'purchaseid_99'}, {'purchase_id': 'purchaseid_190'}, {'purchase_id': 'purchaseid_3'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': [{'book_id': 'bookid_1'}, {'book_id': 'bookid_2'}, {'book_id': 'bookid_3'}, {'book_id': 'bookid_4'}, {'book_id': 'bookid_5'}, {'book_id': 'bookid_6'}, {'book_id': 'bookid_7'}, {'book_id': 'bookid_8'}, {'book_id': 'bookid_9'}, {'book_id': 'bookid_10'}, {'book_id': 'bookid_11'}, {'book_id': 'bookid_12'}, {'book_id': 'bookid_13'}, {'book_id': 'bookid_14'}, {'book_id': 'bookid_15'}, {'book_id': 'bookid_16'}, {'book_id': 'bookid_17'}, {'book_id': 'bookid_18'}, {'book_id': 'bookid_19'}, {'book_id': 'bookid_20'}, {'book_id': 'bookid_21'}, {'book_id': 'bookid_22'}, {'book_id': 'bookid_23'}, {'book_id': 'bookid_24'}, {'book_id': 'bookid_25'}, {'book_id': 'bookid_32'}, {'book_id': 'bookid_26'}, {'book_id': 'bookid_27'}, {'book_id': 'bookid_28'}, {'book_id': 'bookid_29'}, {'book_id': 'bookid_30'}, {'book_id': 'bookid_31'}, {'book_id': 'bookid_33'}, {'book_id': 'bookid_34'}, {'book_id': 'bookid_35'}, {'book_id': 'bookid_36'}, {'book_id': 'bookid_37'}, {'book_id': 'bookid_38'}, {'book_id': 'bookid_56'}, {'book_id': 'bookid_39'}, {'book_id': 'bookid_40'}, {'book_id': 'bookid_41'}, {'book_id': 'bookid_42'}, {'book_id': 'bookid_43'}, {'book_id': 'bookid_62'}, {'book_id': 'bookid_44'}, {'book_id': 'bookid_45'}, {'book_id': 'bookid_46'}, {'book_id': 'bookid_47'}, {'book_id': 'bookid_48'}], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)
