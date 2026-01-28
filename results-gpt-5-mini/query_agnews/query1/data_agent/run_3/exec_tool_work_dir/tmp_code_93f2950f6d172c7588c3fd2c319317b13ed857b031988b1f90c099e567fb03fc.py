code = """import json
fp = var_call_ceck0cnLpqhRoaGEX5lbUXmh
with open(fp, 'r', encoding='utf-8') as f:
    records = json.load(f)

sports_keywords = [
    'sport','sports','game','match','season','goal','scored','score','inning','bat','pitch','basket','basketball',
    'football','soccer','tennis','golf','tournament','coach','league','cup','won','defeat','beat','race','olympic',
    'championship','homers','runs','touchdown','mlb','nba','nhl','nfl','fifa','world cup','rugby','cricket','boxing',
    'fight','fought','motor','formula 1','f1','grand prix','all-star','playoff','playoffs','penalty','penalties',
    'striker','midfielder','goalkeeper','coach','manager','club','side','derby'
]

def is_sports(rec):
    text = ((rec.get('title') or '') + ' ' + (rec.get('description') or '')).lower()
    for kw in sports_keywords:
        if kw in text:
            return True
    return False

sports = [r for r in records if is_sports(r)]

if not sports:
    result = {"title": None, "message": "No sports articles found"}
else:
    for r in sports:
        r['_desc_len'] = len(r.get('description') or '')
    max_len = max(r['_desc_len'] for r in sports)
    max_articles = [r for r in sports if r['_desc_len'] == max_len]
    chosen = max_articles[0]
    result = {"title": chosen.get('title'), "description_length": chosen.get('_desc_len'), "article_id": chosen.get('article_id')}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ceck0cnLpqhRoaGEX5lbUXmh': 'file_storage/call_ceck0cnLpqhRoaGEX5lbUXmh.json'}

exec(code, env_args)
