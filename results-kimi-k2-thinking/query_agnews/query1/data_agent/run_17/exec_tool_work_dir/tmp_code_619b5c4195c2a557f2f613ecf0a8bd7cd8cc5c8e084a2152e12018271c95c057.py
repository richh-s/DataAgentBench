code = """# Load the articles from the stored result
articles = locals()['var_functions.query_db:0']

# Convert to DataFrame for easier processing
import pandas as pd
import json

df = pd.DataFrame(articles)

# Function to check if an article is sports-related
def is_sports_article(row):
    title = str(row['title']).lower()
    description = str(row['description']).lower()
    
    sports_keywords = [
        'sports', 'football', 'basketball', 'baseball', 'soccer', 'tennis',
        'golf', 'athletes', 'athlete', 'olympics', 'game', 'games', 'team',
        'league', 'season', 'coach', 'player', 'players', 'scored', 'win',
        'won', 'victory', 'defeat', 'match', 'race', 'racing', 'championship',
        'tournament', 'cup', 'series', 'final', 'finals', 'quarterfinal',
        'semifinal', 'semifinals', 'playoff', 'playoffs', 'score', 'scores',
        'sport', 'sporting', 'ball', 'nba', 'nfl', 'mlb', 'nhl', 'ncaa',
        'hockey', 'cricket', 'rugby', 'boxing', 'mma', 'ufc'
    ]
    
    combined_text = title + ' ' + description
    
    return any(keyword in combined_text for keyword in sports_keywords)

# Filter sports articles
df['is_sports'] = df.apply(is_sports_article, axis=1)
sports_articles = df[df['is_sports'] == True].copy()

# Calculate description length
if not sports_articles.empty:
    sports_articles['description_length'] = sports_articles['description'].str.len()
    
    # Find article with max description length
    max_length_idx = sports_articles['description_length'].idxmax()
    article_with_longest_desc = sports_articles.loc[max_length_idx]
    
    title = article_with_longest_desc['title']
    desc_length = article_with_longest_desc['description_length']
    desc = article_with_longest_desc['description']
    
    result = {
        'title': title,
        'description': desc,
        'length': int(desc_length)
    }
else:
    result = None

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'_id': '69696de1cd36fccfee92531a', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69696de1cd36fccfee92531b', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69696de1cd36fccfee92531c', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69696de1cd36fccfee92531d', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69696de1cd36fccfee92531e', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
