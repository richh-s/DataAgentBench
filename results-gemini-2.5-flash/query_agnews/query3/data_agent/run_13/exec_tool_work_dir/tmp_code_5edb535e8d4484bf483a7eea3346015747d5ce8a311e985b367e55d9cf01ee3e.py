code = """import pandas as pd
import json

def is_business_article(title, description):
    business_keywords = ['business', 'economy', 'market', 'stock', 'finance', 'company', 'invest', 'profit', 'economic', 'trade', 'bank', 'corporate']
    title_lower = title.lower() if title else ''
    description_lower = description.lower() if description else ''

    for keyword in business_keywords:
        if keyword in title_lower or keyword in description_lower:
            return True
    return False

articles_raw_data = locals()['var_function-call-13676785764808340276']['query_db_response']['results']
business_articles_ids = set()

# Assuming articles_raw_data is a list containing a single string that is a JSON array
if articles_raw_data and isinstance(articles_raw_data, list) and articles_raw_data[0]:
    articles_json_string = articles_raw_data[0]
    # The string contains an initial newline and other text before the actual JSON array.
    # We need to find the start of the JSON array `[` and slice the string.
    json_start_index = articles_json_string.find('[')
    if json_start_index != -1:
        # Ensure the string is properly sliced to contain only the JSON array
        json_data_part = articles_json_string[json_start_index:]
        try:
            articles_data = json.loads(json_data_part)
        except json.JSONDecodeError as e:
            print(f"__RESULT__:\n{{ \"error\": \"JSON decoding failed: {e}\" }}")
            articles_data = [] # Set to empty list on error
    else:
        articles_data = [] # No JSON array found
else:
    articles_data = []

for article in articles_data:
    if is_business_article(article.get('title'), article.get('description')):
        business_articles_ids.add(int(article.get('article_id')))

print('__RESULT__:')
print(json.dumps(list(business_articles_ids)))"""

env_args = {'var_function-call-13676785764808340276': [{'_id': '6943ecefe0113d722733aa3d', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943ecefe0113d722733aa3e', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943ecefe0113d722733aa3f', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943ecefe0113d722733aa40', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943ecefe0113d722733aa41', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
