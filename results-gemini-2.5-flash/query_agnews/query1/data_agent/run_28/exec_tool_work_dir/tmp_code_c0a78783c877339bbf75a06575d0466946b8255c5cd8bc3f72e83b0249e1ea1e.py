code = """import pandas as pd
import json

data_strings = locals()['var_function-call-13890009462590654747']['query_db_response']['results']

# Parse each JSON string in the list to a Python dictionary
data = [json.loads(s) for s in data_strings]

df = pd.DataFrame(data)

sports_articles = df[
    df['title'].str.contains('Sports', case=False) | 
    df['description'].str.contains('Sports', case=False) |
    df['title'].str.contains('Football', case=False) | 
    df['description'].str.contains('Football', case=False) |
    df['title'].str.contains('Basketball', case=False) | 
    df['description'].str.contains('Basketball', case=False) |
    df['title'].str.contains('Baseball', case=False) | 
    df['description'].str.contains('Baseball', case=False) |
    df['title'].str.contains('Tennis', case=False) | 
    df['description'].str.contains('Tennis', case=False) |
    df['title'].str.contains('Golf', case=False) | 
    df['description'].str.contains('Golf', case=False) |
    df['title'].str.contains('Olympics', case=False) | 
    df['description'].str.contains('Olympics', case=False)
]

if not sports_articles.empty:
    sports_articles['description_length'] = sports_articles['description'].apply(len)
    longest_description_article = sports_articles.loc[sports_articles['description_length'].idxmax()]
    result = longest_description_article['title']
else:
    result = "No sports articles found."

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-13890009462590654747': [{'_id': '6943c944083eb087172873bc', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943c944083eb087172873bd', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943c944083eb087172873be', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943c944083eb087172873bf', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943c944083eb087172873c0', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
