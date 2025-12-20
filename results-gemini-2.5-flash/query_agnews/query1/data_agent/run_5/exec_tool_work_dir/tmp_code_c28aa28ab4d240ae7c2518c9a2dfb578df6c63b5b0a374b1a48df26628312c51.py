code = """import pandas as pd
import json

# Read the full JSON data from the file
with open(locals()['var_function-call-17926017845204998208'], 'r') as f:
    articles_data = json.load(f)

df = pd.DataFrame(articles_data)

sports_keywords = [
    "sport", "sports", "game", "team", "match", "play", "athlete", "coach", "league", 
    "championship", "cup", "medal", "olympic", "football", "basketball", "baseball", 
    "soccer", "tennis", "golf", "racing", "wrestling", "boxing", "swimming", 
    "track and field", "nfl", "nba", "mlb", "fifa", "wimbledon", "super bowl",
    "grand slam"
]

def is_sports_article(title, description):
    # Ensure title and description are strings before converting to lower case
    title_str = str(title) if title is not None else ""
    description_str = str(description) if description is not None else ""
    
    text = (title_str + " " + description_str).lower()
    for keyword in sports_keywords:
        if keyword in text:
            return True
    return False

df['is_sports'] = df.apply(lambda row: is_sports_article(row['title'], row['description']), axis=1)

sports_articles = df[df['is_sports']]

if not sports_articles.empty:
    sports_articles.loc[:, 'description_length'] = sports_articles['description'].apply(lambda x: len(str(x)))
    longest_description_article = sports_articles.loc[sports_articles['description_length'].idxmax()]
    result_title = longest_description_article['title']
else:
    result_title = "No sports articles found."

print('__RESULT__:')
print(json.dumps(result_title))"""

env_args = {'var_function-call-6307812241542364529': [{'_id': '6943ae57fa50a4e4730158c1', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943ae57fa50a4e4730158c2', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943ae57fa50a4e4730158c3', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943ae57fa50a4e4730158c4', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943ae57fa50a4e4730158c5', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-17926017845204998208': 'file_storage/function-call-17926017845204998208.json'}

exec(code, env_args)
