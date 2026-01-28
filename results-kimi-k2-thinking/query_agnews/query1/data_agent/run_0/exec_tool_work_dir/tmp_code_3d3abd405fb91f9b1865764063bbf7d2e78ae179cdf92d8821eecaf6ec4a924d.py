code = """import json
import re

# Get all articles from the previous query
articles = locals()['var_functions.query_db:0']

# Debug: print number of articles and first few
print(f"Total articles: {len(articles)}")
print("First 3 articles:")
for i, article in enumerate(articles[:3]):
    print(f"  {i}: {article['title']}")

# Function to check if an article is sports-related
sports_keywords = [
    'sports', 'sport', 'football', 'soccer', 'basketball', 'baseball',
    'tennis', 'golf', 'olympic', 'olympics', 'athlete', 'athletes',
    'game', 'games', 'team', 'teams', 'championship', 'champion',
    'league', 'coach', 'player', 'players', 'season', 'score',
    'nba', 'nfl', 'mlb', 'nhl', 'world cup', 'tournament',
    'match', 'matches', 'race', 'racing', 'marathon', 'fitness',
    'exercise', 'workout', 'training', 'competition', 'compete',
    'victory', 'defeat', 'win', 'wins', 'winning', 'lost', 'loss'
]

def is_sports_article(article):
    """Check if article is sports-related based on title and description"""
    title = article.get('title', '').lower()
    description = article.get('description', '').lower()
    
    # Check for sports keywords
    for keyword in sports_keywords:
        if keyword in title or keyword in description:
            return True
    
    # Additional pattern matching for common sports contexts
    sports_patterns = [
        r'\b(nba|nfl|mlb|nhl|ncaa|fifa|uefa|premier league|bundesliga|la liga|serie a)\b',
        r'\b(quarterback|pitcher|goalie|forward|defender|midfielder)\b',
        r'(defeats?|beats?|triumphs?|wins?|loses?|loss|victory|defeat)',
        r'(injur|suspension|penalty|foul)'
    ]
    
    combined_text = title + ' ' + description
    for pattern in sports_patterns:
        if re.search(pattern, combined_text, re.IGNORECASE):
            return True
    
    return False

# Classify articles and find sports articles
sports_articles = []
for article in articles:
    if is_sports_article(article):
        # Calculate description length
        desc_length = len(article.get('description', ''))
        sports_articles.append({
            'article_id': article['article_id'],
            'title': article['title'],
            'description': article['description'],
            'desc_length': desc_length
        })

print(f"\nFound {len(sports_articles)} sports articles")

if sports_articles:
    # Find article with longest description
    longest_article = max(sports_articles, key=lambda x: x['desc_length'])
    
    print(f"\nLongest sports article:")
    print(f"  Title: {longest_article['title']}")
    print(f"  Description length: {longest_article['desc_length']}")
    print(f"  Description: {longest_article['description'][:100]}...")
    
    result = longest_article['title']
else:
    print("No sports articles found")
    result = None

# Print in required format
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'_id': '69696304c44a224a53ec8f86', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69696304c44a224a53ec8f87', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69696304c44a224a53ec8f88', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69696304c44a224a53ec8f89', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69696304c44a224a53ec8f8a', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
