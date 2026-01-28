code = """import json
import re

# Get the data
articles = locals()['var_functions.query_db:0']

# Categorize articles based on title/description
sports_keywords = ['sports', 'sport', 'game', 'match', 'team', 'player', 'football', 'basketball', 'baseball', 'soccer', 'tennis', 'golf', 'olympic', 'world cup', 'championship', 'league', 'coach', 'athlete']

# Check each article
def is_sports_article(article):
    title = article.get('title', '').lower()
    description = article.get('description', '').lower()
    combined_text = title + ' ' + description
    
    for keyword in sports_keywords:
        if keyword in combined_text:
            return True
    return False

# Find sports articles
sports_articles = []
for article in articles:
    if is_sports_article(article):
        article['description_length'] = len(article.get('description', ''))
        sports_articles.append(article)

# Check if we have any sports articles
if not sports_articles:
    result = "No sports articles found in the database"
else:
    # Find sports article with longest description
    longest_article = max(sports_articles, key=lambda x: x['description_length'])
    result = longest_article['title']

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
