code = """import json
import os
import re

# Find the articles file
articles_file = '/tmp/query_result_articles_database.json'

# Check if file exists
if not os.path.exists(articles_file):
    # Try to find any query result file
    import glob
    files = glob.glob('/tmp/query_result*.json')
    if files:
        articles_file = files[0]

# Load articles
if os.path.exists(articles_file):
    with open(articles_file, 'r') as f:
        articles = json.load(f)
else:
    articles = []

print(f"Loaded {len(articles)} articles")

# More specific sports keywords - focusing on actual sports
sports_keywords = [
    'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf',
    'hockey', 'cricket', 'rugby', 'boxing', 'wrestling', 'olympics',
    'olympic games', 'world cup', 'championship', 'tournament', 'nba',
    'nfl', 'mlb', 'nhl', 'premier league', 'bundesliga', 'la liga',
    'serie a', 'world series', 'super bowl', 'stanley cup', 'march madness',
    'wimbledon', 'us open', 'french open', 'australian open', 'masters',
    'pga', 'nascar', 'formula one', 'f1', 'athlete', 'marathon',
    'track and field', 'gymnastics', 'fencing', 'judo', 'karate',
    'volleyball', 'badminton', 'cycling', 'swimming', 'diving',
    'rowing', 'sailing', 'equestrian', 'handball', 'water polo',
    'table tennis', 'ping pong', 'skiiing', 'snowboarding', 'skating',
    'archery', 'shooting', 'triathlon', 'decathlon', 'pentathlon',
    'ultra marathon', 'ironman', ' Tour de France', 'home run', 'touchdown',
    'field goal', 'basket', 'goal', 'points', 'medal', 'bronze', 'silver', 'gold'
]

# Create regex pattern - use word boundaries and avoid partial matches
pattern = re.compile(
    r'\\b(' + '|'.join(re.escape(k) for k in sports_keywords) + r')\\b',
    re.IGNORECASE
)

# Find actual sports articles
sports_articles = []
for article in articles:
    title = article.get('title', '').lower()
    desc = article.get('description', '').lower()
    
    # Check for sports content
    has_sports = bool(pattern.search(title) or pattern.search(desc))
    
    # Filter out obvious false positives based on context
    if has_sports:
        # Check if it's actually about sports or just mentions sports terms in other contexts
        sports_context_terms = ['game', 'season', 'tournament', 'championship', 'match', 'play', 'player', 'team', 'coach', 'league', 'sport']
        
        title_sports_count = sum(1 for term in sports_context_terms if term in title)
        desc_sports_count = sum(1 for term in sports_context_terms if term in desc)
        
        # If we have multiple sports terms, it's more likely to be a sports article
        if title_sports_count + desc_sports_count >= 2:
            sports_articles.append({
                'title': article['title'],
                'description': article['description'],
                'length': len(article['description'])
            })

print(f"Found {len(sports_articles)} likely sports articles")

if not sports_articles:
    # Try a more relaxed search
    for article in articles:
        title = article.get('title', '').lower()
        desc = article.get('description', '').lower()
        
        sport_terms = ['football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'hockey', 'cricket', 'rugby']
        for term in sport_terms:
            if term in title or term in desc:
                sports_articles.append({
                    'title': article['title'],
                    'description': article['description'],
                    'length': len(article['description'])
                })
                break

if sports_articles:
    # Find the longest description
    longest = max(sports_articles, key=lambda x: x['length'])
    result = longest['title']
    print(f"Sports article with longest description: {result}")
    print(f"Length: {longest['length']} characters")
else:
    result = "No sports articles found"
    print("Could not identify any sports articles")

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': 'No sports articles found in the dataset', 'var_functions.execute_python:6': 'No sports articles found', 'var_functions.execute_python:8': 'Found 2 articles to analyze', 'var_functions.execute_python:10': 'No sports articles found', 'var_functions.query_db:12': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:14': 'No sports articles found in the available data', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': 'No articles loaded', 'var_functions.execute_python:22': 'Failed to load articles', 'var_functions.execute_python:24': 'No articles found to analyze', 'var_functions.execute_python:26': 'Failed to load articles', 'var_functions.execute_python:28': 'No sports articles found', 'var_functions.execute_python:30': 'Failed to load articles', 'var_functions.execute_python:32': 'No articles loaded', 'var_functions.query_db:34': [{'article_id': '56', 'title': 'Stoking the Steamroller', 'description': 'No other recording artist can channel American middle-class tastes quite like Chip Davis and his best-selling band'}, {'article_id': '69', 'title': 'Autodesk tackles project collaboration', 'description': 'Autodesk  this week unwrapped an updated version of its hosted project collaboration service targeted at the construction and manufacturing industries. Autodesk Buzzsaw lets multiple, dispersed project participants -- including building owners, developers, architects, construction teams, and facility managers -- share and manage data throughout the life of a project, according to Autodesk officials.'}, {'article_id': '78', 'title': "'Madden,' 'ESPN' Football Score in Different Ways (Reuters)", 'description': 'Reuters - Was absenteeism a little high\\on Tuesday among the guys at the office? EA Sports would like\\to think it was because "Madden NFL 2005" came out that day,\\and some fans of the football simulation are rabid enough to\\take a sick day to play it.'}, {'article_id': '109', 'title': 'New NASA Supercomputer to Aid Theorists and Shuttle Engineers (SPACE.com)', 'description': "SPACE.com - NASA researchers have teamed up with a pair of Silicon Valley firms to build \\  a supercomputer that ranks alongside the world's largest Linux-based systems."}, {'article_id': '126', 'title': 'The Next Great Space Race: SpaceShipOne and Wild Fire to Go For the Gold (SPACE.com)', 'description': 'SPACE.com - A piloted rocket ship race to claim a  #36;10 million Ansari X Prize purse for privately financed flight to the edge of space is heating up.'}], 'var_functions.query_db:44': [{'article_id': '7', 'title': 'Fed minutes show dissent over inflation (USATODAY.com)', 'description': 'USATODAY.com - Retail sales bounced back a bit in July, and new claims for jobless benefits fell last week, the government said Thursday, indicating the economy is improving from a midsummer slump.'}, {'article_id': '29', 'title': 'Chad seeks refugee aid from IMF', 'description': 'Chad asks the IMF for a loan to pay for looking after more than 100,000 refugees from conflict-torn Darfur in western Sudan.'}, {'article_id': '39', 'title': 'Microsoft Corp. 2.0: a kinder corporate culture', 'description': 'Even a genius can mess up. Bill Gates was a brilliant technologist when he cofounded Microsoft , but as he guided it to greatness in both size and historical consequence, he blundered. He terrorized underlings with his temper and parceled out praise like Scrooge gave to charity. Only the lash inspired the necessary aggressiveness to beat the competition, he thought.'}, {'article_id': '56', 'title': 'Stoking the Steamroller', 'description': 'No other recording artist can channel American middle-class tastes quite like Chip Davis and his best-selling band'}, {'article_id': '69', 'title': 'Autodesk tackles project collaboration', 'description': 'Autodesk  this week unwrapped an updated version of its hosted project collaboration service targeted at the construction and manufacturing industries. Autodesk Buzzsaw lets multiple, dispersed project participants -- including building owners, developers, architects, construction teams, and facility managers -- share and manage data throughout the life of a project, according to Autodesk officials.'}], 'var_functions.query_db:46': [{'article_id': '7', 'title': 'Fed minutes show dissent over inflation (USATODAY.com)', 'description': 'USATODAY.com - Retail sales bounced back a bit in July, and new claims for jobless benefits fell last week, the government said Thursday, indicating the economy is improving from a midsummer slump.'}, {'article_id': '16', 'title': 'Kids Rule for Back-to-School', 'description': 'The purchasing power of kids is a big part of why the back-to-school season has become such a huge marketing phenomenon.'}, {'article_id': '19', 'title': "Shell 'could be target for Total'", 'description': 'Oil giant Shell could be bracing itself for a takeover attempt, possibly from French rival Total, a  press report claims.'}, {'article_id': '29', 'title': 'Chad seeks refugee aid from IMF', 'description': 'Chad asks the IMF for a loan to pay for looking after more than 100,000 refugees from conflict-torn Darfur in western Sudan.'}, {'article_id': '56', 'title': 'Stoking the Steamroller', 'description': 'No other recording artist can channel American middle-class tastes quite like Chip Davis and his best-selling band'}], 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json'}

exec(code, env_args)
