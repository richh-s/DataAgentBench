code = """import json
import pandas as pd

# Load books data
books = locals()['var_function-call-6581685273077668953']

# Load reviews data from file
with open(locals()['var_function-call-6581685273077666796'], 'r') as f:
    reviews = json.load(f)

# Process books: Create a map from ID suffix to title
book_map = {}
for b in books:
    # book_id format: "bookid_X"
    try:
        suffix = b['book_id'].split('_')[1]
        book_map[suffix] = {'title': b['title'], 'ratings': []}
    except IndexError:
        continue

# Process reviews
for r in reviews:
    # purchase_id format: "purchaseid_X"
    try:
        pid = r['purchase_id']
        suffix = pid.split('_')[1]
        
        if suffix in book_map:
            rating = float(r['rating'])
            # Double check date just in case, though SQL handled it
            if r['review_time'] >= '2020-01-01':
                book_map[suffix]['ratings'].append(rating)
    except (IndexError, ValueError, KeyError):
        continue

# Calculate averages and filter
result_titles = []
for suffix, data in book_map.items():
    ratings = data['ratings']
    if ratings:
        avg_rating = sum(ratings) / len(ratings)
        if avg_rating >= 4.5:
            result_titles.append(data['title'])

print("__RESULT__:")
print(json.dumps(result_titles))"""

