code = """import json

file_path = locals()['var_function-call-1631278526276499272']
with open(file_path, 'r') as f:
    articles = json.load(f)

print(f"Total articles: {len(articles)}")

keywords = [
    'olympic', 'athens', 'nfl', 'nba', 'mlb', 'nhl', 'fifa', 'uefa', 
    'wimbledon', 'us open', 'australian open', 'french open', 
    'championship', 'world cup', 'super bowl', 'stanley cup', 'world series',
    'gold medal', 'silver medal', 'bronze medal',
    'football', 'basketball', 'baseball', 'soccer', 'tennis', 'golf', 
    'hockey', 'cricket', 'rugby', 'boxing', 'wrestling', 'swimming', 
    'gymnastics', 'volleyball', 'badminton', 'athletics', 'marathon',
    'formula one', 'nascar', 'racing', 'grand prix', 'tour de france',
    'red sox', 'yankees', 'lakers', 'pistons', 'arsenal', 'manchester united', 'real madrid',
    'sport', 'athlete', 'coach'
]

candidates = []
for art in articles:
    text = (art.get('title', '') + ' ' + art.get('description', '')).lower()
    if any(k in text for k in keywords):
        candidates.append(art)

# Sort by description length
candidates.sort(key=lambda x: len(x.get('description', '')), reverse=True)

# Print top 10
top_10 = []
for c in candidates[:10]:
    top_10.append({
        'title': c['title'],
        'desc_len': len(c['description']),
        'preview': c['description'][:50]
    })

print("__RESULT__:")
print(json.dumps(top_10))"""

env_args = {'var_function-call-3405305575496258850': ['articles'], 'var_function-call-8922034183929127080': [{'_id': '694469dae6ccbefbf4774406', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694469dae6ccbefbf4774407', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694469dae6ccbefbf4774408', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694469dae6ccbefbf4774409', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694469dae6ccbefbf477440a', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-2370693320005028959': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'author_id': '992', 'region': 'North America', 'publication_date': '2004-03-20'}, {'article_id': '2', 'author_id': '820', 'region': 'South America', 'publication_date': '2021-02-04'}, {'article_id': '3', 'author_id': '478', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '4', 'author_id': '39', 'region': 'Africa', 'publication_date': '2012-02-01'}], 'var_function-call-8758874876893031559': [{'_id': '694469dae6ccbefbf4774406', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694469dae6ccbefbf4774407', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694469dae6ccbefbf4774408', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694469dae6ccbefbf4774409', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694469dae6ccbefbf477440a', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-10390619581974537303': {'count': 5, 'sample_titles': ['Wall St. Bears Claw Back Into the Black (Reuters)', 'Carlyle Looks Toward Commercial Aerospace (Reuters)', "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'Oil prices soar to all-time record, posing new menace to US economy (AFP)']}, 'var_function-call-3430141558639675251': 'file_storage/function-call-3430141558639675251.json', 'var_function-call-2308637426162186490': 1000, 'var_function-call-1631278526276499272': 'file_storage/function-call-1631278526276499272.json'}

exec(code, env_args)
