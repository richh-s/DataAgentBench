code = """import json
import re

# Load data from the stored JSON file path provided by the previous query_db call
path = var_call_KFZHPHpvU3Kq1GPkYjmyFIpp
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Define keyword lists for simple rule-based classification
sports_kw = [
    'sport','football','soccer','baseball','basketball','tennis','golf','cricket','race','racing',
    'olympic','olympics','match','team','coach','goal','score','scores','beat','defeat','won','win',
    'draw','season','club','league','pitch','innings','touchdown','home run','homers','foul','cup','EXTRA TIME'
]
business_kw = [
    'market','stocks','shares','economy','company','firm','business','investment','bank','profit','loss','ipo',
    'merger','acquisition','earnings','revenue','trade','oil prices','oil','crude','dollar','interest rate','investor',
    'investment','billion','million','debt','financial'
]
science_kw = [
    'technology','tech','scientist','research','study','nuclear','robot','software','computer','internet','digital',
    'ai','science','nasa','space','lab','biotech','genetic','innovation'
]
world_kw = [
    'president','gov','government','iraq','terror','rebels','country','minister','election','war','conflict','peace',
    'attacks','border','police','military','china','russia','united','world','countries','region','africa','asia',
    'europe','south','north','america'
]

def score_text(text, keywords):
    s = 0
    for kw in keywords:
        # count occurrences, case-insensitive
        s += text.count(kw)
    return s

sports_articles = []

for rec in data:
    title = rec.get('title','') or ''
    desc = rec.get('description','') or ''
    combined = (title + ' ' + desc).lower()

    scores = {
        'Sports': score_text(combined, sports_kw),
        'Business': score_text(combined, business_kw),
        'Science/Technology': score_text(combined, science_kw),
        'World': score_text(combined, world_kw),
    }
    # choose category with highest score
    category = max(scores, key=lambda k: scores[k])

    # If no keywords matched (all zero), try a looser heuristic: look for known sports-specific terms like 'match', 'team', etc.
    if all(v == 0 for v in scores.values()):
        if re.search(r'\b(match|team|league|cup|season|coach|goal|score|scores)\b', combined):
            category = 'Sports'
        else:
            category = 'World'

    if category == 'Sports':
        sports_articles.append({'title': title, 'description': desc, 'desc_len': len(desc)})

# Find the sports article with the longest description
if sports_articles:
    best = max(sports_articles, key=lambda x: x['desc_len'])
    result = best['title']
else:
    result = None

import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_KFZHPHpvU3Kq1GPkYjmyFIpp': 'file_storage/call_KFZHPHpvU3Kq1GPkYjmyFIpp.json'}

exec(code, env_args)
