code = """import pandas as pd
import json
import re

# Access the dictionary containing the query result
response_dict = locals()['var_function-call-9850137662304608246']

# Access the list of results strings
results_list = response_dict['query_db_response']['results']

# The actual list of dictionaries is a string within the first element of results_list
# This string also contains extra text and newlines, so we need to extract the JSON part
if results_list:
    data_string_with_extra = results_list[0]
    # Use regex to find the JSON array part within the string
    match = re.search(r'\[\{.*\}\]', data_string_with_extra, re.DOTALL)
    if match:
        json_array_str = match.group(0)
        data = json.loads(json_array_str)
    else:
        data = [] # Handle case where no JSON array is found
else:
    data = [] # Handle case where results_list is empty

df = pd.DataFrame(data)

sports_keywords = ['sport', 'sports', 'game', 'match', 'team', 'league', 'cup', 'championship', 'olympics', 'athlete', 'player', 'coach', 'football', 'basketball', 'baseball', 'soccer', 'tennis', 'golf', 'racing', 'wrestling', 'boxing', 'formula 1', 'nba', 'nfl', 'mlb', 'nhl']

def is_sports_article(title, description):
    title_lower = title.lower() if title else ""
    description_lower = description.lower() if description else ""
    for keyword in sports_keywords:
        if keyword in title_lower or keyword in description_lower:
            return True
    return False

df['is_sports'] = df.apply(lambda row: is_sports_article(row.get('title'), row.get('description')), axis=1)
sports_articles = df[df['is_sports']]

if not sports_articles.empty:
    sports_articles.loc[:, 'description_length'] = sports_articles['description'].apply(lambda x: len(x) if x else 0)
    longest_description_article = sports_articles.loc[sports_articles['description_length'].idxmax()]
    result = longest_description_article['title']
else:
    result = "No sports articles found."

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-9850137662304608246': [{'_id': '6943c6887c9b17602d3516f6', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943c6887c9b17602d3516f7', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943c6887c9b17602d3516f8', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943c6887c9b17602d3516f9', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943c6887c9b17602d3516fa', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
