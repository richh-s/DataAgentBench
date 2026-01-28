code = """import json, re
path = var_call_SZKmDiGDaV0kUYoFZaLeKkjg
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

sports_keywords = [
    'football','soccer','match','goal','goals','team','teams','league','tournament','cup',
    'coach','manager','season','score','scored','win','won','defeat','defeated','draw',
    'racing','race','athletics','olympic','olympics','baseball','cricket','basketball',
    'tennis','golf','boxing','mma','boxing','rugby','nhl','nba','mlb','nfl','fifa','world cup',
    'stadium','pitch','goalkeeper','striker','midfielder','forward','defence','defense','wicket',
    'innings','batting','boxing','matchday'
]

def is_sports_text(text):
    if not text:
        return False
    t = text.lower()
    for kw in sports_keywords:
        if kw in t:
            return True
    return False

sports_records = []
for rec in data:
    title = rec.get('title') or ''
    desc = rec.get('description') or ''
    desc_len = len(desc)
    if is_sports_text(title) or is_sports_text(desc):
        sports_records.append({'article_id': rec.get('article_id'), 'title': title, 'description': desc, 'description_length': desc_len})

if not sports_records:
    out = json.dumps(None)
else:
    max_len = max(r['description_length'] for r in sports_records)
    candidates = [r for r in sports_records if r['description_length'] == max_len]
    # If multiple, choose the first by appearance
    chosen = candidates[0]
    out = json.dumps({'title': chosen['title'], 'article_id': chosen['article_id'], 'description_length': chosen['description_length']})

print("__RESULT__:")
print(out)"""

env_args = {'var_call_SZKmDiGDaV0kUYoFZaLeKkjg': 'file_storage/call_SZKmDiGDaV0kUYoFZaLeKkjg.json'}

exec(code, env_args)
