code = """import json, pandas as pd
import os

# Load metadata (Europe, 2010-2020)
meta = var_call_oHyuQOO1Gl8I4ZPRI7oLdhhs
if isinstance(meta, str) and os.path.isfile(meta):
    with open(meta, 'r') as f:
        meta = json.load(f)

# Load all articles
arts = var_call_a7WBFmqGenVNsWyn87BoP8fP
if isinstance(arts, str) and os.path.isfile(arts):
    with open(arts, 'r') as f:
        arts = json.load(f)

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# Ensure correct dtypes
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# Merge on article_id to get titles/descriptions for European 2010-2020
merged = meta_df.merge(arts_df, on='article_id', how='left')

# Simple keyword-based classifier for Business vs others
business_keywords = [
    'market','markets','stock','stocks','wall st','wall street','dow','nasdaq','ftse','dax','cac','bond','bonds',
    'bank','banks','banking','loan','loans','ipo','merger','acquisition','m&a','profit','profits','earnings',
    'share','shares','shareholder','dividend','dividends','fund','funds','hedge fund','investment','investor',
    'investors','economy','economic','finance','financial','business','company','companies','corporate',
    'revenue','sales','tariff','trade deficit','trade surplus','trade gap','oil prices','oil price','currency',
    'currencies','euro','dollar','yen','pound','forecast','outlook','jobless','unemployment','inflation',
    'interest rate','interest rates','central bank','ecb','federal reserve','fed ',
]

sports_keywords = ['match','cup','league','tournament','olympics','goal','scored','coach','season','championship']
science_keywords = ['research','scientist','scientists','laboratory','study','studies','nasa','space','technology','tech','software','hardware','device','devices','computer','computers','physics','chemistry','biology']

business_set = set(business_keywords)

def classify(row):
    text = f"{row.get('title','')} {row.get('description','')}".lower()
    # Simple rules: if any business keyword present, mark as Business unless clearly sports or sci/tech dominated
    is_business = any(k in text for k in business_keywords)
    is_sports = any(k in text for k in sports_keywords)
    is_science = any(k in text for k in science_keywords)
    if is_business and not (is_sports or is_science):
        return 'Business'
    if is_sports and not (is_business or is_science):
        return 'Sports'
    if is_science and not (is_business or is_sports):
        return 'Science/Technology'
    # Ties or none: default heuristic
    if is_business:
        return 'Business'
    if is_sports:
        return 'Sports'
    if is_science:
        return 'Science/Technology'
    return 'World'

merged['category'] = merged.apply(classify, axis=1)

# Filter to Business articles
business_df = merged[merged['category'] == 'Business'].copy()

# Extract year
business_df['year'] = business_df['publication_date'].str.slice(0,4).astype(int)

# Count per year and compute average over 2010-2020 inclusive
counts_per_year = business_df.groupby('year')['article_id'].nunique()

# Ensure all years 2010-2020 are represented (with 0 if missing)
years = list(range(2010, 2021))
counts = [int(counts_per_year.get(y, 0)) for y in years]

avg_per_year = sum(counts) / len(years) if years else 0

result = {
    'years': years,
    'business_article_counts_per_year_in_europe': counts,
    'average_business_articles_per_year_in_europe_2010_2020': avg_per_year
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_oHyuQOO1Gl8I4ZPRI7oLdhhs': 'file_storage/call_oHyuQOO1Gl8I4ZPRI7oLdhhs.json', 'var_call_a7WBFmqGenVNsWyn87BoP8fP': 'file_storage/call_a7WBFmqGenVNsWyn87BoP8fP.json'}

exec(code, env_args)
