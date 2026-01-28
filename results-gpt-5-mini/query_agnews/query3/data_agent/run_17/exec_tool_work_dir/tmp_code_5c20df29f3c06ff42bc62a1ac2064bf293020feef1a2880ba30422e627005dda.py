code = """import json
import pandas as pd

# Load the previously stored query results from the provided storage file paths
with open(var_call_lvyb4Nw9euzQkfsxyr6OOOk5, 'r') as f:
    meta_records = json.load(f)
with open(var_call_5exALV3uvSzOb0mxghbhcotx, 'r') as f:
    article_records = json.load(f)

# Create DataFrames
df_meta = pd.DataFrame(meta_records)
df_articles = pd.DataFrame(article_records)

# Normalize article_id types to integers for joining
df_meta['article_id'] = df_meta['article_id'].astype(int)
df_meta['publication_date'] = pd.to_datetime(df_meta['publication_date'], errors='coerce')
df_articles['article_id'] = df_articles['article_id'].astype(int)

# Merge metadata (which is already filtered to Europe and 2010-2020) with articles to get titles/descriptions
df = pd.merge(df_meta, df_articles, on='article_id', how='left')

# Extract year
df['year'] = df['publication_date'].dt.year

# Define business-related keywords for heuristic classification
business_keywords = [
    'market','markets','stock','stocks','economy','economic','trade','trade deficit', 'ipo','ipo',
    'shares','company','companies','profit','profits','revenue','bank','banks','financial','finance',
    'invest','investment','investors','bonds','interest rate','interest rates','inflation','oil prices',
    'oil price','oil','currency','currencies','dollar','eurozone','euro','earnings','revenue','commercial',
    'firm','corporate','merger','acquir','buyout','dividend'
]

# Lowercase title and description for searching
df['title_lower'] = df['title'].fillna('').str.lower()
df['desc_lower'] = df['description'].fillna('').str.lower()

# Heuristic function to detect business articles
def detect_business(row):
    text = row['title_lower'] + ' ' + row['desc_lower']
    for kw in business_keywords:
        if kw in text:
            return True
    return False

# Apply classification
df['is_business'] = df.apply(detect_business, axis=1)

# Count business articles per year for 2010-2020 inclusive
counts = {}
for year in range(2010, 2021):
    counts[year] = int(df[(df['year'] == year) & (df['is_business'])].shape[0])

total_business = sum(counts.values())
average_per_year = total_business / 11.0

# Prepare result
result = {
    'average_business_articles_per_year': round(average_per_year, 2),
    'total_business_articles_2010_2020': int(total_business),
    'per_year_counts': {str(k): v for k, v in counts.items()}
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_lvyb4Nw9euzQkfsxyr6OOOk5': 'file_storage/call_lvyb4Nw9euzQkfsxyr6OOOk5.json', 'var_call_5exALV3uvSzOb0mxghbhcotx': 'file_storage/call_5exALV3uvSzOb0mxghbhcotx.json'}

exec(code, env_args)
