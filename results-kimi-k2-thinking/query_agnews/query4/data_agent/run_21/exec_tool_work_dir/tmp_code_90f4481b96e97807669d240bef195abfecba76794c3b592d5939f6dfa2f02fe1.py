code = """import json

# Load the data
articles_file_path = locals()['var_functions.query_db:20']
with open(articles_file_path, 'r') as f:
    all_articles = json.load(f)

metadata_file_path = locals()['var_functions.query_db:4']
with open(metadata_file_path, 'r') as f:
    metadata_2015 = json.load(f)

# Create lookup for 2015 articles by ID
articles_2015_dict = {}
for meta in metadata_2015:
    article_id = meta['article_id']
    articles_2015_dict[article_id] = {
        'region': meta['region'],
        'publication_date': meta['publication_date']
    }

# Filter articles to only those from 2015
filtered_articles = []
for article in all_articles:
    article_id = article['article_id']
    if article_id in articles_2015_dict:
        filtered_articles.append({
            'article_id': article_id,
            'region': articles_2015_dict[article_id]['region'],
            'title': article['title'].lower(),
            'description': article['description'].lower()
        })

# Categorization function
def categorize_article(title, description):
    text = title + ' ' + description
    
    # Sports keywords
    sports_keywords = ['sports', 'game', 'olympic', 'championship', 'tournament', 'match', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'world cup', 'athlete', 'coach']
    
    # Business keywords
    business_keywords = ['stock', 'wall st', 'wall street', 'economy', 'economic', 'business', 'company', 'corporation', 'profit', 'revenue', 'trade', 'market', 'finance', 'financial', 'dollar', 'oil price', 'ipo', 'investment', 'bank', 'billion', 'million']
    
    # Science/Tech keywords
    sci_tech_keywords = ['science', 'technology', 'scientist', 'research', 'researcher', 'google', 'internet', 'software', 'computer', 'ibm', 'hp', 'data', 'digital', 'tech', 'innovation', 'study', 'medical', 'health', 'disease', 'gene', 'space', 'nasa']
    
    # World keywords - broader international/national news
    world_keywords = ['iraq', 'afghanistan', 'war', 'peace', 'nations', 'united nations', 'un', 'diplomat', 'diplomacy', 'treaty', 'government', 'minister', 'president', 'prime minister', 'senate', 'congress', 'white house', 'parliament', 'election', 'vote', 'country', 'nation', 'international', 'global', 'world', 'africa', 'asia', 'europe', 'america', 'mideast', 'middle east', 'refugee', 'aid', 'foreign', 'military', 'army', 'navy', 'air force']
    
    if any(keyword in text for keyword in sports_keywords):
        return 'Sports'
    elif any(keyword in text for keyword in business_keywords):
        return 'Business'
    elif any(keyword in text for keyword in sci_tech_keywords):
        return 'Science/Technology'
    elif any(keyword in text for keyword in world_keywords):
        return 'World'
    else:
        # Default categorization based on broad patterns
        if 'reuters' in text or 'afp' in text or 'ap' in text:
            if any(word in text for word in ['price', 'stock', 'market', 'economy', 'trade', 'business']):
                return 'Business'
            elif any(word in text for word in ['country', 'government', 'minister', 'war', 'peace', 'nation', 'international']):
                return 'World'
        return 'World'  # Default to World for news articles

# Categorize all 2015 articles
categorized_articles = []
for article in filtered_articles:
    category = categorize_article(article['title'], article['description'])
    categorized_articles.append({
        'article_id': article['article_id'],
        'region': article['region'],
        'category': category
    })

# Count World articles by region
world_articles_by_region = {}
for article in categorized_articles:
    if article['category'] == 'World':
        region = article['region']
        world_articles_by_region[region] = world_articles_by_region.get(region, 0) + 1

# Find the region with most World articles
max_region = max(world_articles_by_region, key=world_articles_by_region.get) if world_articles_by_region else None
max_count = world_articles_by_region.get(max_region, 0) if max_region else 0

print('__RESULT__:')
print(json.dumps({
    'total_2015_articles_processed': len(filtered_articles),
    'world_articles_by_region': world_articles_by_region,
    'max_region': max_region,
    'max_count': max_count,
    'sample_articles': categorized_articles[:10]
}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.list_db:1': ['authors', 'article_metadata'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': [{'_id': '6969e10e4c4e890ccbefaf21', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969e10e4c4e890ccbefaf22', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969e10e4c4e890ccbefaf23', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969e10e4c4e890ccbefaf24', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969e10e4c4e890ccbefaf25', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:12': {'metadata_type': "<class 'str'>", 'articles_type': "<class 'list'>", 'metadata_preview': 'file_storage/functions.query_db:4.json', 'articles_preview': 'not string'}, 'var_functions.execute_python:14': {'total_2015_articles': 0, 'sample_articles': []}, 'var_functions.execute_python:16': {'metadata_id_sample': ['13', '18', '26', '51', '52', '67', '70', '74', '86', '97'], 'articles_id_sample': ['0', '1', '2', '3', '4'], 'total_metadata': 6696, 'total_articles': 5, 'intersection_size': 0}, 'var_functions.query_db:18': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'total_articles_in_collection': 10000, 'total_2015_metadata': 6696, 'sample_articles': [{'id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)'}, {'id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)'}, {'id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)"}], 'sample_metadata': [{'article_id': '13', 'region': 'Europe', 'publication_date': '2015-10-17'}, {'article_id': '18', 'region': 'South America', 'publication_date': '2015-08-15'}, {'article_id': '26', 'region': 'Africa', 'publication_date': '2015-08-03'}]}}

exec(code, env_args)
