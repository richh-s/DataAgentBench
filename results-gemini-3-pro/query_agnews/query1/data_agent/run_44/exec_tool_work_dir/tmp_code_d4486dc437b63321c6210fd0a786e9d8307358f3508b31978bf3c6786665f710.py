code = """import pandas as pd
import json

# Access the file path from the previous tool result
file_path = locals()['var_function-call-7468944605175876879']

with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
df['desc_len'] = df['description'].fillna('').apply(len)

# Define keywords
sports_keywords = [
    "sport", "game", "team", "league", "cup", "match", "score", "win", "won", "lose", "lost", "play", "player", 
    "coach", "season", "champion", "olympic", "medal", "athens", "gold", "silver", "bronze", 
    "race", "run", "ball", "football", "basketball", "baseball", "soccer", "tennis", "golf", 
    "hockey", "cricket", "rugby", "f1", "nascar", "stadium", "club", "tournament", "athlete", 
    "yankees", "red sox", "mets", "dodgers", "lakers", "bulls", "knicks", "celtics", "cowboys", 
    "packers", "giants", "eagles", "patriots", "steelers", "49ers", "raiders", "arsenal", 
    "chelsea", "manchester", "liverpool", "real madrid", "barcelona", "ac milan", "juventus", 
    "inter milan", "bayern munich", "tiger woods", "armstrong", "phelps", "nba", "nfl", "mlb", "nhl", "fifa", "uefa"
]

def is_sports(text):
    text = text.lower()
    score = 0
    for kw in sports_keywords:
        if kw in text:
            score += 1
    return score

# Score based on title and description
df['sports_score'] = (df['title'].fillna('') + " " + df['description'].fillna('')).apply(is_sports)

# Sort by length descending
df_sorted = df.sort_values('desc_len', ascending=False)

# Get top 20 longest descriptions
top_candidates = df_sorted.head(20)[['title', 'description', 'sports_score', 'desc_len']]

print("__RESULT__:")
print(top_candidates.to_json(orient='records'))"""

env_args = {'var_function-call-16604628605560456528': ['articles'], 'var_function-call-16604628605560458041': ['authors', 'article_metadata'], 'var_function-call-17633080332242759373': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-10846640288449309193': [{'_id': '69448634d329c46482887134', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69448634d329c46482887135', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69448634d329c46482887136', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69448634d329c46482887137', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69448634d329c46482887138', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-7468944605175876879': 'file_storage/function-call-7468944605175876879.json'}

exec(code, env_args)
