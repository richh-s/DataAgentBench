code = """import json
import re

# Load books data
with open(locals()['var_function-call-10837257613530230348'], 'r') as f:
    books = json.load(f)

# Load ratings data
ratings = locals()['var_function-call-17485417452501275232']

# Extract numeric IDs from ratings
perfect_ids = set()
for r in ratings:
    pid = r['purchase_id']
    match = re.search(r'purchaseid_(\d+)', pid)
    if match:
        perfect_ids.add(match.group(1))

matching_books = []

for b in books:
    # Check language
    # details field contains text like "is available in English" or "written in English"
    if 'English' not in b.get('details', ''):
        continue
        
    # Check book_id
    bid = b.get('book_id', '')
    match = re.search(r'bookid_(\d+)', bid)
    if match:
        num_id = match.group(1)
        if num_id in perfect_ids:
            matching_books.append(b['title'])

print("__RESULT__:")
print(json.dumps(matching_books))"""

env_args = {'var_function-call-10837257613530230348': 'file_storage/function-call-10837257613530230348.json', 'var_function-call-17624076619956139041': ['review'], 'var_function-call-17485417452501275232': [{'purchase_id': 'purchaseid_101'}, {'purchase_id': 'purchaseid_105'}, {'purchase_id': 'purchaseid_108'}, {'purchase_id': 'purchaseid_110'}, {'purchase_id': 'purchaseid_114'}, {'purchase_id': 'purchaseid_116'}, {'purchase_id': 'purchaseid_117'}, {'purchase_id': 'purchaseid_118'}, {'purchase_id': 'purchaseid_12'}, {'purchase_id': 'purchaseid_121'}, {'purchase_id': 'purchaseid_122'}, {'purchase_id': 'purchaseid_123'}, {'purchase_id': 'purchaseid_124'}, {'purchase_id': 'purchaseid_126'}, {'purchase_id': 'purchaseid_127'}, {'purchase_id': 'purchaseid_128'}, {'purchase_id': 'purchaseid_130'}, {'purchase_id': 'purchaseid_132'}, {'purchase_id': 'purchaseid_133'}, {'purchase_id': 'purchaseid_134'}, {'purchase_id': 'purchaseid_14'}, {'purchase_id': 'purchaseid_143'}, {'purchase_id': 'purchaseid_144'}, {'purchase_id': 'purchaseid_146'}, {'purchase_id': 'purchaseid_150'}, {'purchase_id': 'purchaseid_151'}, {'purchase_id': 'purchaseid_152'}, {'purchase_id': 'purchaseid_153'}, {'purchase_id': 'purchaseid_156'}, {'purchase_id': 'purchaseid_16'}, {'purchase_id': 'purchaseid_160'}, {'purchase_id': 'purchaseid_163'}, {'purchase_id': 'purchaseid_166'}, {'purchase_id': 'purchaseid_168'}, {'purchase_id': 'purchaseid_170'}, {'purchase_id': 'purchaseid_171'}, {'purchase_id': 'purchaseid_172'}, {'purchase_id': 'purchaseid_174'}, {'purchase_id': 'purchaseid_177'}, {'purchase_id': 'purchaseid_180'}, {'purchase_id': 'purchaseid_181'}, {'purchase_id': 'purchaseid_182'}, {'purchase_id': 'purchaseid_184'}, {'purchase_id': 'purchaseid_192'}, {'purchase_id': 'purchaseid_195'}, {'purchase_id': 'purchaseid_197'}, {'purchase_id': 'purchaseid_2'}, {'purchase_id': 'purchaseid_21'}, {'purchase_id': 'purchaseid_24'}, {'purchase_id': 'purchaseid_26'}, {'purchase_id': 'purchaseid_28'}, {'purchase_id': 'purchaseid_29'}, {'purchase_id': 'purchaseid_33'}, {'purchase_id': 'purchaseid_34'}, {'purchase_id': 'purchaseid_38'}, {'purchase_id': 'purchaseid_39'}, {'purchase_id': 'purchaseid_40'}, {'purchase_id': 'purchaseid_41'}, {'purchase_id': 'purchaseid_42'}, {'purchase_id': 'purchaseid_47'}, {'purchase_id': 'purchaseid_54'}, {'purchase_id': 'purchaseid_56'}, {'purchase_id': 'purchaseid_57'}, {'purchase_id': 'purchaseid_59'}, {'purchase_id': 'purchaseid_6'}, {'purchase_id': 'purchaseid_60'}, {'purchase_id': 'purchaseid_64'}, {'purchase_id': 'purchaseid_7'}, {'purchase_id': 'purchaseid_71'}, {'purchase_id': 'purchaseid_73'}, {'purchase_id': 'purchaseid_74'}, {'purchase_id': 'purchaseid_75'}, {'purchase_id': 'purchaseid_79'}, {'purchase_id': 'purchaseid_80'}, {'purchase_id': 'purchaseid_82'}, {'purchase_id': 'purchaseid_83'}, {'purchase_id': 'purchaseid_84'}, {'purchase_id': 'purchaseid_88'}, {'purchase_id': 'purchaseid_9'}, {'purchase_id': 'purchaseid_90'}, {'purchase_id': 'purchaseid_91'}, {'purchase_id': 'purchaseid_97'}, {'purchase_id': 'purchaseid_98'}]}

exec(code, env_args)
