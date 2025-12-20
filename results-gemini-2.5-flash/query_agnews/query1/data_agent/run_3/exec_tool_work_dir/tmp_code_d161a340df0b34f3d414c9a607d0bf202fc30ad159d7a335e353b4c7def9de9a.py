code = """import json

articles = locals()['var_function-call-3553061123882171801']['query_db_response']['results']
sports_articles = []

for article_str in articles:
    article_dict = json.loads(article_str)
    title = article_dict.get('title', '').lower()
    description = article_dict.get('description', '').lower()

    # Check for sports keywords in title or description
    if 'sport' in title or 'sport' in description or \
       'team' in title or 'team' in description or \
       'game' in title or 'game' in description or \
       'match' in title or 'match' in description or \
       'league' in title or 'league' in description or \
       'cup' in title or 'cup' in description:
        sports_articles.append(article_dict)

if not sports_articles:
    result = {"error": "No sports articles found."}
else:
    max_desc_len = -1
    article_with_longest_desc = None
    for article in sports_articles:
        desc_len = len(article.get('description', ''))
        if desc_len > max_desc_len:
            max_desc_len = desc_len
            article_with_longest_desc = article

    result = {"title": article_with_longest_desc.get('title')}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-3553061123882171801': [{'_id': '6943ad31662233f6885122c5', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943ad31662233f6885122c6', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943ad31662233f6885122c7', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943ad31662233f6885122c8', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943ad31662233f6885122c9', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
