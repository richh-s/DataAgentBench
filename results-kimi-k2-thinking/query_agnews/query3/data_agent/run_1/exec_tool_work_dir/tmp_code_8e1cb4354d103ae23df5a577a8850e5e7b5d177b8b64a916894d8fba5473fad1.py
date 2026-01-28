code = """import json
import os
import re
from datetime import datetime

# Load Europe metadata (2010-2020)
metadata_key = 'var_functions.query_db:8'
metadata_result = locals().get(metadata_key)

if isinstance(metadata_result, str) and metadata_result.endswith('.json'):
    with open(metadata_result, 'r') as f:
        europe_metadata = json.load(f)
else:
    europe_metadata = metadata_result

# Load all articles
articles_key = 'var_functions.query_db:16'
articles_result = locals().get(articles_key)

if isinstance(articles_result, str) and articles_result.endswith('.json'):
    with open(articles_result, 'r') as f:
        articles_data = json.load(f)
else:
    articles_data = articles_result

# Create a dictionary for fast lookup of articles by ID
articles_dict = {str(article['article_id']): article for article in articles_data}

# More comprehensive business keywords
business_terms = [
    'wall st', 'wall street', 'stock market', 'stock markets', 'stock', 'stocks',
    'economy', 'economic', 'economics', 'economist', 'economists',
    'oil price', 'oil prices', 'crude oil', 'brent crude', 'wti', 'energy',
    'interest rate', 'interest rates', 'rate hike', 'rate cut', 'central bank',
    'market', 'markets', 'trading', 'trader', 'traders', 'investor', 'investors',
    'trade', 'trade deficit', 'trade surplus', 'export', 'exports', 'import', 'imports',
    'exchange rate', 'exchange rates', 'currency', 'currencies', 'dollar', 'euro', 'yen',
    'investment', 'investments', 'investing', 'private equity', 'venture capital',
    'funds', 'mutual funds', 'hedge funds', 'bonds', 'treasury', 'yield', 'yields',
    'commodity', 'commodities', 'metal', 'metals', 'gold', 'silver', 'copper',
    'real estate', 'property', 'housing', 'mortgage', 'mortgages',
    'bank', 'banks', 'banking', 'banker', 'bankers', 'financial institution',
    'profit', 'profits', 'loss', 'losses', 'earnings', 'revenue', 'sales',
    'capital', 'assets', 'liability', 'liabilities', 'equity', 'equities',
    'finance', 'financial', 'financing', 'fiscal', 'monetary',
    'share', 'shares', 'equity', 'stockholder', 'shareholder', 'dividend',
    'gold', 'silver', 'precious metal', 'precious metals',
    'loan', 'loans', 'credit', 'debt', 'borrowing', 'lending',
    'ipo', 'initial public offering', 'public offering', 'floatation',
    'merger', 'acquisition', 'takeover', 'buyout', 'corporate',
    'company', 'companies', 'corporation', 'corporations', 'firm', 'firms',
    'startup', 'startups', 'technology company', 'tech company',
    'retail', 'retailer', 'retailers', 'consumer', 'consumers', 'spending',
    'inflation', 'deflation', 'gdp', 'gross domestic product',
    'recession', 'recovery', 'growth', 'slowdown', 'contraction',
    'unemployment', 'employment', 'jobs', 'job market', 'labor market',
    'manufacturing', 'production', 'output', 'industrial',
    'transportation', 'logistics', 'supply chain',
    'pharmaceutical', 'pharma', 'biotech', 'biotechnology',
    'insurance', 'insurer', 'insurance company',
    'pension', 'pensions', 'retirement', '401k', 'social security',
    'budget', 'budget deficit', 'national debt', 'public debt',
    'tax', 'taxes', 'taxation', 'tax cut', 'tax increase'
]

# Initialize counts for all years 2010-2020
year_counts = {str(year): 0 for year in range(2010, 2021)}

europe_business_articles = []

for meta_item in europe_metadata:
    article_id = str(meta_item['article_id'])
    if article_id in articles_dict:
        article = articles_dict[article_id]
        title = article.get('title', '').lower()
        description = article.get('description', '').lower()
        
        # Check if it's a business article
        is_business = False
        for term in business_terms:
            if term in title or term in description:
                is_business = True
                break
        
        if is_business:
            year = meta_item['publication_date'][:4]
            if year in year_counts:
                year_counts[year] += 1
                europe_business_articles.append({
                    'article_id': article_id,
                    'year': year,
                    'publication_date': meta_item['publication_date'],
                    'title': article.get('title', '')
                })

# Calculate average across ALL years 2010-2020 (11 years)
total_business_articles = len(europe_business_articles)
avg_per_year = total_business_articles / 11.0

# Get year-by-year breakdown
year_breakdown = [(year, count) for year, count in sorted(year_counts.items(), key=lambda x: x[0])]

print('__RESULT__:')
print(json.dumps({
    'avg_per_year': round(avg_per_year, 2),
    'total_business_articles': total_business_articles,
    'year_range': '2010-2020',
    'total_years': 11,
    'year_breakdown': year_breakdown
}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'_id': '6969a9e8d3fee090036ad705', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969a9e8d3fee090036ad706', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969a9e8d3fee090036ad707', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969a9e8d3fee090036ad708', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969a9e8d3fee090036ad709', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'count': '127600'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:14': {'total_europe_articles': 14860, 'sample_europe_ids': ['3', '9', '13', '14', '21'], 'total_articles_in_db': 5, 'sample_article_ids': ['0', '1', '2', '3', '4']}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': {'avg_per_year': 338.64, 'total_business_articles': 3725, 'total_europe_articles': 14860, 'sample_year_counts': {'2016': 337, '2017': 358, '2020': 342, '2013': 346, '2018': 355}}}

exec(code, env_args)
