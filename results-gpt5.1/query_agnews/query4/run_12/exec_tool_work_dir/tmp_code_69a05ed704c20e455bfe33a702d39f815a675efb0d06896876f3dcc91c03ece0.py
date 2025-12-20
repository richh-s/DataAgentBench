code = """import json, pandas as pd

# Load full results
with open(var_call_ck0YF52lv1Ixcaibulw4feIc, 'r') as f:
    meta = json.load(f)
with open(var_call_rbZzRw3FLzGSQPjKnBd7osKE, 'r') as f:
    arts = json.load(f)

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# Merge metadata with articles on article_id
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

merged = pd.merge(meta_df, arts_df, on='article_id', how='inner')

# Simple heuristic: classify category based on keywords in title+description
text = (merged['title'].fillna('') + ' ' + merged['description'].fillna('')).str.lower()

world_keywords = ['iraq', 'afghanistan', 'united nations', 'u.n.', 'election', 'rebel', 'attack', 'palestinian', 'israel', 'iraqi', 'militant', 'bomb', 'war', 'conflict', 'government', 'president', 'prime minister']
sports_keywords = ['soccer', 'football', 'nba', 'nfl', 'nhl', 'mlb', 'olympic', 'olympics', 'tennis', 'golf', 'cricket', 'baseball', 'basketball', 'hockey', 'tournament', 'cup', 'league']
business_keywords = ['stock', 'stocks', 'market', 'oil', 'economy', 'economic', 'share', 'shares', 'ipo', 'trade deficit', 'growth', 'profit', 'losses', 'earnings', 'merger', 'acquisition']
scitech_keywords = ['scientist', 'research', 'study', 'nasa', 'space', 'technology', 'software', 'computer', 'physics', 'biology', 'internet', 'online', 'science']

categories = []
for t in text:
    cat = None
    if any(k in t for k in sports_keywords):
        cat = 'Sports'
    if cat is None and any(k in t for k in scitech_keywords):
        cat = 'Science/Technology'
    if cat is None and any(k in t for k in business_keywords):
        cat = 'Business'
    if cat is None and any(k in t for k in world_keywords):
        cat = 'World'
    if cat is None:
        # default to World as many general news
        cat = 'World'
    categories.append(cat)

merged['category'] = categories

world_2015 = merged[merged['category'] == 'World']
counts = world_2015.groupby('region').size().sort_values(ascending=False)

result = {"top_region": counts.index[0], "count": int(counts.iloc[0])}

result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_ck0YF52lv1Ixcaibulw4feIc': 'file_storage/call_ck0YF52lv1Ixcaibulw4feIc.json', 'var_call_rbZzRw3FLzGSQPjKnBd7osKE': 'file_storage/call_rbZzRw3FLzGSQPjKnBd7osKE.json'}

exec(code, env_args)
