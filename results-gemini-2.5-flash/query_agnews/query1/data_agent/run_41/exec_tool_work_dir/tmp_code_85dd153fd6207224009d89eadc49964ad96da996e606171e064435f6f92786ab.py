code = """import json
import pandas as pd

articles_data_str = locals()['var_function-call-15072298909103489918']['query_db_response']['results'][0]
articles_data = json.loads(articles_data_str)

df = pd.DataFrame(articles_data)

sports_keywords = ['sport', 'football', 'basketball', 'baseball', 'soccer', 'tennis', 'golf', 'olympics', 'game', 'match', 'playoff', 'team', 'athlete', 'cup', 'league', 'championship', 'world series', 'super bowl', 'nba', 'nfl', 'mlb', 'nhl', 'fifa']

def is_sports_article(row):
    title_lower = row['title'].lower()
    description_lower = row['description'].lower()
    for keyword in sports_keywords:
        if keyword in title_lower or keyword in description_lower:
            return True
    return False

sports_articles_df = df[df.apply(is_sports_article, axis=1)].copy()

if not sports_articles_df.empty:
    sports_articles_df['description_length'] = sports_articles_df['description'].apply(len)
    longest_description_article = sports_articles_df.loc[sports_articles_df['description_length'].idxmax()]
    result_title = longest_description_article['title']
else:
    result_title = "No sports articles found."

print('__RESULT__:')
print(json.dumps(result_title))"""

env_args = {'var_function-call-15072298909103489918': [{'_id': '6943d21c43d59261268b1a7b', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943d21c43d59261268b1a7c', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943d21c43d59261268b1a7d', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943d21c43d59261268b1a7e', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943d21c43d59261268b1a7f', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
