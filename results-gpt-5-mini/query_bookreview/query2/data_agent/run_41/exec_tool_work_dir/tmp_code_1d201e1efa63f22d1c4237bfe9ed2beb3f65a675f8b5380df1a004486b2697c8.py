code = """import json
# Load previous results
books_path = var_call_KgPg7WcafUFyAWr7srkBpqMA
reviews_path = var_call_xE18DlZYp0m9AspJNEL07N4P

with open(books_path, 'r', encoding='utf-8') as f:
    books = json.load(f)
with open(reviews_path, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

# We need to map purchase_id ~ book_id. The hint suggests fuzzy join. Observing patterns: purchaseid_# vs bookid_# likely correspond by number.
# Create mapping by extracting numeric suffix
import re

def extract_num(s):
    m = re.search(r"(\d+)$", s)
    return int(m.group(1)) if m else None

book_map = {}
for b in books:
    bid = b.get('book_id')
    num = extract_num(bid) if bid else None
    if num is not None:
        book_map[num] = b

# Determine which book_ids have only 5.0 ratings (perfect average of 5.0)
# For a perfect average of 5.0, all reviews for that book must be rating 5.0.
# First, group reviews by purchase_id numeric suffix
from collections import defaultdict
rev_by_num = defaultdict(list)
for r in reviews:
    pid = r.get('purchase_id')
    num = extract_num(pid)
    if num is not None:
        # convert rating to float/int
        try:
            rating = float(r.get('rating'))
        except:
            continue
        rev_by_num[num].append(rating)

perfect_books = []
for num, ratings in rev_by_num.items():
    if len(ratings) == 0:
        continue
    if all(r == 5.0 for r in ratings):
        # check if this num exists in book_map and category includes Literature & Fiction and English language
        b = book_map.get(num)
        if not b:
            continue
        cats = b.get('categories') or ''
        details = b.get('details') or ''
        if 'Literature & Fiction' in cats and re.search(r'\bEnglish\b', details, flags=re.IGNORECASE):
            perfect_books.append({'book_id': b.get('book_id'), 'title': b.get('title')})

# Remove duplicates
unique = { (x['book_id'], x['title']) for x in perfect_books }
res = [ {'book_id': k, 'title': v} for (k,v) in unique ]

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_KgPg7WcafUFyAWr7srkBpqMA': 'file_storage/call_KgPg7WcafUFyAWr7srkBpqMA.json', 'var_call_Ltk5zGD6JdrHYt6WczqVqk0Z': [{'book_id': 'bookid_1', 'title': 'Chaucer'}, {'book_id': 'bookid_9', 'title': 'Reunion: The Children of Lauderdale Park'}, {'book_id': 'bookid_13', 'title': 'Girl Made of Glass'}, {'book_id': 'bookid_30', 'title': 'Sugary Sweets (A Taste of Love Series)'}, {'book_id': 'bookid_36', 'title': 'Therapy Mammals'}, {'book_id': 'bookid_37', 'title': "A Most Dangerous Book: Tacitus's Germania from the Roman Empire to the Third Reich"}, {'book_id': 'bookid_38', 'title': 'The Prophet: With Original 1923 Illustrations by the Author'}, {'book_id': 'bookid_39', 'title': 'The Melancholy Strumpet Master'}, {'book_id': 'bookid_44', 'title': 'Reptilian'}, {'book_id': 'bookid_49', 'title': 'Primeval: A Journal of the Uncanny - Issue #1'}, {'book_id': 'bookid_55', 'title': 'Behind the Wheel (Choose Your Own Adventure #35)(Paperback/Revised)'}, {'book_id': 'bookid_69', 'title': 'Out of Sheer Rage: Wrestling with D. H. Lawrence'}, {'book_id': 'bookid_70', 'title': 'Polly and the Shadow Goblin: Book 2, Mother of Witches'}, {'book_id': 'bookid_74', 'title': 'Child Of The King A Journey of Hope Book 1: Earthly Story With A Heavenly Message'}, {'book_id': 'bookid_77', 'title': 'One September Morning'}, {'book_id': 'bookid_82', 'title': 'Fire Cracker'}, {'book_id': 'bookid_84', 'title': 'Local Honey'}, {'book_id': 'bookid_89', 'title': "I'll Ride For My Hood: A Salty Love Story"}, {'book_id': 'bookid_92', 'title': 'Outage'}, {'book_id': 'bookid_93', 'title': 'Simantov'}, {'book_id': 'bookid_98', 'title': 'Hollywood Confessions: Hollywood Headlines Book #3 (Hollywood Headlines Mysteries)'}, {'book_id': 'bookid_99', 'title': 'Buddy the Soldier Bear'}, {'book_id': 'bookid_101', 'title': 'Knowing When To Die: Uncollected Stories'}, {'book_id': 'bookid_106', 'title': 'Looking for Peyton Place: A Novel'}, {'book_id': 'bookid_109', 'title': 'All the Way to the Gallows'}, {'book_id': 'bookid_122', 'title': 'Childe Harold of Dysna'}, {'book_id': 'bookid_137', 'title': 'Oligarchy'}, {'book_id': 'bookid_142', 'title': 'The Jordan Tracks'}, {'book_id': 'bookid_144', 'title': 'Forged in Blood (Freehold)'}, {'book_id': 'bookid_161', 'title': "Time's Demon: BOOK II OF THE ISLEVALE CYCLE"}, {'book_id': 'bookid_167', 'title': 'Dead Silence'}, {'book_id': 'bookid_171', 'title': 'Exits, Desires, & Slow Fires'}, {'book_id': 'bookid_177', 'title': 'Kennebago Moments'}, {'book_id': 'bookid_179', 'title': 'A Cherry Cola Christmas (A Cherry Cola Book Club Novel)'}, {'book_id': 'bookid_180', 'title': 'The Sludge'}, {'book_id': 'bookid_182', 'title': 'Liza of Lambeth'}, {'book_id': 'bookid_187', 'title': 'Consort (A Dark(ish) Faerie Tale Book 3)'}, {'book_id': 'bookid_188', 'title': "The Vampyre and Other Tales of the Macabre (Oxford World's Classics)"}, {'book_id': 'bookid_195', 'title': 'Something That Feels Like Truth (Switchgrass Books)'}], 'var_call_26XWcQmpA3VONeVY3dJRYrxi': ['review'], 'var_call_xE18DlZYp0m9AspJNEL07N4P': 'file_storage/call_xE18DlZYp0m9AspJNEL07N4P.json', 'var_call_N3EPR17hGWwdOb9g6xAAnUMT': ['purchaseid_10', 'purchaseid_100', 'purchaseid_101', 'purchaseid_103', 'purchaseid_104', 'purchaseid_105', 'purchaseid_106', 'purchaseid_107', 'purchaseid_108', 'purchaseid_110', 'purchaseid_111', 'purchaseid_112', 'purchaseid_114', 'purchaseid_115', 'purchaseid_116', 'purchaseid_117', 'purchaseid_118', 'purchaseid_119', 'purchaseid_12', 'purchaseid_121', 'purchaseid_122', 'purchaseid_123', 'purchaseid_124', 'purchaseid_125', 'purchaseid_126', 'purchaseid_127', 'purchaseid_128', 'purchaseid_129', 'purchaseid_13', 'purchaseid_130', 'purchaseid_131', 'purchaseid_132', 'purchaseid_133', 'purchaseid_134', 'purchaseid_135', 'purchaseid_14', 'purchaseid_140', 'purchaseid_142', 'purchaseid_143', 'purchaseid_144', 'purchaseid_145', 'purchaseid_146', 'purchaseid_148', 'purchaseid_149', 'purchaseid_15', 'purchaseid_150', 'purchaseid_151', 'purchaseid_152', 'purchaseid_153', 'purchaseid_154', 'purchaseid_156', 'purchaseid_157', 'purchaseid_158', 'purchaseid_159', 'purchaseid_16', 'purchaseid_160', 'purchaseid_161', 'purchaseid_162', 'purchaseid_163', 'purchaseid_164', 'purchaseid_165', 'purchaseid_166', 'purchaseid_167', 'purchaseid_168', 'purchaseid_169', 'purchaseid_170', 'purchaseid_171', 'purchaseid_172', 'purchaseid_173', 'purchaseid_174', 'purchaseid_175', 'purchaseid_177', 'purchaseid_178', 'purchaseid_179', 'purchaseid_180', 'purchaseid_181', 'purchaseid_182', 'purchaseid_184', 'purchaseid_185', 'purchaseid_186', 'purchaseid_187', 'purchaseid_188', 'purchaseid_189', 'purchaseid_19', 'purchaseid_190', 'purchaseid_191', 'purchaseid_192', 'purchaseid_193', 'purchaseid_194', 'purchaseid_195', 'purchaseid_196', 'purchaseid_197', 'purchaseid_198', 'purchaseid_2', 'purchaseid_20', 'purchaseid_200', 'purchaseid_21', 'purchaseid_22', 'purchaseid_23', 'purchaseid_24', 'purchaseid_26', 'purchaseid_27', 'purchaseid_28', 'purchaseid_29', 'purchaseid_3', 'purchaseid_30', 'purchaseid_32', 'purchaseid_33', 'purchaseid_34', 'purchaseid_35', 'purchaseid_36', 'purchaseid_37', 'purchaseid_38', 'purchaseid_39', 'purchaseid_4', 'purchaseid_40', 'purchaseid_41', 'purchaseid_42', 'purchaseid_44', 'purchaseid_46', 'purchaseid_47', 'purchaseid_48', 'purchaseid_49', 'purchaseid_5', 'purchaseid_50', 'purchaseid_52', 'purchaseid_53', 'purchaseid_54', 'purchaseid_55', 'purchaseid_56', 'purchaseid_57', 'purchaseid_58', 'purchaseid_59', 'purchaseid_6', 'purchaseid_60', 'purchaseid_62', 'purchaseid_63', 'purchaseid_64', 'purchaseid_66', 'purchaseid_68', 'purchaseid_69', 'purchaseid_7', 'purchaseid_71', 'purchaseid_72', 'purchaseid_73', 'purchaseid_74', 'purchaseid_75', 'purchaseid_76', 'purchaseid_77', 'purchaseid_78', 'purchaseid_79', 'purchaseid_8', 'purchaseid_80', 'purchaseid_81', 'purchaseid_82', 'purchaseid_83', 'purchaseid_84', 'purchaseid_85', 'purchaseid_86', 'purchaseid_87', 'purchaseid_88', 'purchaseid_89', 'purchaseid_9', 'purchaseid_90', 'purchaseid_91', 'purchaseid_92', 'purchaseid_94', 'purchaseid_95', 'purchaseid_96', 'purchaseid_97', 'purchaseid_98', 'purchaseid_99']}

exec(code, env_args)
