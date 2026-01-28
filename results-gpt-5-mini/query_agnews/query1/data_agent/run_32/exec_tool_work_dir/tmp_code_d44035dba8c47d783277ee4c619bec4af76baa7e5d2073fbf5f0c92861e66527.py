code = """import json
# data from MongoDB query stored in var_call_Q5BiuwfLBFmF7oFLFGsx0WmE
data = var_call_Q5BiuwfLBFmF7oFLFGsx0WmE
keywords = ['game','match','season','tournament','olympic','olympics','nba','nfl','mlb','soccer','football','baseball','basketball','hockey','goal','coach','player','scored','win','won','defeat','defeated','cup','series','race','rally','pitcher','striker','midfielder','innings']

def is_sports(txt):
    if not txt:
        return False
    t = txt.lower()
    for kw in keywords:
        if kw in t:
            return True
    return False

sports = []
for rec in data:
    title = rec.get('title','')
    desc = rec.get('description','')
    if is_sports(title) or is_sports(desc):
        sports.append({'title': title, 'description': desc, 'desc_len': len(desc or '')})

if sports:
    best = max(sports, key=lambda x: x['desc_len'])
    result = best['title']
else:
    result = None

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Q5BiuwfLBFmF7oFLFGsx0WmE': [{'_id': '6959859b82a6b1d078e96675', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6959859b82a6b1d078e96676', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6959859b82a6b1d078e96677', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6959859b82a6b1d078e96678', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6959859b82a6b1d078e96679', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
