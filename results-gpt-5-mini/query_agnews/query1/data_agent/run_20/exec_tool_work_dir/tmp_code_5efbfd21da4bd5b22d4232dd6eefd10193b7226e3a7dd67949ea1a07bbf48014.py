code = """import json
import re
from pathlib import Path

# Load the query_db result from the stored JSON file path
data_path = Path(var_call_v3avNa2MXFKLvL5ulBW5M8GJ)
with data_path.open('r', encoding='utf-8') as f:
    records = json.load(f)

# Normalize records: ensure description and title exist
for r in records:
    r.setdefault('title', '')
    r.setdefault('description', '')

# Define keyword lists for categories
sports_kw = [
    'football','soccer','basketball','baseball','hockey','tennis','golf','cricket',
    'match','tournament','season','coach','goal','score','scored','won','win','beat',
    'defeat','draw','cup','olympic','nba','mlb','nhl','fifa','rugby','boxing','scoreboard',
    'pitch','bat','innings','home run','hat-trick','matchday','goalkeeper','striker'
]
tech_kw = [
    'scientist','scientists','research','technology','tech','computer','ibm','software',
    'nuclear','drug','experiment','scientific','researchers','internet','online','email','e-mail'
]
business_kw = [
    'stock','stocks','market','shares','ipo','investment','investor','economy','economics',
    'trade deficit','profits','profit','oil prices','oil','barrel','dollar','rate cut','interest rates',
    'shares','company','firm','revenue','quarter','earnings','invest'
]

# helper to check presence of any keyword as whole word
def contains_any(text, keywords):
    t = text.lower()
    for kw in keywords:
        # use simple substring match; also check word boundaries for alpha keywords
        if re.search(r"\b" + re.escape(kw) + r"\b", t):
            return True
    return False

# Classify each record
for r in records:
    combined = (r.get('title','') + ' ' + r.get('description','')).lower()
    if contains_any(combined, sports_kw):
        r['category'] = 'Sports'
    elif contains_any(combined, tech_kw):
        r['category'] = 'Science/Technology'
    elif contains_any(combined, business_kw):
        r['category'] = 'Business'
    else:
        r['category'] = 'World'
    # compute description length
    r['description_len'] = len(r.get('description',''))

# Filter sports articles
sports = [r for r in records if r['category'] == 'Sports']

# If none found, prepare None
if not sports:
    result = None
else:
    # find max by description_len
    max_r = max(sports, key=lambda x: x['description_len'])
    result = max_r.get('title')

import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_v3avNa2MXFKLvL5ulBW5M8GJ': 'file_storage/call_v3avNa2MXFKLvL5ulBW5M8GJ.json'}

exec(code, env_args)
