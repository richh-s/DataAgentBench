code = """import pandas as pd
import json

articles_data = json.loads(locals()['var_function-call-3102122510052250243']['query_db_response']['results'][0])
articles_df = pd.DataFrame(articles_data)

def is_sports_article(title, description):
    keywords = ["sport", "game", "team", "match", "play", "league", "athlet", "cup", "championship", "coach", "player", "olympic"]
    title_lower = title.lower()
    description_lower = description.lower()
    for keyword in keywords:
        if keyword in title_lower or keyword in description_lower:
            return True
    return False

articles_df["is_sports"] = articles_df.apply(lambda row: is_sports_article(row["title"], row["description"]), axis=1)
sports_articles_df = articles_df[articles_df["is_sports"]]

if not sports_articles_df.empty:
    sports_articles_df["description_length"] = sports_articles_df["description"].apply(len)
    longest_description_article = sports_articles_df.loc[sports_articles_df["description_length"].idxmax()]
    result_title = longest_description_article["title"]
else:
    result_title = "No sports articles found."

print("__RESULT__:")
print(json.dumps(result_title))"""

env_args = {'var_function-call-3102122510052250243': [{'_id': '6943c0e59c9b5ec76c27095d', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943c0e59c9b5ec76c27095e', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943c0e59c9b5ec76c27095f', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943c0e59c9b5ec76c270960', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943c0e59c9b5ec76c270961', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
