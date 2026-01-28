code = """import json
import pandas as pd

# Load data from storage keys
# Europe articles from var_functions.query_db:8 (file path)
europe_file_path = var_functions.query_db:8
with open(europe_file_path, 'r') as f:
    europe_articles = json.load(f)

# All articles from var_functions.query_db:7
all_articles = var_functions.query_db:7

# Convert to DataFrames
df_europe = pd.DataFrame(europe_articles)
df_articles = pd.DataFrame(all_articles)

# Extract year from publication_date
df_europe['year'] = pd.to_datetime(df_europe['publication_date']).dt.year

# Business keywords for categorization
business_keywords = [
    'business', 'economy', 'economic', 'market', 'stock', 'financial', 'finance', 'company', 'corporate', 'trade', 
    'investment', 'investing', 'revenue', 'profit', 'earnings', 'wall st', 'wall street', 'bank', 'banking',
    'commercial', 'industry', 'industrial', 'retail', 'sales', 'quarterly', 'acquisition', 'merger'
]

# Check for business keywords in title or description
def is_business_article(title, description):
    if pd.isna(title):
        title = ''
    if pd.isna(description):
        description = ''
    
    text = f"{title} {description}".lower()
    return any(keyword in text for keyword in business_keywords)

# Merge article data with Europe metadata
df_combined = df_europe.merge(df_articles, on='article_id', how='left')

# Apply the function to categorize
df_combined['is_business'] = df_combined.apply(
    lambda row: is_business_article(row.get('title', ''), row.get('description', '')), axis=1
)

# Filter for business articles only
df_business = df_combined[df_combined['is_business'] == True]

# Count business articles per year
business_counts = df_business.groupby('year').size()

# Ensure we have all years from 2010 to 2020
all_years = pd.Series(range(2010, 2021))
business_counts = business_counts.reindex(all_years, fill_value=0)

# Calculate average
average_per_year = business_counts.mean()

# Prepare result
result = {
    'business_counts_per_year': business_counts.to_dict(),
    'total_business_articles': int(business_counts.sum()),
    'average_per_year': round(float(average_per_year), 2),
    'years_covered': len(business_counts)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.list_db:2': ['authors', 'article_metadata'], 'var_functions.query_db:5': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'author_id': '992', 'region': 'North America', 'publication_date': '2004-03-20'}, {'article_id': '2', 'author_id': '820', 'region': 'South America', 'publication_date': '2021-02-04'}, {'article_id': '3', 'author_id': '478', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '4', 'author_id': '39', 'region': 'Africa', 'publication_date': '2012-02-01'}, {'article_id': '5', 'author_id': '802', 'region': 'Africa', 'publication_date': '2011-02-21'}, {'article_id': '6', 'author_id': '156', 'region': 'North America', 'publication_date': '2017-09-20'}, {'article_id': '7', 'author_id': '570', 'region': 'Europe', 'publication_date': '2022-12-23'}, {'article_id': '8', 'author_id': '272', 'region': 'Africa', 'publication_date': '2011-03-30'}, {'article_id': '9', 'author_id': '399', 'region': 'Europe', 'publication_date': '2016-05-24'}], 'var_functions.query_db:7': [{'_id': '6969beac5487ab0a07c7ac76', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969beac5487ab0a07c7ac77', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969beac5487ab0a07c7ac78', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969beac5487ab0a07c7ac79', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969beac5487ab0a07c7ac7a', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
