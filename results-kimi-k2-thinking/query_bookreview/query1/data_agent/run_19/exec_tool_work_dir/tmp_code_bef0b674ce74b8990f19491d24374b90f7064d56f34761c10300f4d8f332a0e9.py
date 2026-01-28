code = """import json
import re

# Read data from files
books_file = locals()['var_functions.query_db:16']
reviews_file = locals()['var_functions.query_db:10']

with open(books_file, 'r') as f:
    books = json.load(f)

with open(reviews_file, 'r') as f:
    reviews = json.load(f)

# Extract publication year from books
books_with_years = []
for book in books:
    details = book.get('details', '') or ''
    # Look for 4-digit years between 1900-2023
    year_matches = re.findall(r'(19\d{2}|20[0-2]\d)', details)
    
    year = None
    if year_matches:
        # Take the first year found (most likely publication year)
        year = int(year_matches[0])
    
    # Extract numeric part of book_id
    book_id_num = None
    book_id_match = re.search(r'bookid_(\d+)', book['book_id'])
    if book_id_match:
        book_id_num = int(book_id_match.group(1))
    
    books_with_years.append({
        'book_id': book['book_id'],
        'book_id_num': book_id_num,
        'title': book['title'],
        'publication_year': year,
        'decade': f"{year//10*10}s" if year else None
    })

# Extract numeric part from purchase_id in reviews
reviews_with_nums = []
for review in reviews:
    purchase_id = review.get('purchase_id', '')
    purchase_id_num = None
    purchase_match = re.search(r'purchaseid_(\d+)', purchase_id)
    if purchase_match:
        purchase_id_num = int(purchase_match.group(1))
    
    reviews_with_nums.append({
        'purchase_id': purchase_id,
        'purchase_id_num': purchase_id_num,
        'rating': float(review['rating']),
        'title': review['title']
    })

# Try direct matching first
matched_reviews = []
for review in reviews_with_nums:
    for book in books_with_years:
        if review['purchase_id_num'] == book['book_id_num']:
            matched_reviews.append({
                'book_id': book['book_id'],
                'purchase_id': review['purchase_id'],
                'title': book['title'],
                'rating': review['rating'],
                'publication_year': book['publication_year'],
                'decade': book['decade']
            })

# Statistics
books_with_year_count = len([b for b in books_with_years if b['publication_year']])
total_books = len(books)
total_reviews = len(reviews)
matched_count = len(matched_reviews)

print(f'Total books: {total_books}', flush=True)
print(f'Books with publication year: {books_with_year_count}', flush=True)
print(f'Total reviews: {total_reviews}', flush=True)
print(f'Matched reviews to books: {matched_count}', flush=True)

# Show some examples
print('Sample matched reviews:', flush=True)
for i, mr in enumerate(matched_reviews[:10]):
    print(f"  {i}: {mr['book_id']} <-> {mr['purchase_id']} - {mr['title']} - {mr['publication_year']} - Rating: {mr['rating']}", flush=True)

print('__RESULT__:')
print(json.dumps({
    'total_books': total_books,
    'books_with_year': books_with_year_count,
    'total_reviews': total_reviews,
    'matched_reviews': matched_count,
    'sample_matches': matched_reviews[:10]
}))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['books_info'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'rating': '4', 'title': 'Ha! On me!  I thought this was a cookbook!', 'text': 'Lucky for me it\'s more than a cookbook.<br /><br />The story of a modern Daniel Boone, growing up in Michigan, one of three sons of a hunter.  Beginning at age eight when he shot a squirrel, to age 13 his first deer, then hunting his way through college, a career as a fur trapper, hunting sheep in Alaska, canoeing the Missouri River for deer and ending in Brooklyn age 37. Brooklyn?<br /><br />I especially liked that I share his disgust at catch & release fishing - if you fish it, you have to eat it - anything else is sadism (my words).<br /><br />My brother in law is the cook in the family and I wanted to see if this would be a good gift for him and I struck pay dirt following each chapter are "Tasting Notes" where the author speaks of cooking wild game.<br /><br />I also enjoyed it for the history of the land he has hunted as well as the history of the hunt (I too was a big Daniel Boone fan growing up!).<br /><br />I think more pictures (everything but dead things) would have made this a keeper.', 'review_time': '2012-11-24 18:52:00', 'helpful_vote': '0', 'verified_purchase': '0', 'purchase_id': 'purchaseid_186'}, {'rating': '4', 'title': 'Four Stars', 'text': 'Not as developed as Stephanie but I like the characters so far.', 'review_time': '2015-12-31 13:35:00', 'helpful_vote': '0', 'verified_purchase': '1', 'purchase_id': 'purchaseid_191'}, {'rating': '4', 'title': 'A wonderful adventure in France', 'text': "I loved this book all the way until the end. I have recently discovered that the author is intending to release another book, and from what I understand it will continue where this one left off. I am thankful for this, as the way this book ended was definitely a negative for me. I wanted to know more! What happened to the author, did she learn what she came to learn? Did she get the job she was hoping for? So many questions.<br /><br />From the beginning of Linda's book, it is easy to love her. She is open, honest and definitely has the type of personality you want your heroine to have, whether the book is fiction or reality. I couldn't help but root for Linda throughout her trials with her host family, even when I thought she acted as a bit of a brat herself. Listening to her internal thoughts about what she went through and her desire to achieve her goals made this book feel close to my heart.<br /><br />I applaud the adventurous spirit of the author and her decision to keep journal entries from that chapter of her life. What great material to have later to inspire a book! While I enjoyed the entire memoir, my favourite part of this book would have to be the author's descriptions of the many places she visited and the people she met along the way. While I think she could definitely have made a better impression on the family she worked for if she had been honest about her lack of French language skills from the beginning, she is a pioneer. Her drive and desire to learn the language from those in the actual country was inspiring. Not many people would have been gutsy enough to do what Linda did.<br /><br />I also particularly enjoyed the relationship between Linda and Antoine. The Kind heart of the author was apparent in her actions toward the children, even when she struggled with them.<br /><br />There is some romance, and I appreciated the way the author handled it. While sex scenes are not necessarily automatically offensive, there is something about memoirs that makes me uncomfortable if they are filled with them. This author manages to hint at her experiences without going into too much detail, leaving the reader to decide exactly what happened. Great writing.<br /><br />When you step into reading this book, you learn a lot about French customs, French cuisine and wine. You also get the opportunity to brush up on your French skills a bit and get to step outside yourself and live an adventure through the eyes of the author. I read this book in one sitting with very few breaks in between and found myself enthralled in the sights, sounds and atmosphere of this memoir.<br /><br />In the end, I was disappointed that the book ended. I could have kept reading about Linda's experiences without stopping anytime in the foreseeable future. The end of the book leaves many unanswered questions, that I am assuming the author will be answering in her next book. Were this a standalone, I would be very disappointed with the way the book ended, but with the knowledge that she is writing another book to continue with her story, I can't fault this one. One thing is for sure, if you read this book, you will be anxiously awaiting the next.<br /><br />I would recommend this to anyone who likes books about travel, memoirs or just a good story that came from the recollections and heart of the author. Read it, you will be glad you did. Overall, this was a VERY enjoyable read that gave me many reasons to wish I could drop everything and head off to France!", 'review_time': '2013-05-05 10:47:00', 'helpful_vote': '1', 'verified_purchase': '0', 'purchase_id': 'purchaseid_190'}, {'rating': '5', 'title': 'Best beginner book.  Been looking for something like this for a long time.', 'text': "Looked online for years for something like this.  It's the best I've seen.", 'review_time': '2020-08-12 11:06:00', 'helpful_vote': '0', 'verified_purchase': '1', 'purchase_id': 'purchaseid_8'}, {'rating': '4', 'title': 'Referance Guide', 'text': 'Good reference guide for the basics', 'review_time': '2014-11-13 18:55:00', 'helpful_vote': '0', 'verified_purchase': '1', 'purchase_id': 'purchaseid_178'}], 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:14': {'status': 'success', 'total_books': 200, 'books_with_year': 191}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
