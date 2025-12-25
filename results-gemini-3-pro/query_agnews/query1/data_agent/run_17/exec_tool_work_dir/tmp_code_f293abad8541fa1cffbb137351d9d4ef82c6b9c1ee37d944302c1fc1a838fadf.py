code = """import json
import re

data_key = 'var_function-call-3846196706058509729'
data = locals().get(data_key)
if isinstance(data, str):
    with open(data, 'r') as f:
        articles = json.load(f)
else:
    articles = data

sports_kw = ['basketball', 'swimming', 'gymnastics', 'tennis', 'soccer', 'baseball', 'football', 'volleyball', 'boxing', 'wrestling', 'athletics', 'marathon', 'sprint', 'cycling', 'rowing', 'diving']
tech_biz_kw = ['software', 'technology', 'internet', 'market', 'stocks', 'profit', 'revenue', 'microsoft', 'google', 'intel', 'oil', 'price', 'economy']

candidates = []
for art in articles:
    text = (art.get('title', '') + ' ' + art.get('description', '')).lower()
    
    # Check for sports keywords
    has_sport = False
    for kw in sports_kw:
        if kw in text:
            has_sport = True
            break
            
    # Check for tech/biz keywords to exclude
    is_tech_biz = False
    for kw in tech_biz_kw:
        if kw in text:
            is_tech_biz = True
            break
            
    if has_sport and not is_tech_biz:
        candidates.append(art)

print('Candidates found:', len(candidates))
for c in candidates[:10]:
    print(f"Title: {c['title']}")
    print(f"Desc: {c['description'][:100]}...")

# Find longest description among these
max_len = -1
best = None
for c in candidates:
    desc_len = len(c.get('description', ''))
    if desc_len > max_len:
        max_len = desc_len
        best = c

result = {}
if best:
    result = {'title': best['title'], 'length': max_len}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-10490437154642486884': ['articles'], 'var_function-call-16060478269300868870': [{'_id': '69447092d43dab771ac0dd01', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447092d43dab771ac0dd02', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447092d43dab771ac0dd03', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447092d43dab771ac0dd04', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447092d43dab771ac0dd05', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-9311861591054791868': [{'_id': '69447092d43dab771ac0dd01', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447092d43dab771ac0dd02', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447092d43dab771ac0dd03', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447092d43dab771ac0dd04', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447092d43dab771ac0dd05', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-2138815974854363807': [{'_id': '69447092d43dab771ac0dd01', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447092d43dab771ac0dd02', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447092d43dab771ac0dd03', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447092d43dab771ac0dd04', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447092d43dab771ac0dd05', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-16333879224723824131': 'No sports articles found.', 'var_function-call-3846196706058509729': 'file_storage/function-call-3846196706058509729.json', 'var_function-call-16733021958024539417': {'title': "Why Windows isn't Unix", 'length': 708, 'description_snippet': '\\\\"I first heard about this from one of the develo'}, 'var_function-call-6924971850173435336': {'error': 'No sports articles found'}, 'var_function-call-9843822974461349720': {'count': 78, 'examples': ["'Madden,' 'ESPN' Football Score in Different Ways (Reuters)", "'Invisible' technology for Olympics", 'Satellite boosts Olympic security', "'Madden,' 'ESPN' Football Score in Different Ways", 'GAO Calls Stryker Too Heavy for Transport']}}

exec(code, env_args)
