code = """import pandas as pd
import json
import re

tool_output = locals()['var_function-call-16761073810345406468']
results_list_of_strings = tool_output['query_db_response']['results']
full_output_string = results_list_of_strings[0]

# Use regex to find the JSON array part, which starts with '[' and ends with ']'
# re.DOTALL is important to match across newlines
match = re.search(r'\[.*\]', full_output_string, re.DOTALL)

articles_data = []
if match:
    json_string = match.group(0)

    # The raw output shows backslashes and single quotes escaped. For json.loads to work,
    # we need to correct these non-standard escapings.
    # Step 1: Correct escaped backslashes. If the original JSON had `\`, it's output as `\\`.
    # We need to change `\\` (in the raw string from tool output) to `\` for `json.loads`.
    # In Python, `\\` is a string literal for two backslashes. We want to replace it with `\` (one backslash).
    # So, four backslashes in the Python string `json_string` should become two backslashes for `json.loads`.
    # The actual string stored in `json_string` contains `\\\\` for a single backslash in the original content.
    # So we need to replace `\\\\` (eight backslashes) with `\\` (four backslashes) for json.loads.
    # No, this is incorrect. The example shows `\\band`, meaning the original data had `\band`.
    # When this `\band` is put into the JSON string, it becomes `"\\band"`.
    # When this JSON string is put into the Python output string, it becomes `"\\\\band"`.
    # So, we should replace `\\\\` with `\\`.
    json_string_cleaned = json_string.replace("\\\\", "\\")

    # Step 2: Correct non-standard escaped single quotes.
    # The example shows `Wall Street\'s`. This means the original data had `Wall Street's`.
    # When `Wall Street's` is put into JSON, it should ideally be `"Wall Street's"` (single quote unescaped if in double quotes).
    # However, the output shows `\'`. This means the single quote was escaped with a backslash.
    # In Python, `\'` is a string literal for `\'`. 
    # `json.loads` does not understand `\'`. It expects just `'` if the outer string were single-quoted, or `'` as is in a double quoted string.
    # We want to replace `\'` (backslash-single-quote literal) with `'` (single-quote literal).
    json_string_cleaned = json_string_cleaned.replace("\\'", "'")

    articles_data = json.loads(json_string_cleaned)

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
