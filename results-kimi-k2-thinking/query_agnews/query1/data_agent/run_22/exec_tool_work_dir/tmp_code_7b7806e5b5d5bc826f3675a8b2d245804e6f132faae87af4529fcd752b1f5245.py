code = """import json
articles = locals()['var_functions.query_db:2']

def classify_article_category(title, description):
    title_lower = title.lower()
    desc_lower = description.lower()
    
    sports_keywords = ['sport', 'game', 'team', 'player', 'coach', 'league', 'tournament', 'match', 'score', 'championship', 'final', 'semi', 'quarter', 'olympic', 'athlete', 'football', 'soccer', 'basketball', 'baseball', 'hockey', 'tennis', 'golf', 'cricket', 'rugby', 'nfl', 'nba', 'mlb', 'nhl', 'world cup', 'super bowl']
    business_keywords = ['business', 'economy', 'stock', 'market', 'wall st', 'wall street', 'finance', 'financial', 'company', 'corporate', 'investment', 'investor', 'profit', 'loss', 'revenue', 'sales', 'trade', 'trading', 'bank', 'banking', 'fund', 'hedge fund', 'private equity', 'carlyle', 'aerospace', 'oil', 'crude', 'energy']
    tech_keywords = ['technology', 'tech', 'science', 'scientific', 'research', 'discovery', 'innovation', 'digital', 'internet', 'software', 'hardware', 'computer', 'ai', 'artificial intelligence', 'robot', 'space', 'nasa', 'medical', 'medicine', 'health', 'disease', 'cure', 'vaccine', 'genetic', 'dna', 'clinical trial']
    world_keywords = ['world', 'international', 'global', 'united nations', 'un', 'europe', 'asia', 'africa', 'america', 'country', 'nation', 'government', 'president', 'prime minister', 'war', 'conflict', 'peace', 'treaty', 'diplomatic', 'iraq', 'iran', 'afghanistan', 'israel', 'palestine', 'syria', 'ukraine', 'russia', 'china', 'india', 'military', 'army', 'terrorist', 'terrorism']
    
    sports_score = sum(1 for keyword in sports_keywords if keyword in title_lower or keyword in desc_lower)
    business_score = sum(1 for keyword in business_keywords if keyword in title_lower or keyword in desc_lower)
    tech_score = sum(1 for keyword in tech_keywords if keyword in title_lower or keyword in desc_lower)
    world_score = sum(1 for keyword in world_keywords if keyword in title_lower or keyword in desc_lower)
    
    scores = {'Sports': sports_score, 'Business': business_score, 'Science/Technology': tech_score, 'World': world_score}
    max_score = max(scores.values())
    
    if max_score == 0:
        return 'World'
    
    max_categories = [cat for cat, score in scores.items() if score == max_score]
    return max_categories[0]

sports_articles = []
for article in articles:
    category = classify_article_category(article['title'], article['description'])
    if category == 'Sports':
        sports_articles.append({
            'article_id': article['article_id'],
            'title': article['title'],
            'description': article['description'],
            'description_length': len(article['description'])
        })

if sports_articles:
    longest = max(sports_articles, key=lambda x: x['description_length'])
    result = {'title': longest['title']}
else:
    result = {'title': None, 'message': 'No sports articles'}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'_id': '69696fbf477cc36744114c00', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69696fbf477cc36744114c01', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69696fbf477cc36744114c02', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69696fbf477cc36744114c03', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69696fbf477cc36744114c04', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:2': [{'_id': '69696fbf477cc36744114c00', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69696fbf477cc36744114c01', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69696fbf477cc36744114c02', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69696fbf477cc36744114c03', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69696fbf477cc36744114c04', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
