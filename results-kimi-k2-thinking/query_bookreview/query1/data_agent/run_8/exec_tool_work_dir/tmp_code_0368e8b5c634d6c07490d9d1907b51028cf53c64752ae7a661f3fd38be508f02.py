code = """import json
import re

book_file_path = locals()['var_functions.query_db:10']
reviews_file_path = locals()['var_functions.query_db:6']

# Load the query results
with open(book_file_path, 'r') as f:
    books_data = json.load(f)

with open(reviews_file_path, 'r') as f:
    reviews_data = json.load(f)

# Extract year from details field and calculate decade
book_year_info = []

for book in books_data:
    details = book.get('details', '')
    year = None
    
    # Look for date patterns like "May 20, 1996" or "2004" etc.
    # First try patterns with month and comma
    date_patterns = [
        r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+(\d{4})',
        r'on\s+(\d{1,2})\s+(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{4})',
        r'\b(18\d{2}|19\d{2}|20\d{2}|21\d{2})\b',
    ]
    
    for pattern in date_patterns:
        matches = re.findall(pattern, details, re.IGNORECASE)
        if matches:
            # Take the first year from the matches
            year_str = matches[0]
            if isinstance(year_str, tuple):
                year = int(year_str[1])  # For patterns with month/date/year
            else:
                year = int(year_str)
            break
    
    if year:
        decade = f"{(year // 10) * 10}s"
        book_year_info.append({
            'book_id': book.get('book_id'),
            'year': year,
            'decade': decade
        })
    else:
        # Try simpler approach - look for 4 digits that could be years
        all_4digits = re.findall(r'\b(1\d{3}|2\d{3})\b', details)
        if all_4digits:
            for y in all_4digits:
                y_int = int(y)
                if 1900 <= y_int <= 2023:
                    year = y_int
                    break
        
        if year:
            decade = f"{(year // 10) * 10}s"
            book_year_info.append({
                'book_id': book.get('book_id'),
                'year': year,
                'decade': decade
            })
        else:
            book_year_info.append({
                'book_id': book.get('book_id'),
                'year': None,
                'decade': None
            })

# Create mapping from book_id to decade
book_to_decade = {item['book_id']: item['decade'] for item in book_year_info}

# Count how many books have year info vs don't have
books_with_year = sum(1 for item in book_year_info if item['year'] is not None)
books_without_year = sum(1 for item in book_year_info if item['year'] is None)

# Sample of decade assignments
sample_decades = [(item['book_id'], item['decade']) for item in book_year_info if item['decade']][:10]

result = {
    "total_books": len(books_data),
    "books_with_year": books_with_year,
    "books_without_year": books_without_year,
    "sample_decades": sample_decades
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['books_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['review'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.', 'title': 'Chaucer'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.', 'title': 'Notes from a Kidwatcher'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.', 'title': 'Service: A Navy SEAL at War'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.', 'title': 'Parker & Knight'}, {'book_id': 'bookid_6', 'details': 'This book, published independently on December 30, 2021, is written in English and consists of 24 pages. It has an ISBN 13 of 979-8528537702 and weighs 3.2 ounces. The dimensions of the book are 7 x 0.06 x 9 inches.', 'title': 'Writings from a Black Woman Living in the Land of the "Free": Strength, Power, Resilience'}, {'book_id': 'bookid_7', 'details': 'The book, published by Guilford in its second edition in January 2004, is also noted as the 8082nd edition from January 1, 1994. It has a remarkably light item weight of just 0.01 ounces.', 'title': "Child Development: A Practitioner's Guide:2nd (Second) edition"}, {'book_id': 'bookid_8', 'details': 'This book, published by Make Community, LLC, in its second edition on September 22, 2015, is available in English and spans 352 pages in paperback format. It has an ISBN of 9781680450262 for the 10-digit version and 978-1680450262 for the 13-digit version. The content is suitable for readers aged 11 to 17 years. The book weighs 2.91 pounds and its dimensions are 8 inches in width, 0.5 inches in thickness, and 10 inches in height.', 'title': 'Make: Electronics: Learning Through Discovery'}, {'book_id': 'bookid_9', 'details': 'This book, published independently on September 25, 2019, is written in English and spans 367 pages. It is available in paperback format and has an ISBN-10 of 1694621731 and an ISBN-13 of 978-1694621733. The item weighs 1.38 pounds and measures 6 x 0.92 x 9 inches.', 'title': 'Reunion: The Children of Lauderdale Park'}, {'book_id': 'bookid_10', 'details': 'This book, published by WallBuilder Press in its first edition on November 8, 2004, is available in English and comprises 51 pages in paperback format. It has an ISBN-10 of 1932225323 and an ISBN-13 of 978-1932225327, with a total item weight of 3.52 ounces.', 'title': 'Four Centuries of American Education'}, {'book_id': 'bookid_12', 'details': 'This book, published by Lisette Marshall on May 29, 2022, is written in English and is available in paperback, comprising 215 pages. It has an ISBN 10 number of 9083256898 and an ISBN 13 number of 978-9083256894. The item weighs 11.4 ounces and has dimensions of 6 x 0.54 x 9 inches.', 'title': 'Heart of Silk and Shadows: A Fae Fantasy Romance (Fae Isles)'}, {'book_id': 'bookid_13', 'details': 'The book, published by Central Avenue Publishing on January 24, 2023, is available in English and comes in paperback format, consisting of 144 pages. It has an ISBN-10 number of 1771682760 and an ISBN-13 number of 978-1771682763. The item weighs 5.1 ounces and has dimensions of 5.25 x 0.4 x 8 inches.', 'title': 'Girl Made of Glass'}, {'book_id': 'bookid_14', 'details': 'The book, published by Jessica Mathews, LLC on November 13, 2019, is written in English and features a paperback format comprising 26 pages. It has an ISBN-10 of 1087848539 and an ISBN-13 of 978-1087848532. Suitable for readers aged 3 to 8 years, it is appropriate for students in Kindergarten through 3rd grade. The item weighs 3.03 ounces and has dimensions of 8.5 x 0.05 x 11 inches.', 'title': 'The Old Man and the Pirate Princess'}, {'book_id': 'bookid_15', 'details': 'The book is published by Kegan Paul and is a first edition released on November 15, 2000. It is written in English and is available in hardcover, comprising 348 pages. The ISBN-10 for this edition is 0710306911, while the ISBN-13 is 978-0710306913. The item weighs 2.23 pounds and has dimensions of 5.5 x 1.25 x 8.5 inches.', 'title': 'Japanese Girls and Women'}, {'book_id': 'bookid_16', 'details': 'This book is published by Prentice Hall College Division and is in its third edition, released on January 1, 1997. It is written in English and is available in paperback, consisting of 390 pages. The ISBN-10 for this book is 0130840963, while the ISBN-13 is 978-0130840967. The item weighs 1.3 pounds and has dimensions of 7.01 x 0.67 x 9.17 inches.', 'title': 'Behavior Principles in Everyday Life'}, {'book_id': 'bookid_17', 'details': 'This book, published by Edelsa Grupo Didascalia in a September 1, 1987 edition, is written in Spanish and consists of 44 pages. It has an ISBN-10 number of 8477110190 and an ISBN-13 number of 978-8477110194. The item weighs 2.05 ounces and has dimensions of 5.12 x 0.16 x 7.48 inches.', 'title': 'PQL 3 - Lola (Spanish Edition)'}, {'book_id': 'bookid_18', 'details': 'The book, published by Gale, Sabin Americana on February 21, 2012, is written in English and is available in paperback format, comprising 26 pages. It has an ISBN-10 of 1275627234 and an ISBN-13 of 978-1275627239. The item weighs 2.4 ounces and has dimensions of 7.44 x 0.05 x 9.69 inches.', 'title': 'A sermon, preached at the execution of Moses Paul, an Indian: who was executed at New-Haven, on the 2d of September, 1772, for the murder of Mr. Moses ... 1771 : preached at the desire of said Paul.'}, {'book_id': 'bookid_19', 'details': "The book, published by Foundation Press in its 2013th edition on March 22, 2013, is available in English and spans 355 pages. It has an ISBN-10 number of 1609303687 and an ISBN-13 number of 978-1609303686. Weighing 1.5 pounds, the book's dimensions are 7 inches in width, 0.5 inches in thickness, and 9.75 inches in height.", 'title': 'Business Associations: Agency, Partnerships, LLCs, and Corporations- 2013 Statutes and Rules'}, {'book_id': 'bookid_20', 'details': 'The book, published by Soho Crime in a revised edition on July 1, 2003, is available in English and has a total print length of 372 pages. It has a file size of 2295 KB and supports various features such as Text to Speech, a screen reader, enhanced typesetting, X-Ray, Word Wise, and sticky notes on Kindle Scribe.', 'title': 'Inspector Imanishi Investigates (Soho Crime)'}, {'book_id': 'bookid_21', 'details': 'The book, published by Random House in its first edition on January 1, 1945, is written in English and weighs 12 ounces.', 'title': 'Officially Dead'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:16': {'books': 200, 'reviews': 1833}, 'var_functions.execute_python:18': {'total_books': 200, 'books_with_year': 0, 'books_without_year': 200, 'sample_years': []}, 'var_functions.execute_python:20': {'total_books': 200, 'books_with_year': 0, 'books_without_year': 200, 'sample_years': [], 'sample_no_year': ['Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of', 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN', 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363']}}

exec(code, env_args)
