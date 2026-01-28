code = """import json

# Load metadata for 2015 articles
metadata = var_functions.query_db:4
articles_data = var_functions.query_db:5

# Filter metadata for 2015
# metadata is already filtered by the query

# Categorization logic: World category articles are likely about international news
world_keywords = ['world', 'global', 'international', 'united nations', 'u.n.', 'foreign', 'diplomatic', 'war', 'peace', 'treaty', 'alliance', 'europe', 'asia', 'africa', 'america', 'nato', 'eu', 'un']

# Business: financial, market, stocks, economy, corporate, etc.
# Sports: game, match, tournament, league, sport, team, player
# Science/Technology: science, tech, research, study, innovation, digital

world_articles = []
for article in articles_data:
    article_id = article.get('article_id')
    title = article.get('title', '').lower()
    description = article.get('description', '').lower()
    
    # Simple heuristic: if contains geopolitical keywords and not sports/business/science signals
    has_world = any(kw in title or kw in description for kw in world_keywords)
    
    # Exclusion for other categories
    sports_words = ['game', 'match', 'tournament', 'play', 'win', 'lose', 'score', 'team', 'sport', 'player', 'league', 'cup', 'final', 'champion']
    business_words = ['stock', 'market', 'economy', 'economic', 'business', 'company', 'corporate', 'financial', 'wall st', 'nyse', 'profit', 'revenue', 'trade', 'investment']
    science_words = ['study', 'research', 'scientist', 'technology', 'tech', 'digital', 'innovation', 'lab', 'experiment', 'data', 'science']
    
    is_sports = any(word in title or word in description for word in sports_words)
    is_business = any(word in title or word in description for word in business_words)
    is_science = any(word in title or word in description for word in science_words)
    
    if has_world and not (is_sports or is_business or is_science):
        world_articles.append(article_id)

# Now count per region from metadata
region_counts = {}
for meta in metadata:
    article_id = str(meta.get('article_id'))
    region = meta.get('region')
    
    if article_id in world_articles:
        region_counts[region] = region_counts.get(region, 0) + 1

# Sort regions by count
sorted_regions = sorted(region_counts.items(), key=lambda x: x[1], reverse=True)

print('__RESULT__:')
print(json.dumps({
    'world_articles_count': len(world_articles),
    'region_counts': region_counts,
    'top_region': sorted_regions[0] if sorted_regions else None
}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.list_db:1': ['authors', 'article_metadata'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': [{'_id': '6969e22fc8ea0d34cb738e98', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969e22fc8ea0d34cb738e99', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969e22fc8ea0d34cb738e9a', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969e22fc8ea0d34cb738e9b', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969e22fc8ea0d34cb738e9c', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
