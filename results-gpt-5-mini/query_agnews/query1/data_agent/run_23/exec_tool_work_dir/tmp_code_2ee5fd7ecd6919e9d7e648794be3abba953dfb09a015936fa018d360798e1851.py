code = """import json
import pandas as pd
records = var_call_rU1BzOtLaLjGf5OncjrY6

def is_sports_text(text):
    if not text:
        return False
    text = text.lower()
    keywords = ['game','season','scored','coach','team','match','tournament','olympic','win','loss','goal','league','playoff','inning','bat','basket','basketball','football','soccer','baseball','tennis','golf','hockey','stadium','player','players','score','defeat','victory','draw']
    return any(k in text for k in keywords)

sports = []
for r in records:
    title = r.get('title','')
    desc = r.get('description','')
    combined = (title or '') + ' ' + (desc or '')
    if is_sports_text(combined):
        sports.append({'article_id': r.get('article_id'), 'title': title, 'description': desc, 'description_length': len(desc)})

if not sports:
    result = {'found': False, 'title': None, 'message': 'No sports articles found in articles collection.'}
else:
    maxrec = max(sports, key=lambda x: x['description_length'])
    result = {'found': True, 'title': maxrec['title'], 'article_id': maxrec['article_id'], 'description_length': maxrec['description_length']}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_BJHoyOhggtoLFTT5HX0MTygz': ['articles'], 'var_call_rU1BzOtLaLjGf5OncjrY6nv6': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
