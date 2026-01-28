code = """import json
import re

# Read the data
articles_path = locals()['var_functions.query_db:4']
metadata_path = locals()['var_functions.query_db:10']

with open(articles_path, 'r') as f:
    articles = json.load(f)

with open(metadata_path, 'r') as f:
    metadata = json.load(f)

# Create a dictionary of articles by article_id for fast lookup
articles_dict = {str(a['article_id']): a for a in articles}

# Filter metadata for 2015
metadata_2015 = [m for m in metadata if m['publication_date'] and m['publication_date'].startswith('2015')]

# Build final dataset for 2015 articles
articles_2015 = []
for meta in metadata_2015:
    article_id = str(meta['article_id'])
    if article_id in articles_dict:
        article = articles_dict[article_id]
        articles_2015.append({
            'article_id': article_id,
            'title': article.get('title', ''),
            'description': article.get('description', ''),
            'region': meta['region'],
            'publication_date': meta['publication_date']
        })

# Categorization function
def categorize(title, description):
    text = (title + ' ' + description).lower()
    
    # Define category keywords
    sports_keywords = ['football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'olympic', 'athlete', 'sport', 'game']
    business_keywords = ['stock', 'market', 'economy', 'business', 'company', 'wall st', 'reuters', 'financial', 'trade', 'dollar', 'euro']
    sci_tech_keywords = ['technology', 'tech', 'science', 'google', 'computer', 'software', 'hardware', 'internet', 'web', 'nuclear']
    
    score_sports = sum(1 for k in sports_keywords if k in text)
    score_business = sum(1 for k in business_keywords if k in text)
    score_sci_tech = sum(1 for k in sci_tech_keywords if k in text)
    
    max_score = max(score_sports, score_business, score_sci_tech)
    
    if max_score == 0:
        # If no keywords found, it's likely World news (politics, international affairs)
        return 'World'
    elif score_sports == max_score:
        return 'Sports'
    elif score_business == max_score:
        return 'Business'
    elif score_sci_tech == max_score:
        return 'Science/Technology'
    else:
        return 'World'

# Categorize all 2015 articles
for article in articles_2015:
    article['category'] = categorize(article['title'], article['description'])

# Filter for World category
world_articles = [a for a in articles_2015 if a['category'] == 'World']

# Count by region
region_counts = {}
for article in world_articles:
    region = article['region']
    region_counts[region] = region_counts.get(region, 0) + 1

# Sort regions by count
top_region = max(region_counts.items(), key=lambda x: x[1]) if region_counts else None

result = {
    'total_2015_articles': len(articles_2015),
    'total_world_articles': len(world_articles),
    'region_counts': region_counts,
    'top_region': top_region
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.list_db:1': ['authors', 'article_metadata'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'author_id': '992', 'region': 'North America', 'publication_date': '2004-03-20'}, {'article_id': '2', 'author_id': '820', 'region': 'South America', 'publication_date': '2021-02-04'}, {'article_id': '3', 'author_id': '478', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '4', 'author_id': '39', 'region': 'Africa', 'publication_date': '2012-02-01'}, {'article_id': '5', 'author_id': '802', 'region': 'Africa', 'publication_date': '2011-02-21'}, {'article_id': '6', 'author_id': '156', 'region': 'North America', 'publication_date': '2017-09-20'}, {'article_id': '7', 'author_id': '570', 'region': 'Europe', 'publication_date': '2022-12-23'}, {'article_id': '8', 'author_id': '272', 'region': 'Africa', 'publication_date': '2011-03-30'}, {'article_id': '9', 'author_id': '399', 'region': 'Europe', 'publication_date': '2016-05-24'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:18': {'total_articles': 100, 'total_metadata': 127600, 'sample_article': {'_id': '6969dd0a62aecdd4f6f2e54d', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, 'sample_metadata': {'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}}}

exec(code, env_args)
