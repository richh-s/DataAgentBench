code = """import json
import pandas as pd

# Access stored results
art_key = 'var_functions.query_db:0'
meta_key = 'var_functions.query_db:2'

articles_data = locals()[art_key]
metadata_data = locals()[meta_key]

# Load data if it's a filepath string
if type(articles_data) is str and '.json' in articles_data:
    articles_list = json.loads(open(articles_data).read())
else:
    articles_list = articles_data

if type(metadata_data) is str and '.json' in metadata_data:
    metadata_list = json.loads(open(metadata_data).read())
else:
    metadata_list = metadata_data

# Create DataFrames
df_art = pd.DataFrame(articles_list)
df_meta = pd.DataFrame(metadata_list)

# Convert article_id to string for matching
df_art['article_id'] = df_art['article_id'].astype(str)
df_meta['article_id'] = df_meta['article_id'].astype(str)

# Merge dataframes
df = pd.merge(df_art, df_meta, on='article_id', how='inner')

# Define business keywords
biz_words = ['business', 'economy', 'stock', 'stocks', 'wall st', 'wall street', 
             'company', 'companies', 'corporate', 'investment', 'investing',
             'market', 'markets', 'trade', 'trading', 'finance', 'financial',
             'profit', 'revenue', 'sales', 'oil', 'energy', 'bank', 'banking', 
             'job', 'jobs', 'dollar', 'euro']

# Check if article is business-related
def check_biz(title, desc):
    text = (str(title) + ' ' + str(desc)).lower()
    return any(word in text for word in biz_words)

# Apply classification
df['biz'] = df.apply(lambda x: check_biz(x['title'], x['description']), axis=1)

# Filter business articles from Europe (2010-2020)
df_biz = df[df['biz'] == True].copy()

# Extract year from publication date
df_biz['year'] = pd.to_datetime(df_biz['publication_date']).dt.year

# Filter years 2010-2020
df_biz = df_biz[(df_biz['year'] >= 2010) & (df_biz['year'] <= 2020)]

# Count articles per year
year_counts = df_biz.groupby('year').size().reset_index(name='count')

# Calculate average
if len(year_counts) > 0:
    avg = float(year_counts['count'].mean())
    total = int(year_counts['count'].sum())
    years = int(len(year_counts))
else:
    avg = 0.0
    total = 0
    years = 0

result = {
    'average_business_articles_per_year': round(avg, 2),
    'total_business_articles': total,
    'years_covered': years
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