env_args = {'var_function-call-4678174813572187535': ['books_info'], 'var_function-call-4678174813572188118': ['review'], 'var_function-call-7217246715262370832': [{'book_id': 'bookid_1', 'title': 'Chaucer', 'categories': '["Books", "Literature & Fiction", "History & Criticism"]'}, {'book_id': 'bookid_2', 'title': 'Notes from a Kidwatcher', 'categories': '["Books", "Reference", "Words, Language & Grammar"]'}, {'book_id': 'bookid_3', 'title': 'Service: A Navy SEAL at War', 'categories': '["Books", "Biographies & Memoirs", "Leaders & Notable People"]'}, {'book_id': 'bookid_4', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_5', 'title': 'Parker & Knight', 'categories': '["Books", "Mystery, Thriller & Suspense", "Thrillers & Suspense"]'}], 'var_function-call-7217246715262371061': [{'purchase_id': 'purchaseid_186', 'rating': '4', 'review_time': '2012-11-24 18:52:00'}, {'purchase_id': 'purchaseid_191', 'rating': '4', 'review_time': '2015-12-31 13:35:00'}, {'purchase_id': 'purchaseid_190', 'rating': '4', 'review_time': '2013-05-05 10:47:00'}, {'purchase_id': 'purchaseid_8', 'rating': '5', 'review_time': '2020-08-12 11:06:00'}, {'purchase_id': 'purchaseid_178', 'rating': '4', 'review_time': '2014-11-13 18:55:00'}], 'var_function-call-6653206486902443680': [{'rating': '5', 'title': 'Great beginner reader.', 'text': 'My first grader loved this whole series and she can’t wait for the next one. Great beginning reader books who love silly zombie mutant stories.', 'review_time': '2021-03-29 08:10:00', 'helpful_vote': '0', 'verified_purchase': '1', 'purchase_id': 'purchaseid_4'}, {'rating': '5', 'title': 'Good series for boys.', 'text': "I help my neighbor kids with reading and homework and the nine year old boy loves the Dr. Roach books.  He doesn't know all the words but still enjoys the stories.  The illustrations provide clarity and humor.  We love Dr. Roach!  He liked the books so much that he took all four to school to show to his teacher and other kids.  It is a bonus that they are affordable.", 'review_time': '2013-11-05 07:53:00', 'helpful_vote': '1', 'verified_purchase': '1', 'purchase_id': 'purchaseid_4'}, {'rating': '4', 'title': 'Short, fun, easy for kids to read.', 'text': 'My six year old liked it.  He thought the book was &#34;awesome&#34;.  I agree that it is pretty good, but none of the books in the series (we read all of them) could compare in entertainment to the Attack of the Giant Hamster.', 'review_time': '2014-07-09 18:31:00', 'helpful_vote': '0', 'verified_purchase': '1', 'purchase_id': 'purchaseid_4'}, {'rating': '4', 'title': 'My 7 yo enjoyed it and got perfect AR test scores', 'text': "My 7 yo enjoyed it and got perfect AR test scores. I wished fun books like this would incorporate some facts so that they're also learning nonfiction", 'review_time': '2014-10-15 14:12:00', 'helpful_vote': '0', 'verified_purchase': '1', 'purchase_id': 'purchaseid_4'}, {'rating': '1', 'title': 'The book came in bad condition in order to be read as opposed to ...', 'text': 'The book came in bad condition in order to be read as opposed to &#34;very good condition&#34; as advertised.', 'review_time': '2016-08-08 15:22:00', 'helpful_vote': '0', 'verified_purchase': '0', 'purchase_id': 'purchaseid_4'}, {'rating': '3', 'title': 'Three Stars', 'text': 'Gift', 'review_time': '2014-10-10 12:11:23', 'helpful_vote': '0', 'verified_purchase': '1', 'purchase_id': 'purchaseid_4'}, {'rating': '5', 'title': 'Five Stars', 'text': 'My son loves this whole series', 'review_time': '2016-04-27 09:55:00', 'helpful_vote': '0', 'verified_purchase': '1', 'purchase_id': 'purchaseid_4'}, {'rating': '5', 'title': 'Great Read!', 'text': "Purchased as a Christmas gift for a nephew. He loved it. Couldn't put it down until he finished it. Bought the entire Mr. Roach series for him. This was his favorite.", 'review_time': '2014-02-16 11:37:00', 'helpful_vote': '0', 'verified_purchase': '1', 'purchase_id': 'purchaseid_4'}, {'rating': '5', 'title': 'Great1', 'text': 'Arrived well within the projected timeline.  My grandson is thrilled with it.  The book itself is in excellent physical condition.', 'review_time': '2014-06-23 08:18:00', 'helpful_vote': '0', 'verified_purchase': '0', 'purchase_id': 'purchaseid_4'}], 'var_function-call-6581685273077668953': [{'book_id': 'bookid_4', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still'}, {'book_id': 'bookid_14', 'title': 'The Old Man and the Pirate Princess'}, {'book_id': 'bookid_32', 'title': 'The Very Hungry Caterpillar (English and Arabic Edition)'}, {'book_id': 'bookid_40', 'title': 'Egypt (Enchantment of the World)'}, {'book_id': 'bookid_48', 'title': 'Clark the Shark: Tooth Trouble, No. 1'}, {'book_id': 'bookid_52', 'title': "I Hadn't Meant to Tell You This"}, {'book_id': 'bookid_54', 'title': 'Favorite Thorton W. Burgess Stories: 6 Books'}, {'book_id': 'bookid_55', 'title': 'Behind the Wheel (Choose Your Own Adventure #35)(Paperback/Revised)'}, {'book_id': 'bookid_57', 'title': "Goodnight Riley and the Moon, It's Almost Bedtime: Personalized Children’s Books, Personalized Gifts, and Bedtime Stories (A Magnificent Me! estorytime.com Series)"}, {'book_id': 'bookid_96', 'title': 'Cheer Up, Ben Franklin! (Young Historians)'}, {'book_id': 'bookid_99', 'title': 'Buddy the Soldier Bear'}, {'book_id': 'bookid_108', 'title': 'The Library Book'}, {'book_id': 'bookid_111', 'title': 'Can You Buy Me The Wind?'}, {'book_id': 'bookid_116', 'title': 'From the Earth to the Moon by Jules Verne, Fiction, Fantasy & Magic'}, {'book_id': 'bookid_120', 'title': "Caroline's Color Dreams: Los Sueños Coloridos De Carolina : Babl Children's Books in Spanish and English"}, {'book_id': 'bookid_124', 'title': 'Skeleton Play: A Fun, Rhyming Halloween Book for Kids! (1)'}, {'book_id': 'bookid_130', 'title': "Benny Goes To The Moon: The great new book from Top Children's entertainer Gerry Ogilvie (1)"}, {'book_id': 'bookid_132', 'title': 'Mae and Jane in the Rain'}, {'book_id': 'bookid_145', 'title': 'Kirsten: An American Girl : 1854 (The American Girls Collection/Boxed Set)'}, {'book_id': 'bookid_146', 'title': 'LunaLu the Llamacorn'}, {'book_id': 'bookid_149', 'title': 'Trouble in the CTC!: The Terra Prime Adventures Book 2'}, {'book_id': 'bookid_152', 'title': 'Around the World Mazes'}, {'book_id': 'bookid_158', 'title': 'Cleo Porter and the Body Electric'}, {'book_id': 'bookid_163', 'title': 'Monster Kisses'}, {'book_id': 'bookid_170', 'title': 'Pokémon: Sun & Moon, Vol. 8 (8)'}], 'var_function-call-6581685273077666796': 'file_storage/function-call-6581685273077666796.json'}

exec(code, env_args)
