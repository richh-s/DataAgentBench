code = """import json
import re

# Load data
with open('var_function-call-3791474810110582574.json', 'r') as f:
    books_list = json.load(f)

with open('var_function-call-8564397495806396179.json', 'r') as f:
    reviews_list = json.load(f)

# Parse years from books
book_years = {}
# Regex for finding year. 
# Strategy: Look for "published ... \d{4}" or dates.
# The examples show the date is often explicitly mentioned.
# We will look for 4 digit numbers starting with 19 or 20.
year_pattern = re.compile(r'\b(19\d{2}|20\d{2})\b')

# Debugging: let's inspect some details and what we extract
print("DEBUG: Extracting years...")
count = 0
for book in books_list:
    b_id = book['book_id']
    details = book['details']
    
    # We want to prioritize years connected to "published" or "released".
    # But for simplicity, let's find all years and take the first one that appears after "published" or just the first one.
    # Most descriptions start with "This book, published..." or "Published by..."
    
    years = year_pattern.findall(details)
    if years:
        # Heuristic: Use the first found year. 
        # In the example "published ... in January 2004 ... from 1994", 2004 comes first.
        # In "published ... on May 20, 1996", 1996 is found.
        # Check if there is a case where copyright is earlier?
        # Usually the first year mentioned in these generated descriptions is the publication year of the edition.
        year = int(years[0])
        
        # Normalize ID: "bookid_1" -> "1"
        try:
            id_num = b_id.split('_')[1]
            book_years[id_num] = year
        except:
            pass
        
        if count < 5:
            print(f"ID: {b_id}, Year: {year}, Details snippet: {details[:100]}")
            count += 1
    else:
        pass

print(f"DEBUG: Found years for {len(book_years)} books.")

# Process reviews
decade_stats = {} # {decade_str: {'ratings': [], 'book_ids': set()}}

for review in reviews_list:
    p_id = review['purchase_id']
    rating = float(review['rating'])
    
    # Normalize ID: "purchaseid_186" -> "186"
    try:
        id_num = p_id.split('_')[1]
    except:
        continue
        
    if id_num in book_years:
        year = book_years[id_num]
        decade_start = (year // 10) * 10
        decade_str = f"{decade_start}s"
        
        if decade_str not in decade_stats:
            decade_stats[decade_str] = {'ratings': [], 'book_ids': set()}
        
        decade_stats[decade_str]['ratings'].append(rating)
        decade_stats[decade_str]['book_ids'].add(id_num)

# Analyze results
results = []
for decade, stats in decade_stats.items():
    num_books = len(stats['book_ids'])
    avg_rating = sum(stats['ratings']) / len(stats['ratings'])
    results.append({
        'decade': decade,
        'num_books': num_books,
        'avg_rating': avg_rating
    })

# Filter
filtered_results = [r for r in results if r['num_books'] >= 10]

# Sort
filtered_results.sort(key=lambda x: x['avg_rating'], reverse=True)

print("__RESULT__:")
print(json.dumps(filtered_results))"""

env_args = {'var_function-call-8730651834486863362': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'var_function-call-3791474810110581591': ['review'], 'var_function-call-3791474810110582574': 'file_storage/function-call-3791474810110582574.json', 'var_function-call-686918671668584251': [{'count': '200'}], 'var_function-call-686918671668581572': [{'count(*)': '1833'}], 'var_function-call-8564397495806396179': 'file_storage/function-call-8564397495806396179.json'}

exec(code, env_args)
