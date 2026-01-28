code = """import json
import os

# Load all articles
articles_file = locals()['var_functions.query_db:8']
with open(articles_file, 'r') as f:
    articles = json.load(f)

# Define category keywords
sports_keywords = ['sports', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'hockey', 'cricket', 'rugby', 'volleyball', 'athlete', 'olympics', 'world cup', 'super bowl', 'nba', 'nfl', 'mlb', 'nhl', 'match', 'game', 'player', 'team', 'coach', 'league', 'tournament', 'championship', 'medal', 'record', 'season', 'quarterback', 'pitcher', 'goalkeeper', 'score', 'win', 'lose', 'defeat', 'victory']

business_keywords = ['business', 'wall st', 'stock', 'economy', 'market', 'company', 'firm', 'investment', 'finance', 'corporate', 'trade', 'dollar', 'shares', 'profit', 'bank', 'interest rates']

world_keywords = ['iraq', 'war', 'peace', 'conflict', 'oil', 'pipeline', 'presidential', 'elections', 'afghanistan', 'israel', 'palestine', 'iran', 'nuclear', 'united nations', 'security council', 'refugee', 'africa', 'europe', 'asia', 'mideast', 'military']

scitech_keywords = ['technology', 'science', 'research', 'study', 'scientist', 'tech', 'innovation', 'space', 'google', 'computer', 'software', 'internet', 'nuclear', 'physics', 'chemistry', 'biology', 'astronomy', 'satellite']

# Categorize articles
categorized_articles = []
sports_articles = []

for article in articles:
    title = article.get('title', '').lower()
    description = article.get('description', '').lower()
    text = title + ' ' + description
    
    # Initialize category scores
    category_scores = {
        'Sports': 0,
        'Business': 0,
        'World': 0,
        'Science/Technology': 0
    }
    
    # Count keyword matches
    for keyword in sports_keywords:
        if keyword in text:
            category_scores['Sports'] += 1
    
    for keyword in business_keywords:
        if keyword in text:
            category_scores['Business'] += 1
    
    for keyword in world_keywords:
        if keyword in text:
            category_scores['World'] += 1
    
    for keyword in scitech_keywords:
        if keyword in text:
            category_scores['Science/Technology'] += 1
    
    # Assign category with highest score, or 'Uncategorized' if no matches
    max_score = max(category_scores.values())
    if max_score > 0:
        category = max(category_scores, key=category_scores.get)
    else:
        category = 'Uncategorized'
    
    categorized_article = {
        'article_id': str(article.get('article_id')),
        'title': article.get('title', ''),
        'description': article.get('description', ''),
        'description_length': len(article.get('description', '')),
        'category': category,
        'category_scores': category_scores
    }
    
    categorized_articles.append(categorized_article)
    
    if category == 'Sports':
        sports_articles.append(categorized_article)

# Find sports article with longest description
sports_with_max_desc = None
if sports_articles:
    sports_with_max_desc = max(sports_articles, key=lambda x: x['description_length'])

# Sort sports articles by description length (descending)
sports_by_length = sorted(sports_articles, key=lambda x: x['description_length'], reverse=True)

result = {
    'total_articles': len(categorized_articles),
    'total_sports': len(sports_articles),
    'sports_article_with_longest_description': sports_with_max_desc,
    'top_10_sports_by_description_length': sports_by_length[:10],
    'category_counts': {
        'Sports': len([a for a in categorized_articles if a['category'] == 'Sports']),
        'Business': len([a for a in categorized_articles if a['category'] == 'Business']),
        'World': len([a for a in categorized_articles if a['category'] == 'World']),
        'Science/Technology': len([a for a in categorized_articles if a['category'] == 'Science/Technology']),
        'Uncategorized': len([a for a in categorized_articles if a['category'] == 'Uncategorized'])
    }
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': [{'_id': '696974d78d4ca6ceda5b83fc', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '696974d78d4ca6ceda5b83fd', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '696974d78d4ca6ceda5b83fe', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '696974d78d4ca6ceda5b83ff', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '696974d78d4ca6ceda5b8400', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:2': {'total_articles': 5, 'preview': [{'_id': '696974d78d4ca6ceda5b83fc', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '696974d78d4ca6ceda5b83fd', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '696974d78d4ca6ceda5b83fe', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}]}, 'var_functions.execute_python:5': {'articles': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again.", 'description_length': 94}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.', 'description_length': 214}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.', 'description_length': 184}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.', 'description_length': 195}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.', 'description_length': 160}], 'total_count': 5}, 'var_functions.execute_python:6': {'all_articles': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again.", 'description_length': 94, 'category': 'Business'}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.', 'description_length': 214, 'category': 'Business'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.', 'description_length': 184, 'category': 'Business'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.', 'description_length': 195, 'category': 'World'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.', 'description_length': 160, 'category': 'Business'}], 'sports_articles': [], 'total_articles': 5, 'total_sports': 0}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'total_articles_loaded': 1000}}

exec(code, env_args)
