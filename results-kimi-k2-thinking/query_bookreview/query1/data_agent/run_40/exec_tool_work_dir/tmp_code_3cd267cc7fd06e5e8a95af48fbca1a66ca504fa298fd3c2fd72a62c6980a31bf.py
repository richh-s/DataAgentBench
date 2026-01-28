code = """import json
import re
from collections import defaultdict, Counter

# Access review data from storage
review_file = var_functions.query_db:8
book_file = var_functions.query_db:10

# Load both datasets
with open(review_file, 'r') as f:
    review_data = json.load(f)

with open(book_file, 'r') as f:
    book_data = json.load(f)

print('__RESULT__:')
print(f'Loaded {len(review_data)} reviews and {len(book_data)} books')

# Function to extract year from details string
def extract_year(details):
    # Look for 4-digit years between 1900-2023
    match = re.search(r'(19\d{2}|20[0-2]\d)', details)
    if match:
        return int(match.group(1))
    return None

# Extract years and create decade mapping
book_decade_map = {}
year_counts = defaultdict(int)
no_year_count = 0

print('\\nExtracting years from books...')
for book in book_data:
    year = extract_year(book['details'])
    if year:
        decade = (year // 10) * 10
        book_decade_map[book['book_id']] = decade
        year_counts[decade] += 1
    else:
        no_year_count += 1

print(f'Books with year extracted: {len(book_decade_map)}')
print(f'Books without year: {no_year_count}')

# Map purchase_id to book_id (they have similar format)
# purchase_id like "purchaseid_186" and book_id like "bookid_186"
purchase_to_book = {}
for review in review_data[:10]:  # Sample first few
    purchase_id = review['purchase_id']
    # Extract the number part
    match = re.search(r'(\\d+)$', purchase_id)
    if match:
        num = match.group(1)
        purchase_to_book[purchase_id] = f'bookid_{num}'

print('\\nSample ID mapping:')
for i, (purchase, book) in enumerate(list(purchase_to_book.items())[:5]):
    print(f'{purchase} -> {book}')

# Now process all reviews and match to books with decades
print('\\nProcessing reviews...')
decade_ratings = defaultdict(list)
book_decade_reviews = defaultdict(set)  # Track unique books per decade

for review in review_data:
    purchase_id = review['purchase_id']
    rating = float(review['rating'])
    
    # Convert purchase_id to book_id format
    match = re.search(r'(\\d+)$', purchase_id)
    if match:
        book_id = f'bookid_{match.group(1)}'
        
        # Check if this book has decade info
        if book_id in book_decade_map:
            decade = book_decade_map[book_id]
            decade_ratings[decade].append(rating)
            book_decade_reviews[decade].add(book_id)

print(f'Reviews matched to books with decade info: {sum(len(ratings) for ratings in decade_ratings.values())}')

# Calculate statistics per decade
results = []
for decade in sorted(decade_ratings.keys()):
    ratings = decade_ratings[decade]
    unique_books = len(book_decade_reviews[decade])
    
    if unique_books >= 10:  # Only include decades with at least 10 distinct books
        avg_rating = sum(ratings) / len(ratings)
        results.append({
            'decade': f'{decade}s',
            'avg_rating': round(avg_rating, 3),
            'unique_books': unique_books,
            'total_ratings': len(ratings)
        })

print('\\nDecades with at least 10 books:')
for r in results:
    print(f"{r['decade']}: avg={r['avg_rating']}, books={r['unique_books']}, ratings={r['total_ratings']}")

# Find decade with highest average rating
if results:
    best = max(results, key=lambda x: x['avg_rating'])
    print(f'\\nBest decade: {best["decade"]} with average rating {best["avg_rating"]}')
    print(f'Based on {best["unique_books"]} unique books and {best["total_ratings"]} total ratings')
else:
    print('\\nNo decades found with at least 10 books')"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['books_info'], 'var_functions.query_db:4': [{'rating': '4', 'title': 'Ha! On me!  I thought this was a cookbook!', 'text': 'Lucky for me it\'s more than a cookbook.<br /><br />The story of a modern Daniel Boone, growing up in Michigan, one of three sons of a hunter.  Beginning at age eight when he shot a squirrel, to age 13 his first deer, then hunting his way through college, a career as a fur trapper, hunting sheep in Alaska, canoeing the Missouri River for deer and ending in Brooklyn age 37. Brooklyn?<br /><br />I especially liked that I share his disgust at catch & release fishing - if you fish it, you have to eat it - anything else is sadism (my words).<br /><br />My brother in law is the cook in the family and I wanted to see if this would be a good gift for him and I struck pay dirt following each chapter are "Tasting Notes" where the author speaks of cooking wild game.<br /><br />I also enjoyed it for the history of the land he has hunted as well as the history of the hunt (I too was a big Daniel Boone fan growing up!).<br /><br />I think more pictures (everything but dead things) would have made this a keeper.', 'review_time': '2012-11-24 18:52:00', 'helpful_vote': '0', 'verified_purchase': '0', 'purchase_id': 'purchaseid_186'}, {'rating': '4', 'title': 'Four Stars', 'text': 'Not as developed as Stephanie but I like the characters so far.', 'review_time': '2015-12-31 13:35:00', 'helpful_vote': '0', 'verified_purchase': '1', 'purchase_id': 'purchaseid_191'}, {'rating': '4', 'title': 'A wonderful adventure in France', 'text': "I loved this book all the way until the end. I have recently discovered that the author is intending to release another book, and from what I understand it will continue where this one left off. I am thankful for this, as the way this book ended was definitely a negative for me. I wanted to know more! What happened to the author, did she learn what she came to learn? Did she get the job she was hoping for? So many questions.<br /><br />From the beginning of Linda's book, it is easy to love her. She is open, honest and definitely has the type of personality you want your heroine to have, whether the book is fiction or reality. I couldn't help but root for Linda throughout her trials with her host family, even when I thought she acted as a bit of a brat herself. Listening to her internal thoughts about what she went through and her desire to achieve her goals made this book feel close to my heart.<br /><br />I applaud the adventurous spirit of the author and her decision to keep journal entries from that chapter of her life. What great material to have later to inspire a book! While I enjoyed the entire memoir, my favourite part of this book would have to be the author's descriptions of the many places she visited and the people she met along the way. While I think she could definitely have made a better impression on the family she worked for if she had been honest about her lack of French language skills from the beginning, she is a pioneer. Her drive and desire to learn the language from those in the actual country was inspiring. Not many people would have been gutsy enough to do what Linda did.<br /><br />I also particularly enjoyed the relationship between Linda and Antoine. The Kind heart of the author was apparent in her actions toward the children, even when she struggled with them.<br /><br />There is some romance, and I appreciated the way the author handled it. While sex scenes are not necessarily automatically offensive, there is something about memoirs that makes me uncomfortable if they are filled with them. This author manages to hint at her experiences without going into too much detail, leaving the reader to decide exactly what happened. Great writing.<br /><br />When you step into reading this book, you learn a lot about French customs, French cuisine and wine. You also get the opportunity to brush up on your French skills a bit and get to step outside yourself and live an adventure through the eyes of the author. I read this book in one sitting with very few breaks in between and found myself enthralled in the sights, sounds and atmosphere of this memoir.<br /><br />In the end, I was disappointed that the book ended. I could have kept reading about Linda's experiences without stopping anytime in the foreseeable future. The end of the book leaves many unanswered questions, that I am assuming the author will be answering in her next book. Were this a standalone, I would be very disappointed with the way the book ended, but with the knowledge that she is writing another book to continue with her story, I can't fault this one. One thing is for sure, if you read this book, you will be anxiously awaiting the next.<br /><br />I would recommend this to anyone who likes books about travel, memoirs or just a good story that came from the recollections and heart of the author. Read it, you will be glad you did. Overall, this was a VERY enjoyable read that gave me many reasons to wish I could drop everything and head off to France!", 'review_time': '2013-05-05 10:47:00', 'helpful_vote': '1', 'verified_purchase': '0', 'purchase_id': 'purchaseid_190'}, {'rating': '5', 'title': 'Best beginner book.  Been looking for something like this for a long time.', 'text': "Looked online for years for something like this.  It's the best I've seen.", 'review_time': '2020-08-12 11:06:00', 'helpful_vote': '0', 'verified_purchase': '1', 'purchase_id': 'purchaseid_8'}, {'rating': '4', 'title': 'Referance Guide', 'text': 'Good reference guide for the basics', 'review_time': '2014-11-13 18:55:00', 'helpful_vote': '0', 'verified_purchase': '1', 'purchase_id': 'purchaseid_178'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
