code = """import json
import pandas as pd

# Load the data
data_var = locals()['var_function-call-15686240030509850180']
if isinstance(data_var, str):
    with open(data_var, 'r') as f:
        articles = json.load(f)
else:
    articles = data_var

# Convert to DataFrame
df = pd.DataFrame(articles)

# Keywords for sports
# Note: AG News is from 2004.
sports_keywords = [
    'sport', 'sports', 'football', 'baseball', 'basketball', 'soccer', 'tennis', 'golf', 'hockey',
    'olympic', 'olympics', 'athens', 'medal', 'gold', 'silver', 'bronze',
    'nfl', 'nba', 'mlb', 'nhl', 'fifa', 'uefa',
    'championship', 'champion', 'tournament', 'league', 'cup', 'world cup',
    'game', 'match', 'team', 'coach', 'player', 'athlete',
    'score', 'win', 'won', 'winner', 'loss', 'lost', 'defeat', 'victory',
    'season', 'playoff', 'super bowl', 'world series', 'stanley cup',
    'grand prix', 'f1', 'nascar', 'racing',
    'wimbledon', 'us open', 'french open', 'australian open',
    'yankees', 'red sox', 'lakers', 'pistons', 'patriots', 'eagles',
    'real madrid', 'manchester', 'arsenal', 'chelsea',
    'tiger woods', 'federer', 'roddick', 'williams', 'armstrong', 'phelps', 'thorpe'
]

def is_sports(row):
    text = (str(row['title']) + " " + str(row['description'])).lower()
    # Simple check: if any keyword is present as a whole word or significant part
    # To be more robust, we can check for word boundaries or just inclusion
    # Given the specificity, inclusion is likely fine, but short words like 'cup' or 'win' might be risky in other contexts.
    # Let's count hits.
    score = 0
    for k in sports_keywords:
        if k in text:
            score += 1
    return score

# Score each article
df['sports_score'] = df.apply(is_sports, axis=1)

# Filter for likely sports articles (score >= 1)
# To be safe, maybe score >= 2 or check specific strong keywords?
# Let's look at the top candidates by description length among those with score >= 1.
sports_df = df[df['sports_score'] >= 1].copy()

# Calculate description length
sports_df['desc_len'] = sports_df['description'].astype(str).apply(len)

# Sort by length descending
top_sports = sports_df.sort_values(by='desc_len', ascending=False).head(5)

# Prepare result
result = top_sports[['title', 'description', 'sports_score', 'desc_len']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-9486180232665500453': ['articles'], 'var_function-call-9486180232665501096': ['authors', 'article_metadata'], 'var_function-call-14264674136081503679': [{'_id': '6944762b1d6282a841d85ad9', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-14264674136081505188': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}], 'var_function-call-6725456994874746152': [{'_id': '6944762b1d6282a841d85ad9', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944762b1d6282a841d85ada', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944762b1d6282a841d85adb', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944762b1d6282a841d85adc', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944762b1d6282a841d85add', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-15686240030509850180': [{'_id': '6944762b1d6282a841d85ad9', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944762b1d6282a841d85ada', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944762b1d6282a841d85adb', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944762b1d6282a841d85adc', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944762b1d6282a841d85add', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
