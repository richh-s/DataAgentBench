code = """import json, pandas as pd
from pathlib import Path
import re

# Load metadata (Europe 2010-2020)
meta_path = Path(var_call_2kLC9CJKgcHqMx3qCt2nFgef)
meta_records = json.loads(meta_path.read_text())
meta_df = pd.DataFrame(meta_records)
meta_df['article_id'] = meta_df['article_id'].astype(int)

# Load all articles
arts_path = Path(var_call_Q0mU3AwYURBfWVhIjImc4mHs)
arts_records = json.loads(arts_path.read_text())
arts_df = pd.DataFrame(arts_records)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# Simple heuristic classifier for Business category
text = (arts_df['title'].fillna('') + ' ' + arts_df['description'].fillna('')).str.lower()

business_keywords = [
    'stock', 'stocks', 'share', 'shares', 'market', 'markets', 'wall st', 'dow ', 'nasdaq', 's&p',
    'economy', 'economic', 'trade deficit', 'trade gap', 'gdp', 'inflation', 'recession',
    'company', 'companies', 'firm ', 'firms', 'corporate', 'business', 'commerce',
    'oil price', 'oil prices', 'crude', 'opec',
    'ipo', 'initial public offering', 'merger', 'acquisition', 'm&a', 'takeover',
    'profit', 'profits', 'earnings', 'revenue', 'sales', 'dividend', 'investor', 'investors',
    'loan', 'loans', 'bank', 'banks', 'credit', 'finance', 'financial', 'fund', 'funds',
    'budget', 'deficit', 'tax', 'tariff', 'currency', 'dollar', 'euro', 'yen',
]

science_keywords = ['research', 'study', 'scientist', 'scientists', 'laboratory', 'lab ', 'experiment', 'physics', 'chemistry', 'biology', 'space', 'nasa', 'astronomy', 'tech ', 'technology', 'software', 'hardware', 'internet', 'computer', 'computers', 'ai ', 'robot', 'robots']

sports_keywords = ['match', 'game', 'games', 'tournament', 'league', 'cup ', 'championship', 'coach', 'player', 'players', 'team', 'teams', 'score', 'scored', 'goal', 'goals', 'season', 'olympic', 'olympics', 'nfl', 'nba', 'mlb', 'soccer', 'football', 'cricket', 'tennis', 'golf']

# Helper: compile regex pattern

def make_pattern(keywords):
    escaped = [re.escape(k) for k in keywords]
    return '(' + '|'.join(escaped) + ')'

biz_pat = make_pattern(business_keywords)
science_pat = make_pattern(science_keywords)
sports_pat = make_pattern(sports_keywords)

is_business = text.str.contains(biz_pat, regex=True)
is_science = text.str.contains(science_pat, regex=True)
is_sports = text.str.contains(sports_pat, regex=True)

arts_df['is_business'] = is_business & ~is_science & ~is_sports

# Merge with Europe metadata
merged = meta_df.merge(arts_df[['article_id', 'is_business']], on='article_id', how='left')

# Filter to business articles
biz = merged[merged['is_business'] == True].copy()

# Extract year
merged['year'] = merged['publication_date'].str.slice(0,4).astype(int)
biz['year'] = biz['publication_date'].str.slice(0,4).astype(int)

# Count per year and average 2010-2020 inclusive
counts = biz.groupby('year')['article_id'].nunique()
all_years = list(range(2010, 2021))
counts = counts.reindex(all_years, fill_value=0)

average_per_year = float(counts.mean())

result = json.dumps({'average_business_articles_per_year_europe_2010_2020': average_per_year, 'counts_per_year': counts.to_dict()})

print("__RESULT__:")
print(result)"""

env_args = {'var_call_2kLC9CJKgcHqMx3qCt2nFgef': 'file_storage/call_2kLC9CJKgcHqMx3qCt2nFgef.json', 'var_call_Q0mU3AwYURBfWVhIjImc4mHs': 'file_storage/call_Q0mU3AwYURBfWVhIjImc4mHs.json', 'var_call_DfLshTfP4DcrwOY2CsypmY8q': ['articles'], 'var_call_hoCopc0vlZExdSUglQd2egRK': ['authors', 'article_metadata']}

exec(code, env_args)
