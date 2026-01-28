code = """import json

# Read the data
with open('file_storage/functions.query_db:20.json', 'r') as f:
    articles = json.load(f)

with open('file_storage/functions.query_db:22.json', 'r') as f:
    metadata_2015 = json.load(f)

# Create article_id to region mapping for 2015
article_to_region = {m['article_id']: m['region'] for m in metadata_2015}

# Filter articles to only those from 2015
articles_2015 = [a for a in articles if a['article_id'] in article_to_region]

# Classification function
def classify_article(title, description):
    text = (title + ' ' + description).lower()
    
    # World category keywords - international conflicts, politics, diplomacy, global events
    world_keywords = [
        'iraq', 'iran', 'afghanistan', 'war', 'conflict', 'attack', 'bomb', 'terror',
        'militia', 'rebel', 'insurgent', 'diplomat', 'embassy', 'united nations',
        'peace', 'treaty', 'sanction', 'invasion', 'middle east', 'africa', 'asia',
        'europe', 'president', 'prime minister', 'government', 'election',
        'refugee', 'aid', 'humanitarian', 'crisis', 'death', 'kill', 'violence',
        'protest', 'demonstration', 'coup', 'military', 'civilian'
    ]
    
    # Sports category keywords
    sports_keywords = [
        'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf',
        'olympic', 'world cup', 'championship', 'tournament', 'match',
        'game', 'team', 'player', 'coach', 'score', 'win', 'lose',
        'league', 'season', 'sport'
    ]
    
    # Business category keywords
    business_keywords = [
        'stock', 'wall st', 'economy', 'oil', 'business', 'reuters', 'market',
        'finance', 'investment', 'company', 'corporate', 'profit', 'loss',
        'trade', 'deficit', 'budget', 'bank', 'rate', 'interest', 'price',
        'share', 'quarter', 'earnings', 'dollar', 'euro', 'currency'
    ]
    
    # Science/Tech category keywords
    tech_keywords = [
        'google', 'technology', 'internet', 'software', 'hardware', 'computer',
        'digital', 'tech', 'science', 'research', 'study', 'scientist',
        'discovery', 'innovation', 'patent', 'algorithm', 'data', 'ai'
    ]
    
    # Score each category
    world_score = sum(1 for kw in world_keywords if kw in text)
    sports_score = sum(1 for kw in sports_keywords if kw in text)
    business_score = sum(1 for kw in business_keywords if kw in text)
    tech_score = sum(1 for kw in tech_keywords if kw in text)
    
    # Determine category with highest score
    scores = {
        'World': world_score,
        'Sports': sports_score,
        'Business': business_score,
        'Science/Technology': tech_score
    }
    
    max_category = max(scores, key=scores.get)
    max_score = scores[max_category]
    
    # Only classify if we have at least one matching keyword
    if max_score > 0:
        return max_category
    else:
        return None

# Classify 2015 articles and count World articles by region
world_articles_by_region = {}
classified_articles = []

for article in articles_2015:
    article_id = article['article_id']
    title = article['title']
    description = article.get('description', '')
    
    category = classify_article(title, description)
    region = article_to_region[article_id]
    
    classified_articles.append({
        'article_id': article_id,
        'category': category,
        'region': region,
        'title': title[:50] + '...' if len(title) > 50 else title
    })
    
    if category == 'World':
        world_articles_by_region[region] = world_articles_by_region.get(region, 0) + 1

# Find region with most World articles
if world_articles_by_region:
    top_region = max(world_articles_by_region, key=world_articles_by_region.get)
    top_count = world_articles_by_region[top_region]
else:
    # If no World articles found, check some samples to debug
    world_samples = [a for a in classified_articles if a['category'] == 'World']
    top_region = "Unknown"
    top_count = 0

print('__RESULT__:')
print(json.dumps({
    'total_2015_articles': len(articles_2015),
    'world_articles_by_region': world_articles_by_region,
    'top_region': top_region,
    'top_region_count': top_count,
    'samples': classified_articles[:10]
}))"""

env_args = {'var_functions.query_db:0': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.execute_python:10': {'file_path': 'file_storage/functions.query_db:1.json'}, 'var_functions.execute_python:12': {'metadata_2015_count': 6696, 'sample_articles': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}], 'sample_metadata': [{'article_id': '13', 'region': 'Europe', 'publication_date': '2015-10-17'}, {'article_id': '18', 'region': 'South America', 'publication_date': '2015-08-15'}, {'article_id': '26', 'region': 'Africa', 'publication_date': '2015-08-03'}]}, 'var_functions.query_db:14': [{'_id': '6969f0f397433cb14fb14247', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969f0f397433cb14fb14248', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969f0f397433cb14fb14249', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969f0f397433cb14fb1424a', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969f0f397433cb14fb1424b', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:16': {'articles_type': "<class 'list'>", 'metadata_type': "<class 'str'>", 'articles_len': 5, 'metadata_len': 0}, 'var_functions.execute_python:18': {'articles_found': 0, 'metadata_found': 127600, 'articles_sample': None, 'metadata_sample': [{'article_id': '0', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'region': 'North America', 'publication_date': '2004-03-20'}]}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:24': {'total_articles': 20000, 'articles_2015_count': 6696}}

exec(code, env_args)
