code = """import json
import pandas as pd

# Load metadata JSON from file path stored in var_call_3cvDIxlgOKjcJmaTOZlfO9gC
metadata_path = var_call_3cvDIxlgOKjcJmaTOZlfO9gC
with open(metadata_path, 'r', encoding='utf-8') as f:
    metadata = json.load(f)

# Load articles data from variable var_call_eKFULgr7qXp2kDuSIm9E1LIO
articles = var_call_eKFULgr7qXp2kDuSIm9E1LIO

# Convert to DataFrame for easier processing
md = pd.DataFrame(metadata)
art = pd.DataFrame(articles)

# Ensure article_id fields are strings for consistent join
md['article_id'] = md['article_id'].astype(str)
art['article_id'] = art['article_id'].astype(str)

# Merge metadata (filtered to Europe & 2010-2020 was in query) with articles
merged = pd.merge(md, art, on='article_id', how='left')

# Define simple rule-based classifier
business_kw = [
    'business','market','markets','stock','stocks','earnings','economy','economic','oil','oil prices',
    'investment','investor','investors','financial','finance','bank','banks','shares','revenue','company',
    'companies','carlyle','wall st','wall street','short-sellers','short sellers','commercial','aerospace','private investment'
]

sports_kw = [
    'match','goal','score','season','coach','team','teams','olympic','olympics','fifa','nba','nfl','mlb','soccer','football',
    'baseball','basketball','tennis','cricket','victory','defeat','win','losing'
]

sci_kw = [
    'technology','tech','scientist','scientists','research','nasa','space','robot','ai','artificial intelligence',
    'study','scientific','software','hardware','internet','gadget'
]

# Helper to classify

def contains_any(text, keywords):
    if not isinstance(text, str):
        return False
    t = text.lower()
    for kw in keywords:
        if kw in t:
            return True
    return False

import math

def safe_text(val):
    if val is None:
        return ''
    if isinstance(val, float) and math.isnan(val):
        return ''
    return str(val)

def classify_row(row):
    title = safe_text(row.get('title', ''))
    desc = safe_text(row.get('description', ''))
    combined = title + ' ' + desc
    if contains_any(combined, business_kw):
        return 'Business'
    if contains_any(combined, sports_kw):
        return 'Sports'
    if contains_any(combined, sci_kw):
        return 'Science/Technology'
    return 'World'

merged['category'] = merged.apply(classify_row, axis=1)

# Extract year
merged['year'] = merged['publication_date'].str.slice(0,4).astype(int)

# Filter years 2010..2020
years = list(range(2010, 2021))
counts = {}
for y in years:
    counts[y] = int(((merged['year'] == y) & (merged['category'] == 'Business')).sum())

total_business = sum(counts.values())
avg = total_business / len(years) if len(years) > 0 else 0.0

result = {
    'average_business_articles_per_year': round(avg, 2),
    'total_business_articles': int(total_business),
    'years_considered': years,
    'yearly_business_counts': [{'year': y, 'business_count': counts[y]} for y in years]
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_3cvDIxlgOKjcJmaTOZlfO9gC': 'file_storage/call_3cvDIxlgOKjcJmaTOZlfO9gC.json', 'var_call_eKFULgr7qXp2kDuSIm9E1LIO': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
