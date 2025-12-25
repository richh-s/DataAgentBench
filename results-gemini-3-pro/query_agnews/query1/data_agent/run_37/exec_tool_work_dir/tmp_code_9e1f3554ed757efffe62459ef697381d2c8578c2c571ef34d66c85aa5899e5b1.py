code = """import json
import pandas as pd

# Load the data from the file
file_path = locals()['var_function-call-7752384695117518704']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Define keywords for each category
keywords = {
    'World': ['iraq', 'president', 'minister', 'war', 'explosion', 'kill', 'dead', 'official', 'government', 'election', 'country', 'nuclear', 'police', 'military', 'bomb', 'protest', 'un', 'united nations', 'palestinian', 'israel', 'baghdad', 'troops', 'security', 'peace', 'attack'],
    'Business': ['stock', 'price', 'market', 'economy', 'company', 'corp', 'inc', 'profit', 'loss', 'dollar', 'bank', 'trade', 'oil', 'sales', 'rate', 'deal', 'ceo', 'share', 'investor', 'wall st', 'reuters', 'business', 'financial', 'fed', 'inflation', 'growth', 'budget'],
    'Sci/Tech': ['microsoft', 'intel', 'google', 'software', 'internet', 'computer', 'phone', 'technology', 'space', 'nasa', 'launch', 'system', 'device', 'web', 'online', 'network', 'virus', 'server', 'linux', 'apple', 'ibm', 'science', 'research', 'study', 'cell', 'mobile', 'wireless'],
    'Sports': ['sport', 'olympic', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'hockey', 'game', 'team', 'league', 'cup', 'champion', 'match', 'score', 'win', 'coach', 'player', 'athlete', 'medal', 'gold', 'silver', 'bronze', 'tournament', 'racing', 'f1', 'cricket', 'rugby', 'nfl', 'nba', 'mlb', 'nhl', 'athens', 'greece'] # Athens 2004 Olympics might be relevant given the dates in sample (2004)
}

def classify_article(text):
    text = text.lower()
    scores = {cat: 0 for cat in keywords}
    for cat, kws in keywords.items():
        for kw in kws:
            if kw in text:
                scores[cat] += 1
    
    # Return category with max score
    # If tie, or all 0, return 'Unknown'
    if max(scores.values()) == 0:
        return 'Unknown'
    return max(scores, key=scores.get)

sports_articles = []

for article in articles:
    text = article.get('title', '') + " " + article.get('description', '')
    category = classify_article(text)
    if category == 'Sports':
        sports_articles.append(article)

# Find the one with max description length
if not sports_articles:
    print('__RESULT__:')
    print(json.dumps("No sports articles found"))
else:
    best_article = max(sports_articles, key=lambda x: len(x.get('description', '')))
    print('__RESULT__:')
    print(json.dumps(best_article))"""

env_args = {'var_function-call-13104621924763589325': [{'_id': '694480101a20f323c78a04b2', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694480101a20f323c78a04b3', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694480101a20f323c78a04b4', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694480101a20f323c78a04b5', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694480101a20f323c78a04b6', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-6733588393098441366': [{'_id': '694480101a20f323c78a04b2', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694480101a20f323c78a04b3', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694480101a20f323c78a04b4', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694480101a20f323c78a04b5', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694480101a20f323c78a04b6', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-12515281274921194462': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'author_id': '992', 'region': 'North America', 'publication_date': '2004-03-20'}, {'article_id': '2', 'author_id': '820', 'region': 'South America', 'publication_date': '2021-02-04'}, {'article_id': '3', 'author_id': '478', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '4', 'author_id': '39', 'region': 'Africa', 'publication_date': '2012-02-01'}], 'var_function-call-4082764859491298474': [{'_id': '694480101a20f323c78a04b2', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694480101a20f323c78a04b3', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694480101a20f323c78a04b4', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694480101a20f323c78a04b5', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694480101a20f323c78a04b6', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-7752384695117518704': 'file_storage/function-call-7752384695117518704.json'}

exec(code, env_args)
