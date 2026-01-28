code = """import json
import re

# Load metadata_database results from file
metadata_path = var_functions.query_db:2
with open(metadata_path, 'r') as f:
    metadata_list = json.load(f)

# Load articles_database results from file  
articles_path = var_functions.query_db:14
with open(articles_path, 'r') as f:
    articles_list = json.load(f)

# Create mapping of article ID to article data
articles_by_id = {}
for article in articles_list:
    try:
        article_id = int(article.get('article_id'))
        articles_by_id[article_id] = {
            'title': article.get('title', ''),
            'description': article.get('description', '')
        }
    except:
        continue

# Process Europe articles and extract business articles
business_keywords = ['business', 'economy', 'stock', 'stocks', 'wall st', 'wall street', 'finance', 'financial', 'corporate', 'bank', 'investment', 'trade', 'dollar', 'euro', 'oil price', 'market', 'economy', 'shares', 'profit', 'loss', 'gdp', 'inflation', 'retail', 'commercial', 'fund', 'funds', 'trade', 'export', 'import', 'rate', 'rates', 'banking']

business_articles = []
for record in metadata_list:
    try:
        article_id = int(record['article_id'])
        publication_date = record['publication_date']
        year = int(publication_date.split('-')[0])
        
        # Check if year is in range
        if 2010 <= year <= 2020:
            article = articles_by_id.get(article_id)
            if article:
                # Combine title and description for keyword matching
                text = (article['title'] + ' ' + article['description']).lower()
                
                # Check for business keywords
                is_business = any(keyword in text for keyword in business_keywords)
                
                if is_business:
                    business_articles.append({'article_id': article_id, 'year': year})
    except:
        continue

# Count business articles per year
year_counts = {}
for item in business_articles:
    year = item['year']
    year_counts[year] = year_counts.get(year, 0) + 1

# Calculate average for 2010-2020
total_business = sum(year_counts.values())
num_years = len(range(2010, 2021))  # 2010-2020 inclusive
average_per_year = total_business / num_years

print('__RESULT__:')
print(json.dumps({
    'total_business_articles': total_business,
    'years_considered': num_years,
    'average_per_year': round(average_per_year, 2),
    'per_year_breakdown': year_counts
}))"""

env_args = {'var_functions.list_db:0': ['authors', 'article_metadata'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': [{'_id': '6969abd2d85d3c92a2e13bcc', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969abd2d85d3c92a2e13bcd', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969abd2d85d3c92a2e13bce', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969abd2d85d3c92a2e13bcf', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969abd2d85d3c92a2e13bd0', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': [{'_id': '6969abd2d85d3c92a2e13bcc', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969abd2d85d3c92a2e13bcd', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969abd2d85d3c92a2e13bce', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969abd2d85d3c92a2e13bcf', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969abd2d85d3c92a2e13bd0', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
