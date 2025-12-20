code = """import json
import pandas as pd
data_str = locals()['var_function-call-10328380462736807367']['query_db_response']['results'][0]
# The string itself has newlines and extra formatting that needs to be cleaned up for json.loads
cleaned_data_str = data_str.strip().replace('\\n', '') # Remove newlines and escape characters
data = json.loads(cleaned_data_str)
df = pd.DataFrame(data)

# Filter for sports articles by checking for the word 'Sports' (case-insensitive) in title or description
sports_articles = df[df['title'].str.contains('Sports', case=False) | df['description'].str.contains('Sports', case=False)]

if not sports_articles.empty:
    # Calculate description length
    sports_articles['description_length'] = sports_articles['description'].str.len()
    # Find article with the greatest description length
    longest_description_article = sports_articles.loc[sports_articles['description_length'].idxmax()]
    result = longest_description_article['title']
else:
    result = "No sports articles found."

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-10328380462736807367': [{'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
