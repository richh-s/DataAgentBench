code = """import json

# Load english_lit_books_map
english_lit_books_map = locals()['var_function-call-15702231700308223649']

# Load perfect_rating_purchases
perfect_rating_purchases_list = locals()['var_function-call-14209735675183742243']
# It's a list of dicts: [{"purchase_id": "purchaseid_101"}, ...]
perfect_rating_ids = [item['purchase_id'] for item in perfect_rating_purchases_list]

# Helper to extract ID
def extract_id(id_str):
    if not isinstance(id_str, str):
        return None
    # Assuming format "prefix_NUMBER"
    parts = id_str.split('_')
    if len(parts) > 1:
        return parts[1]
    return None

# Create map: numeric_id -> title
numeric_id_to_title = {}
for book_id, title in english_lit_books_map.items():
    num_id = extract_id(book_id)
    if num_id:
        numeric_id_to_title[num_id] = title

# Get perfect rating numeric IDs
perfect_numeric_ids = set()
for pid in perfect_rating_ids:
    num_id = extract_id(pid)
    if num_id:
        perfect_numeric_ids.add(num_id)

# Find intersection
result_titles = []
for num_id in perfect_numeric_ids:
    if num_id in numeric_id_to_title:
        result_titles.append(numeric_id_to_title[num_id])

print("__RESULT__:")
print(json.dumps(result_titles))"""

