code = """import json
import re
# var_call_2dGUKOpRmpOF9KYi59rimcN9 is provided by the previous query_db call
records = var_call_2dGUKOpRmpOF9KYi59rimcN9

sports_keywords = [
    'sport', 'sports', 'game', 'match', 'tournament', 'league', 'season', 'coach', 'score',
    'goal', 'final', 'defeat', 'victory', 'win', 'loss', 'baseball', 'basketball', 'football',
    'soccer', 'hockey', 'tennis', 'golf', 'olympic', 'cup', 'rally', 'race', 'track', 'boxing',
    'mma', 'fight', 'athlete', 'athletes', 'pitch', 'inning', 'quarterback', 'nba', 'mlb', 'nhl'
]

sports_articles = []
for r in records:
    title = r.get('title','') or ''
    desc = r.get('description','') or ''
    text = (title + ' ' + desc).lower()
    if any(kw in text for kw in sports_keywords):
        sports_articles.append({'title': title, 'description': desc, 'desc_len': len(desc)})

if sports_articles:
    # find the sports article with greatest description length
    max_article = max(sports_articles, key=lambda x: x['desc_len'])
    result = {
        'sports_article_titles': [a['title'] for a in sports_articles],
        'sports_article_with_longest_description': max_article['title']
    }
else:
    result = {
        'sports_article_titles': [],
        'sports_article_with_longest_description': None
    }

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_2dGUKOpRmpOF9KYi59rimcN9': [{'_id': '695989825eefb37cabc3943d', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '695989825eefb37cabc3943e', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '695989825eefb37cabc3943f', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '695989825eefb37cabc39440', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '695989825eefb37cabc39441', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
