code = """import json
import pandas as pd

# Load metadata query result from file path variable
with open(var_call_83p0YDA0BuPuxOyPBfCT96dC, 'r') as f:
    meta_records = json.load(f)

# Articles records available directly
articles_records = var_call_GkmiD2u6uguxrF9tigGFF0V4

# Create dataframes
df_meta = pd.DataFrame(meta_records)
df_articles = pd.DataFrame(articles_records)

# Normalize types
# Some article_id values may be strings; convert to int for merge
df_meta['article_id'] = df_meta['article_id'].astype(int)
if 'article_id' in df_articles.columns:
    df_articles['article_id'] = df_articles['article_id'].astype(int)

# Merge
df = pd.merge(df_meta, df_articles, on='article_id', how='left')

# Extract year
df['year'] = pd.to_datetime(df['publication_date']).dt.year

# Define simple keyword-based classifier
business_kw = [
    'economy','economic','market','markets','stock','stocks','oil','business','company','companies',
    'investment','finance','financial','bank','revenue','profit','profits','share','shares','wall st','wall street',
    'carlyle','ipo','tax','trade','inflation','unemployment','short-sellers','short sellers'
]

sports_kw = ['football','soccer','basketball','tennis','golf','match','tournament','score','scores','goal','season','club','coach','league']

tech_kw = ['technology','tech','scientist','research','nasa','space','scientists','software','computer','ai','artificial intelligence','robot','science','scientific','internet']

def classify_text(title, desc):
    text = ''
    if pd.notna(title):
        text += title.lower() + ' '
    if pd.notna(desc):
        text += desc.lower()
    # Check business
    for kw in business_kw:
        if kw in text:
            return 'Business'
    for kw in sports_kw:
        if kw in text:
            return 'Sports'
    for kw in tech_kw:
        if kw in text:
            return 'Science/Technology'
    return 'World'

# Apply classifier
df['category'] = df.apply(lambda r: classify_text(r.get('title',''), r.get('description','')), axis=1)

# Consider years 2010-2020 inclusive
years = list(range(2010, 2021))
counts_by_year = {str(y): 0 for y in years}

for y in years:
    sub = df[df['year'] == y]
    # Count articles classified as Business
    c = int((sub['category'] == 'Business').sum())
    counts_by_year[str(y)] = c

# Compute average over the 11 years
total = sum(counts_by_year.values())
average = total / len(years)

# Prepare result
result = {
    'average_business_articles_per_year': average,
    'years_included': years,
    'business_articles_per_year': counts_by_year,
    'total_business_articles': total,
    'notes': 'Classification used simple keyword matching on title+description.'
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_83p0YDA0BuPuxOyPBfCT96dC': 'file_storage/call_83p0YDA0BuPuxOyPBfCT96dC.json', 'var_call_GkmiD2u6uguxrF9tigGFF0V4': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
