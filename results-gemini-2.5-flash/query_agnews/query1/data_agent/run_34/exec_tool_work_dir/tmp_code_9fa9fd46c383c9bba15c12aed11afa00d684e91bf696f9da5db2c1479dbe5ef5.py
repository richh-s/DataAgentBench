code = """import pandas as pd
import json

raw_output = locals()['var_function-call-6273068033283457536']['query_db_response']['results'][0]

# Extract the JSON array part from the raw output string
json_start = raw_output.find('[')
json_end = raw_output.rfind(']')

articles = []
if json_start != -1 and json_end != -1:
    articles_json_str = raw_output[json_start : json_end + 1]
    
    # The JSON string itself might have escaped backslashes in description fields
    # These need to be handled carefully. json.loads usually handles \\ -> \ correctly.
    # Let's try to load directly and if it fails, then try cleaning specific patterns.
    try:
        articles = json.loads(articles_json_str)
    except json.JSONDecodeError as e:
        # If direct load fails, try some common problematic escape sequence replacements
        # This is a bit of a guess, based on common issues with JSON strings containing file paths or similar.
        # Let's try to replace \\\\ with \\ first, and then \\' with \'
        cleaned_articles_json_str = articles_json_str.replace('\\\\', '\\').replace('\\\'', '\'')
        try:
            articles = json.loads(cleaned_articles_json_str)
        except Exception as e_inner:
            # Fallback for logging or returning an error if both attempts fail
            print(f'Error parsing JSON after cleaning: {e_inner}')
            articles = [] # Ensure articles is an empty list on failure
            

if articles:
    df = pd.DataFrame(articles)

    sports_keywords = ['sport', 'game', 'team', 'match', 'win', 'lose', 'cup', 'league', 'athlete', 'football', 'basketball', 'baseball', 'tennis', 'golf', 'olympic', 'super bowl', 'championship']

    def is_sports_article(row):
        title_lower = str(row['title']).lower()
        description_lower = str(row['description']).lower()
        for keyword in sports_keywords:
            if keyword in title_lower or keyword in description_lower:
                return True
        return False

    sports_articles = df[df.apply(is_sports_article, axis=1)].copy()

    if not sports_articles.empty:
        # Calculate length after stripping potential escape characters that aren't part of the actual description text
        sports_articles['description_length'] = sports_articles['description'].apply(lambda x: len(str(x).replace('\\', '')))
        longest_description_article = sports_articles.loc[sports_articles['description_length'].idxmax()]
        result_title = longest_description_article['title']
    else:
        result_title = "No sports articles found."
else:
    result_title = "Failed to parse articles data or no articles found."

print('__RESULT__:')
print(pd.json_normalize([{'title': result_title}]).to_json(orient='records'))"""

env_args = {'var_function-call-6273068033283457536': [{'_id': '6943cdac478bde7900adefc4', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943cdac478bde7900adefc5', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943cdac478bde7900adefc6', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943cdac478bde7900adefc7', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943cdac478bde7900adefc8', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
