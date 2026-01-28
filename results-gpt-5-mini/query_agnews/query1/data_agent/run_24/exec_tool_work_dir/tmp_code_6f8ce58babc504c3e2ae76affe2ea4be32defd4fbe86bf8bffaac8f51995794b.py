code = """import json
path = var_call_Y12wS5ASYHmrdM6d3a3GdsiP
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

search_terms = ['match','goal','football','soccer','tennis','league','player','coach','season','cup','scored','olympic','win','won','score','nba','mlb','nfl','nhl','bat','innings','pitcher','goalkeeper','striker']
results = {term:0 for term in search_terms}
matches = {term:[] for term in search_terms}
for rec in data:
    text = ((rec.get('title') or '') + ' ' + (rec.get('description') or '')).lower()
    for term in search_terms:
        if term in text:
            results[term] += 1
            if len(matches[term])<5:
                matches[term].append({'article_id': rec.get('article_id'), 'title': rec.get('title')})

out = {'counts': results, 'examples': matches}
import json
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Y12wS5ASYHmrdM6d3a3GdsiP': 'file_storage/call_Y12wS5ASYHmrdM6d3a3GdsiP.json', 'var_call_VltVVT6qtx8Lici358433nGz': None, 'var_call_XCYNyRQ53RLPNxT40GwxJHM2': 'file_storage/call_XCYNyRQ53RLPNxT40GwxJHM2.json', 'var_call_JepEl8eqcJOmrF7F29jifAwi': None, 'var_call_HwyWCdfchlzcrGpTPiXMorlt': None}

exec(code, env_args)
