code = """import json
import re

# Step 1: Load article_ids from 2015
with open('file_storage/functions.query_db:14.json', 'r') as f:
    metadata = json.load(f)

article_ids_2015 = [int(item['article_id']) for item in metadata]
region_lookup = {int(item['article_id']): item['region'] for item in metadata}

# Step 2: Function to determine category based on title and description
def categorize_article(title, description):
    """Categorize article into World, Sports, Business, or Science/Technology"""
    if not title and not description:
        return 'Unknown'
    
    # Combine title and description for analysis
    text = f"{title} {description}".lower()
    
    # World category indicators
    world_indicators = [
        'world', 'global', 'international', 'nation', 'country', 'countries',
        'conflict', 'war', 'peace', 'treaty', 'diplomatic', 'diplomacy',
        'united nations', 'un', 'eu', 'european union', 'nato', 'african union',
        'foreign', 'abroad', 'overseas', 'embassy', 'ambassador',
        'terrorist', 'terrorism', 'isis', 'taliban', 'al qaeda',
        'refugee', 'migrant', 'immigration', 'border',
        'sanction', 'trade war', 'diplomat', 'summit', 'negotiation'
    ]
    
    # Sports category indicators
    sports_indicators = [
        'olympic', 'olympics', 'world cup', 'championship', 'tournament',
        'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf',
        'fifa', 'uefa', 'nfl', 'nba', 'mlb', 'nhl', 'premier league',
        'athlete', 'coach', 'medal', 'gold medal', 'silver medal', 'bronze medal',
        'game', 'match', 'score', 'victory', 'defeat', 'champion', 'title'
    ]
    
    # Business category indicators  
    business_indicators = [
        'stock', 'market', 'economy', 'economic', 'finance', 'financial',
        'wall street', 'investment', 'investor', 'profit', 'loss', 'revenue',
        'earnings', 'quarterly', 'shares', 'trading', 'ipo', 'initial public offering',
        'merger', 'acquisition', 'bankruptcy', 'bank', 'banking', 'interest rate',
        'gdp', 'inflation', 'unemployment', 'jobs', 'employment',
        'company', 'corporation', 'business', 'industry', 'sector'
    ]
    
    # Science/Technology category indicators
    tech_indicators = [
        'technology', 'tech', 'science', 'scientific', 'research', 'study',
        'digital', 'internet', 'online', 'software', 'hardware', 'computer',
        'artificial intelligence', 'ai', 'machine learning', 'robot', 'robotics',
        'space', 'nasa', 'spacex', 'satellite', 'rocket', 'mars', 'moon',
        'climate', 'environment', 'energy', 'renewable', 'solar', 'wind',
        'biotech', 'genetic', 'dna', 'medical', 'medicine', 'health',
        'vaccine', 'disease', 'virus', 'bacteria', 'pharma', 'pharmaceutical'
    ]
    
    # Check indicators and return most likely category
    # World category gets priority for conflicts, diplomacy, international relations
    world_score = sum(1 for indicator in world_indicators if indicator in text)
    sports_score = sum(1 for indicator in sports_indicators if indicator in text)
    business_score = sum(1 for indicator in business_indicators if indicator in text)
    tech_score = sum(1 for indicator in tech_indicators if indicator in text)
    
    # If any category has 2+ matches, use that
    max_score = max(world_score, sports_score, business_score, tech_score)
    
    if max_score >= 2:
        if world_score == max_score:
            return 'World'
        elif sports_score == max_score:
            return 'Sports'
        elif business_score == max_score:
            return 'Business'
        else:
            return 'Science/Technology'
    
    # Check for single strong indicators
    if world_score > 0:
        return 'World'
    elif business_score > 0:
        return 'Business'
    elif tech_score > 0:
        return 'Science/Technology'
    elif sports_score > 0:
        return 'Sports'
    
    return 'Unknown'

# Output total count
print('__RESULT__:')
print(f'Sample data loaded: {len(article_ids_2015)} articles from 2015')"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'type': 'str', 'value': 'file_storage/functions.query_db:2.json'}, 'var_functions.execute_python:8': {'count_2015': 6696, 'sample_ids': [13, 18, 26, 51, 52, 67, 70, 74, 86, 97]}, 'var_functions.query_db:12': [{'_id': '6969ee90d879a09892c35643', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'_id': '6969ee90d879a09892c35648', 'article_id': '18', 'title': 'US trade deficit swells in June', 'description': 'The US trade deficit has exploded 19 to a record \\$55.8bn as oil costs drove imports higher, according to a latest figures.'}, {'_id': '6969ee90d879a09892c35650', 'article_id': '26', 'title': 'Google auction begins on Friday', 'description': 'An auction of shares in Google, the web search engine which could be floated for as much as \\$36bn, takes place on Friday.'}, {'_id': '6969ee90d879a09892c35669', 'article_id': '51', 'title': 'Delightful Dell', 'description': "The company's results show that it's not grim all over tech world. Just all of it that isn't Dell."}, {'_id': '6969ee90d879a09892c3566a', 'article_id': '52', 'title': "Chrysler's Bling King", 'description': "After a tough year, Detroit's troubled carmaker is back -- thanks to a maverick designer and a car that is dazzling the hip-hop crowd"}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'total_articles': 6696, 'num_batches': 7, 'batch_size': 1000}}

exec(code, env_args)
