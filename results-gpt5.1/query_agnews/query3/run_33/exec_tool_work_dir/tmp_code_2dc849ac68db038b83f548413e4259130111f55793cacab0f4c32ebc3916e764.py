code = """import json, pandas as pd

# Load Europe metadata full result
path = var_call_EP0q5KABNTkTYhabimuRQkoW
with open(path, 'r') as f:
    europe_meta = json.load(f)

articles = var_call_Jzu9pGhu1v5pdizprA1u8SFJ

# Build DataFrames
meta_df = pd.DataFrame(europe_meta)
meta_df['article_id'] = meta_df['article_id'].astype(int)
meta_df['year'] = meta_df['publication_date'].str.slice(0,4).astype(int)

art_df = pd.DataFrame(articles)
art_df['article_id'] = art_df['article_id'].astype(int)

# Merge
df = meta_df.merge(art_df, on='article_id', how='left')

# Business classifier using simple keywords
business_keywords = [
    'market','markets','stock','stocks','bond','bonds','trade','trading','economy','economic','business','company','companies',
    'finance','financial','merger','acquisition','deal','investment','investor','investors','profit','loss','revenue','earnings',
    'bank','banking','corporate','industry','industries','tariff','tariffs','unemployment','inflation','gdp','currency','currencies'
]

import re
pattern = re.compile(r"|".join(r"\\b"+re.escape(k)+r"\\b" for k in business_keywords), re.IGNORECASE)

def is_business(row):
    text = (str(row.get('title','')) + ' ' + str(row.get('description','')))
    return bool(pattern.search(text))

df['is_business'] = df.apply(is_business, axis=1)

# Count business articles per year
year_counts = df[df['is_business']].groupby('year')['article_id'].nunique()

# Ensure all years 2010-2020 present
years = list(range(2010, 2021))
counts = [int(year_counts.get(y, 0)) for y in years]

avg = sum(counts)/len(years)

result = json.dumps({
    'years': years,
    'business_counts': counts,
    'average_business_articles_per_year_2010_2020_Europe': avg
})

print("__RESULT__:")
print(result)"""

env_args = {'var_call_EP0q5KABNTkTYhabimuRQkoW': 'file_storage/call_EP0q5KABNTkTYhabimuRQkoW.json', 'var_call_Jzu9pGhu1v5pdizprA1u8SFJ': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_call_qwy46IKPXyBNssoz9pH644Uv': {'status': 'classifier_ready'}}

exec(code, env_args)
