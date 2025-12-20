code = """import json
import pandas as pd

# Load metadata
with open(locals()['var_function-call-16230520417025150586'], 'r') as f:
    metadata_list = json.load(f)
metadata = pd.DataFrame(metadata_list)
metadata['article_id'] = metadata['article_id'].astype(int)

# Load articles
with open(locals()['var_function-call-15625371316220222437'], 'r') as f:
    articles_list = json.load(f)
articles = pd.DataFrame(articles_list)
articles['article_id'] = articles['article_id'].astype(int)

# Merge
df = pd.merge(metadata, articles, on='article_id', how='inner')

# Define keywords
keywords = {
    'Business': ['market', 'stock', 'price', 'company', 'corp', 'inc', 'shares', 'profit', 'earnings', 'quarter', 'dollar', 'euro', 'bank', 'economy', 'trade', 'investment', 'investor', 'sale', 'oil', 'gas', 'fed', 'rate', 'inflation', 'business', 'deal', 'merger', 'ceo'],
    'Sci/Tech': ['technology', 'science', 'computer', 'software', 'internet', 'web', 'online', 'mobile', 'phone', 'chip', 'google', 'microsoft', 'apple', 'ibm', 'nasa', 'space', 'shuttle', 'launch', 'orbit', 'virus', 'study', 'research', 'linux', 'windows', 'digital', 'network'],
    'Sports': ['sport', 'game', 'match', 'team', 'cup', 'win', 'lose', 'score', 'goal', 'player', 'season', 'league', 'championship', 'olympic', 'medal', 'coach', 'manager', 'club', 'ball', 'run', 'race', 'football', 'basketball', 'baseball', 'tennis', 'soccer', 'hockey', 'cricket', 'rugby', 'nfl', 'nba', 'mlb', 'nhl'],
    'World': ['world', 'international', 'war', 'iraq', 'afghanistan', 'gaza', 'israel', 'palestinian', 'syria', 'iran', 'korea', 'china', 'russia', 'eu', 'un', 'nato', 'president', 'prime minister', 'minister', 'official', 'kill', 'bomb', 'attack', 'blast', 'military', 'troop', 'rebel', 'government', 'leader', 'election', 'poll', 'vote', 'protest', 'strike', 'court', 'trial', 'prison', 'rights', 'treaty', 'talks', 'diplomat', 'foreign', 'ministry', 'police', 'security', 'peace', 'nuclear']
}

def classify(row):
    text = (row['title'] + " " + row['description']).lower()
    scores = {cat: 0 for cat in keywords}
    for cat, kws in keywords.items():
        for kw in kws:
            if kw in text:
                scores[cat] += 1
    # Special handling: if 'oil' is present, it's often business unless 'iraq' or 'war' is also present.
    # But simple count is usually effective for these benchmarks.
    return max(scores, key=scores.get)

df['category'] = df.apply(classify, axis=1)

# Filter World
world_df = df[df['category'] == 'World']

# Group by Region
result = world_df.groupby('region').size().reset_index(name='count')
result = result.sort_values('count', ascending=False)

print("__RESULT__:")
print(result.to_json(orient='records'))"""

env_args = {'var_function-call-16230520417025150586': 'file_storage/function-call-16230520417025150586.json', 'var_function-call-3657157287295125768': 'file_storage/function-call-3657157287295125768.json', 'var_function-call-11380327074732110447': {'min': 13, 'max': 127570, 'count': 6696}, 'var_function-call-7239028984248077893': [{'COUNT(*)': '127600'}], 'var_function-call-4952987129056377997': {'count': 6695.0, 'mean': 19.0525765497, 'std': 18.3984364514, 'min': 1.0, '25%': 6.0, '50%': 14.0, '75%': 26.0, 'max': 181.0}, 'var_function-call-16156824569502898974': 'file_storage/function-call-16156824569502898974.json', 'var_function-call-15625371316220222437': 'file_storage/function-call-15625371316220222437.json'}

exec(code, env_args)
