code = """import json
import re
from collections import defaultdict

# Read the books data
books_file = locals()['var_functions.query_db:14']
with open(books_file, 'r') as f:
    books_data = json.load(f)

# Read the reviews data
reviews_file = locals()['var_functions.query_db:12']
with open(reviews_file, 'r') as f:
    reviews_data = json.load(f)

# Extract publication years from book details and create book_id mapping
book_id_to_decade = {}
book_num_to_id = {}
for book in books_data:
    details = book.get('details', '')
    year_match = re.search(r'((?:19|20)\d{2})', details)
    if year_match:
        year = int(year_match.group(1))
        decade = f"{year//10*10}s"
        book_id = book['book_id']
        book_id_to_decade[book_id] = decade
        
        # Extract numeric part from book_id (e.g., "bookid_1" -> 1)
        num_match = re.search(r'\d+$', book_id)
        if num_match:
            book_num = int(num_match.group())
            book_num_to_id[book_num] = book_id

# Create mapping from purchase_id numeric part to book decade
purchase_num_to_decade = {}
for review in reviews_data:
    purchase_id = review.get('purchase_id', '')
    
    # Extract numeric part from purchase_id (e.g., "purchaseid_186" -> 186)
    num_match = re.search(r'\d+$', purchase_id)
    if num_match:
        purchase_num = int(num_match.group())
        # Match by numeric ID - purchaseid_X should match bookid_X
        if purchase_num in book_num_to_id:
            book_id = book_num_to_id[purchase_num]
            if book_id in book_id_to_decade:
                purchase_num_to_decade[purchase_num] = book_id_to_decade[book_id]

# Process reviews
reviews_with_decades = []
for review in reviews_data:
    purchase_id = review.get('purchase_id', '')
    num_match = re.search(r'\d+$', purchase_id)
    if num_match:
        purchase_num = int(num_match.group())
        if purchase_num in purchase_num_to_decade:
            reviews_with_decades.append({
                'purchase_id': purchase_id,
                'rating': float(review.get('rating', 0)),
                'decade': purchase_num_to_decade[purchase_num],
                'book_num': purchase_num
            })

# Group by decade and calculate statistics
decade_stats = defaultdict(lambda: {'ratings': [], 'books': set()})
for review in reviews_with_decades:
    decade = review['decade']
    decade_stats[decade]['ratings'].append(review['rating'])
    decade_stats[decade]['books'].add(review['book_num'])

# Calculate average rating and count distinct books for each decade
decade_results = []
for decade, stats in sorted(decade_stats.items()):
    book_count = len(stats['books'])
    if book_count >= 10:  # At least 10 distinct books
        avg_rating = sum(stats['ratings']) / len(stats['ratings'])
        decade_results.append({
            'decade': decade,
            'avg_rating': round(avg_rating, 3),
            'books_rated': book_count,
            'total_reviews': len(stats['ratings'])
        })

# Find decade with highest average rating
if decade_results:
    top_decade = max(decade_results, key=lambda x: x['avg_rating'])
else:
    top_decade = None

print('__RESULT__:')
print(json.dumps({
    'matches_found': len(reviews_with_decades),
    'unique_books_matched': len(set(r['book_num'] for r in reviews_with_decades)),
    'decades_analyzed': len(decade_results),
    'decade_rankings': sorted(decade_results, key=lambda x: x['avg_rating'], reverse=True),
    'top_decade': top_decade
}))"""

