code = """import json
import pandas as pd

records = var_call_MwZzcEFl16NlwooCap3LfKox

def is_sports(text: str) -> bool:
    if not isinstance(text, str):
        return False
    t = text.lower()
    keywords = [
        'sport','sports','game','match','season','league','tournament','cup','olympic','nba','nfl','mlb','nhl','soccer','football','basketball','baseball','hockey','tennis','golf','cricket','rugby','f1','formula','grand prix','nascar',
        'coach','player','team','quarterback','goal','goals','touchdown','home run','innings','pitcher','referee','rankings','medal'
    ]
    return any(k in t for k in keywords)

sports = []
for r in records:
    title = r.get('title')
    desc = r.get('description')
    if is_sports(title) or is_sports(desc):
        sports.append({
            'article_id': r.get('article_id'),
            'title': title,
            'description': desc,
            'desc_len': len(desc) if isinstance(desc, str) else None
        })

if sports:
    best = max([s for s in sports if s['desc_len'] is not None], key=lambda x: x['desc_len'])
    out = {'title': best['title'], 'article_id': best['article_id'], 'desc_len': best['desc_len']}
else:
    out = {'title': None, 'article_id': None, 'desc_len': None}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_MwZzcEFl16NlwooCap3LfKox': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
