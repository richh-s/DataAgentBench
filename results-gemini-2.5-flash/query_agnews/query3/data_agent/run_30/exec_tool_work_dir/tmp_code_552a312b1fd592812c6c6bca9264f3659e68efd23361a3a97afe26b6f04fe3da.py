code = """import json
import pandas as pd
import re

articles_data_raw = locals()['var_function-call-5014513872523189925']['results'][0]

# Extract the JSON array string from the raw output
json_match = re.search(r'\[.*\]', articles_data_raw, re.DOTALL)
if json_match:
    articles_json_str = json_match.group(0)
    articles_list = json.loads(articles_json_str)
else:
    articles_list = [] # Handle case where no JSON is found

df_articles = pd.DataFrame(articles_list)

def is_business_article(title, description):
    business_keywords = ["business", "economy", "market", "finance", "company", "stocks", "trade", "economic", "industry", "corporate", "investment", "shares", "banking", "euro", "profit", "revenue"]
    title_lower = title.lower() if title else ""
    description_lower = description.lower() if description else ""

    for keyword in business_keywords:
        if keyword in title_lower or keyword in description_lower:
            return True
    return False

df_articles['is_business'] = df_articles.apply(lambda row: is_business_article(row['title'], row['description']), axis=1)

business_article_ids = df_articles[df_articles['is_business']]['article_id'].tolist()

print("__RESULT__:")
print(json.dumps(business_article_ids))"""

env_args = {'var_function-call-5014513872523189925': [{'_id': '6943efbe567a959f6dfa279a', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943efbe567a959f6dfa279b', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943efbe567a959f6dfa279c', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943efbe567a959f6dfa279d', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943efbe567a959f6dfa279e', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
