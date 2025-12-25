code = """import pandas as pd
import json
import re

tool_output = locals()['var_function-call-16761073810345406468']
results_list_of_strings = tool_output['query_db_response']['results']
full_output_string = results_list_of_strings[0]

# Extract the JSON array string using regex
# This regex should capture everything from the first '[' to the last ']'
match = re.search(r'\[.*\]', full_output_string, re.DOTALL)

articles_data = []
if match:
    json_string = match.group(0)

    # The tool output string represents a JSON string. 
    # In the tool output, a backslash `\` in the *original* JSON is represented as `\\`.
    # For example, `\\band` in the JSON output means the original description had `\band`.
    # In the Python string `json_string`, this appears as `\\\\band` (four backslashes).
    # We need to replace `\\\\` (four literal backslashes) with `\\` (two literal backslashes) for `json.loads`.
    json_string_corrected_backslashes = json_string.replace("\\\\", "\\")

    # Similarly, a single quote `'` in the *original* JSON (if escaped) is represented as `\'`.
    # For example, `Wall Street\'s` in the JSON output means the original description had `Wall Street's`.
    # In the Python string `json_string`, this appears as `\\\'s` (three backslashes, one single quote).
    # We need to replace `\\\'` (three literal backslashes and one single quote) with `\'` (one literal backslash and one single quote) for `json.loads`.
    # However, for `json.loads` to successfully parse, single quotes inside double-quoted strings don't need escaping.
    # So, replacing `\\\'` with `'` (one single quote) is more robust for `json.loads`.
    json_string_final = json_string_corrected_backslashes.replace("\\\'", "'")

    articles_data = json.loads(json_string_final)

df = pd.DataFrame(articles_data)

def is_sports(title, description):
    sports_keywords = ['sport', 'team', 'game', 'match', 'athlete', 'player', 'coach', 'league', 'championship', 'olympic', 'football', 'basketball', 'baseball', 'soccer', 'tennis', 'golf', 'race', 'cup', 'medal']
    title_lower = title.lower()
    description_lower = description.lower()
    for keyword in sports_keywords:
        if keyword in title_lower or keyword in description_lower:
            return True
    return False

sports_articles = df[df.apply(lambda row: is_sports(row['title'], row['description']), axis=1)]

if not sports_articles.empty:
    sports_articles = sports_articles.copy() # Avoid SettingWithCopyWarning
    sports_articles['description_length'] = sports_articles['description'].apply(len)
    longest_description_article = sports_articles.loc[sports_articles['description_length'].idxmax()]
    result = longest_description_article['title']
else:
    result = "No sports articles found."

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-16761073810345406468': [{'_id': '6943b93d4fe1f9b3c9810669', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943b93d4fe1f9b3c981066a', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943b93d4fe1f9b3c981066b', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943b93d4fe1f9b3c981066c', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943b93d4fe1f9b3c981066d', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
