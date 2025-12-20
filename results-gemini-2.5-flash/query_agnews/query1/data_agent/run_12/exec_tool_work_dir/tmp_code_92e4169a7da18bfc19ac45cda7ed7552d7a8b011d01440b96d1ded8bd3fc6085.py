code = """import pandas as pd
import json

articles_data_raw_str = locals()['var_function-call-2822739896604509108']['query_db_response']['results'][0]

# Find the start of the actual JSON array after "The result is:\n"
json_start_indicator = "The result is:\n"
start_index = articles_data_raw_str.find(json_start_indicator)
if start_index != -1:
    # Adjust start_index to point to the beginning of the JSON array '['
    json_array_start = articles_data_raw_str.find('[', start_index + len(json_start_indicator))
    json_array_end = articles_data_raw_str.rfind(']')

    if json_array_start != -1 and json_array_end != -1:
        articles_json_str = articles_data_raw_str[json_array_start : json_array_end + 1]
        articles_data = json.loads(articles_json_str)
        df = pd.DataFrame(articles_data)

        sports_keywords = ['sport', 'football', 'basketball', 'baseball', 'soccer', 'hockey', 'tennis', 'golf', 'olympics', 'game', 'match', 'athlete', 'team', 'league', 'championship', 'world cup']

        def is_sports_article(row):
            title_lower = row['title'].lower()
            description_lower = row['description'].lower()
            for keyword in sports_keywords:
                if keyword in title_lower or keyword in description_lower:
                    return True
            return False

        df['is_sports'] = df.apply(is_sports_article, axis=1)
        sports_articles = df[df['is_sports']]

        if not sports_articles.empty:
            sports_articles = sports_articles.copy() # Avoid SettingWithCopyWarning
            sports_articles['description_length'] = sports_articles['description'].apply(len)
            longest_description_article = sports_articles.loc[sports_articles['description_length'].idxmax()]
            result = longest_description_article['title']
        else:
            result = "No sports articles found."
    else:
        result = "Could not find JSON array in the string."
else:
    result = "Could not find JSON start indicator."

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-2822739896604509108': [{'_id': '6943b4e481c24a3baf7dd5ce', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943b4e481c24a3baf7dd5cf', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943b4e481c24a3baf7dd5d0', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943b4e481c24a3baf7dd5d1', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943b4e481c24a3baf7dd5d2', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
