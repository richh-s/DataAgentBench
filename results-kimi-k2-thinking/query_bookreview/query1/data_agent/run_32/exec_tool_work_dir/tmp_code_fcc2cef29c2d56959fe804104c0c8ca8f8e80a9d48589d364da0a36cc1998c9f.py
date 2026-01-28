code = """import json
import re
from collections import defaultdict
import math

# Read the stored JSON files
with open('file_storage/functions.query_db:24.json', 'r') as f:
    books_data = json.load(f)

with open('file_storage/functions.query_db:12.json', 'r') as f:
    reviews_data = json.load(f)

# Extract publication years from book details
book_years = {}
year_pattern = re.compile(r'(?:published|released|edition) on (?:[A-Za-z]+ )?(\d{1,2}, )?(\d{4})', re.IGNORECASE)

for book in books_data:
    book_id = book['book_id']
    details = book['details']
    
    # Try to find year in details text
    match = year_pattern.search(details)
    if match:
        # Get the year from the match
        year_str = match.group(2)
        try:
            year = int(year_str)
            book_years[book_id] = year
        except:
            continue
    else:
        # Try alternative patterns
        alt_patterns = [
            r'(?:January|February|March|April|May|June|July|August|September|October|November|December)[\s,]+\d{1,2}[\s,]+(\d{4})',
            r'published in (\d{4})',
            r'first edition on (\d{4})'
        ]
        for pattern in alt_patterns:
            match = re.search(pattern, details, re.IGNORECASE)
            if match:
                try:
                    year = int(match.group(1))
                    book_years[book_id] = year
                    break
                except:
                    continue

# Group reviews by book_id and calculate average ratings
book_reviews = defaultdict(list)
for review in reviews_data:
    purchase_id = review['purchase_id']
    rating = float(review['rating'])
    book_id = purchase_id.replace('purchaseid_', 'bookid_')
    book_reviews[book_id].append(rating)

# Calculate average rating per book
book_avg_ratings = {}
for book_id, ratings in book_reviews.items():
    book_avg_ratings[book_id] = sum(ratings) / len(ratings)

# Group books by decade and calculate statistics
decade_stats = defaultdict(lambda: {'total_rating': 0, 'count': 0, 'books': set()})

for book_id, year in book_years.items():
    if year > 1000 and year <= 2023:  # Filter out invalid years
        decade = (year // 10) * 10
        if book_id in book_avg_ratings:
            decade_stats[decade]['total_rating'] += book_avg_ratings[book_id]
            decade_stats[decade]['count'] += 1
            decade_stats[decade]['books'].add(book_id)

# Filter decades with at least 10 distinct books and find the highest average
valid_decades = []
for decade, stats in decade_stats.items():
    if len(stats['books']) >= 10:
        avg_rating = stats['total_rating'] / stats['count']
        valid_decades.append({
            'decade': f"{decade}s",
            'avg_rating': avg_rating,
            'num_books': len(stats['books']),
            'total_reviews': stats['count']
        })

# Sort by average rating
decades_sorted = sorted(valid_decades, key=lambda x: x['avg_rating'], reverse=True)

print('__RESULT__:')
print(json.dumps({
    'decades_analyzed': len(valid_decades),
    'highest_decade': decades_sorted[0] if decades_sorted else None,
    'all_decades': decades_sorted
}))"""

