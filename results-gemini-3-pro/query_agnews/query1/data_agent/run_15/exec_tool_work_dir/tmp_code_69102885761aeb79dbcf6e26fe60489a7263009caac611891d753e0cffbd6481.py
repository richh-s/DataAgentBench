code = """import json
import pandas as pd

data_source = locals()['var_function-call-17368558568938504511']

if isinstance(data_source, str):
    with open(data_source, 'r') as f:
        data = json.load(f)
else:
    data = data_source

df = pd.DataFrame(data)
df['desc_len'] = df['description'].fillna('').apply(len)

# Define sports keywords
sports_keywords = [
    'sport', 'game', 'team', 'cup', 'olympic', 'league', 'football', 'soccer', 
    'basketball', 'baseball', 'tennis', 'racing', 'nfl', 'nba', 'fifa', 'nhl', 
    'athlete', 'medal', 'championship', 'tournament', 'match', 'coach', 'score',
    'sox', 'yankee', 'mets', 'reds', 'bulls', 'lakers', 'knicks', 'giants', 'jets',
    'patriots', 'cowboys', '49ers', 'packers', 'steelers', 'eagles', 'liverpool',
    'arsenal', 'chelsea', 'united', 'real madrid', 'barcelona', 'milan', 'juventus',
    'ferrari', 'mclaren', 'williams', 'renault', 'honda', 'toyota', 'f1', 'nascar',
    'pga', 'lpga', 'atp', 'wta', 'davis cup', 'fed cup', 'wimbledon', 'us open',
    'french open', 'australian open', 'world cup', 'super bowl', 'world series',
    'stanley cup', 'gold medal', 'silver medal', 'bronze medal', 'record'
]

def is_sports(row):
    text = (str(row['title']) + " " + str(row['description'])).lower()
    # Simple check: if any keyword is in text
    # This might be too broad (e.g. "team" in business). 
    # But let's score it.
    score = 0
    found_keywords = []
    for kw in sports_keywords:
        if kw in text:
            score += 1
            found_keywords.append(kw)
    return score, found_keywords

df['sports_score'], df['keywords'] = zip(*df.apply(is_sports, axis=1))

# Sort by length desc
df_sorted = df.sort_values('desc_len', ascending=False)

# Get top 10 longest articles and their sports score/keywords to manual check
top_candidates = df_sorted.head(20)[['title', 'description', 'desc_len', 'sports_score', 'keywords']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(top_candidates))"""

env_args = {'var_function-call-3670063267380480662': [{'_id': '69446e5dc64be37359a8800d', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-3670063267380480271': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}], 'var_function-call-12635129205779054370': [{'_id': '69446e5dc64be37359a8800d', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69446e5dc64be37359a8800e', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69446e5dc64be37359a8800f', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69446e5dc64be37359a88010', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69446e5dc64be37359a88011', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-1009271780945625603': [{'_id': '69446e5dc64be37359a8800d', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69446e5dc64be37359a8800e', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69446e5dc64be37359a8800f', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69446e5dc64be37359a88010', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69446e5dc64be37359a88011', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-17368558568938504511': [{'_id': '69446e5dc64be37359a8800d', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69446e5dc64be37359a8800e', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69446e5dc64be37359a8800f', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69446e5dc64be37359a88010', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69446e5dc64be37359a88011', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
