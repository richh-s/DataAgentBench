code = """import json
import re
from collections import defaultdict

# Load books data with years
books_file = locals()['var_functions.query_db:8']
with open(books_file, 'r') as f:
    books_data = json.load(f)

# Extract publication year for each book
book_years = {}
for book in books_data:
    details = book.get('details', '')
    book_id = book['book_id']
    
    # Pattern to match date in format "on Month DD, YYYY"
    year_match = re.search(r'on\s\w+\s\d{1,2},\s+(\d{4})', details)
    if year_match:
        book_years[book_id] = int(year_match.group(1))
        continue
        
    # Alternate pattern: "in January 2004" 
    year_match2 = re.search(r'in\s\w+\s+(\d{4})', details)
    if year_match2:
        book_years[book_id] = int(year_match2.group(1))
        continue
        
    # Also look for any 4-digit year in publication context
    year_match3 = re.search(r'(published|released|edition|January|February|March|April|May|June|July|August|September|October|November|December).*?(\d{4})', details, re.IGNORECASE)
    if year_match3:
        year_candidate = int(year_match3.group(2))
        if 1900 <= year_candidate <= 2025:
            book_years[book_id] = year_candidate

# Load reviews data
reviews_file = locals()['var_functions.query_db:18']
with open(reviews_file, 'r') as f:
    reviews_data = json.load(f)

# Create decade groups and calculate statistics
decade_reviews = defaultdict(list)
decade_books = defaultdict(set)

for review in reviews_data:
    review_book_id = review['book_id']
    rating = float(review['rating'])
    
    # Find matching book ID
    for book_id in book_years:
        # Check for exact match
        if book_id == review_book_id:
            year = book_years[book_id]
            decade = f"{year//10*10}s"  # e.g., 2004 -> 2000s
            decade_reviews[decade].append(rating)
            decade_books[decade].add(book_id)
            break

# Filter decades with at least 10 distinct books
valid_decades = {}
for decade, books in decade_books.items():
    if len(books) >= 10:
        ratings = decade_reviews[decade]
        avg_rating = sum(ratings) / len(ratings)
        valid_decades[decade] = {
            'avg_rating': avg_rating,
            'num_books': len(books),
            'num_reviews': len(ratings)
        }

# Find decade with highest average rating
if valid_decades:
    best_decade = max(valid_decades.items(), key=lambda x: x[1]['avg_rating'])
    result = {
        'decade': best_decade[0],
        'avg_rating': best_decade[1]['avg_rating'],
        'num_books': best_decade[1]['num_books'],
        'num_reviews': best_decade[1]['num_reviews']
    }
else:
    result = {'error': 'No decades found with at least 10 books'}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['books_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['review'], 'var_functions.query_db:9': [{'rating': '4', 'title': 'Ha! On me!  I thought this was a cookbook!', 'text': 'Lucky for me it\'s more than a cookbook.<br /><br />The story of a modern Daniel Boone, growing up in Michigan, one of three sons of a hunter.  Beginning at age eight when he shot a squirrel, to age 13 his first deer, then hunting his way through college, a career as a fur trapper, hunting sheep in Alaska, canoeing the Missouri River for deer and ending in Brooklyn age 37. Brooklyn?<br /><br />I especially liked that I share his disgust at catch & release fishing - if you fish it, you have to eat it - anything else is sadism (my words).<br /><br />My brother in law is the cook in the family and I wanted to see if this would be a good gift for him and I struck pay dirt following each chapter are "Tasting Notes" where the author speaks of cooking wild game.<br /><br />I also enjoyed it for the history of the land he has hunted as well as the history of the hunt (I too was a big Daniel Boone fan growing up!).<br /><br />I think more pictures (everything but dead things) would have made this a keeper.', 'review_time': '2012-11-24 18:52:00', 'helpful_vote': '0', 'verified_purchase': '0', 'purchase_id': 'purchaseid_186'}, {'rating': '4', 'title': 'Four Stars', 'text': 'Not as developed as Stephanie but I like the characters so far.', 'review_time': '2015-12-31 13:35:00', 'helpful_vote': '0', 'verified_purchase': '1', 'purchase_id': 'purchaseid_191'}, {'rating': '4', 'title': 'A wonderful adventure in France', 'text': "I loved this book all the way until the end. I have recently discovered that the author is intending to release another book, and from what I understand it will continue where this one left off. I am thankful for this, as the way this book ended was definitely a negative for me. I wanted to know more! What happened to the author, did she learn what she came to learn? Did she get the job she was hoping for? So many questions.<br /><br />From the beginning of Linda's book, it is easy to love her. She is open, honest and definitely has the type of personality you want your heroine to have, whether the book is fiction or reality. I couldn't help but root for Linda throughout her trials with her host family, even when I thought she acted as a bit of a brat herself. Listening to her internal thoughts about what she went through and her desire to achieve her goals made this book feel close to my heart.<br /><br />I applaud the adventurous spirit of the author and her decision to keep journal entries from that chapter of her life. What great material to have later to inspire a book! While I enjoyed the entire memoir, my favourite part of this book would have to be the author's descriptions of the many places she visited and the people she met along the way. While I think she could definitely have made a better impression on the family she worked for if she had been honest about her lack of French language skills from the beginning, she is a pioneer. Her drive and desire to learn the language from those in the actual country was inspiring. Not many people would have been gutsy enough to do what Linda did.<br /><br />I also particularly enjoyed the relationship between Linda and Antoine. The Kind heart of the author was apparent in her actions toward the children, even when she struggled with them.<br /><br />There is some romance, and I appreciated the way the author handled it. While sex scenes are not necessarily automatically offensive, there is something about memoirs that makes me uncomfortable if they are filled with them. This author manages to hint at her experiences without going into too much detail, leaving the reader to decide exactly what happened. Great writing.<br /><br />When you step into reading this book, you learn a lot about French customs, French cuisine and wine. You also get the opportunity to brush up on your French skills a bit and get to step outside yourself and live an adventure through the eyes of the author. I read this book in one sitting with very few breaks in between and found myself enthralled in the sights, sounds and atmosphere of this memoir.<br /><br />In the end, I was disappointed that the book ended. I could have kept reading about Linda's experiences without stopping anytime in the foreseeable future. The end of the book leaves many unanswered questions, that I am assuming the author will be answering in her next book. Were this a standalone, I would be very disappointed with the way the book ended, but with the knowledge that she is writing another book to continue with her story, I can't fault this one. One thing is for sure, if you read this book, you will be anxiously awaiting the next.<br /><br />I would recommend this to anyone who likes books about travel, memoirs or just a good story that came from the recollections and heart of the author. Read it, you will be glad you did. Overall, this was a VERY enjoyable read that gave me many reasons to wish I could drop everything and head off to France!", 'review_time': '2013-05-05 10:47:00', 'helpful_vote': '1', 'verified_purchase': '0', 'purchase_id': 'purchaseid_190'}, {'rating': '5', 'title': 'Best beginner book.  Been looking for something like this for a long time.', 'text': "Looked online for years for something like this.  It's the best I've seen.", 'review_time': '2020-08-12 11:06:00', 'helpful_vote': '0', 'verified_purchase': '1', 'purchase_id': 'purchaseid_8'}, {'rating': '4', 'title': 'Referance Guide', 'text': 'Good reference guide for the basics', 'review_time': '2014-11-13 18:55:00', 'helpful_vote': '0', 'verified_purchase': '1', 'purchase_id': 'purchaseid_178'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'total_books': 200, 'books_with_years': 0, 'sample_books': []}, 'var_functions.execute_python:14': [{'id': 'bookid_1', 'details_sample': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of'}, {'id': 'bookid_2', 'details_sample': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN'}, {'id': 'bookid_3', 'details_sample': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363'}, {'id': 'bookid_4', 'details_sample': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575'}, {'id': 'bookid_5', 'details_sample': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it s'}, {'id': 'bookid_6', 'details_sample': 'This book, published independently on December 30, 2021, is written in English and consists of 24 pages. It has an ISBN 13 of 979-8528537702 and weighs 3.2 ounces. The dimensions of the book are 7 x 0'}, {'id': 'bookid_7', 'details_sample': 'The book, published by Guilford in its second edition in January 2004, is also noted as the 8082nd edition from January 1, 1994. It has a remarkably light item weight of just 0.01 ounces.'}, {'id': 'bookid_8', 'details_sample': 'This book, published by Make Community, LLC, in its second edition on September 22, 2015, is available in English and spans 352 pages in paperback format. It has an ISBN of 9781680450262 for the 10-di'}, {'id': 'bookid_9', 'details_sample': 'This book, published independently on September 25, 2019, is written in English and spans 367 pages. It is available in paperback format and has an ISBN-10 of 1694621731 and an ISBN-13 of 978-16946217'}, {'id': 'bookid_10', 'details_sample': 'This book, published by WallBuilder Press in its first edition on November 8, 2004, is available in English and comprises 51 pages in paperback format. It has an ISBN-10 of 1932225323 and an ISBN-13 o'}, {'id': 'bookid_11', 'details_sample': 'Published by Caxton Press on January 1, 1993, this book is available in English and spans 407 pages. It has an ISBN-10 of 0893011673 and an ISBN-13 of 978-0893011673. Weighing 1.51 pounds, the book me'}, {'id': 'bookid_12', 'details_sample': 'This book, published by Lisette Marshall on May 29, 2022, is written in English and is available in paperback, comprising 215 pages. It has an ISBN 10 number of 9083256898 and an ISBN 13 number of 978'}, {'id': 'bookid_13', 'details_sample': 'The book, published by Central Avenue Publishing on January 24, 2023, is available in English and comes in paperback format, consisting of 144 pages. It has an ISBN-10 number of 1771682760 and an ISBN'}, {'id': 'bookid_14', 'details_sample': 'The book, published by Jessica Mathews, LLC on November 13, 2019, is written in English and features a paperback format comprising 26 pages. It has an ISBN-10 of 1087848539 and an ISBN-13 of 978-10878'}, {'id': 'bookid_15', 'details_sample': 'The book is published by Kegan Paul and is a first edition released on November 15, 2000. It is written in English and is available in hardcover, comprising 348 pages. The ISBN-10 for this edition is '}, {'id': 'bookid_16', 'details_sample': 'This book is published by Prentice Hall College Division and is in its third edition, released on January 1, 1997. It is written in English and is available in paperback, consisting of 390 pages. The '}, {'id': 'bookid_17', 'details_sample': 'This book, published by Edelsa Grupo Didascalia in a September 1, 1987 edition, is written in Spanish and consists of 44 pages. It has an ISBN-10 number of 8477110190 and an ISBN-13 number of 978-8477'}, {'id': 'bookid_18', 'details_sample': 'The book, published by Gale, Sabin Americana on February 21, 2012, is written in English and is available in paperback format, comprising 26 pages. It has an ISBN-10 of 1275627234 and an ISBN-13 of 97'}, {'id': 'bookid_19', 'details_sample': 'The book, published by Foundation Press in its 2013th edition on March 22, 2013, is available in English and spans 355 pages. It has an ISBN-10 number of 1609303687 and an ISBN-13 number of 978-160930'}, {'id': 'bookid_20', 'details_sample': 'The book, published by Soho Crime in a revised edition on July 1, 2003, is available in English and has a total print length of 372 pages. It has a file size of 2295 KB and supports various features s'}], 'var_functions.execute_python:16': {'books_with_years': 189, 'sample_mappings': [['bookid_1', 2004], ['bookid_2', 1996], ['bookid_3', 2012], ['bookid_4', 2013], ['bookid_5', 2014], ['bookid_6', 2021], ['bookid_7', 2004], ['bookid_8', 2015], ['bookid_9', 2019], ['bookid_10', 2004]]}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
