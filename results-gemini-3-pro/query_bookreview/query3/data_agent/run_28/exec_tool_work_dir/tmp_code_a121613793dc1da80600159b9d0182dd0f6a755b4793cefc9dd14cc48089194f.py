code = """import json

# Access previous results
reviews = locals()['var_function-call-2843063560853834993']
books = locals()['var_function-call-17630784567638764917']

# Normalize IDs
# purchase_id format: purchaseid_X
# book_id format: bookid_X

# Create a set of normalized IDs from reviews (which already have avg rating >= 4.5)
# And we want to find matching books.
# Or better, create a map of normalized_id -> title from books (which are Children's Books)
# And then check if normalized_id from reviews is in that map.

book_map = {}
for b in books:
    bid = b['book_id']
    # Extract number. assuming format "bookid_<number>"
    if '_' in bid:
        num = bid.split('_')[1]
        book_map[num] = b['title']

matching_titles = []
for r in reviews:
    pid = r['purchase_id']
    if '_' in pid:
        num = pid.split('_')[1]
        if num in book_map:
            matching_titles.append(book_map[num])

# Remove duplicates if any (though grouped by purchase_id, book_id should be unique)
matching_titles = sorted(list(set(matching_titles)))

print("__RESULT__:")
print(json.dumps(matching_titles))"""

env_args = {'var_function-call-3455036731092560775': ['review'], 'var_function-call-18070357255192980131': ['books_info'], 'var_function-call-4437774897874809658': [{'review_time': '2012-11-24 18:52:00', 'rating': '4', 'purchase_id': 'purchaseid_186'}, {'review_time': '2015-12-31 13:35:00', 'rating': '4', 'purchase_id': 'purchaseid_191'}, {'review_time': '2013-05-05 10:47:00', 'rating': '4', 'purchase_id': 'purchaseid_190'}, {'review_time': '2020-08-12 11:06:00', 'rating': '5', 'purchase_id': 'purchaseid_8'}, {'review_time': '2014-11-13 18:55:00', 'rating': '4', 'purchase_id': 'purchaseid_178'}], 'var_function-call-525746070638184788': [{'categories': '["Books", "Literature & Fiction", "History & Criticism"]'}, {'categories': '["Books", "Reference", "Words, Language & Grammar"]'}, {'categories': '["Books", "Biographies & Memoirs", "Leaders & Notable People"]'}, {'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'categories': '["Books", "Mystery, Thriller & Suspense", "Thrillers & Suspense"]'}], 'var_function-call-9927838283606701077': [{'book_id': 'bookid_1'}, {'book_id': 'bookid_2'}, {'book_id': 'bookid_3'}, {'book_id': 'bookid_4'}, {'book_id': 'bookid_5'}], 'var_function-call-2843063560853834993': [{'purchase_id': 'purchaseid_10', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_105', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_108', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_110', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_115', 'avg_rating': '4.75'}, {'purchase_id': 'purchaseid_118', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_12', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_122', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_126', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_129', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_13', 'avg_rating': '4.923076923076923'}, {'purchase_id': 'purchaseid_130', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_14', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_144', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_146', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_149', 'avg_rating': '4.9'}, {'purchase_id': 'purchaseid_152', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_154', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_158', 'avg_rating': '4.708333333333333'}, {'purchase_id': 'purchaseid_161', 'avg_rating': '4.5'}, {'purchase_id': 'purchaseid_169', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_170', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_172', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_178', 'avg_rating': '4.795918367346939'}, {'purchase_id': 'purchaseid_182', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_184', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_185', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_187', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_192', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_196', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_198', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_200', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_22', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_23', 'avg_rating': '4.5'}, {'purchase_id': 'purchaseid_3', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_33', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_37', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_38', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_39', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_4', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_40', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_41', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_46', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_48', 'avg_rating': '4.75'}, {'purchase_id': 'purchaseid_50', 'avg_rating': '4.5'}, {'purchase_id': 'purchaseid_54', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_55', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_6', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_60', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_66', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_72', 'avg_rating': '4.5'}, {'purchase_id': 'purchaseid_74', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_76', 'avg_rating': '4.75'}, {'purchase_id': 'purchaseid_8', 'avg_rating': '4.709677419354839'}, {'purchase_id': 'purchaseid_80', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_83', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_88', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_94', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_96', 'avg_rating': '5.0'}], 'var_function-call-17630784567638764917': [{'title': 'Monstrous Stories #4: The Day the Mice Stood Still', 'book_id': 'bookid_4'}, {'title': 'The Old Man and the Pirate Princess', 'book_id': 'bookid_14'}, {'title': 'The Very Hungry Caterpillar (English and Arabic Edition)', 'book_id': 'bookid_32'}, {'title': 'Egypt (Enchantment of the World)', 'book_id': 'bookid_40'}, {'title': 'Clark the Shark: Tooth Trouble, No. 1', 'book_id': 'bookid_48'}, {'title': "I Hadn't Meant to Tell You This", 'book_id': 'bookid_52'}, {'title': 'Favorite Thorton W. Burgess Stories: 6 Books', 'book_id': 'bookid_54'}, {'title': 'Behind the Wheel (Choose Your Own Adventure #35)(Paperback/Revised)', 'book_id': 'bookid_55'}, {'title': "Goodnight Riley and the Moon, It's Almost Bedtime: Personalized Children’s Books, Personalized Gifts, and Bedtime Stories (A Magnificent Me! estorytime.com Series)", 'book_id': 'bookid_57'}, {'title': 'Cheer Up, Ben Franklin! (Young Historians)', 'book_id': 'bookid_96'}, {'title': 'Buddy the Soldier Bear', 'book_id': 'bookid_99'}, {'title': 'The Library Book', 'book_id': 'bookid_108'}, {'title': 'Can You Buy Me The Wind?', 'book_id': 'bookid_111'}, {'title': 'From the Earth to the Moon by Jules Verne, Fiction, Fantasy & Magic', 'book_id': 'bookid_116'}, {'title': "Caroline's Color Dreams: Los Sueños Coloridos De Carolina : Babl Children's Books in Spanish and English", 'book_id': 'bookid_120'}, {'title': 'Skeleton Play: A Fun, Rhyming Halloween Book for Kids! (1)', 'book_id': 'bookid_124'}, {'title': "Benny Goes To The Moon: The great new book from Top Children's entertainer Gerry Ogilvie (1)", 'book_id': 'bookid_130'}, {'title': 'Mae and Jane in the Rain', 'book_id': 'bookid_132'}, {'title': 'Kirsten: An American Girl : 1854 (The American Girls Collection/Boxed Set)', 'book_id': 'bookid_145'}, {'title': 'LunaLu the Llamacorn', 'book_id': 'bookid_146'}, {'title': 'Trouble in the CTC!: The Terra Prime Adventures Book 2', 'book_id': 'bookid_149'}, {'title': 'Around the World Mazes', 'book_id': 'bookid_152'}, {'title': 'Cleo Porter and the Body Electric', 'book_id': 'bookid_158'}, {'title': 'Monster Kisses', 'book_id': 'bookid_163'}, {'title': 'Pokémon: Sun & Moon, Vol. 8 (8)', 'book_id': 'bookid_170'}]}

exec(code, env_args)