env_args = {'var_function-call-10727912544765417180': 'file_storage/function-call-10727912544765417180.json', 'var_function-call-15702231700308223649': {'bookid_1': 'Chaucer', 'bookid_9': 'Reunion: The Children of Lauderdale Park', 'bookid_13': 'Girl Made of Glass', 'bookid_30': 'Sugary Sweets (A Taste of Love Series)', 'bookid_36': 'Therapy Mammals', 'bookid_37': "A Most Dangerous Book: Tacitus's Germania from the Roman Empire to the Third Reich", 'bookid_38': 'The Prophet: With Original 1923 Illustrations by the Author', 'bookid_39': 'The Melancholy Strumpet Master', 'bookid_44': 'Reptilian', 'bookid_49': 'Primeval: A Journal of the Uncanny - Issue #1', 'bookid_55': 'Behind the Wheel (Choose Your Own Adventure #35)(Paperback/Revised)', 'bookid_69': 'Out of Sheer Rage: Wrestling with D. H. Lawrence', 'bookid_70': 'Polly and the Shadow Goblin: Book 2, Mother of Witches', 'bookid_74': 'Child Of The King A Journey of Hope Book 1: Earthly Story With A Heavenly Message', 'bookid_77': 'One September Morning', 'bookid_82': 'Fire Cracker', 'bookid_84': 'Local Honey', 'bookid_89': "I'll Ride For My Hood: A Salty Love Story", 'bookid_92': 'Outage', 'bookid_93': 'Simantov', 'bookid_98': 'Hollywood Confessions: Hollywood Headlines Book #3 (Hollywood Headlines Mysteries)', 'bookid_99': 'Buddy the Soldier Bear', 'bookid_101': 'Knowing When To Die: Uncollected Stories', 'bookid_106': 'Looking for Peyton Place: A Novel', 'bookid_109': 'All the Way to the Gallows', 'bookid_111': 'Can You Buy Me The Wind?', 'bookid_122': 'Childe Harold of Dysna', 'bookid_137': 'Oligarchy', 'bookid_142': 'The Jordan Tracks', 'bookid_144': 'Forged in Blood (Freehold)', 'bookid_161': "Time's Demon: BOOK II OF THE ISLEVALE CYCLE", 'bookid_167': 'Dead Silence', 'bookid_171': 'Exits, Desires, & Slow Fires', 'bookid_177': 'Kennebago Moments', 'bookid_179': 'A Cherry Cola Christmas (A Cherry Cola Book Club Novel)', 'bookid_180': 'The Sludge', 'bookid_182': 'Liza of Lambeth', 'bookid_187': 'Consort (A Dark(ish) Faerie Tale Book 3)', 'bookid_188': "The Vampyre and Other Tales of the Macabre (Oxford World's Classics)", 'bookid_195': 'Something That Feels Like Truth (Switchgrass Books)'}, 'var_function-call-11364415707601128708': ['review'], 'var_function-call-5730446870678890805': [{'purchase_id': 'purchaseid_186'}, {'purchase_id': 'purchaseid_191'}, {'purchase_id': 'purchaseid_190'}, {'purchase_id': 'purchaseid_8'}, {'purchase_id': 'purchaseid_178'}], 'var_function-call-14209735675183742243': [{'purchase_id': 'purchaseid_101'}, {'purchase_id': 'purchaseid_105'}, {'purchase_id': 'purchaseid_108'}, {'purchase_id': 'purchaseid_110'}, {'purchase_id': 'purchaseid_114'}, {'purchase_id': 'purchaseid_116'}, {'purchase_id': 'purchaseid_117'}, {'purchase_id': 'purchaseid_118'}, {'purchase_id': 'purchaseid_12'}, {'purchase_id': 'purchaseid_121'}, {'purchase_id': 'purchaseid_122'}, {'purchase_id': 'purchaseid_123'}, {'purchase_id': 'purchaseid_124'}, {'purchase_id': 'purchaseid_126'}, {'purchase_id': 'purchaseid_127'}, {'purchase_id': 'purchaseid_128'}, {'purchase_id': 'purchaseid_130'}, {'purchase_id': 'purchaseid_132'}, {'purchase_id': 'purchaseid_133'}, {'purchase_id': 'purchaseid_134'}, {'purchase_id': 'purchaseid_14'}, {'purchase_id': 'purchaseid_143'}, {'purchase_id': 'purchaseid_144'}, {'purchase_id': 'purchaseid_146'}, {'purchase_id': 'purchaseid_150'}, {'purchase_id': 'purchaseid_151'}, {'purchase_id': 'purchaseid_152'}, {'purchase_id': 'purchaseid_153'}, {'purchase_id': 'purchaseid_156'}, {'purchase_id': 'purchaseid_16'}, {'purchase_id': 'purchaseid_160'}, {'purchase_id': 'purchaseid_163'}, {'purchase_id': 'purchaseid_166'}, {'purchase_id': 'purchaseid_168'}, {'purchase_id': 'purchaseid_170'}, {'purchase_id': 'purchaseid_171'}, {'purchase_id': 'purchaseid_172'}, {'purchase_id': 'purchaseid_174'}, {'purchase_id': 'purchaseid_177'}, {'purchase_id': 'purchaseid_180'}, {'purchase_id': 'purchaseid_181'}, {'purchase_id': 'purchaseid_182'}, {'purchase_id': 'purchaseid_184'}, {'purchase_id': 'purchaseid_192'}, {'purchase_id': 'purchaseid_195'}, {'purchase_id': 'purchaseid_197'}, {'purchase_id': 'purchaseid_2'}, {'purchase_id': 'purchaseid_21'}, {'purchase_id': 'purchaseid_24'}, {'purchase_id': 'purchaseid_26'}, {'purchase_id': 'purchaseid_28'}, {'purchase_id': 'purchaseid_29'}, {'purchase_id': 'purchaseid_33'}, {'purchase_id': 'purchaseid_34'}, {'purchase_id': 'purchaseid_38'}, {'purchase_id': 'purchaseid_39'}, {'purchase_id': 'purchaseid_40'}, {'purchase_id': 'purchaseid_41'}, {'purchase_id': 'purchaseid_42'}, {'purchase_id': 'purchaseid_47'}, {'purchase_id': 'purchaseid_54'}, {'purchase_id': 'purchaseid_56'}, {'purchase_id': 'purchaseid_57'}, {'purchase_id': 'purchaseid_59'}, {'purchase_id': 'purchaseid_6'}, {'purchase_id': 'purchaseid_60'}, {'purchase_id': 'purchaseid_64'}, {'purchase_id': 'purchaseid_7'}, {'purchase_id': 'purchaseid_71'}, {'purchase_id': 'purchaseid_73'}, {'purchase_id': 'purchaseid_74'}, {'purchase_id': 'purchaseid_75'}, {'purchase_id': 'purchaseid_79'}, {'purchase_id': 'purchaseid_80'}, {'purchase_id': 'purchaseid_82'}, {'purchase_id': 'purchaseid_83'}, {'purchase_id': 'purchaseid_84'}, {'purchase_id': 'purchaseid_88'}, {'purchase_id': 'purchaseid_9'}, {'purchase_id': 'purchaseid_90'}, {'purchase_id': 'purchaseid_91'}, {'purchase_id': 'purchaseid_97'}, {'purchase_id': 'purchaseid_98'}]}

exec(code, env_args)
