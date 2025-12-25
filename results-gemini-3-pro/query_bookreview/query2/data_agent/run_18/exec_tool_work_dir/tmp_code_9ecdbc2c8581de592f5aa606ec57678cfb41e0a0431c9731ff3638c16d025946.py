code = """import json
import pandas as pd

# Load books (large result)
with open(locals()['var_function-call-592610660680423383'], 'r') as f:
    books_data = json.load(f)

# Load perfect reviews
perfect_reviews = locals()['var_function-call-5749709345454239326']

# Create set of perfect book IDs (normalized)
perfect_ids = set()
for r in perfect_reviews:
    pid = r['purchase_id']
    # assume format purchaseid_X
    if '_' in pid:
        perfect_ids.add(pid.split('_')[1])
    else:
        perfect_ids.add(pid)

matching_titles = []

for book in books_data:
    bid_full = book['book_id']
    # assume format bookid_X
    if '_' in bid_full:
        bid = bid_full.split('_')[1]
    else:
        bid = bid_full
    
    # Filter 1: Must have perfect rating
    if bid not in perfect_ids:
        continue
    
    # Filter 2: Category 'Literature & Fiction'
    # The SQL filtered broad matches, let's verify exact category inclusion if possible
    cat_str = book['categories']
    try:
        # Try json load
        cats = json.loads(cat_str)
    except:
        try:
            # Try ast literal eval if simple quotes
            import ast
            cats = ast.literal_eval(cat_str)
        except:
            cats = []
    
    # Check if 'Literature & Fiction' is in the list
    if 'Literature & Fiction' not in cats:
        # Fallback: if structure failed, check string presence again (redundant but safe)
        if 'Literature & Fiction' not in cat_str:
            continue

    # Filter 3: English language
    # Look for 'English' in details
    details = book.get('details', '')
    if 'English' not in details:
        continue
        
    matching_titles.append(book['title'])

print("__RESULT__:")
print(json.dumps(matching_titles))"""

env_args = {'var_function-call-592610660680423383': 'file_storage/function-call-592610660680423383.json', 'var_function-call-16884191789318926408': ['review'], 'var_function-call-5749709345454239326': [{'purchase_id': 'purchaseid_101'}, {'purchase_id': 'purchaseid_105'}, {'purchase_id': 'purchaseid_108'}, {'purchase_id': 'purchaseid_110'}, {'purchase_id': 'purchaseid_114'}, {'purchase_id': 'purchaseid_116'}, {'purchase_id': 'purchaseid_117'}, {'purchase_id': 'purchaseid_118'}, {'purchase_id': 'purchaseid_12'}, {'purchase_id': 'purchaseid_121'}, {'purchase_id': 'purchaseid_122'}, {'purchase_id': 'purchaseid_123'}, {'purchase_id': 'purchaseid_124'}, {'purchase_id': 'purchaseid_126'}, {'purchase_id': 'purchaseid_127'}, {'purchase_id': 'purchaseid_128'}, {'purchase_id': 'purchaseid_130'}, {'purchase_id': 'purchaseid_132'}, {'purchase_id': 'purchaseid_133'}, {'purchase_id': 'purchaseid_134'}, {'purchase_id': 'purchaseid_14'}, {'purchase_id': 'purchaseid_143'}, {'purchase_id': 'purchaseid_144'}, {'purchase_id': 'purchaseid_146'}, {'purchase_id': 'purchaseid_150'}, {'purchase_id': 'purchaseid_151'}, {'purchase_id': 'purchaseid_152'}, {'purchase_id': 'purchaseid_153'}, {'purchase_id': 'purchaseid_156'}, {'purchase_id': 'purchaseid_16'}, {'purchase_id': 'purchaseid_160'}, {'purchase_id': 'purchaseid_163'}, {'purchase_id': 'purchaseid_166'}, {'purchase_id': 'purchaseid_168'}, {'purchase_id': 'purchaseid_170'}, {'purchase_id': 'purchaseid_171'}, {'purchase_id': 'purchaseid_172'}, {'purchase_id': 'purchaseid_174'}, {'purchase_id': 'purchaseid_177'}, {'purchase_id': 'purchaseid_180'}, {'purchase_id': 'purchaseid_181'}, {'purchase_id': 'purchaseid_182'}, {'purchase_id': 'purchaseid_184'}, {'purchase_id': 'purchaseid_192'}, {'purchase_id': 'purchaseid_195'}, {'purchase_id': 'purchaseid_197'}, {'purchase_id': 'purchaseid_2'}, {'purchase_id': 'purchaseid_21'}, {'purchase_id': 'purchaseid_24'}, {'purchase_id': 'purchaseid_26'}, {'purchase_id': 'purchaseid_28'}, {'purchase_id': 'purchaseid_29'}, {'purchase_id': 'purchaseid_33'}, {'purchase_id': 'purchaseid_34'}, {'purchase_id': 'purchaseid_38'}, {'purchase_id': 'purchaseid_39'}, {'purchase_id': 'purchaseid_40'}, {'purchase_id': 'purchaseid_41'}, {'purchase_id': 'purchaseid_42'}, {'purchase_id': 'purchaseid_47'}, {'purchase_id': 'purchaseid_54'}, {'purchase_id': 'purchaseid_56'}, {'purchase_id': 'purchaseid_57'}, {'purchase_id': 'purchaseid_59'}, {'purchase_id': 'purchaseid_6'}, {'purchase_id': 'purchaseid_60'}, {'purchase_id': 'purchaseid_64'}, {'purchase_id': 'purchaseid_7'}, {'purchase_id': 'purchaseid_71'}, {'purchase_id': 'purchaseid_73'}, {'purchase_id': 'purchaseid_74'}, {'purchase_id': 'purchaseid_75'}, {'purchase_id': 'purchaseid_79'}, {'purchase_id': 'purchaseid_80'}, {'purchase_id': 'purchaseid_82'}, {'purchase_id': 'purchaseid_83'}, {'purchase_id': 'purchaseid_84'}, {'purchase_id': 'purchaseid_88'}, {'purchase_id': 'purchaseid_9'}, {'purchase_id': 'purchaseid_90'}, {'purchase_id': 'purchaseid_91'}, {'purchase_id': 'purchaseid_97'}, {'purchase_id': 'purchaseid_98'}]}

exec(code, env_args)
