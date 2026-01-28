code = """import json
import pandas as pd
import re

# Load metadata records from the file path stored in var_call_nB1p5TIHl9VbLipRXchbATYi
meta_path = var_call_nB1p5TIHl9VbLipRXchbATYi
with open(meta_path, 'r', encoding='utf-8') as f:
    meta_records = json.load(f)

# Load articles records from the variable
articles_records = var_call_wNli2k0PoKdwC7I6wt7qSNsq

# Build DataFrames
df_meta = pd.DataFrame(meta_records)
# Ensure proper types
df_meta['article_id'] = df_meta['article_id'].astype(int)
# Extract year
df_meta['year'] = df_meta['publication_date'].str.slice(0,4).astype(int)
# Filter years 2010-2020 (should already be)
df_meta = df_meta[(df_meta['year'] >= 2010) & (df_meta['year'] <= 2020)]

df_articles = pd.DataFrame(articles_records)
# article_id may be string
if df_articles['article_id'].dtype == object:
    df_articles['article_id'] = df_articles['article_id'].astype(int)
# fill NA
if 'description' not in df_articles.columns:
    df_articles['description'] = ''
else:
    df_articles['description'] = df_articles['description'].fillna('')
if 'title' not in df_articles.columns:
    df_articles['title'] = ''
else:
    df_articles['title'] = df_articles['title'].fillna('')

# Merge
df = pd.merge(df_meta, df_articles, on='article_id', how='left')

# Define keyword lists
business_kw = ['business','market','markets','stock','stocks','economy','economic','finance','financial','bank','banks','firm','company','companies','investment','investor','investors','merger','acquisition','acquisitions','earnings','revenue','profit','profits','ipo','oil prices','oil','short-sellers','short sellers','private investment','wall st','bear','bears','carlyle']

sports_kw = ['game','match','tournament','score','goal','football','soccer','basketball','baseball','tennis','cricket','nhl','nfl','mlb','cup','season','coach','player','athlete']

science_kw = ['technology','tech','scientist','research','study','nasa','space','computer','software','ai','artificial intelligence','scientific','science','biotech','medical','medicine','disease','researchers']

# classification function
def classify_row(title, desc):
    text = (str(title) + ' ' + str(desc)).lower()
    # check business
    for kw in business_kw:
        if kw in text:
            return 'Business'
    for kw in sports_kw:
        if kw in text:
            return 'Sports'
    for kw in science_kw:
        if kw in text:
            return 'Science/Technology'
    return 'World'

# Apply classification
df['category'] = df.apply(lambda r: classify_row(r['title'], r['description']), axis=1)

# Count business articles per year
years = list(range(2010, 2021))
counts = {str(y): int(df[(df['year']==y) & (df['category']=='Business')].shape[0]) for y in years}

total_business = sum(counts.values())
num_years = len(years)
avg = total_business / num_years if num_years>0 else 0.0
# round to 2 decimals
avg_rounded = round(avg, 2)

result = {
    'year_counts': counts,
    'average_business_articles_per_year': avg_rounded,
    'total_business_articles': int(total_business),
    'years_included': years
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_nB1p5TIHl9VbLipRXchbATYi': 'file_storage/call_nB1p5TIHl9VbLipRXchbATYi.json', 'var_call_3ft82kwov3WmIRbhPYm9MnAV': 'file_storage/call_3ft82kwov3WmIRbhPYm9MnAV.json', 'var_call_Aplmiw8fk9365EYpPVtaVJK6': ['articles'], 'var_call_wNli2k0PoKdwC7I6wt7qSNsq': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
