code = """import json
from pathlib import Path

# Load the MongoDB query result stored in the variable from previous tool call
# The storage variable name provided by the system is var_call_EamLaJwfTyeDBnDAaG8Cwrrv
file_path = var_call_EamLaJwfTyeDBnDAaG8Cwrrv

with open(file_path, 'r', encoding='utf-8') as f:
    records = json.load(f)

# Define simple keyword-based classifier for Sports
sports_keywords = [
    'football','soccer','basketball','baseball','cricket','rugby','match','tournament',
    'season','goal','scored','coach','manager','defeat','defeated','beat','wins','won','loss',
    'draw','series','innings','home run','pitcher','goalkeeper','fifa','uefa','olympic',
    'nba','mlb','nfl','nhl','golf','tennis','cup','league','race','racing','marathon',
    'athlete','boxing','fight','wrestling','rebound','penalty','kick','try','strike','victory',
    'defeats','trounce','trounced','beat','beats','losses','winless','halftime','full-time','scoring',
]

sports_set = set()

def is_sports(text):
    if not text:
        return False
    t = text.lower()
    for kw in sports_keywords:
        if kw in t:
            return True
    return False

# Collect sports articles
sports_articles = []
for r in records:
    title = r.get('title') or ''
    desc = r.get('description') or ''
    combined = title + ' ' + desc
    if is_sports(combined):
        sports_articles.append({'title': title, 'description': desc, 'len': len(desc)})

# If none found by keywords, attempt a looser heuristic: look for words 'team' or 'coach' etc.
if not sports_articles:
    fallback_keywords = ['team','teams','coach','player','players','match','game','season','score','scores','scored']
    for r in records:
        title = r.get('title') or ''
        desc = r.get('description') or ''
        combined = title + ' ' + desc
        t = combined.lower()
        if any(k in t for k in fallback_keywords):
            sports_articles.append({'title': title, 'description': desc, 'len': len(desc)})

# Determine the sports article(s) with maximum description length
result_titles = []
if sports_articles:
    max_len = max(a['len'] for a in sports_articles)
    result_titles = [a['title'] for a in sports_articles if a['len'] == max_len]

# Prepare output: if single title, return as string; else return list
if not result_titles:
    output = None
elif len(result_titles) == 1:
    output = result_titles[0]
else:
    output = result_titles

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_EamLaJwfTyeDBnDAaG8Cwrrv': 'file_storage/call_EamLaJwfTyeDBnDAaG8Cwrrv.json'}

exec(code, env_args)
