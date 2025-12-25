code = """import json

# Load the result from the previous step
with open('var_function-call-2103226498786508374.json', 'r') as f:
    articles = json.load(f)

print(f"Total articles: {len(articles)}")

# Define sports keywords
keywords = ['sport', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 
            'hockey', 'cricket', 'rugby', 'olympic', 'nba', 'nfl', 'nhl', 'mlb', 
            'fifa', 'uefa', 'world cup', 'super bowl', 'athlete', 'championship', 
            'tournament', 'league', 'medal', 'wrestling', 'boxing', 'swimming', 'marathon']

# Find potential sports articles
sports_candidates = []
for art in articles:
    text = (art.get('title', '') + " " + art.get('description', '')).lower()
    # Simple check: if any strong keyword is present
    if any(k in text for k in keywords):
        sports_candidates.append(art)

print(f"Potential sports articles: {len(sports_candidates)}")

# Sort by description length descending
sports_candidates.sort(key=lambda x: len(x.get('description', '')), reverse=True)

# Print top 3 to verify
print("__RESULT__:")
print(json.dumps(sports_candidates[:3], indent=2))"""

env_args = {'var_function-call-16533696639845188657': ['articles'], 'var_function-call-2103226498786508374': [{'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
