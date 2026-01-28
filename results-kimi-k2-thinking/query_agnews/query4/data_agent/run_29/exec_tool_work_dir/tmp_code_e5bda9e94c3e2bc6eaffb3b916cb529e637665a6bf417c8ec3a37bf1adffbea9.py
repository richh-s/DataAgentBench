code = """import json
import pandas as pd
import re

# Load files
metadata_file = globals()['var_functions.query_db_20']
articles_file = globals()['var_functions.query_db_22']

with open(metadata_file, 'r') as f:
    metadata_2015 = json.load(f)

with open(articles_file, 'r') as f:
    all_articles = json.load(f)

# Create DataFrames
metadata_df = pd.DataFrame(metadata_2015)
metadata_df['article_id'] = metadata_df['article_id'].astype(int)

# All articles DataFrame
articles_df = pd.DataFrame(all_articles)
articles_df['article_id'] = articles_df['article_id'].astype(int)

# Merge on article_id
merged_df = pd.merge(articles_df, metadata_df, on='article_id', how='inner')

# Define keywords for categorization
def categorize_article(title, description):
    text = f"{title} {description}".lower()
    
    # World category keywords
    world_keywords = [
        'iraq', 'war', 'peace', 'united nations', 'un', 'global', 'world',
        'international', 'foreign', 'diplomat', 'diplomacy', 'treaty',
        'conflict', 'crisis', 'humanitarian', 'aid', 'embassy',
        'military', 'terror', 'terrorist', 'attack', 'bomb', 'violence',
        'election', 'president', 'government', 'political', 'protest',
        'iran', 'north korea', 'china', 'russia', 'israel', 'palestine',
        'afghanistan', 'syria', 'lebanon', 'pakistan', 'india',
        'mexico', 'canada', 'europe', 'africa', 'asia', 'america',
        'killed', 'death', 'dead', 'injured', 'hostage', 'kidnap'
    ]
    
    # Sports category keywords
    sports_keywords = [
        'sport', 'game', 'match', 'team', 'player', 'coach', 'season',
        'tournament', 'championship', 'league', 'olympic', 'football',
        'basketball', 'baseball', 'soccer', 'tennis', 'golf', 'racing',
        'score', 'win', 'loss', 'victory', 'defeat', 'competition'
    ]
    
    # Business category keywords  
    business_keywords = [
        'stock', 'market', 'economy', 'economic', 'business', 'company',
        'corporate', 'earnings', 'profit', 'loss', 'revenue', 'sales',
        'investment', 'investor', 'fund', 'trading', 'bank', 'finance',
        'financial', 'oil', 'price', 'prices', 'quarter', 'executive',
        'ceo', 'acquisition', 'merger', 'deal', 'contract', 'industry'
    ]
    
    # Science/Tech category keywords
    tech_keywords = [
        'technology', 'tech', 'science', 'scientific', 'research',
        'study', 'university', 'scientist', 'researcher', 'digital',
        'internet', 'software', 'hardware', 'computer', 'phone',
        'mobile', 'wireless', 'medical', 'health', 'disease', 'drug',
        'treatment', 'breakthrough', 'discovery', 'innovation',
        'space', 'nasa', 'satellite', 'robot', 'ai', 'artificial intelligence'
    ]
    
    world_score = sum(1 for keyword in world_keywords if keyword in text)
    sports_score = sum(1 for keyword in sports_keywords if keyword in text)
    business_score = sum(1 for keyword in business_keywords if keyword in text)
    tech_score = sum(1 for keyword in tech_keywords if keyword in text)
    
    scores = {
        'World': world_score,
        'Sports': sports_score,
        'Business': business_score,
        'Science/Technology': tech_score
    }
    
    # Return category with highest score, or 'Other' if all scores are 0
    max_score = max(scores.values())
    if max_score == 0:
        return 'Other'
    
    # Return the category with the highest score
    return max(scores, key=scores.get)

# Apply categorization
categories = []
for _, row in merged_df.iterrows():
    cat = categorize_article(row['title'], row['description'])
    categories.append(cat)

merged_df['category'] = categories

# Filter for World category in 2015
world_2015 = merged_df[merged_df['category'] == 'World']

# Count by region
region_counts = world_2015['region'].value_counts()

print('__RESULT__:')
print(json.dumps({
    'world_articles_2015_count': len(world_2015),
    'region_counts': region_counts.to_dict(),
    'top_region': region_counts.index[0] if len(region_counts) > 0 else None,
    'top_region_count': int(region_counts.iloc[0]) if len(region_counts) > 0 else 0
}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': {'message': 'testing variable access'}, 'var_functions.query_db:14': [{'_id': '6969e4a77dc683d979b3844a', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969e4a77dc683d979b3844b', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969e4a77dc683d979b3844c', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969e4a77dc683d979b3844d', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}, {'_id': '6969e4a77dc683d979b3844e', 'article_id': '5', 'title': 'Stocks End Up, But Near Year Lows (Reuters)', 'description': 'Reuters - Stocks ended slightly higher on Friday\\but stayed near lows for the year as oil prices surged past  #36;46\\a barrel, offsetting a positive outlook from computer maker\\Dell Inc. (DELL.O)'}, {'_id': '6969e4a77dc683d979b3844f', 'article_id': '6', 'title': 'Money Funds Fell in Latest Week (AP)', 'description': "AP - Assets of the nation's retail money market mutual funds fell by  #36;1.17 billion in the latest week to  #36;849.98 trillion, the Investment Company Institute said Thursday."}, {'_id': '6969e4a77dc683d979b38450', 'article_id': '7', 'title': 'Fed minutes show dissent over inflation (USATODAY.com)', 'description': 'USATODAY.com - Retail sales bounced back a bit in July, and new claims for jobless benefits fell last week, the government said Thursday, indicating the economy is improving from a midsummer slump.'}, {'_id': '6969e4a77dc683d979b38451', 'article_id': '8', 'title': 'Safety Net (Forbes.com)', 'description': 'Forbes.com - After earning a PH.D. in Sociology, Danny Bazil Riley started to work as the general manager at a commercial real estate firm at an annual base salary of  #36;70,000. Soon after, a financial planner stopped by his desk to drop off brochures about insurance benefits available through his employer. But, at 32, "buying insurance was the furthest thing from my mind," says Riley.'}, {'_id': '6969e4a77dc683d979b38452', 'article_id': '9', 'title': 'Wall St. Bears Claw Back Into the Black', 'description': " NEW YORK (Reuters) - Short-sellers, Wall Street's dwindling  band of ultra-cynics, are seeing green again."}, {'_id': '6969e4a77dc683d979b38453', 'article_id': '10', 'title': "Oil and Economy Cloud Stocks' Outlook", 'description': ' NEW YORK (Reuters) - Soaring crude prices plus worries  about the economy and the outlook for earnings are expected to  hang over the stock market next week during the depth of the  summer doldrums.'}], 'var_functions.execute_python:16': ['var_functions.query_db:2', 'var_functions.query_db:14'], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:28': ['var_functions.query_db:14', 'var_functions.query_db:2', 'var_functions.query_db:20', 'var_functions.query_db:22']}

exec(code, env_args)
