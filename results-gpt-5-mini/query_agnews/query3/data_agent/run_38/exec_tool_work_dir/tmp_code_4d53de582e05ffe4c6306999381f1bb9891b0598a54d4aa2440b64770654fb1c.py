code = """import json
import pandas as pd

# Load metadata JSON from file path provided in var_call_AvprAxNSyJFSY2VmNRgFkXCc
with open(var_call_AvprAxNSyJFSY2VmNRgFkXCc, 'r') as f:
    metadata = json.load(f)

articles = var_call_X2J3aYsxgNSIrqDWoS488Lj9

# Create DataFrames
md = pd.DataFrame(metadata)
art = pd.DataFrame(articles)

# Ensure article_id fields are comparable strings
md['article_id'] = md['article_id'].astype(str)
art['article_id'] = art['article_id'].astype(str)

# Extract year
md['year'] = pd.to_datetime(md['publication_date'], errors='coerce').dt.year

# Merge metadata with articles to get title and description
df = md.merge(art[['article_id','title','description']], on='article_id', how='left')

# Define business keywords
business_keywords = [
    'market','markets','stock','stocks','wall st','wall street','economy','economic',
    'company','companies','business','bank','banks','investment','investor','investors',
    'firm','firms','shares','finance','financial','merger','acquisition','carlyle',
    'private investment','oil prices','oil price','crude','short-sellers','short sellers'
]

# Build text field
df['text'] = (df['title'].fillna('') + ' ' + df['description'].fillna('')).str.lower()

# Flag business articles
import re

# Prepare regex pattern for keywords (escape and join)
pattern = r"|".join(re.escape(k) for k in business_keywords)

# Use regex search
df['is_business'] = df['text'].str.contains(pattern, regex=True)

# Consider only years 2010-2020 inclusive
years = list(range(2010, 2021))
counts_by_year = {}
for y in years:
    cnt = int(df.loc[df['year'] == y, 'is_business'].sum())
    counts_by_year[str(y)] = cnt

# Compute average
avg = float(sum(counts_by_year.values()) / len(years))
# Round to 2 decimal places
avg_rounded = round(avg, 2)

result = {
    'average_business_articles_per_year': avg_rounded,
    'counts_by_year': counts_by_year,
    'total_business_articles': int(sum(counts_by_year.values())),
    'years_included': [str(y) for y in years]
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_AvprAxNSyJFSY2VmNRgFkXCc': 'file_storage/call_AvprAxNSyJFSY2VmNRgFkXCc.json', 'var_call_X2J3aYsxgNSIrqDWoS488Lj9': [{'_id': '69599f3affc7a2d287e8f04a', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69599f3affc7a2d287e8f04b', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69599f3affc7a2d287e8f04c', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69599f3affc7a2d287e8f04d', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69599f3affc7a2d287e8f04e', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
