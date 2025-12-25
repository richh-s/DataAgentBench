code = """import pandas as pd
import json
import re

tool_output = locals()['var_function-call-16761073810345406468']
results_list_of_strings = tool_output['query_db_response']['results']
full_output_string = results_list_of_strings[0]

# Extract the JSON array string using regex
match = re.search(r'\[.*\]', full_output_string, re.DOTALL)

articles_data = []
if match:
    json_string_raw = match.group(0)

    # First, handle the non-standard escaping of single quotes.
    # The raw output has `\'` (backslash followed by a single quote).
    # In the Python string `json_string_raw`, this appears as `\'` (literal backslash then literal single quote).
    # For `json.loads` to parse this within a double-quoted string, it should simply be a literal single quote.
    # So, replace `\'` with `'`.
    json_string_corrected_quotes = json_string_raw.replace("\\\'", "'")

    # Second, handle non-standard escaping of backslashes.
    # The raw output has `\\` (two backslashes).
    # In the Python string `json_string_raw`, this appears as `\` (one literal backslash).
    # For `json.loads` to parse a literal backslash, it needs to be `\\` (two backslashes).
    # So, replace `\` with `\\`.
    # Note: This replacement needs to happen AFTER correcting single quotes, to avoid double-escaping corrected quotes.
    json_string_final = json_string_corrected_quotes.replace("\\", "\\")

    try:
        articles_data = json.loads(json_string_final)
    except json.JSONDecodeError as e:
        result = f"JSON decoding failed: {e}"
        print('__RESULT__:')
        print(json.dumps(result))
        exit()

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
