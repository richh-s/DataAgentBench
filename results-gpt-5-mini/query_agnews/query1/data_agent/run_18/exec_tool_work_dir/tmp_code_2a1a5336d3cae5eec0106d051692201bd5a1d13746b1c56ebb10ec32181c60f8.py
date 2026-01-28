code = """import json
# Access the query result stored in var_call_NEWGzFEqlVUwIbW6l4yrL0xc
records = var_call_NEWGzFEqlVUwIbW6l4yrL0xc

sports_keywords = [
    'sport', 'sports', 'football', 'soccer', 'basketball', 'baseball', 'hockey',
    'tennis', 'golf', 'cricket', 'match', 'score', 'goal', 'coach', 'team', 'season',
    'olympic', 'olympics', 'nba', 'nfl', 'mlb', 'nhl', 'fifa', 'race', 'runner', 'boxing', 'boxing', 'athlete'
]

def is_sports(rec):
    text = ''
    if rec.get('title'):
        text += rec['title'].lower() + ' '
    if rec.get('description'):
        text += rec['description'].lower()
    for kw in sports_keywords:
        if kw in text:
            return True
    return False

sports_records = [r for r in records if is_sports(r)]

if not sports_records:
    result = None
else:
    # find the sports article with the longest description (number of characters)
    best = max(sports_records, key=lambda r: len(r.get('description') or ''))
    result = best.get('title')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_NEWGzFEqlVUwIbW6l4yrL0xc': [{'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
