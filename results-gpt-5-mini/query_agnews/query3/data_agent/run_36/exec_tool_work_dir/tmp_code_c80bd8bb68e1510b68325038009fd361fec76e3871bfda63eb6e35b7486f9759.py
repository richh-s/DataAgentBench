code = """import json
import pandas as pd

# Load data from the storage-provided file paths
with open(var_call_dW6nX7gtm0IQgMnUftmgv4bc, 'r', encoding='utf-8') as f:
    meta = json.load(f)
with open(var_call_84kM5drG4d12CKhlvpEyOD8i, 'r', encoding='utf-8') as f:
    articles = json.load(f)

# Create DataFrames
df_meta = pd.DataFrame(meta)
df_articles = pd.DataFrame(articles)

# Ensure article_id types align
# Some article_id values may be strings; convert to int
df_meta['article_id'] = df_meta['article_id'].astype(int)
df_articles['article_id'] = df_articles['article_id'].astype(int)

# Merge metadata with article content
df = pd.merge(df_meta, df_articles[['article_id','title','description']], on='article_id', how='left')

# Extract year
df['year'] = pd.to_datetime(df['publication_date']).dt.year

# Define business-related keywords for simple rule-based classification
business_keywords = [
    'market','markets','stock','stocks','share','shares','ipo','initial public offering',
    'earnings','profit','profits','loss','losses','revenue','revenues','company','companies','firm','firms',
    'investment','investor','investors','bank','banks','economy','economic','trade deficit','trade','business',
    'financial','finance','billion','million','merger','acquisition','acquisitions','oil prices','oil prices',
    'interest rate','interest rates','rate cut','rate hike','inflation','fed','import','exports','export','imports'
]

# Lowercase text for matching
df['text'] = (df['title'].fillna('') + ' ' + df['description'].fillna('')).str.lower()

# Function to classify as business if any keyword present
import re
pattern = re.compile(r"\b(" + r"|".join(re.escape(k) for k in business_keywords) + r")\b")

def is_business(text):
    return bool(pattern.search(text))

# Apply classification
df['is_business'] = df['text'].apply(is_business)

# Count business articles per year for 2010-2020 inclusive
years = list(range(2010, 2021))
counts = {}
for y in years:
    counts[y] = int(df[(df['year'] == y) & (df['is_business'])].shape[0])

total_business = sum(counts.values())
average_per_year = total_business / len(years)

# Prepare JSON-serializable result
result = {
    'average_business_articles_per_year': round(average_per_year, 2),
    'total_business_articles': int(total_business),
    'years_considered': years,
    'counts_by_year': counts
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_dW6nX7gtm0IQgMnUftmgv4bc': 'file_storage/call_dW6nX7gtm0IQgMnUftmgv4bc.json', 'var_call_84kM5drG4d12CKhlvpEyOD8i': 'file_storage/call_84kM5drG4d12CKhlvpEyOD8i.json'}

exec(code, env_args)
