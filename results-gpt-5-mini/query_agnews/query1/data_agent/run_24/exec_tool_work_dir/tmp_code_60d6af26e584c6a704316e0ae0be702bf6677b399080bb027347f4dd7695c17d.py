code = """import json, re
path = var_call_Y12wS5ASYHmrdM6d3a3GdsiP
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

keywords = [
    'sport','sports','match','goal','scor','score','team','coach','player','players','league',
    'cup','tournament','race','racing','win','won','runner','bat','innings','pitcher','cricket',
    'soccer','football','basketball','baseball','tennis','golf','boxing','olympic','olympics',
    'fifa','nhl','nba','nfl','mlb','f1','motorsport','derby','goalkeeper','striker','midfield',
    'athlete','athletes','season','cup final','cup-final'
]

def is_sports_text(text):
    t = (text or '').lower()
    for kw in keywords:
        # allow 'scor' prefix catch 'score','scored'
        if kw.endswith('scor'):
            if re.search(r"\bscor\w*", t):
                return True
        elif re.search(r"\b" + re.escape(kw) + r"\b", t):
            return True
    return False

max_len = -1
max_rec = None
for rec in data:
    title = rec.get('title') or ''
    desc = rec.get('description') or ''
    combined = title + ' ' + desc
    if is_sports_text(combined):
        l = len(desc)
        if l > max_len:
            max_len = l
            max_rec = rec

import json
print('__RESULT__:')
if max_rec is None:
    print(json.dumps(None))
else:
    print(json.dumps(max_rec.get('title')))"""

env_args = {'var_call_Y12wS5ASYHmrdM6d3a3GdsiP': 'file_storage/call_Y12wS5ASYHmrdM6d3a3GdsiP.json', 'var_call_VltVVT6qtx8Lici358433nGz': None, 'var_call_XCYNyRQ53RLPNxT40GwxJHM2': 'file_storage/call_XCYNyRQ53RLPNxT40GwxJHM2.json'}

exec(code, env_args)
