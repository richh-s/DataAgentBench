code = """import json
import re
from collections import defaultdict

reviews = var_call_ZtBQ9vEfXUbSnr4s53AnyG82
# convert review_count to int
for r in reviews:
    r['review_count'] = int(r['review_count'])

# load business docs from file
path = var_call_pUs5k4VQtqyj5u840oFTJDAa
with open(path, 'r') as f:
    businesses = json.load(f)

bdesc = {b.get('business_id'): b.get('description') for b in businesses}


def parse_categories(desc):
    if not desc:
        return []
    s = desc
    parts = re.split(r'[.?!]', s)
    last = ''
    for p in reversed(parts):
        if p.strip():
            last = p.strip()
            break
    s = last
    low = s.lower()
    pos_offers = low.find('offers')
    pos_in = -1
    if pos_offers != -1:
        pos_in = low.find(' in ', pos_offers)
    if pos_in == -1:
        pos_in = low.rfind(' in ')
    if pos_in != -1:
        cats = s[pos_in+4:]
    else:
        m = re.search(r'(including|specializes in|categories of|offers a range of services in|offers a diverse range of services in)', low)
        if m:
            cats = s[m.end():]
        else:
            cats = s
    cats = re.split(r'(to meet|perfect for|making it|to meet all|for all your)', cats)[0]
    cats = re.sub(r'\band\b', ',', cats, flags=re.I)
    items = [it.strip() for it in re.split(r',', cats) if it.strip()]
    items = [it for it in items if it and not re.match(r'^(offers|services|service|food|this)$', it.lower())]
    cleaned = []
    for it in items:
        it = re.sub(r'^(the |a |an )','', it.strip(), flags=re.I)
        it = it.rstrip(' .')
        if it:
            cleaned.append(it)
    return cleaned

counts = defaultdict(int)
for r in reviews:
    br = r['business_ref']
    parts = br.split('_')
    if len(parts) < 2:
        continue
    num = parts[1]
    bid = 'businessid_' + num
    desc = bdesc.get(bid)
    cats = parse_categories(desc)
    if not cats and desc:
        # fallback: try taking last sentence and split by comma/and
        last_sentence = re.split(r'[.?!]', desc)
        last_sentence = last_sentence[-2] if len(last_sentence) >= 2 else last_sentence[-1]
        cats = [c.strip() for c in re.split(r',| and ', last_sentence) if c.strip()]
    for c in cats:
        counts[c] += r['review_count']

items = sorted(counts.items(), key=lambda x: x[1], reverse=True)
top5 = [{'category': k, 'review_count': v} for k, v in items[:5]]

print('__RESULT__:')
print(json.dumps(top5))"""

env_args = {'var_call_02W1Vic9rmEXHVAl8SYlsiSR': [{'user_id': 'userid_746'}, {'user_id': 'userid_1109'}, {'user_id': 'userid_1950'}, {'user_id': 'userid_1316'}, {'user_id': 'userid_1182'}, {'user_id': 'userid_151'}, {'user_id': 'userid_1158'}, {'user_id': 'userid_508'}, {'user_id': 'userid_435'}, {'user_id': 'userid_958'}, {'user_id': 'userid_1879'}, {'user_id': 'userid_308'}, {'user_id': 'userid_1179'}, {'user_id': 'userid_324'}, {'user_id': 'userid_863'}, {'user_id': 'userid_100'}, {'user_id': 'userid_1333'}, {'user_id': 'userid_1636'}, {'user_id': 'userid_1850'}, {'user_id': 'userid_711'}, {'user_id': 'userid_729'}, {'user_id': 'userid_1505'}, {'user_id': 'userid_1315'}, {'user_id': 'userid_1708'}, {'user_id': 'userid_1661'}, {'user_id': 'userid_850'}, {'user_id': 'userid_1675'}, {'user_id': 'userid_227'}, {'user_id': 'userid_577'}, {'user_id': 'userid_257'}, {'user_id': 'userid_598'}, {'user_id': 'userid_847'}, {'user_id': 'userid_673'}, {'user_id': 'userid_1856'}, {'user_id': 'userid_384'}, {'user_id': 'userid_935'}, {'user_id': 'userid_210'}, {'user_id': 'userid_1101'}, {'user_id': 'userid_945'}, {'user_id': 'userid_842'}, {'user_id': 'userid_1351'}, {'user_id': 'userid_230'}, {'user_id': 'userid_593'}, {'user_id': 'userid_1431'}, {'user_id': 'userid_686'}, {'user_id': 'userid_527'}, {'user_id': 'userid_244'}, {'user_id': 'userid_393'}, {'user_id': 'userid_1178'}, {'user_id': 'userid_526'}, {'user_id': 'userid_90'}, {'user_id': 'userid_238'}, {'user_id': 'userid_1105'}], 'var_call_ZtBQ9vEfXUbSnr4s53AnyG82': [{'business_ref': 'businessref_13', 'review_count': '1'}, {'business_ref': 'businessref_79', 'review_count': '1'}, {'business_ref': 'businessref_6', 'review_count': '1'}, {'business_ref': 'businessref_74', 'review_count': '2'}, {'business_ref': 'businessref_66', 'review_count': '2'}, {'business_ref': 'businessref_15', 'review_count': '1'}, {'business_ref': 'businessref_33', 'review_count': '2'}, {'business_ref': 'businessref_36', 'review_count': '2'}, {'business_ref': 'businessref_60', 'review_count': '2'}, {'business_ref': 'businessref_12', 'review_count': '1'}, {'business_ref': 'businessref_53', 'review_count': '1'}, {'business_ref': 'businessref_31', 'review_count': '1'}, {'business_ref': 'businessref_57', 'review_count': '2'}, {'business_ref': 'businessref_86', 'review_count': '1'}, {'business_ref': 'businessref_62', 'review_count': '1'}, {'business_ref': 'businessref_37', 'review_count': '1'}, {'business_ref': 'businessref_92', 'review_count': '2'}, {'business_ref': 'businessref_26', 'review_count': '1'}, {'business_ref': 'businessref_68', 'review_count': '1'}, {'business_ref': 'businessref_41', 'review_count': '1'}, {'business_ref': 'businessref_10', 'review_count': '1'}, {'business_ref': 'businessref_45', 'review_count': '3'}, {'business_ref': 'businessref_96', 'review_count': '2'}, {'business_ref': 'businessref_98', 'review_count': '1'}, {'business_ref': 'businessref_14', 'review_count': '1'}, {'business_ref': 'businessref_20', 'review_count': '1'}], 'var_call_Zuv2jCBECuUQp5b8gUallwsz': ['business', 'checkin'], 'var_call_pUs5k4VQtqyj5u840oFTJDAa': 'file_storage/call_pUs5k4VQtqyj5u840oFTJDAa.json'}

exec(code, env_args)
