code = """import json
import os

# Access the Europe articles metadata file path
metadata_file = locals()['var_functions.query_db:2']

# Open and read the full Europe articles metadata
with open(metadata_file, 'r') as f:
    europe_articles = json.load(f)

# Access the articles data (should be the actual data, not a file path)
# But let's check what type it is first
articles_data = locals()['var_functions.query_db:4']

# If it's a file path, read it; if it's already data, use it directly
if isinstance(articles_data, str) and os.path.exists(articles_data):
    with open(articles_data, 'r') as f:
        all_articles = json.load(f)
else:
    all_articles = articles_data

print(f"Number of Europe articles: {len(europe_articles)}")
print(f"Number of all articles: {len(all_articles)}")
print("First few Europe articles:", europe_articles[:3])
print("First few all articles:", all_articles[:3])

# Extract Europe article IDs
europe_article_ids = set(str(art['article_id']) for art in europe_articles)

# Filter articles to only include those from Europe
europe_articles_content = [art for art in all_articles if str(art['article_id']) in europe_article_ids]

print(f"Number of Europe article content pieces: {len(europe_articles_content)}")
print("Sample Europe article:", europe_articles_content[0] if europe_articles_content else "None")

# Try to classify Business articles based on title/description keywords
business_keywords = ['business', 'economy', 'stock', 'market', 'finance', 'financial', 'company', 'companies', 'investment', 'investing', 'trade', 'trading', 'wall st', 'wall street', 'ceo', 'quarterly', 'earnings', 'revenue', 'profit', 'sales', 'deal', 'acquisition', 'merger', 'bank', 'banking']

business_articles = []
for art in europe_articles_content:
    title = art.get('title', '').lower()
    desc = art.get('description', '').lower()
    text = f"{title} {desc}"
    
    if any(keyword in text for keyword in business_keywords):
        business_articles.append(art)

print(f"Number of potential Business articles: {len(business_articles)}")
print("Sample Business article:", business_articles[0] if business_articles else "None")

# Count articles per year
from collections import Counter
year_counts = Counter()

for art in europe_articles:
    date = art.get('publication_date', '')
    if date:
        year = date.split('-')[0]
        year_counts[year] += 1

# Count Business articles per year
business_year_counts = Counter()
for art in business_articles:
    article_id = str(art['article_id'])
    # Find the metadata for this article
    for meta in europe_articles:
        if str(meta['article_id']) == article_id:
            date = meta.get('publication_date', '')
            if date:
                year = date.split('-')[0]
                business_year_counts[year] += 1
            break

print("All articles per year:", dict(year_counts))
print("Business articles per year:", dict(business_year_counts))

# Calculate average Business articles per year from 2010-2020
years = [str(y) for y in range(2010, 2021)]
business_counts = [business_year_counts.get(year, 0) for year in years]
total_business = sum(business_counts)
average_business = total_business / len(years)

print(f"Total Business articles 2010-2020: {total_business}")
print(f"Average Business articles per year: {average_business}")

# Also calculate what percentage this is of total Europe articles
total_europe_counts = [year_counts.get(year, 0) for year in years]
total_europe = sum(total_europe_counts)
print(f"Total Europe articles 2010-2020: {total_europe}")

# Prepare result
result = {
    'average_business_articles_per_year': round(average_business, 2),
    'total_business_articles_2010_2020': total_business,
    'business_articles_by_year': dict(business_year_counts),
    'total_europe_articles_2010_2020': total_europe
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['authors', 'article_metadata'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': [{'_id': '6969c158a2d45f9a2caeb2af', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969c158a2d45f9a2caeb2b0', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969c158a2d45f9a2caeb2b1', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969c158a2d45f9a2caeb2b2', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969c158a2d45f9a2caeb2b3', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
