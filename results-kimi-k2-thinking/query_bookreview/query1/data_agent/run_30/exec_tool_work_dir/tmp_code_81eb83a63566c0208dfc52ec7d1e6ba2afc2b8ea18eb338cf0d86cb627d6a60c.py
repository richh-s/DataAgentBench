code = """import json
import re

# Access the books data
books_storage = locals()['var_functions.query_db:2']

# Load books data (it's stored in a file)
if isinstance(books_storage, str) and books_storage.endswith('.json'):
    with open(books_storage, 'r') as f:
        books_data = json.load(f)
else:
    books_data = books_storage

print(f'Loaded {len(books_data)} books')

# Extract publication years from details field
year_book_mapping = []
no_year_count = 0

for book in books_data:
    details = book.get('details', '')
    if not details:
        no_year_count += 1
        continue
    
    # Look for 4-digit year patterns
    year_match = re.search(r'(\d{4})', details)
    if year_match:
        year = int(year_match.group(1))
        # Check if it's a reasonable publication year
        if 1900 <= year <= 2030:
            year_book_mapping.append({
                'book_id': book['book_id'],
                'title': book['title'],
                'year': year,
                'decade': str(year//10*10) + 's'
            })
        else:
            no_year_count += 1
    else:
        no_year_count += 1

print(f'Successfully extracted years for {len(year_book_mapping)} books')
print(f'Failed to extract year for {no_year_count} books')

if year_book_mapping:
    years = [item['year'] for item in year_book_mapping]
    print(f'Year range: {min(years)} - {max(years)}')

# Now load the review data to get ratings
review_storage = locals()['var_functions.query_db:9']
if isinstance(review_storage, str) and review_storage.endswith('.json'):
    with open(review_storage, 'r') as f:
        review_data = json.load(f)
else:
    review_data = review_storage

print(f'\nLoaded {len(review_data)} reviews')

# Create mapping of purchase_id to rating
purchase_rating_map = {}
for review in review_data:
    purchase_id = review.get('purchase_id')
    rating_str = review.get('rating', '0')
    try:
        rating = float(rating_str)
    except (ValueError, TypeError):
        rating = 0.0
    
    if purchase_id:
        if purchase_id not in purchase_rating_map:
            purchase_rating_map[purchase_id] = []
        purchase_rating_map[purchase_id].append(rating)

print(f'Found {len(purchase_rating_map)} unique books with reviews')

# Match books with their reviews and calculate average rating per decade
from collections import defaultdict

decade_stats = defaultdict(lambda: {'total_rating': 0, 'review_count': 0, 'books': set()})

for book in year_book_mapping:
    book_id = book['book_id']
    # Extract numeric part from book_id (e.g., "bookid_1" -> "1")
    book_id_match = re.search(r'bookid_(\d+)', book_id)
    if book_id_match:
        book_num = book_id_match.group(1)
        # Look for purchase_id containing the same number
        for purchase_id, ratings in purchase_rating_map.items():
            if book_num in purchase_id:
                avg_rating = sum(ratings) / len(ratings)
                decade = book['decade']
                decade_stats[decade]['total_rating'] += avg_rating
                decade_stats[decade]['review_count'] += len(ratings)
                decade_stats[decade]['books'].add(book_id)
                break  # Found match, move to next book

# Filter decades with at least 10 distinct books and calculate average
decade_results = []
for decade, stats in decade_stats.items():
    book_count = len(stats['books'])
    if book_count >= 10:
        avg_rating = stats['total_rating'] / book_count
        decade_results.append({
            'decade': decade,
            'avg_rating': round(avg_rating, 2),
            'book_count': book_count,
            'total_reviews': stats['review_count']
        })

# Sort by average rating
decade_results.sort(key=lambda x: x['avg_rating'], reverse=True)

print('\nDecade statistics (with at least 10 books):')
for result in decade_results:
    print(str(result['decade']) + ': ' + str(result['avg_rating']) + ' avg rating, ' + 
          str(result['book_count']) + ' books, ' + str(result['total_reviews']) + ' reviews')

# Return the top decade
if decade_results:
    top_decade = decade_results[0]['decade']
    print('\nTop decade: ' + top_decade)
else:
    print('\nNo decades found with at least 10 books')
    top_decade = None

# Print results in JSON format
output = {
    'top_decade': top_decade,
    'decade_rankings': decade_results
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['books_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['review'], 'var_functions.query_db:9': [{'rating': '4', 'title': 'Ha! On me!  I thought this was a cookbook!', 'text': 'Lucky for me it\'s more than a cookbook.<br /><br />The story of a modern Daniel Boone, growing up in Michigan, one of three sons of a hunter.  Beginning at age eight when he shot a squirrel, to age 13 his first deer, then hunting his way through college, a career as a fur trapper, hunting sheep in Alaska, canoeing the Missouri River for deer and ending in Brooklyn age 37. Brooklyn?<br /><br />I especially liked that I share his disgust at catch & release fishing - if you fish it, you have to eat it - anything else is sadism (my words).<br /><br />My brother in law is the cook in the family and I wanted to see if this would be a good gift for him and I struck pay dirt following each chapter are "Tasting Notes" where the author speaks of cooking wild game.<br /><br />I also enjoyed it for the history of the land he has hunted as well as the history of the hunt (I too was a big Daniel Boone fan growing up!).<br /><br />I think more pictures (everything but dead things) would have made this a keeper.', 'review_time': '2012-11-24 18:52:00', 'helpful_vote': '0', 'verified_purchase': '0', 'purchase_id': 'purchaseid_186'}, {'rating': '4', 'title': 'Four Stars', 'text': 'Not as developed as Stephanie but I like the characters so far.', 'review_time': '2015-12-31 13:35:00', 'helpful_vote': '0', 'verified_purchase': '1', 'purchase_id': 'purchaseid_191'}, {'rating': '4', 'title': 'A wonderful adventure in France', 'text': "I loved this book all the way until the end. I have recently discovered that the author is intending to release another book, and from what I understand it will continue where this one left off. I am thankful for this, as the way this book ended was definitely a negative for me. I wanted to know more! What happened to the author, did she learn what she came to learn? Did she get the job she was hoping for? So many questions.<br /><br />From the beginning of Linda's book, it is easy to love her. She is open, honest and definitely has the type of personality you want your heroine to have, whether the book is fiction or reality. I couldn't help but root for Linda throughout her trials with her host family, even when I thought she acted as a bit of a brat herself. Listening to her internal thoughts about what she went through and her desire to achieve her goals made this book feel close to my heart.<br /><br />I applaud the adventurous spirit of the author and her decision to keep journal entries from that chapter of her life. What great material to have later to inspire a book! While I enjoyed the entire memoir, my favourite part of this book would have to be the author's descriptions of the many places she visited and the people she met along the way. While I think she could definitely have made a better impression on the family she worked for if she had been honest about her lack of French language skills from the beginning, she is a pioneer. Her drive and desire to learn the language from those in the actual country was inspiring. Not many people would have been gutsy enough to do what Linda did.<br /><br />I also particularly enjoyed the relationship between Linda and Antoine. The Kind heart of the author was apparent in her actions toward the children, even when she struggled with them.<br /><br />There is some romance, and I appreciated the way the author handled it. While sex scenes are not necessarily automatically offensive, there is something about memoirs that makes me uncomfortable if they are filled with them. This author manages to hint at her experiences without going into too much detail, leaving the reader to decide exactly what happened. Great writing.<br /><br />When you step into reading this book, you learn a lot about French customs, French cuisine and wine. You also get the opportunity to brush up on your French skills a bit and get to step outside yourself and live an adventure through the eyes of the author. I read this book in one sitting with very few breaks in between and found myself enthralled in the sights, sounds and atmosphere of this memoir.<br /><br />In the end, I was disappointed that the book ended. I could have kept reading about Linda's experiences without stopping anytime in the foreseeable future. The end of the book leaves many unanswered questions, that I am assuming the author will be answering in her next book. Were this a standalone, I would be very disappointed with the way the book ended, but with the knowledge that she is writing another book to continue with her story, I can't fault this one. One thing is for sure, if you read this book, you will be anxiously awaiting the next.<br /><br />I would recommend this to anyone who likes books about travel, memoirs or just a good story that came from the recollections and heart of the author. Read it, you will be glad you did. Overall, this was a VERY enjoyable read that gave me many reasons to wish I could drop everything and head off to France!", 'review_time': '2013-05-05 10:47:00', 'helpful_vote': '1', 'verified_purchase': '0', 'purchase_id': 'purchaseid_190'}, {'rating': '5', 'title': 'Best beginner book.  Been looking for something like this for a long time.', 'text': "Looked online for years for something like this.  It's the best I've seen.", 'review_time': '2020-08-12 11:06:00', 'helpful_vote': '0', 'verified_purchase': '1', 'purchase_id': 'purchaseid_8'}, {'rating': '4', 'title': 'Referance Guide', 'text': 'Good reference guide for the basics', 'review_time': '2014-11-13 18:55:00', 'helpful_vote': '0', 'verified_purchase': '1', 'purchase_id': 'purchaseid_178'}]}

exec(code, env_args)
