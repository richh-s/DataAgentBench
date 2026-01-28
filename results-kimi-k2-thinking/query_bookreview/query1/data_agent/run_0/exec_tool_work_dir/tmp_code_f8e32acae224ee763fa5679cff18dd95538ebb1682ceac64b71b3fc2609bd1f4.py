code = """import json
import re

# Get the file paths
books_file = locals().get('var_functions.query_db:18')
reviews_file = locals().get('var_functions.query_db:16')

# Load data
with open(books_file, 'r') as f:
    books = json.load(f)

with open(reviews_file, 'r') as f:
    reviews = json.load(f)

# Extract numeric IDs
book_numeric_ids = {}
for book in books:
    book_id = book['book_id']
    # Extract number from bookid_X
    match = re.search(r'bookid_(\d+)', book_id)
    if match:
        num_id = int(match.group(1))
        book_numeric_ids[num_id] = book

review_numeric_ids = {}
for review in reviews:
    purchase_id = review['purchase_id']
    # Extract number from purchaseid_X
    match = re.search(r'purchaseid_(\d+)', purchase_id)
    if match:
        num_id = int(match.group(1))
        if num_id not in review_numeric_ids:
            review_numeric_ids[num_id] = []
        review_numeric_ids[num_id].append(review)

print(f'Books with numeric IDs: {len(book_numeric_ids)}')
print(f'Reviews grouped by numeric IDs: {len(review_numeric_ids)}')

# Find overlap
book_nums = set(book_numeric_ids.keys())
review_nums = set(review_numeric_ids.keys())
overlap = book_nums.intersection(review_nums)
print(f'Numeric ID overlap: {len(overlap)}')

if len(overlap) > 0:
    # Show some examples
    examples = list(overlap)[:5]
    for num in examples:
        print(f'ID {num}: Book "{book_numeric_ids[num].get("title", "N/A")[:50]}" has {len(review_numeric_ids[num])} reviews')

# Now let's extract publication years and calculate decade stats
books_with_years = []
for book in books:
    details = book.get('details', '')
    # Look for 4-digit years
    years = re.findall(r'(\d{4})', details)
    valid_years = [int(y) for y in years if 1900 <= int(y) <= 2025]
    
    if valid_years:
        pub_year = min(valid_years)  # Take earliest year
        book_num_match = re.search(r'bookid_(\d+)', book['book_id'])
        if book_num_match:
            books_with_years.append({
                'book_num_id': int(book_num_match.group(1)),
                'pub_year': pub_year,
                'decade': f"{pub_year//10*10}s"
            })

print(f'Books with valid years and numeric IDs: {len(books_with_years)}')

# Calculate average rating per numeric book ID
book_avg_ratings = {}
review_counts = {}
for num_id, reviews_list in review_numeric_ids.items():
    if reviews_list:
        ratings = [float(r['rating']) for r in reviews_list]
        book_avg_ratings[num_id] = sum(ratings) / len(ratings)
        review_counts[num_id] = len(reviews_list)

print(f'Books with calculated average ratings: {len(book_avg_ratings)}')

# Join and group by decade
decade_books = {}
for book in books_with_years:
    book_num_id = book['book_num_id']
    if book_num_id in book_avg_ratings:
        decade = book['decade']
        if decade not in decade_books:
            decade_books[decade] = []
        decade_books[decade].append({
            'book_num_id': book_num_id,
            'pub_year': book['pub_year'],
            'avg_rating': book_avg_ratings[book_num_id],
            'review_count': review_counts[book_num_id]
        })

print(f'Decades with matching books: {list(decade_books.keys())}')

# Calculate decade statistics (only decades with >= 10 books)
decade_stats = {}
for decade, books in decade_books.items():
    if len(books) >= 10:
        avg_rating = sum(b['avg_rating'] for b in books) / len(books)
        decade_stats[decade] = {
            'avg_rating': round(avg_rating, 3),
            'book_count': len(books),
            'total_reviews': sum(b['review_count'] for b in books)
        }

print(f'Decades with >= 10 books: {len(decade_stats)}')

if decade_stats:
    # Sort by average rating
    sorted_decades = sorted(decade_stats.items(), key=lambda x: x[1]['avg_rating'], reverse=True)
    
    print('\nTop decades by average rating:')
    for decade, stats in sorted_decades[:10]:
        print(f"{decade}: avg rating {stats['avg_rating']}, {stats['book_count']} books, {stats['total_reviews']} total reviews")
    
    best_decade = sorted_decades[0]
    result = {
        'best_decade': best_decade[0],
        'avg_rating': best_decade[1]['avg_rating'],
        'book_count': best_decade[1]['book_count'],
        'total_reviews': best_decade[1]['total_reviews']
    }
else:
    result = 'No decades found with at least 10 books'

print('__RESULT__:')
print(json.dumps(str(result) if isinstance(result, str) else result))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['books_info'], 'var_functions.query_db:4': [{'rating': '4', 'title': 'Ha! On me!  I thought this was a cookbook!', 'text': 'Lucky for me it\'s more than a cookbook.<br /><br />The story of a modern Daniel Boone, growing up in Michigan, one of three sons of a hunter.  Beginning at age eight when he shot a squirrel, to age 13 his first deer, then hunting his way through college, a career as a fur trapper, hunting sheep in Alaska, canoeing the Missouri River for deer and ending in Brooklyn age 37. Brooklyn?<br /><br />I especially liked that I share his disgust at catch & release fishing - if you fish it, you have to eat it - anything else is sadism (my words).<br /><br />My brother in law is the cook in the family and I wanted to see if this would be a good gift for him and I struck pay dirt following each chapter are "Tasting Notes" where the author speaks of cooking wild game.<br /><br />I also enjoyed it for the history of the land he has hunted as well as the history of the hunt (I too was a big Daniel Boone fan growing up!).<br /><br />I think more pictures (everything but dead things) would have made this a keeper.', 'review_time': '2012-11-24 18:52:00', 'helpful_vote': '0', 'verified_purchase': '0', 'purchase_id': 'purchaseid_186'}, {'rating': '4', 'title': 'Four Stars', 'text': 'Not as developed as Stephanie but I like the characters so far.', 'review_time': '2015-12-31 13:35:00', 'helpful_vote': '0', 'verified_purchase': '1', 'purchase_id': 'purchaseid_191'}, {'rating': '4', 'title': 'A wonderful adventure in France', 'text': "I loved this book all the way until the end. I have recently discovered that the author is intending to release another book, and from what I understand it will continue where this one left off. I am thankful for this, as the way this book ended was definitely a negative for me. I wanted to know more! What happened to the author, did she learn what she came to learn? Did she get the job she was hoping for? So many questions.<br /><br />From the beginning of Linda's book, it is easy to love her. She is open, honest and definitely has the type of personality you want your heroine to have, whether the book is fiction or reality. I couldn't help but root for Linda throughout her trials with her host family, even when I thought she acted as a bit of a brat herself. Listening to her internal thoughts about what she went through and her desire to achieve her goals made this book feel close to my heart.<br /><br />I applaud the adventurous spirit of the author and her decision to keep journal entries from that chapter of her life. What great material to have later to inspire a book! While I enjoyed the entire memoir, my favourite part of this book would have to be the author's descriptions of the many places she visited and the people she met along the way. While I think she could definitely have made a better impression on the family she worked for if she had been honest about her lack of French language skills from the beginning, she is a pioneer. Her drive and desire to learn the language from those in the actual country was inspiring. Not many people would have been gutsy enough to do what Linda did.<br /><br />I also particularly enjoyed the relationship between Linda and Antoine. The Kind heart of the author was apparent in her actions toward the children, even when she struggled with them.<br /><br />There is some romance, and I appreciated the way the author handled it. While sex scenes are not necessarily automatically offensive, there is something about memoirs that makes me uncomfortable if they are filled with them. This author manages to hint at her experiences without going into too much detail, leaving the reader to decide exactly what happened. Great writing.<br /><br />When you step into reading this book, you learn a lot about French customs, French cuisine and wine. You also get the opportunity to brush up on your French skills a bit and get to step outside yourself and live an adventure through the eyes of the author. I read this book in one sitting with very few breaks in between and found myself enthralled in the sights, sounds and atmosphere of this memoir.<br /><br />In the end, I was disappointed that the book ended. I could have kept reading about Linda's experiences without stopping anytime in the foreseeable future. The end of the book leaves many unanswered questions, that I am assuming the author will be answering in her next book. Were this a standalone, I would be very disappointed with the way the book ended, but with the knowledge that she is writing another book to continue with her story, I can't fault this one. One thing is for sure, if you read this book, you will be anxiously awaiting the next.<br /><br />I would recommend this to anyone who likes books about travel, memoirs or just a good story that came from the recollections and heart of the author. Read it, you will be glad you did. Overall, this was a VERY enjoyable read that gave me many reasons to wish I could drop everything and head off to France!", 'review_time': '2013-05-05 10:47:00', 'helpful_vote': '1', 'verified_purchase': '0', 'purchase_id': 'purchaseid_190'}, {'rating': '5', 'title': 'Best beginner book.  Been looking for something like this for a long time.', 'text': "Looked online for years for something like this.  It's the best I've seen.", 'review_time': '2020-08-12 11:06:00', 'helpful_vote': '0', 'verified_purchase': '1', 'purchase_id': 'purchaseid_8'}, {'rating': '4', 'title': 'Referance Guide', 'text': 'Good reference guide for the basics', 'review_time': '2014-11-13 18:55:00', 'helpful_vote': '0', 'verified_purchase': '1', 'purchase_id': 'purchaseid_178'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}, {'book_id': 'bookid_6', 'details': 'This book, published independently on December 30, 2021, is written in English and consists of 24 pages. It has an ISBN 13 of 979-8528537702 and weighs 3.2 ounces. The dimensions of the book are 7 x 0.06 x 9 inches.'}, {'book_id': 'bookid_7', 'details': 'The book, published by Guilford in its second edition in January 2004, is also noted as the 8082nd edition from January 1, 1994. It has a remarkably light item weight of just 0.01 ounces.'}, {'book_id': 'bookid_8', 'details': 'This book, published by Make Community, LLC, in its second edition on September 22, 2015, is available in English and spans 352 pages in paperback format. It has an ISBN of 9781680450262 for the 10-digit version and 978-1680450262 for the 13-digit version. The content is suitable for readers aged 11 to 17 years. The book weighs 2.91 pounds and its dimensions are 8 inches in width, 0.5 inches in thickness, and 10 inches in height.'}, {'book_id': 'bookid_9', 'details': 'This book, published independently on September 25, 2019, is written in English and spans 367 pages. It is available in paperback format and has an ISBN-10 of 1694621731 and an ISBN-13 of 978-1694621733. The item weighs 1.38 pounds and measures 6 x 0.92 x 9 inches.'}, {'book_id': 'bookid_10', 'details': 'This book, published by WallBuilder Press in its first edition on November 8, 2004, is available in English and comprises 51 pages in paperback format. It has an ISBN-10 of 1932225323 and an ISBN-13 of 978-1932225327, with a total item weight of 3.52 ounces.'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:14': [{'purchase_id': 'purchaseid_186', 'rating': '4'}, {'purchase_id': 'purchaseid_191', 'rating': '4'}, {'purchase_id': 'purchaseid_190', 'rating': '4'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '4'}, {'purchase_id': 'purchaseid_186', 'rating': '4'}, {'purchase_id': 'purchaseid_76', 'rating': '5'}, {'purchase_id': 'purchaseid_186', 'rating': '4'}, {'purchase_id': 'purchaseid_115', 'rating': '5'}, {'purchase_id': 'purchaseid_167', 'rating': '2'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:26': 'No decades found with at least 10 books', 'var_functions.execute_python:28': {'total_books': 200, 'books_with_years': 190, 'total_reviews': 1833, 'books_with_reviews': 200, 'overlap': 0}}

exec(code, env_args)
