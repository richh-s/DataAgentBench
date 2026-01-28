code = """import json
import random

# Read the articles from the file
data_file = locals()['var_functions.query_db:10']
with open(data_file, 'r') as f:
    articles = json.load(f)

# Sample 20 random articles to understand the data better
random_articles = random.sample(articles, 20)

samples = []
for article in random_articles:
    samples.append({
        'article_id': article['article_id'],
        'title': article['title'],
        'description_preview': article['description'][:100] + '...' if len(article['description']) > 100 else article['description'],
        'desc_length': len(article['description'])
    })

# Also look for articles with specific sports terms
sports_hunting = []

# Look for articles with obvious sports terms
strong_sports_terms = ['football', 'basketball', 'baseball', 'soccer', 'tennis', 'golf', 'nfl', 'nba', 'mlb', 'nhl', 'olympics', 'world cup']

for article in articles:
    combined = (article['title'] + ' ' + article['description']).lower()
    for term in strong_sports_terms:
        if term in combined:
            sports_hunting.append({
                'article_id': article['article_id'],
                'title': article['title'],
                'term_found': term,
                'desc_length': len(article['description'])
            })
            break  # Only add once per article

# Sort by length to see longest sports-like articles
sports_hunting.sort(key=lambda x: x['desc_length'], reverse=True)

result = {
    'random_samples': samples,
    'sports_candidates': sports_hunting[:10],  # Top 10 sports candidates
    'total_sports_candidates': len(sports_hunting)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'_id': '6969666e3efec42e10016862', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969666e3efec42e10016863', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969666e3efec42e10016864', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969666e3efec42e10016865', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969666e3efec42e10016866', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:8': {'found_sports_articles': 0, 'message': 'No sports articles found'}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': {'total_articles': 1000}, 'var_functions.execute_python:14': {'title': "Why Windows isn't Unix", 'description_length': 708, 'total_sports_articles_found': 268}, 'var_functions.execute_python:16': {'title': 'China Begins Countdown for Next Manned Space Flight', 'description_length': 580, 'total_sports_articles_found': 136, 'article_id': '279'}, 'var_functions.execute_python:18': {'title': 'RuntimeProperties... Reflection from System Properties', 'description_length': 708, 'total_sports_articles_found': 217, 'article_id': '167', 'top_5_longest': [{'title': 'RuntimeProperties... Reflection from System Properties', 'length': 708}, {'title': 'Pretty Log4J', 'length': 708}, {'title': "Kerry's Disgusting Ad", 'length': 708}, {'title': 'My Blog as a Time Machine', 'length': 602}, {'title': 'China Begins Countdown for Next Manned Space Flight', 'length': 580}]}}

exec(code, env_args)
