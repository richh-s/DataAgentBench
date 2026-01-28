code = """import json
import re
from collections import defaultdict

# Read data
books_file = locals()['var_functions.query_db:16']
reviews_file = locals()['var_functions.query_db:10']

with open(books_file, 'r') as f:
    books = json.load(f)

with open(reviews_file, 'r') as f:
    reviews = json.load(f)

# Create book lookup by numeric ID
book_lookup = {}
book_counts = defaultdict(int)

for book in books:
    details = book.get('details', '') or ''
    year_match = re.search(r'(19\d{2}|20[0-2]\d)', details)
    
    if year_match:
        year = int(year_match.group(1))
        decade = str(year // 10 * 10) + "s"
        book_counts[decade] += 1
        
        book_id_match = re.search(r'bookid_(\d+)', book['book_id'])
        if book_id_match:
            book_id_num = int(book_id_match.group(1))
            book_lookup[book_id_num] = {'book_id': book['book_id'], 'decade': decade}

# Match reviews and calculate decade ratings
rated_books_per_decade = defaultdict(set)
decade_ratings = defaultdict(list)
matched_reviews = 0

for review in reviews:
    purchase_match = re.search(r'purchaseid_(\d+)', review.get('purchase_id', ''))
    if not purchase_match:
        continue
    
    purchase_id_num = int(purchase_match.group(1))
    rating = float(review['rating'])
    
    if purchase_id_num in book_lookup:
        decade = book_lookup[purchase_id_num]['decade']
        book_id = book_lookup[purchase_id_num]['book_id']
        
        decade_ratings[decade].append(rating)
        rated_books_per_decade[decade].add(book_id)
        matched_reviews += 1

# Find decades meeting criteria (>=10 distinct books with ratings)
eligible_decades = []

for decade in sorted(decade_ratings.keys()):
    ratings = decade_ratings[decade]
    distinct_books = len(rated_books_per_decade[decade])
    
    if distinct_books >= 10:
        avg_rating = sum(ratings) / len(ratings)
        eligible_decades.append({
            'decade': decade,
            'avg_rating': round(avg_rating, 2),
            'distinct_books': distinct_books,
            'rating_count': len(ratings)
        })

# Sort by average rating descending
eligible_decades.sort(key=lambda x: x['avg_rating'], reverse=True)

# Determine winner
winner = None
winner_rating = None

if eligible_decades:
    winner = eligible_decades[0]
    winner_decade = winner['decade']
    winner_rating = winner['avg_rating']

# Return final result
print('__RESULT__:')
print(json.dumps({
    'winner_decade': winner_decade if winner else None,
    'winner_rating': winner_rating
}))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['books_info'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'rating': '4', 'title': 'Ha! On me!  I thought this was a cookbook!', 'text': 'Lucky for me it\'s more than a cookbook.<br /><br />The story of a modern Daniel Boone, growing up in Michigan, one of three sons of a hunter.  Beginning at age eight when he shot a squirrel, to age 13 his first deer, then hunting his way through college, a career as a fur trapper, hunting sheep in Alaska, canoeing the Missouri River for deer and ending in Brooklyn age 37. Brooklyn?<br /><br />I especially liked that I share his disgust at catch & release fishing - if you fish it, you have to eat it - anything else is sadism (my words).<br /><br />My brother in law is the cook in the family and I wanted to see if this would be a good gift for him and I struck pay dirt following each chapter are "Tasting Notes" where the author speaks of cooking wild game.<br /><br />I also enjoyed it for the history of the land he has hunted as well as the history of the hunt (I too was a big Daniel Boone fan growing up!).<br /><br />I think more pictures (everything but dead things) would have made this a keeper.', 'review_time': '2012-11-24 18:52:00', 'helpful_vote': '0', 'verified_purchase': '0', 'purchase_id': 'purchaseid_186'}, {'rating': '4', 'title': 'Four Stars', 'text': 'Not as developed as Stephanie but I like the characters so far.', 'review_time': '2015-12-31 13:35:00', 'helpful_vote': '0', 'verified_purchase': '1', 'purchase_id': 'purchaseid_191'}, {'rating': '4', 'title': 'A wonderful adventure in France', 'text': "I loved this book all the way until the end. I have recently discovered that the author is intending to release another book, and from what I understand it will continue where this one left off. I am thankful for this, as the way this book ended was definitely a negative for me. I wanted to know more! What happened to the author, did she learn what she came to learn? Did she get the job she was hoping for? So many questions.<br /><br />From the beginning of Linda's book, it is easy to love her. She is open, honest and definitely has the type of personality you want your heroine to have, whether the book is fiction or reality. I couldn't help but root for Linda throughout her trials with her host family, even when I thought she acted as a bit of a brat herself. Listening to her internal thoughts about what she went through and her desire to achieve her goals made this book feel close to my heart.<br /><br />I applaud the adventurous spirit of the author and her decision to keep journal entries from that chapter of her life. What great material to have later to inspire a book! While I enjoyed the entire memoir, my favourite part of this book would have to be the author's descriptions of the many places she visited and the people she met along the way. While I think she could definitely have made a better impression on the family she worked for if she had been honest about her lack of French language skills from the beginning, she is a pioneer. Her drive and desire to learn the language from those in the actual country was inspiring. Not many people would have been gutsy enough to do what Linda did.<br /><br />I also particularly enjoyed the relationship between Linda and Antoine. The Kind heart of the author was apparent in her actions toward the children, even when she struggled with them.<br /><br />There is some romance, and I appreciated the way the author handled it. While sex scenes are not necessarily automatically offensive, there is something about memoirs that makes me uncomfortable if they are filled with them. This author manages to hint at her experiences without going into too much detail, leaving the reader to decide exactly what happened. Great writing.<br /><br />When you step into reading this book, you learn a lot about French customs, French cuisine and wine. You also get the opportunity to brush up on your French skills a bit and get to step outside yourself and live an adventure through the eyes of the author. I read this book in one sitting with very few breaks in between and found myself enthralled in the sights, sounds and atmosphere of this memoir.<br /><br />In the end, I was disappointed that the book ended. I could have kept reading about Linda's experiences without stopping anytime in the foreseeable future. The end of the book leaves many unanswered questions, that I am assuming the author will be answering in her next book. Were this a standalone, I would be very disappointed with the way the book ended, but with the knowledge that she is writing another book to continue with her story, I can't fault this one. One thing is for sure, if you read this book, you will be anxiously awaiting the next.<br /><br />I would recommend this to anyone who likes books about travel, memoirs or just a good story that came from the recollections and heart of the author. Read it, you will be glad you did. Overall, this was a VERY enjoyable read that gave me many reasons to wish I could drop everything and head off to France!", 'review_time': '2013-05-05 10:47:00', 'helpful_vote': '1', 'verified_purchase': '0', 'purchase_id': 'purchaseid_190'}, {'rating': '5', 'title': 'Best beginner book.  Been looking for something like this for a long time.', 'text': "Looked online for years for something like this.  It's the best I've seen.", 'review_time': '2020-08-12 11:06:00', 'helpful_vote': '0', 'verified_purchase': '1', 'purchase_id': 'purchaseid_8'}, {'rating': '4', 'title': 'Referance Guide', 'text': 'Good reference guide for the basics', 'review_time': '2014-11-13 18:55:00', 'helpful_vote': '0', 'verified_purchase': '1', 'purchase_id': 'purchaseid_178'}], 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:14': {'status': 'success', 'total_books': 200, 'books_with_year': 191}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'total_books': 200, 'books_with_year': 191, 'total_reviews': 1000, 'matched_reviews': 1000, 'sample_matches': [{'book_id': 'bookid_186', 'purchase_id': 'purchaseid_186', 'title': 'Meat Eater: Adventures from the Life of an American Hunter', 'rating': 4.0, 'publication_year': 2012, 'decade': '2010s'}, {'book_id': 'bookid_191', 'purchase_id': 'purchaseid_191', 'title': 'Wicked Appetite (Lizzy and Diesel)', 'rating': 4.0, 'publication_year': 2015, 'decade': '2010s'}, {'book_id': 'bookid_190', 'purchase_id': 'purchaseid_190', 'title': 'French Illusions: My Story as an American Au Pair in the Loire Valley', 'rating': 4.0, 'publication_year': 2012, 'decade': '2010s'}, {'book_id': 'bookid_8', 'purchase_id': 'purchaseid_8', 'title': 'Make: Electronics: Learning Through Discovery', 'rating': 5.0, 'publication_year': 2015, 'decade': '2010s'}, {'book_id': 'bookid_178', 'purchase_id': 'purchaseid_178', 'title': 'Welding Symbols Quick Card (English and Ukrainian Edition)', 'rating': 4.0, 'publication_year': 2010, 'decade': '2010s'}, {'book_id': 'bookid_186', 'purchase_id': 'purchaseid_186', 'title': 'Meat Eater: Adventures from the Life of an American Hunter', 'rating': 4.0, 'publication_year': 2012, 'decade': '2010s'}, {'book_id': 'bookid_76', 'purchase_id': 'purchaseid_76', 'title': 'Coffee Cup Cozies (Christmas Crochet Book 1)', 'rating': 5.0, 'publication_year': 2013, 'decade': '2010s'}, {'book_id': 'bookid_186', 'purchase_id': 'purchaseid_186', 'title': 'Meat Eater: Adventures from the Life of an American Hunter', 'rating': 4.0, 'publication_year': 2012, 'decade': '2010s'}, {'book_id': 'bookid_115', 'purchase_id': 'purchaseid_115', 'title': 'The Mid-Atlantic Championship', 'rating': 5.0, 'publication_year': 2019, 'decade': '2010s'}, {'book_id': 'bookid_167', 'purchase_id': 'purchaseid_167', 'title': 'Dead Silence', 'rating': 2.0, 'publication_year': 2020, 'decade': '2020s'}]}, 'var_functions.execute_python:24': {'decades': [{'decade': '2010s', 'avg_rating': 4.61, 'rating_count': 698, 'distinct_books': 82}, {'decade': '2020s', 'avg_rating': 4.59, 'rating_count': 58, 'distinct_books': 18}, {'decade': '2000s', 'avg_rating': 4.14, 'rating_count': 139, 'distinct_books': 40}, {'decade': '1990s', 'avg_rating': 4.12, 'rating_count': 43, 'distinct_books': 15}], 'top_decade': '2010s', 'top_rating': 4.61}}

exec(code, env_args)
