code = """import json
import pandas as pd

# Load metadata results (file path provided in var_call_lez0YaJxV26I2k8UBd9ce3mt)
with open(var_call_lez0YaJxV26I2k8UBd9ce3mt, 'r') as f:
    meta = json.load(f)

with open(var_call_SujNAAOwNP0rUeptrllLbr9W, 'r') as f:
    articles = json.load(f)

meta_df = pd.DataFrame(meta)
articles_df = pd.DataFrame(articles)

# Normalize types
meta_df['article_id'] = meta_df['article_id'].astype(int)
meta_df['publication_date'] = pd.to_datetime(meta_df['publication_date'])
meta_df['year'] = meta_df['publication_date'].dt.year

articles_df['article_id'] = articles_df['article_id'].astype(int)
articles_df['title'] = articles_df['title'].fillna('')
articles_df['description'] = articles_df['description'].fillna('')

# Merge metadata with articles
df = meta_df.merge(articles_df, on='article_id', how='left')

# Define business keywords
business_keywords = [
    'market','markets','stock','stocks','economy','economic','business','company','companies',
    'firm','firms','shares','share','ipo','investment','investor','investors','bank','banks',
    'profit','profits','trade','trading','oil prices','oil','finance','financial','eurozone','reuters',
    'wall st','wall street','dollar','exchange','merger','acquisition','acquires','acquire','billion','million'
]

def is_business(row):
    text = (str(row.get('title','')) + ' ' + str(row.get('description',''))).lower()
    for kw in business_keywords:
        if kw in text:
            return True
    return False

# Apply classification
df['is_business'] = df.apply(is_business, axis=1)

# Consider years 2010 through 2020 inclusive
years = list(range(2010, 2021))
counts_by_year = {str(y): 0 for y in years}

for y in years:
    counts_by_year[str(y)] = int(df[(df['year'] == y) & (df['is_business'])].shape[0])

total_business = sum(counts_by_year.values())
average_per_year = total_business / len(years)

result = {
    'average_business_articles_per_year': round(average_per_year, 2),
    'total_business_articles_2010_2020': int(total_business),
    'counts_by_year': counts_by_year
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_lez0YaJxV26I2k8UBd9ce3mt': 'file_storage/call_lez0YaJxV26I2k8UBd9ce3mt.json', 'var_call_SujNAAOwNP0rUeptrllLbr9W': 'file_storage/call_SujNAAOwNP0rUeptrllLbr9W.json'}

exec(code, env_args)
