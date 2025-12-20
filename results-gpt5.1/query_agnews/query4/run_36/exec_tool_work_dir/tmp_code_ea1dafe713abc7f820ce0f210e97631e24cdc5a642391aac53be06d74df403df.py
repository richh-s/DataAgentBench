code = """import json, pandas as pd
from pathlib import Path

# Load full results from JSON files
meta_path = Path(var_call_cxdLiK235DIHTtad4wIlltRM)
with open(meta_path, 'r') as f:
    meta = json.load(f)

arts_path = Path(var_call_QBVdJE0jqZsxG69hlcXp8H1U)
with open(arts_path, 'r') as f:
    arts = json.load(f)

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# Merge
df = meta_df.merge(arts_df, on='article_id', how='inner')

# Simple rule-based categorization into World, Sports, Business, Science/Technology
def categorize(row):
    text = (str(row['title']) + ' ' + str(row['description'])).lower()
    business_kw = ['stock', 'stocks', 'market', 'shares', 'ipo', 'economy', 'economic', 'trade deficit', 'interest rate', 'rates', 'loan', 'bank', 'funds', 'investment', 'investor', 'company', 'profit', 'profits', 'revenue', 'oil prices', 'dollar', 'euro', 'yen', 'jobless', 'unemployment']
    sports_kw = ['football', 'soccer', 'nba', 'nfl', 'mlb', 'nhl', 'tennis', 'golf', 'olympic', 'olympics', 'world cup', 'grand prix', 'cricket', 'baseball', 'basketball', 'hockey', 'coach', 'season opener', 'playoffs']
    sci_kw = ['nasa', 'space', 'shuttle', 'galaxy', 'star', 'neutron', 'physics', 'chemistry', 'biology', 'genetic', 'researchers', 'scientists', 'technology', 'software', 'computer', 'computing', 'internet', 'robot', 'robots', 'ai ', 'artificial intelligence', 'virus', 'bacteria', 'climate', 'global warming']

    if any(k in text for k in sports_kw):
        return 'Sports'
    if any(k in text for k in business_kw):
        return 'Business'
    if any(k in text for k in sci_kw):
        return 'Science/Technology'
    return 'World'

df['category'] = df.apply(categorize, axis=1)

world_2015 = df[df['category'] == 'World']
counts = world_2015['region'].value_counts()

if counts.empty:
    result = None
else:
    top_region = counts.idxmax()
    result = top_region

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_cxdLiK235DIHTtad4wIlltRM': 'file_storage/call_cxdLiK235DIHTtad4wIlltRM.json', 'var_call_QBVdJE0jqZsxG69hlcXp8H1U': 'file_storage/call_QBVdJE0jqZsxG69hlcXp8H1U.json'}

exec(code, env_args)
