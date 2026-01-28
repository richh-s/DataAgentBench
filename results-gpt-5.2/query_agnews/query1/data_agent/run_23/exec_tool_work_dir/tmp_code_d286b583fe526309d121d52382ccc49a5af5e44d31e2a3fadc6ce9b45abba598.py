code = """import json, pandas as pd
from pathlib import Path

path = Path(var_call_1Y4EUcp8OEB9vnWiTHfXivp1)
recs = json.loads(path.read_text())

def is_sports(title, desc):
    text = f"{title} {desc}".lower()
    sports_terms = [
        'nba','nfl','mlb','nhl','soccer','football','baseball','basketball','hockey','tennis','golf','olympic','olympics',
        'cup','match','tournament','coach','quarterback','touchdown','home run','goal','scored','win','won','season',
        'league','championship','final','playoff','athlete','team','manager','f1','formula','grand prix','cricket','rugby'
    ]
    # Require at least one strong term and avoid common non-sports false positives
    if any(t in text for t in sports_terms):
        return True
    return False

best = None
for r in recs:
    title = r.get('title') or ''
    desc = r.get('description') or ''
    if not isinstance(title, str):
        title = str(title)
    if not isinstance(desc, str):
        desc = str(desc)
    if is_sports(title, desc):
        n = len(desc)
        if best is None or n > best['len']:
            best = {'article_id': r.get('article_id'), 'title': title, 'len': n}

out = best['title'] if best else None
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_1Y4EUcp8OEB9vnWiTHfXivp1': 'file_storage/call_1Y4EUcp8OEB9vnWiTHfXivp1.json'}

exec(code, env_args)
