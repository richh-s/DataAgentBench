code = """import json
import pandas as pd

# Load the results from previous tool calls. The storage keys are available as variables.
# var_call_FxwnmaAPB0Cy4pehLZjYI0Bo and var_call_qieaBz8Px2MrtIl7BUivBiCv

def load_var(v):
    if isinstance(v, str):
        # It's a file path to a JSON file
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return v

metadata = load_var(var_call_FxwnmaAPB0Cy4pehLZjYI0Bo)
articles = load_var(var_call_qieaBz8Px2MrtIl7BUivBiCv)

# Create DataFrames
md = pd.DataFrame(metadata)
art = pd.DataFrame(articles)

# Ensure article_id type consistency as strings
md['article_id'] = md['article_id'].astype(str)
art['article_id'] = art['article_id'].astype(str)

# Merge metadata (which is already filtered to Europe and 2010-2020) with articles on article_id
df = pd.merge(md, art, on='article_id', how='left')

# Prepare simple keyword-based classifier for Business category
business_keywords = [
    'business','economy','economic','markets','market','stock','stocks','shares','bank','banks',
    'invest','investment','investors','ipo','ipo','trade','trading','currency','financial','finance',
    'profit','profits','earnings','acquisition','merger','mergers','company','companies','inflation',
    'interest rate','interest rates','fed','securities','bond','bonds','unemployment','recession',
    'oil prices','oil price','oil','petrol','energy','carlyle','wall st','wall street','eurozone','euro'
]

# Lowercase combined text
def is_business(row):
    title = (row.get('title') or '')
    desc = (row.get('description') or '')
    text = f"{title} {desc}".lower()
    for kw in business_keywords:
        if kw in text:
            return True
    return False

# Apply classifier
df['is_business'] = df.apply(is_business, axis=1)

# Extract year from publication_date
df['year'] = pd.to_datetime(df['publication_date'], errors='coerce').dt.year

# Filter years 2010-2020 inclusive
df = df[df['year'].between(2010, 2020)]

# Count business articles per year
counts = df[df['is_business']].groupby('year').size().to_dict()

# Ensure all years present
counts_by_year = {year: int(counts.get(year, 0)) for year in range(2010, 2021)}

total_business = sum(counts_by_year.values())
num_years = 2020 - 2010 + 1
average_per_year = total_business / num_years if num_years > 0 else 0.0

# Prepare result
result = {
    'average_business_articles_per_year': round(average_per_year, 2),
    'total_business_articles_2010_2020': int(total_business),
    'counts_by_year': counts_by_year
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_FxwnmaAPB0Cy4pehLZjYI0Bo': 'file_storage/call_FxwnmaAPB0Cy4pehLZjYI0Bo.json', 'var_call_qieaBz8Px2MrtIl7BUivBiCv': 'file_storage/call_qieaBz8Px2MrtIl7BUivBiCv.json'}

exec(code, env_args)
