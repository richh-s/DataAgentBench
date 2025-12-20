code = """import pandas as pd
import json

raw_string_output = locals()['var_function-call-7193223085481348698']['query_db_response']['results'][0]

# Locate the actual JSON array string
json_start_indicator = 'The result is:\n'
start_index = raw_string_output.find(json_start_indicator)

if start_index != -1:
    # Extract the substring that should be the JSON array
    json_array_str = raw_string_output[start_index + len(json_start_indicator):].strip()
    articles_data = json.loads(json_array_str)
else:
    articles_data = [] # No JSON found, handle gracefully

df = pd.DataFrame(articles_data)

sports_keywords = ['sport', 'game', 'team', 'player', 'match', 'league', 'cup', 'championship', 'olympic', 'athletics', 'football', 'basketball', 'baseball', 'soccer', 'tennis', 'golf', 'race', 'coach', 'stadium']
sports_articles = df[df['title'].str.contains('|'.join(sports_keywords), case=False, na=False) | df['description'].str.contains('|'.join(sports_keywords), case=False, na=False)]

if not sports_articles.empty:
    sports_articles = sports_articles.copy()  # Avoid SettingWithCopyWarning
    sports_articles['description_length'] = sports_articles['description'].str.len()
    max_desc_article = sports_articles.loc[sports_articles['description_length'].idxmax()]
    result = max_desc_article['title']
else:
    result = "No sports articles found."

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-7040163389624421777': ['articles'], 'var_function-call-7193223085481348698': [{'_id': '6943c841f208d02ac96e6d1c', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943c841f208d02ac96e6d1d', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943c841f208d02ac96e6d1e', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943c841f208d02ac96e6d1f', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943c841f208d02ac96e6d20', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
