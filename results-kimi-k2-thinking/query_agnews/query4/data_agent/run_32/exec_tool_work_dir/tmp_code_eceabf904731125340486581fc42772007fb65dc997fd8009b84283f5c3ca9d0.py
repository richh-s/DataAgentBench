code = """import json
import pandas as pd
import re

# Load metadata
metadata_file = locals()['var_functions.query_db:6']
with open(metadata_file, 'r') as f:
    metadata_2015 = json.load(f)

df_metadata = pd.DataFrame(metadata_2015)

# Create mapping of article_id to region
region_map = dict(zip(df_metadata['article_id'].astype(int), df_metadata['region']))

# Category classification keywords
world_keywords = ['war', 'peace', 'diplomat', 'treaty', 'united nations', 'un', 'security council', 'afghanistan', 'iraq', 'iran', 'israel', 'palestine', 'china', 'russia', 'ukraine', 'syria', 'global', 'international', 'foreign', 'embassy', 'ambassador', 'trade deficit', 'trade', 'military', 'defense', 'nuclear', 'weapon', 'terrorist', 'terrorism', 'world', 'global']
sports_keywords = ['football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'olympic', 'world cup', 'championship', 'game', 'team', 'player', 'coach', 'league', 'race', 'sports', 'nfl', 'nba', 'mlb', 'nhl', 'win', 'lose', 'score', 'pimlico']
business_keywords = ['stock', 'market', 'economy', 'corporate', 'company', 'ipo', 'investment', 'bank', 'financial', 'profit', 'loss', 'quarterly', 'shares', 'trading', 'business', '&', 'merger', 'acquisition', 'wall st', 'nasdaq', 'dow']
science_tech_keywords = ['nasa', 'space', 'spacecraft', 'satellite', 'genetics', 'dna', 'software', 'technology', 'computer', 'internet', 'web', 'tech', 'science', 'research', 'study', 'scientist', 'lab', 'laboratory', 'data', 'system', 'genesis']  

def classify_article(title, description):
    text = f"{title} {description}".lower()
    
    # Check World first (priority)
    for keyword in world_keywords:
        if keyword in text:
            return 'World'
    
    # Check other categories to avoid misclassification
    for keyword in sports_keywords:
        if keyword in text:
            return 'Sports'
    
    for keyword in business_keywords:
        if keyword in text:
            return 'Business'
    
    for keyword in science_tech_keywords:
        if keyword in text:
            return 'Science/Technology'
    
    return 'Other'

# Count World articles by region
world_counts = {}
processed = 0
errors = 0

# Process all articles in batches using the stored file
articles_file = locals()['var_functions.query_db:24']
with open(articles_file, 'r') as f:
    articles = json.load(f)

for article in articles:
    try:
        article_id = int(article['article_id'])
        if article_id in region_map:
            category = classify_article(article['title'], article['description'])
            if category == 'World':
                region = region_map[article_id]
                world_counts[region] = world_counts.get(region, 0) + 1
            processed += 1
    except Exception as e:
        errors += 1

# Also query more articles to process all 6696
all_article_ids = list(region_map.keys())
remaining_ids = [aid for aid in all_article_ids if aid not in [int(a['article_id']) for a in articles]]

print('__RESULT__:')
print(json.dumps({
    'processed_in_first_batch': processed,
    'world_articles_found': world_counts,
    'remaining_to_fetch': len(remaining_ids),
    'total_2015_articles': len(all_article_ids)
}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'_id': '6969e9310b470561e5db3037', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969e9310b470561e5db3038', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969e9310b470561e5db3039', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969e9310b470561e5db303a', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969e9310b470561e5db303b', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.list_db:4': ['authors', 'article_metadata'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'count': 6696, 'sample': ['13', '18', '26', '51', '52']}, 'var_functions.query_db:14': [], 'var_functions.execute_python:16': {'total_count': 6696, 'sample_ids': [13, 18, 26, 51, 52, 67, 70, 74, 86, 97], 'id_type': "<class 'int'>"}, 'var_functions.execute_python:22': {'query': '{"collection": "articles", "filter": {"article_id": {"$in": [13,18,26,51,52,67,70,74,86,97,116,117,141,165,179,203,240,243,266,271,309,314,364,365,369,379,408,429,488,498,501,509,519,534,606,652,698,743,745,879,885,902,907,924,932,935,941,970,987,993,1001,1045,1053,1061,1065,1077,1084,1108,1137,1171,1190,1242,1244,1277,1332,1363,1366,1386,1435,1470,1477,1494,1531,1548,1570,1589,1611,1631,1662,1678,1689,1720,1727,1736,1769,1791,1792,1848,1853,1866,1880,1905,1910,1969,1978,1996,2009,2010,2017,2023]}}, "limit": 100}'}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'total_articles_2015': 6696, 'regions': {'Europe': 1357, 'Africa': 1345, 'Asia': 1333, 'South America': 1332, 'North America': 1329}}, 'var_functions.execute_python:30': {'total_batches': 14, 'batch_size': 500, 'total_articles': 6696, 'first_batch_sample': [13, 18, 26, 51, 52]}, 'var_functions.execute_python:32': {'total_to_process': 6696, 'batches_created': 14, 'processed_count': 6696}}

exec(code, env_args)