env_args = {'var_functions.list_db:0': ['books_info'], 'var_functions.list_db:2': ['review'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'rating': '4', 'title': 'Ha! On me!  I thought this was a cookbook!', 'text': 'Lucky for me it\'s more than a cookbook.<br /><br />The story of a modern Daniel Boone, growing up in Michigan, one of three sons of a hunter.  Beginning at age eight when he shot a squirrel, to age 13 his first deer, then hunting his way through college, a career as a fur trapper, hunting sheep in Alaska, canoeing the Missouri River for deer and ending in Brooklyn age 37. Brooklyn?<br /><br />I especially liked that I share his disgust at catch & release fishing - if you fish it, you have to eat it - anything else is sadism (my words).<br /><br />My brother in law is the cook in the family and I wanted to see if this would be a good gift for him and I struck pay dirt following each chapter are "Tasting Notes" where the author speaks of cooking wild game.<br /><br />I also enjoyed it for the history of the land he has hunted as well as the history of the hunt (I too was a big Daniel Boone fan growing up!).<br /><br />I think more pictures (everything but dead things) would have made this a keeper.', 'review_time': '2012-11-24 18:52:00', 'helpful_vote': '0', 'verified_purchase': '0', 'purchase_id': 'purchaseid_186'}, {'rating': '4', 'title': 'Four Stars', 'text': 'Not as developed as Stephanie but I like the characters so far.', 'review_time': '2015-12-31 13:35:00', 'helpful_vote': '0', 'verified_purchase': '1', 'purchase_id': 'purchaseid_191'}, {'rating': '4', 'title': 'A wonderful adventure in France', 'text': "I loved this book all the way until the end. I have recently discovered that the author is intending to release another book, and from what I understand it will continue where this one left off. I am thankful for this, as the way this book ended was definitely a negative for me. I wanted to know more! What happened to the author, did she learn what she came to learn? Did she get the job she was hoping for? So many questions.<br /><br />From the beginning of Linda's book, it is easy to love her. She is open, honest and definitely has the type of personality you want your heroine to have, whether the book is fiction or reality. I couldn't help but root for Linda throughout her trials with her host family, even when I thought she acted as a bit of a brat herself. Listening to her internal thoughts about what she went through and her desire to achieve her goals made this book feel close to my heart.<br /><br />I applaud the adventurous spirit of the author and her decision to keep journal entries from that chapter of her life. What great material to have later to inspire a book! While I enjoyed the entire memoir, my favourite part of this book would have to be the author's descriptions of the many places she visited and the people she met along the way. While I think she could definitely have made a better impression on the family she worked for if she had been honest about her lack of French language skills from the beginning, she is a pioneer. Her drive and desire to learn the language from those in the actual country was inspiring. Not many people would have been gutsy enough to do what Linda did.<br /><br />I also particularly enjoyed the relationship between Linda and Antoine. The Kind heart of the author was apparent in her actions toward the children, even when she struggled with them.<br /><br />There is some romance, and I appreciated the way the author handled it. While sex scenes are not necessarily automatically offensive, there is something about memoirs that makes me uncomfortable if they are filled with them. This author manages to hint at her experiences without going into too much detail, leaving the reader to decide exactly what happened. Great writing.<br /><br />When you step into reading this book, you learn a lot about French customs, French cuisine and wine. You also get the opportunity to brush up on your French skills a bit and get to step outside yourself and live an adventure through the eyes of the author. I read this book in one sitting with very few breaks in between and found myself enthralled in the sights, sounds and atmosphere of this memoir.<br /><br />In the end, I was disappointed that the book ended. I could have kept reading about Linda's experiences without stopping anytime in the foreseeable future. The end of the book leaves many unanswered questions, that I am assuming the author will be answering in her next book. Were this a standalone, I would be very disappointed with the way the book ended, but with the knowledge that she is writing another book to continue with her story, I can't fault this one. One thing is for sure, if you read this book, you will be anxiously awaiting the next.<br /><br />I would recommend this to anyone who likes books about travel, memoirs or just a good story that came from the recollections and heart of the author. Read it, you will be glad you did. Overall, this was a VERY enjoyable read that gave me many reasons to wish I could drop everything and head off to France!", 'review_time': '2013-05-05 10:47:00', 'helpful_vote': '1', 'verified_purchase': '0', 'purchase_id': 'purchaseid_190'}, {'rating': '5', 'title': 'Best beginner book.  Been looking for something like this for a long time.', 'text': "Looked online for years for something like this.  It's the best I've seen.", 'review_time': '2020-08-12 11:06:00', 'helpful_vote': '0', 'verified_purchase': '1', 'purchase_id': 'purchaseid_8'}, {'rating': '4', 'title': 'Referance Guide', 'text': 'Good reference guide for the basics', 'review_time': '2014-11-13 18:55:00', 'helpful_vote': '0', 'verified_purchase': '1', 'purchase_id': 'purchaseid_178'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:18': {'num_books': 38, 'num_reviews': 39, 'first_books': 'fi', 'first_reviews': 'fi'}, 'var_functions.execute_python:20': ['var_functions.list_db:0', 'var_functions.list_db:2', 'var_functions.query_db:5', 'var_functions.query_db:6', 'var_functions.query_db:8', 'var_functions.query_db:10', 'var_functions.query_db:12', 'var_functions.execute_python:18', '__builtins__', 'json'], 'var_functions.execute_python:22': {'num_books': 39, 'num_reviews': 39, 'sample_book': 'f', 'sample_review': 'f'}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'books_type': "<class 'str'>", 'reviews_type': "<class 'str'>", 'books_content': 'file_storage/functions.query_db:24.json', 'reviews_content': 'file_storage/functions.query_db:12.json'}}

exec(code, env_args)
