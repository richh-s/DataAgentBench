code = """import json

# Load all articles from file
file_path = locals()['var_functions.query_db:10']
with open(file_path, 'r') as f:
    all_articles = json.load(f)

# More strict sports keywords - focus on specific sports and context
specific_sports = {
    'football', 'soccer', 'basketball', 'baseball', 'hockey', 'tennis', 'golf',
    'cricket', 'rugby', 'volleyball', 'swimming', 'cycling', 'boxing', 'wrestling',
    'athletics', 'gymnastics', 'skiing', 'snowboarding', 'skating', 'fencing',
    'olympics', 'olympic', 'world cup', 'championship', 'tournament', 'marathon',
    'formula 1', 'f1', 'nascar', 'racing'
}

sports_context_words = {
    'season', 'player', 'players', 'team', 'teams', 'coach', 'coaches', 'game',
    'games', 'match', 'matches', 'score', 'victory', 'defeat', 'medal', 'medals',
    'champion', 'title', 'league', 'cup', 'final', 'semifinal', 'quarterfinal',
    'quarter', 'half', 'inning', 'innings', 'period', 'round', 'bout',
    'record', 'records', 'win', 'wins', 'won', 'loss', 'beat', 'beats',
    'athlete', 'athletes', 'competition', 'compete', 'competing'
}

# Function to identify sports articles more accurately
def is_sports_article_strict(article):
    title = article.get('title', '').lower()
    description = article.get('description', '').lower()
    
    text = f"{title} {description}"
    
    # Check for specific sport names first (strong indicator)
    has_specific_sport = any(sport in text for sport in specific_sports)
    
    # Count sports context words
    context_matches = sum(1 for word in sports_context_words if word in text)
    
    # Must have either a specific sport name or multiple context words
    return has_specific_sport or context_matches >= 3

# Find sports articles with strict filtering
sports_articles = []

for article in all_articles:
    if is_sports_article_strict(article):
        sports_articles.append({
            'title': article.get('title'),
            'description': article.get('description'),
            'desc_length': len(article.get('description', '')),
            'article_id': article.get('article_id')
        })

# Sort by description length (descending)
sports_articles_sorted = sorted(sports_articles, key=lambda x: x['desc_length'], reverse=True)

# Get top 10 longest sports articles for verification
top_10_longest = sports_articles_sorted[:10]

result = {
    'total_articles': len(all_articles),
    'sports_articles_found': len(sports_articles),
    'longest_sports_article': sports_articles_sorted[0] if sports_articles_sorted else None,
    'top_10_longest': [(a['title'], a['desc_length']) for a in top_10_longest]
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'_id': '69698264236002a1bb5b856a', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69698264236002a1bb5b856b', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69698264236002a1bb5b856c', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69698264236002a1bb5b856d', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69698264236002a1bb5b856e', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.list_db:4': ['authors', 'article_metadata'], 'var_functions.execute_python:8': {'message': 'No sports articles found', 'total_sports_articles_found': 0}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'_id': '69698264236002a1bb5b856a', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69698264236002a1bb5b856b', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69698264236002a1bb5b856c', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69698264236002a1bb5b856d', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69698264236002a1bb5b856e', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:14': [{'_id': '69698264236002a1bb5b856a', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69698264236002a1bb5b856b', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69698264236002a1bb5b856c', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69698264236002a1bb5b856d', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69698264236002a1bb5b856e', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:20': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'author_id': '992', 'region': 'North America', 'publication_date': '2004-03-20'}, {'article_id': '2', 'author_id': '820', 'region': 'South America', 'publication_date': '2021-02-04'}, {'article_id': '3', 'author_id': '478', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '4', 'author_id': '39', 'region': 'Africa', 'publication_date': '2012-02-01'}], 'var_functions.execute_python:28': {'count': 1000, 'first_article': {'_id': '69698264236002a1bb5b856a', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}}, 'var_functions.execute_python:30': {'total_articles': 1000, 'sports_articles_found': 198, 'longest_sports_article': {'title': 'Pretty Log4J', 'description': '\\\\I\'ve been a big fan of Log4J  for a while now but haven\'t migrated any code\\over for one central reason.  The following line of code:\\\\    final static Logger logger = Logger.getLogger( "some.name" );\\\\... is amazingly ugly and difficult to work with.\\\\Most people use Log4J with a logger based on the classname:\\\\So we would probably see:\\\\    static Logger logger = Logger.getLogger( "org.apache.commons.feedparser.locate.FeedLocator" );\\\\Which is amazingly verbose.  A lot of developers shorten this to:\\\\    static Logger logger = Logger.getLogger( FeedLocator.class );\\\\But this still leaves us with cut and paste errors.\\\\What if we could just reduce it to:\\\\    static Logger logger = Logger.g ...\\\\', 'desc_length': 708, 'article_id': '172'}}}

exec(code, env_args)
