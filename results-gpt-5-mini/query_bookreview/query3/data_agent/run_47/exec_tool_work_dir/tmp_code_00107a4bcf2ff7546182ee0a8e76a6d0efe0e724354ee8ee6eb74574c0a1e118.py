code = """import re
import json
# datasets from previous queries
reviews = var_call_9Je5apuJGz30Y9vY12pmiu4M
books = var_call_40nHd7Z1x8au8G0LySZIAdoW

# helper to extract numeric id
def extract_num(s):
    if s is None:
        return None
    m = re.search(r"(\d+)", str(s))
    return m.group(1) if m else None

# build dict from purchase numeric -> review info
rev_map = {}
for r in reviews:
    pid = r.get('purchase_id')
    num = extract_num(pid)
    if num:
        rev_map[num] = {
            'purchase_id': pid,
            'avg_rating': float(r.get('avg_rating')),
            'n_reviews': int(r.get('n_reviews'))
        }

# iterate books and join where numeric matches and categories contain "Children's Books"
results = []
for b in books:
    bid = b.get('book_id')
    num = extract_num(bid)
    if not num:
        continue
    if num in rev_map:
        entry = {
            'book_id': bid,
            'title': b.get('title'),
            'categories': b.get('categories'),
            'purchase_id': rev_map[num]['purchase_id'],
            'avg_rating': rev_map[num]['avg_rating'],
            'n_reviews': rev_map[num]['n_reviews']
        }
        results.append(entry)

# sort results by avg_rating desc, then n_reviews desc
results.sort(key=lambda x: (-x['avg_rating'], -x['n_reviews']))

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_MOFutjAYEKeSqdQxKiO6HpDR': ['review'], 'var_call_AGNHdDBWiyp2yqVJ0j3l0735': ['books_info'], 'var_call_OZtnOfFihal94bX3inwIN8eM': 'file_storage/call_OZtnOfFihal94bX3inwIN8eM.json', 'var_call_40nHd7Z1x8au8G0LySZIAdoW': [{'book_id': 'bookid_4', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_14', 'title': 'The Old Man and the Pirate Princess', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_32', 'title': 'The Very Hungry Caterpillar (English and Arabic Edition)', 'categories': '["Books", "Children\'s Books", "Early Learning"]'}, {'book_id': 'bookid_40', 'title': 'Egypt (Enchantment of the World)', 'categories': '["Books", "Children\'s Books", "Geography & Cultures"]'}, {'book_id': 'bookid_48', 'title': 'Clark the Shark: Tooth Trouble, No. 1', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_52', 'title': "I Hadn't Meant to Tell You This", 'categories': '["Books", "Children\'s Books", "Geography & Cultures"]'}, {'book_id': 'bookid_54', 'title': 'Favorite Thorton W. Burgess Stories: 6 Books', 'categories': '["Books", "Children\'s Books", "Animals"]'}, {'book_id': 'bookid_55', 'title': 'Behind the Wheel (Choose Your Own Adventure #35)(Paperback/Revised)', 'categories': '["Books", "Children\'s Books", "Literature & Fiction"]'}, {'book_id': 'bookid_57', 'title': "Goodnight Riley and the Moon, It's Almost Bedtime: Personalized Children’s Books, Personalized Gifts, and Bedtime Stories (A Magnificent Me! estorytime.com Series)", 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_96', 'title': 'Cheer Up, Ben Franklin! (Young Historians)', 'categories': '["Books", "Children\'s Books", "History"]'}, {'book_id': 'bookid_99', 'title': 'Buddy the Soldier Bear', 'categories': '["Books", "Children\'s Books", "Literature & Fiction"]'}, {'book_id': 'bookid_108', 'title': 'The Library Book', 'categories': '["Books", "Children\'s Books", "Education & Reference"]'}, {'book_id': 'bookid_111', 'title': 'Can You Buy Me The Wind?', 'categories': '["Books", "Children\'s Books", "Literature & Fiction"]'}, {'book_id': 'bookid_116', 'title': 'From the Earth to the Moon by Jules Verne, Fiction, Fantasy & Magic', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_120', 'title': "Caroline's Color Dreams: Los Sueños Coloridos De Carolina : Babl Children's Books in Spanish and English", 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_124', 'title': 'Skeleton Play: A Fun, Rhyming Halloween Book for Kids! (1)', 'categories': '["Books", "Children\'s Books", "Holidays & Celebrations"]'}, {'book_id': 'bookid_130', 'title': "Benny Goes To The Moon: The great new book from Top Children's entertainer Gerry Ogilvie (1)", 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_132', 'title': 'Mae and Jane in the Rain', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_145', 'title': 'Kirsten: An American Girl : 1854 (The American Girls Collection/Boxed Set)', 'categories': '["Books", "Boxed Sets", "Children\'s Books"]'}, {'book_id': 'bookid_146', 'title': 'LunaLu the Llamacorn', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_149', 'title': 'Trouble in the CTC!: The Terra Prime Adventures Book 2', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_152', 'title': 'Around the World Mazes', 'categories': '["Books", "Children\'s Books", "Activities, Crafts & Games"]'}, {'book_id': 'bookid_158', 'title': 'Cleo Porter and the Body Electric', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_163', 'title': 'Monster Kisses', 'categories': '["Books", "Children\'s Books", "Growing Up & Facts of Life"]'}, {'book_id': 'bookid_170', 'title': 'Pokémon: Sun & Moon, Vol. 8 (8)', 'categories': '["Books", "Children\'s Books", "Comics & Graphic Novels"]'}], 'var_call_9Je5apuJGz30Y9vY12pmiu4M': [{'purchase_id': 'purchaseid_96', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_94', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_88', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_83', 'avg_rating': '5.0', 'n_reviews': '14'}, {'purchase_id': 'purchaseid_80', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_74', 'avg_rating': '5.0', 'n_reviews': '8'}, {'purchase_id': 'purchaseid_66', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_60', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_6', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_55', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_54', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_46', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_41', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_40', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_4', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_39', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_38', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_37', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_33', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_3', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_22', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_200', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_198', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_196', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_192', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_187', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_185', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_184', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_182', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_172', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_170', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_169', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_154', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_152', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_146', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_144', 'avg_rating': '5.0', 'n_reviews': '4'}, {'purchase_id': 'purchaseid_14', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_130', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_129', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_126', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_122', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_12', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_118', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_110', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_108', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_105', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_10', 'avg_rating': '5.0', 'n_reviews': '4'}, {'purchase_id': 'purchaseid_13', 'avg_rating': '4.923076923076923', 'n_reviews': '13'}, {'purchase_id': 'purchaseid_149', 'avg_rating': '4.9', 'n_reviews': '10'}, {'purchase_id': 'purchaseid_178', 'avg_rating': '4.795918367346939', 'n_reviews': '49'}, {'purchase_id': 'purchaseid_76', 'avg_rating': '4.75', 'n_reviews': '4'}, {'purchase_id': 'purchaseid_48', 'avg_rating': '4.75', 'n_reviews': '4'}, {'purchase_id': 'purchaseid_115', 'avg_rating': '4.75', 'n_reviews': '8'}, {'purchase_id': 'purchaseid_8', 'avg_rating': '4.709677419354839', 'n_reviews': '31'}, {'purchase_id': 'purchaseid_158', 'avg_rating': '4.708333333333333', 'n_reviews': '24'}, {'purchase_id': 'purchaseid_72', 'avg_rating': '4.5', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_50', 'avg_rating': '4.5', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_23', 'avg_rating': '4.5', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_161', 'avg_rating': '4.5', 'n_reviews': '2'}]}

exec(code, env_args)