env_args = {'var_functions.list_db:0': ['books_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.list_db:6': ['review'], 'var_functions.query_db:8': [{'rating': '4', 'title': 'Ha! On me!  I thought this was a cookbook!', 'text': 'Lucky for me it\'s more than a cookbook.<br /><br />The story of a modern Daniel Boone, growing up in Michigan, one of three sons of a hunter.  Beginning at age eight when he shot a squirrel, to age 13 his first deer, then hunting his way through college, a career as a fur trapper, hunting sheep in Alaska, canoeing the Missouri River for deer and ending in Brooklyn age 37. Brooklyn?<br /><br />I especially liked that I share his disgust at catch & release fishing - if you fish it, you have to eat it - anything else is sadism (my words).<br /><br />My brother in law is the cook in the family and I wanted to see if this would be a good gift for him and I struck pay dirt following each chapter are "Tasting Notes" where the author speaks of cooking wild game.<br /><br />I also enjoyed it for the history of the land he has hunted as well as the history of the hunt (I too was a big Daniel Boone fan growing up!).<br /><br />I think more pictures (everything but dead things) would have made this a keeper.', 'review_time': '2012-11-24 18:52:00', 'helpful_vote': '0', 'verified_purchase': '0', 'purchase_id': 'purchaseid_186'}, {'rating': '4', 'title': 'Four Stars', 'text': 'Not as developed as Stephanie but I like the characters so far.', 'review_time': '2015-12-31 13:35:00', 'helpful_vote': '0', 'verified_purchase': '1', 'purchase_id': 'purchaseid_191'}, {'rating': '4', 'title': 'A wonderful adventure in France', 'text': "I loved this book all the way until the end. I have recently discovered that the author is intending to release another book, and from what I understand it will continue where this one left off. I am thankful for this, as the way this book ended was definitely a negative for me. I wanted to know more! What happened to the author, did she learn what she came to learn? Did she get the job she was hoping for? So many questions.<br /><br />From the beginning of Linda's book, it is easy to love her. She is open, honest and definitely has the type of personality you want your heroine to have, whether the book is fiction or reality. I couldn't help but root for Linda throughout her trials with her host family, even when I thought she acted as a bit of a brat herself. Listening to her internal thoughts about what she went through and her desire to achieve her goals made this book feel close to my heart.<br /><br />I applaud the adventurous spirit of the author and her decision to keep journal entries from that chapter of her life. What great material to have later to inspire a book! While I enjoyed the entire memoir, my favourite part of this book would have to be the author's descriptions of the many places she visited and the people she met along the way. While I think she could definitely have made a better impression on the family she worked for if she had been honest about her lack of French language skills from the beginning, she is a pioneer. Her drive and desire to learn the language from those in the actual country was inspiring. Not many people would have been gutsy enough to do what Linda did.<br /><br />I also particularly enjoyed the relationship between Linda and Antoine. The Kind heart of the author was apparent in her actions toward the children, even when she struggled with them.<br /><br />There is some romance, and I appreciated the way the author handled it. While sex scenes are not necessarily automatically offensive, there is something about memoirs that makes me uncomfortable if they are filled with them. This author manages to hint at her experiences without going into too much detail, leaving the reader to decide exactly what happened. Great writing.<br /><br />When you step into reading this book, you learn a lot about French customs, French cuisine and wine. You also get the opportunity to brush up on your French skills a bit and get to step outside yourself and live an adventure through the eyes of the author. I read this book in one sitting with very few breaks in between and found myself enthralled in the sights, sounds and atmosphere of this memoir.<br /><br />In the end, I was disappointed that the book ended. I could have kept reading about Linda's experiences without stopping anytime in the foreseeable future. The end of the book leaves many unanswered questions, that I am assuming the author will be answering in her next book. Were this a standalone, I would be very disappointed with the way the book ended, but with the knowledge that she is writing another book to continue with her story, I can't fault this one. One thing is for sure, if you read this book, you will be anxiously awaiting the next.<br /><br />I would recommend this to anyone who likes books about travel, memoirs or just a good story that came from the recollections and heart of the author. Read it, you will be glad you did. Overall, this was a VERY enjoyable read that gave me many reasons to wish I could drop everything and head off to France!", 'review_time': '2013-05-05 10:47:00', 'helpful_vote': '1', 'verified_purchase': '0', 'purchase_id': 'purchaseid_190'}, {'rating': '5', 'title': 'Best beginner book.  Been looking for something like this for a long time.', 'text': "Looked online for years for something like this.  It's the best I've seen.", 'review_time': '2020-08-12 11:06:00', 'helpful_vote': '0', 'verified_purchase': '1', 'purchase_id': 'purchaseid_8'}, {'rating': '4', 'title': 'Referance Guide', 'text': 'Good reference guide for the basics', 'review_time': '2014-11-13 18:55:00', 'helpful_vote': '0', 'verified_purchase': '1', 'purchase_id': 'purchaseid_178'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:18': {'books_count': 200, 'reviews_count': 1833, 'sample_books': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}], 'sample_reviews': [{'purchase_id': 'purchaseid_186', 'rating': '4'}, {'purchase_id': 'purchaseid_191', 'rating': '4'}, {'purchase_id': 'purchaseid_190', 'rating': '4'}]}, 'var_functions.execute_python:20': {'total_books_with_years': 191, 'decades': ['2000s', '1990s', '2010s', '2020s', '1980s', '1940s', '1930s', '1970s', '1920s'], 'books_per_decade': {'1920s': 1, '1930s': 4, '1940s': 1, '1970s': 2, '1980s': 11, '1990s': 16, '2000s': 47, '2010s': 88, '2020s': 21}, 'sample_books': [{'book_id': 'bookid_1', 'year': 2004, 'decade': '2000s'}, {'book_id': 'bookid_2', 'year': 1996, 'decade': '1990s'}, {'book_id': 'bookid_3', 'year': 2012, 'decade': '2010s'}, {'book_id': 'bookid_4', 'year': 2013, 'decade': '2010s'}, {'book_id': 'bookid_5', 'year': 2014, 'decade': '2010s'}]}, 'var_functions.execute_python:22': {'decades_analyzed': 0, 'decade_rankings': [], 'top_decade': None, 'total_reviews_processed': 0}}

exec(code, env_args)
