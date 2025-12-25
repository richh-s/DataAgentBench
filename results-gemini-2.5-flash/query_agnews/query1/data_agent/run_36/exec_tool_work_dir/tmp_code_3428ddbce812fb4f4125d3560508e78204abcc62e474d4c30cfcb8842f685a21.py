code = """import json
import pandas as pd

# Load the full JSON data
with open(locals()['var_function-call-14601129608225625672']) as f:
    articles_data = json.load(f)

df = pd.DataFrame(articles_data)

# Convert article_id to string to ensure consistent type for comparison
df['article_id'] = df['article_id'].astype(str)


# Filter for sports articles
sports_keywords = ['sport', 'football', 'basketball', 'baseball', 'soccer', 'tennis', 'golf', 'olympics', 'game', 'team', 'match', 'athlete', 'championship', 'league', 'cup', 'race']
def is_sports_article(row):
    title_lower = row['title'].lower()
    description_lower = row['description'].lower()
    return any(keyword in title_lower or keyword in description_lower for keyword in sports_keywords)

sports_articles = df[df.apply(is_sports_article, axis=1)]

# Calculate description length
sports_articles['description_length'] = sports_articles['description'].apply(len)

# Find article with the greatest description length
if not sports_articles.empty:
    longest_description_article = sports_articles.loc[sports_articles['description_length'].idxmax()]
    result = longest_description_article['title']
else:
    result = "No sports articles found."

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-14601129608225625672': [{'_id': '6943d029c90689048a26dc38', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943d029c90689048a26dc39', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943d029c90689048a26dc3a', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943d029c90689048a26dc3b', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943d029c90689048a26dc3c', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
