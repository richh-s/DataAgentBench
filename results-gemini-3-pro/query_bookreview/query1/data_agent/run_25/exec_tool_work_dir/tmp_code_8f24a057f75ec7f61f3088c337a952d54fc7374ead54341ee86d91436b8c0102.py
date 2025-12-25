code = """import json
import re

with open(locals()['var_function-call-2121501170623890719'], 'r') as f:
    books = json.load(f)

with open(locals()['var_function-call-18001450288197137579'], 'r') as f:
    reviews = json.load(f)

def get_id_num(s):
    parts = s.split('_')
    if len(parts) > 1 and parts[1].isdigit():
        return int(parts[1])
    return None

def extract_year(text):
    if not text:
        return None
    m = re.search(r'on\s+[A-Z][a-z]+\s+\d{1,2},\s+(\d{4})', text)
    if m:
        return int(m.group(1))
    years = re.findall(r'\b(19\d{2}|20\d{2})\b', text)
    if years:
        return int(years[0])
    return None

book_decade_map = {}
for b in books:
    bid = get_id_num(b.get('book_id', ''))
    if bid is not None:
        year = extract_year(b.get('details', ''))
        if year:
            decade = (year // 10) * 10
            book_decade_map[bid] = f"{decade}s"

# Calculate average rating per book first
book_ratings = {} # bid -> [ratings]

for r in reviews:
    pid = get_id_num(r.get('purchase_id', ''))
    if pid is not None and pid in book_decade_map:
        if pid not in book_ratings:
            book_ratings[pid] = []
        try:
            book_ratings[pid].append(float(r['rating']))
        except:
            pass

# Decade stats: list of book averages
decade_book_avgs = {}

for bid, ratings in book_ratings.items():
    avg = sum(ratings) / len(ratings)
    dec = book_decade_map[bid]
    if dec not in decade_book_avgs:
        decade_book_avgs[dec] = []
    decade_book_avgs[dec].append(avg)

results = []
for dec, avgs in decade_book_avgs.items():
    if len(avgs) >= 10:
        overall_avg = sum(avgs) / len(avgs)
        results.append({'decade': dec, 'avg_rating': overall_avg, 'num_books': len(avgs)})

results.sort(key=lambda x: x['avg_rating'], reverse=True)
print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-320067200377554574': ['books_info'], 'var_function-call-11943378612225912076': ['review'], 'var_function-call-14618173827546617959': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'var_function-call-4446095158176834776': [{'rating': '4', 'title': 'Ha! On me!  I thought this was a cookbook!', 'text': 'Lucky for me it\'s more than a cookbook.<br /><br />The story of a modern Daniel Boone, growing up in Michigan, one of three sons of a hunter.  Beginning at age eight when he shot a squirrel, to age 13 his first deer, then hunting his way through college, a career as a fur trapper, hunting sheep in Alaska, canoeing the Missouri River for deer and ending in Brooklyn age 37. Brooklyn?<br /><br />I especially liked that I share his disgust at catch & release fishing - if you fish it, you have to eat it - anything else is sadism (my words).<br /><br />My brother in law is the cook in the family and I wanted to see if this would be a good gift for him and I struck pay dirt following each chapter are "Tasting Notes" where the author speaks of cooking wild game.<br /><br />I also enjoyed it for the history of the land he has hunted as well as the history of the hunt (I too was a big Daniel Boone fan growing up!).<br /><br />I think more pictures (everything but dead things) would have made this a keeper.', 'review_time': '2012-11-24 18:52:00', 'helpful_vote': '0', 'verified_purchase': '0', 'purchase_id': 'purchaseid_186'}, {'rating': '4', 'title': 'Four Stars', 'text': 'Not as developed as Stephanie but I like the characters so far.', 'review_time': '2015-12-31 13:35:00', 'helpful_vote': '0', 'verified_purchase': '1', 'purchase_id': 'purchaseid_191'}, {'rating': '4', 'title': 'A wonderful adventure in France', 'text': "I loved this book all the way until the end. I have recently discovered that the author is intending to release another book, and from what I understand it will continue where this one left off. I am thankful for this, as the way this book ended was definitely a negative for me. I wanted to know more! What happened to the author, did she learn what she came to learn? Did she get the job she was hoping for? So many questions.<br /><br />From the beginning of Linda's book, it is easy to love her. She is open, honest and definitely has the type of personality you want your heroine to have, whether the book is fiction or reality. I couldn't help but root for Linda throughout her trials with her host family, even when I thought she acted as a bit of a brat herself. Listening to her internal thoughts about what she went through and her desire to achieve her goals made this book feel close to my heart.<br /><br />I applaud the adventurous spirit of the author and her decision to keep journal entries from that chapter of her life. What great material to have later to inspire a book! While I enjoyed the entire memoir, my favourite part of this book would have to be the author's descriptions of the many places she visited and the people she met along the way. While I think she could definitely have made a better impression on the family she worked for if she had been honest about her lack of French language skills from the beginning, she is a pioneer. Her drive and desire to learn the language from those in the actual country was inspiring. Not many people would have been gutsy enough to do what Linda did.<br /><br />I also particularly enjoyed the relationship between Linda and Antoine. The Kind heart of the author was apparent in her actions toward the children, even when she struggled with them.<br /><br />There is some romance, and I appreciated the way the author handled it. While sex scenes are not necessarily automatically offensive, there is something about memoirs that makes me uncomfortable if they are filled with them. This author manages to hint at her experiences without going into too much detail, leaving the reader to decide exactly what happened. Great writing.<br /><br />When you step into reading this book, you learn a lot about French customs, French cuisine and wine. You also get the opportunity to brush up on your French skills a bit and get to step outside yourself and live an adventure through the eyes of the author. I read this book in one sitting with very few breaks in between and found myself enthralled in the sights, sounds and atmosphere of this memoir.<br /><br />In the end, I was disappointed that the book ended. I could have kept reading about Linda's experiences without stopping anytime in the foreseeable future. The end of the book leaves many unanswered questions, that I am assuming the author will be answering in her next book. Were this a standalone, I would be very disappointed with the way the book ended, but with the knowledge that she is writing another book to continue with her story, I can't fault this one. One thing is for sure, if you read this book, you will be anxiously awaiting the next.<br /><br />I would recommend this to anyone who likes books about travel, memoirs or just a good story that came from the recollections and heart of the author. Read it, you will be glad you did. Overall, this was a VERY enjoyable read that gave me many reasons to wish I could drop everything and head off to France!", 'review_time': '2013-05-05 10:47:00', 'helpful_vote': '1', 'verified_purchase': '0', 'purchase_id': 'purchaseid_190'}, {'rating': '5', 'title': 'Best beginner book.  Been looking for something like this for a long time.', 'text': "Looked online for years for something like this.  It's the best I've seen.", 'review_time': '2020-08-12 11:06:00', 'helpful_vote': '0', 'verified_purchase': '1', 'purchase_id': 'purchaseid_8'}, {'rating': '4', 'title': 'Referance Guide', 'text': 'Good reference guide for the basics', 'review_time': '2014-11-13 18:55:00', 'helpful_vote': '0', 'verified_purchase': '1', 'purchase_id': 'purchaseid_178'}], 'var_function-call-8292174448986764558': [{'count': '200'}], 'var_function-call-4516742327513211206': [{'COUNT(*)': '1833'}], 'var_function-call-2121501170623890719': 'file_storage/function-call-2121501170623890719.json', 'var_function-call-18001450288197137579': 'file_storage/function-call-18001450288197137579.json', 'var_function-call-8049879981333925104': [{'decade': '2020s', 'avg_rating': 4.663636363636364, 'num_books': 21}, {'decade': '2010s', 'avg_rating': 4.606714628297362, 'num_books': 87}, {'decade': '2000s', 'avg_rating': 4.273684210526316, 'num_books': 46}, {'decade': '1980s', 'avg_rating': 4.225352112676056, 'num_books': 10}, {'decade': '1990s', 'avg_rating': 3.8208955223880596, 'num_books': 16}]}

exec(code, env_args)
