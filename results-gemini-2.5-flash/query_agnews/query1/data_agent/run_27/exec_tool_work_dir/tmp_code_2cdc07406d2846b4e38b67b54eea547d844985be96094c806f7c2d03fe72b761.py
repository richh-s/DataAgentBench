code = """import pandas as pd
import json

# Access the raw string result from the correct path
raw_string_output = locals()['var_function-call-7193223085481348698']['results'][0]

# The actual JSON array is enclosed within a string that also contains descriptive text.
# We need to find the beginning of the JSON array '[' and the end ']'.

start_idx = raw_string_output.find('[')
end_idx = raw_string_output.rfind(']')

if start_idx != -1 and end_idx != -1 and start_idx < end_idx:
    json_array_str = raw_string_output[start_idx : end_idx + 1]
    # Replace escaped single quotes with actual single quotes for valid JSON parsing if necessary
    # This specific error might be related to how json.loads handles backslashes within strings.
    # The provided data uses \\ for escaping, which is standard for JSON. Let's re-evaluate.
    articles_data = json.loads(json_array_str)
else:
    articles_data = [] # If JSON array not found, initialize as empty list

df = pd.DataFrame(articles_data)

sports_keywords = ['sport', 'game', 'team', 'player', 'match', 'league', 'cup', 'championship', 'olympic', 'athletics', 'football', 'basketball', 'baseball', 'soccer', 'tennis', 'golf', 'race', 'coach', 'stadium']

# Filter for sports articles based on title or description
sports_articles = df[df['title'].str.contains('|'.join(sports_keywords), case=False, na=False) | 
                     df['description'].str.contains('|'.join(sports_keywords), case=False, na=False)]

if not sports_articles.empty:
    # Create a copy to avoid SettingWithCopyWarning
    sports_articles = sports_articles.copy()
    sports_articles['description_length'] = sports_articles['description'].str.len()
    max_desc_article = sports_articles.loc[sports_articles['description_length'].idxmax()]
    result = max_desc_article['title']
else:
    result = "No sports articles found."

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-7040163389624421777': ['articles'], 'var_function-call-7193223085481348698': [{'_id': '6943c841f208d02ac96e6d1c', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943c841f208d02ac96e6d1d', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943c841f208d02ac96e6d1e', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943c841f208d02ac96e6d1f', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943c841f208d02ac96e6d20', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
