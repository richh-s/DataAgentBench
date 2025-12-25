code = """import json
import pandas as pd
import re

# Load metadata IDs and publication dates
with open(locals()['var_function-call-9790443739614513755'], 'r') as f:
    metadata_list = json.load(f)

# Create a mapping from article_id to year
# article_id in metadata seems to be string in the JSON preview "3", but I converted them to int previously.
# The query result had strings.
# I need to handle potential string/int mismatch.
article_year_map = {}
for item in metadata_list:
    aid = int(item['article_id'])
    date = item['publication_date'] # "YYYY-MM-DD"
    year = int(date.split('-')[0])
    article_year_map[aid] = year

# Load articles
with open(locals()['var_function-call-13176827165821674892'], 'r') as f:
    articles_list = json.load(f)

# Keywords for Business category
business_keywords = [
    "market", "stock", "trade", "economy", "economic", "business", "financial", 
    "investor", "investment", "bank", "profit", "loss", "dollar", "euro", "currency", 
    "oil", "price", "rate", "inflation", "fed", "treasury", "corporate", "company", 
    "merger", "acquisition", "deal", "sale", "revenue", "ipo", "nasdaq", "dow", 
    "wall street", "ceo", "cfo", "bankrupt", "debt", "loan", "credit", "fund", 
    "commodity", "crude", "opec", "wto", "imf", "gdp", "recession", 
    "employment", "jobless", "jobs", "retail", "consumer", "spending", "budget", 
    "tax", "deficit", "shares", "dividend", "earnings", "quarterly", "bond"
]

business_regex = re.compile(r'\b(' + '|'.join(business_keywords) + r')\b', re.IGNORECASE)

business_counts = {year: 0 for year in range(2010, 2021)}

count_business = 0
count_total_filtered = 0

for article in articles_list:
    # article_id in articles_list is integer or string? 
    # Preview: "article_id": "0". So it is string.
    try:
        aid = int(article.get('article_id'))
    except:
        continue
        
    if aid in article_year_map:
        count_total_filtered += 1
        # Check classification
        text = (article.get('title', '') + " " + article.get('description', '')).lower()
        
        # Simple classification: if matches business keywords
        if business_regex.search(text):
            year = article_year_map[aid]
            if 2010 <= year <= 2020:
                business_counts[year] += 1
                count_business += 1

# Calculate average
total_business_articles = sum(business_counts.values())
num_years = 11
average = total_business_articles / num_years

print("__RESULT__:")
print(json.dumps({
    "business_counts_per_year": business_counts,
    "total_business": total_business_articles,
    "average": average,
    "filtered_articles": count_total_filtered
}))"""

env_args = {'var_function-call-9790443739614513755': 'file_storage/function-call-9790443739614513755.json', 'var_function-call-3385916558167782532': 'file_storage/function-call-3385916558167782532.json', 'var_function-call-16581665091431742479': 14860, 'var_function-call-13176827165821674892': 'file_storage/function-call-13176827165821674892.json'}

exec(code, env_args)
