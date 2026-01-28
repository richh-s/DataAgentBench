code = """import json
import pandas as pd

# Load 2015 metadata
meta_2015_file = locals()['var_functions.query_db:12']
if isinstance(meta_2015_file, str) and meta_2015_file.endswith('.json'):
    with open(meta_2015_file, 'r') as f:
        metadata_2015 = json.load(f)
else:
    metadata_2015 = locals()['var_functions.query_db:12']

# Load all articles
articles_data = locals()['var_functions.query_db:2']

# Convert to DataFrames
df_meta = pd.DataFrame(metadata_2015)
df_articles = pd.DataFrame(articles_data)

# Ensure article_id is int for matching
df_meta['article_id'] = pd.to_numeric(df_meta['article_id'])
df_articles['article_id'] = pd.to_numeric(df_articles['article_id'])

# Merge to get articles from 2015
df_merged = df_articles.merge(df_meta, on='article_id', how='inner')

print(f"Total articles from 2015: {len(df_merged)}")

# Define category detection based on title and description
def categorize_article(title, description):
    title_desc = f"{title} {description}".lower()
    
    # World category keywords
    world_keywords = ['world', 'global', 'international', 'united nations', 'war', 'peace', 'diplomatic', 'treaty', 'conflict', 'foreign', 'abroad', 'overseas', 'embassy', 'ambassador', 'minister', 'president', 'prime minister', 'chancellor', 'king', 'queen', 'iran', 'iraq', 'afghanistan', 'syria', 'russia', 'china', 'japan', 'korea', 'europe', 'africa', 'asia', 'south america', 'australia', 'israel', 'palestine', 'lebanon', 'turkey', 'pakistan', 'india']
    
    # Sports category keywords
    sports_keywords = ['sports', 'game', 'olympic', 'olympics', 'world cup', 'championship', 'tournament', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'hockey', 'nfl', 'nba', 'mlb', 'nhl', 'coach', 'player', 'team', 'score', 'win', 'lose', 'final', 'quarterfinal', 'semifinal', 'gold medal', 'silver medal', 'bronze medal', 'athlete']
    
    # Business category keywords
    business_keywords = ['business', 'economy', 'stocks', 'stock', 'market', 'markets', 'wall st', 'wall street', 'dow jones', 'nasdaq', 'investment', 'investors', 'shares', 'trading', 'earnings', 'profit', 'loss', 'revenue', 'company', 'companies', 'corporate', 'bank', 'banks', 'banking', 'finance', 'financial', 'oil', 'energy', 'prices', 'federal reserve', 'fed', 'interest rates', 'economist']
    
    # Science/Technology category keywords
    science_tech_keywords = ['science', 'technology', 'tech', 'scientists', 'research', 'study', 'researchers', 'computer', 'internet', 'software', 'hardware', 'mobile', 'phone', 'smartphone', 'robot', 'ai', 'artificial intelligence', 'nasa', 'space', 'satellite', 'launch', 'rocket', 'genetic', 'dna', 'clinical', 'medical', 'health', 'disease', 'vaccine', 'climate', 'environment', 'energy', 'solar', 'battery']
    
    # Check for World category - if matches world keywords but NOT sports, business, or science/tech
    # (to avoid miscategorization)
    text = f"{title} {description}".lower()
    
    is_world = any(kw in text for kw in world_keywords)
    is_sports = any(kw in text for kw in sports_keywords)
    is_business = any(kw in text for kw in business_keywords)
    is_science_tech = any(kw in text for kw in science_tech_keywords)
    
    # Classification priority: Sports, Business, Science/Tech first, then World
    if is_sports:
        return 'Sports'
    elif is_business:
        return 'Business'
    elif is_science_tech:
        return 'Science/Technology'
    elif is_world:
        return 'World'
    else:
        return 'Other'

# Apply categorization
df_merged['category'] = df_merged.apply(lambda row: categorize_article(row['title'], row['description']), axis=1)

# Filter for World category
world_articles = df_merged[df_merged['category'] == 'World']

print(f"Articles in World category from 2015: {len(world_articles)}")

# Count by region
region_counts = world_articles['region'].value_counts()

print("Region counts for World category:")
print(region_counts)

# Find region with max count
if not region_counts.empty:
    top_region = region_counts.idxmax()
    max_count = region_counts.max()
    print(f"Region with most World articles: {top_region} ({max_count} articles)")
else:
    top_region = None
    max_count = 0

result = {
    'total_2015_articles': len(df_merged),
    'world_articles_count': len(world_articles),
    'region_counts': region_counts.to_dict(),
    'top_region': top_region,
    'max_count': max_count
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'_id': '6969da34a43fb535d0881320', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969da34a43fb535d0881321', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969da34a43fb535d0881322', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969da34a43fb535d0881323', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969da34a43fb535d0881324', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:6': {'total_2015_articles': 0, 'sample': []}, 'var_functions.query_db:8': [{'publication_date': '2022-09-18'}, {'publication_date': '2004-03-20'}, {'publication_date': '2021-02-04'}, {'publication_date': '2020-03-04'}, {'publication_date': '2012-02-01'}, {'publication_date': '2011-02-21'}, {'publication_date': '2017-09-20'}, {'publication_date': '2022-12-23'}, {'publication_date': '2011-03-30'}, {'publication_date': '2016-05-24'}], 'var_functions.query_db:10': [{'year': '2004'}, {'year': '2005'}, {'year': '2006'}, {'year': '2007'}, {'year': '2008'}, {'year': '2009'}, {'year': '2010'}, {'year': '2011'}, {'year': '2012'}, {'year': '2013'}, {'year': '2014'}, {'year': '2015'}, {'year': '2016'}, {'year': '2017'}, {'year': '2018'}, {'year': '2019'}, {'year': '2020'}, {'year': '2021'}, {'year': '2022'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
