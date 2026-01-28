code = """import json
import pandas as pd

# Load data from storage-provided file paths
with open(var_call_ScEfTawah2wbv8HWrpOCrHct, 'r') as f:
    europe_meta = json.load(f)
with open(var_call_Zd2lpQveN8epMTR3Md6KSBfA, 'r') as f:
    articles = json.load(f)

# Create DataFrames
df_meta = pd.DataFrame(europe_meta)
df_articles = pd.DataFrame(articles)

# Ensure article_id types align
df_meta['article_id'] = df_meta['article_id'].astype(str)
df_articles['article_id'] = df_articles['article_id'].astype(str)

# Merge metadata for Europe with articles content
df = pd.merge(df_meta, df_articles, on='article_id', how='left')

# Extract year from publication_date
df['year'] = pd.to_datetime(df['publication_date'], errors='coerce').dt.year

# Define a simple keyword-based classifier for Business
business_keywords = [
    'business','economy','economic','market','markets','stock','stocks','share','shares',
    'bank','banks','financial','finance','company','companies','profit','profits','merger',
    'acquisition','ipo','inflation','unemployment','interest rate','rates','revenue',
    'earnings','investment','investor','investors','trade','oil','oil prices','currency',
    'currencies','exchange','retail','sales','businesses'
]

def is_business(row):
    text = ''
    if pd.notna(row.get('title')):
        text += str(row['title']) + ' '
    if pd.notna(row.get('description')):
        text += str(row['description'])
    text = text.lower()
    for kw in business_keywords:
        if kw in text:
            return True
    return False

# Apply classifier
df['is_business'] = df.apply(is_business, axis=1)

# Count business articles per year for 2010-2020 inclusive
years = list(range(2010, 2021))
counts_by_year = {}
for y in years:
    counts_by_year[str(y)] = int(df[(df['year'] == y) & (df['is_business'])].shape[0])

total_business = sum(counts_by_year.values())
num_years = len(years)
average_per_year = total_business / num_years if num_years > 0 else 0.0

result = {
    'counts_by_year': counts_by_year,
    'total_business_articles': int(total_business),
    'num_years': num_years,
    'average_per_year': round(average_per_year, 2)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ScEfTawah2wbv8HWrpOCrHct': 'file_storage/call_ScEfTawah2wbv8HWrpOCrHct.json', 'var_call_Zd2lpQveN8epMTR3Md6KSBfA': 'file_storage/call_Zd2lpQveN8epMTR3Md6KSBfA.json'}

exec(code, env_args)
