code = """import pandas as pd
import json

# Access the full result from the storage variable
# The result is a dictionary with 'results' key, which contains a list of strings.
# The first element of this list is the JSON array string along with some text.
raw_result_list = locals()['var_function-call-6160732592000302650']['results']
articles_data_with_text = raw_result_list[0]

# Extract the JSON array string from the raw result string.
# The JSON array starts with '[' and ends with ']'.
json_start_index = articles_data_with_text.find('[')
json_end_index = articles_data_with_text.rfind(']')
articles_data_json_str = articles_data_with_text[json_start_index : json_end_index + 1]

# Parse the JSON string to get the list of dictionaries
articles_data = json.loads(articles_data_json_str)

df = pd.DataFrame(articles_data)

# Calculate the length of the description for each article
df['description_length'] = df['description'].apply(lambda x: len(x) if x is not None else 0)

# Define keywords for sports articles (case-insensitive).
sports_keywords = [
    'sport', 'sports', 'game', 'games', 'match', 'matches', 'team', 'teams', 'league', 'championship',
    'cup', 'olympics', 'athlete', 'player', 'coach', 'referee', 'tournament', 'season', 'score', 'win', 'lose', 'defeat',
    'victory', 'draw', 'tie', 'race', 'track', 'field', 'arena', 'stadium', 'pitch', 'court', 'golf', 'tennis',
    'football', 'soccer', 'basketball', 'baseball', 'hockey', 'rugby', 'cricket', 'boxing', 'wrestling',
    'swimming', 'cycling', 'athletics', 'skiing', 'snowboarding', 'surfing', 'volleyball', 'handball',
    'badminton', 'table tennis', 'formula 1', 'f1', 'nascar', 'super bowl', 'world series', 'nba', 'nfl',
    'mlb', 'nhl', 'fifa', 'wimbledon', 'grand slam', 'marathon'
]

# Function to check if an article is sports-related using a broader keyword set
def is_sports_article(title, description, keywords):
    text = ""
    if title is not None:
        text += title.lower() + " "
    if description is not None:
        text += description.lower()
    
    for keyword in keywords:
        if keyword in text:
            return True
    return False

# Filter for sports articles
df['is_sports'] = df.apply(lambda row: is_sports_article(row['title'], row['description'], sports_keywords), axis=1)
sports_articles_df = df[df['is_sports'] == True]

result_title = ""
if not sports_articles_df.empty:
    # Find the sports article with the greatest number of characters in its description
    longest_description_sports_article = sports_articles_df.loc[sports_articles_df['description_length'].idxmax()]
    result_title = longest_description_sports_article['title']
else:
    result_title = "No sports articles found in the dataset with current keywords."

print('__RESULT__:')
print(json.dumps(result_title))"""

env_args = {'var_function-call-6160732592000302650': [{'_id': '6943be3658bf4c3958610175', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943be3658bf4c3958610176', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943be3658bf4c3958610177', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943be3658bf4c3958610178', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943be3658bf4c3958610179', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
