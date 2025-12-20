code = """import pandas as pd
import json

articles = json.loads(locals()['var_function-call-18057397066400663115']['query_db_response']['results'][0])
df = pd.DataFrame(articles)

sports_keywords = ['sport', 'football', 'basketball', 'baseball', 'soccer', 'tennis', 'golf', 'olympics', 'game', 'team', 'athlete', 'race', 'cup', 'league', 'championship']

def is_sports_article(title, description):
    if title is None or description is None:
        return False
    for keyword in sports_keywords:
        if keyword in title.lower() or keyword in description.lower():
            return True
    return False

df['is_sports'] = df.apply(lambda row: is_sports_article(row['title'], row['description']), axis=1)
sports_articles = df[df['is_sports']]

if not sports_articles.empty:
    sports_articles['description_length'] = sports_articles['description'].apply(len)
    longest_description_article = sports_articles.loc[sports_articles['description_length'].idxmax()]
    result = longest_description_article['title']
else:
    result = "No sports articles found."

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-8285660236995326991': ['articles'], 'var_function-call-18057397066400663115': [{'_id': '6943d55d061e84939cf0fb52', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943d55d061e84939cf0fb53', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943d55d061e84939cf0fb54', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943d55d061e84939cf0fb55', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943d55d061e84939cf0fb56', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
