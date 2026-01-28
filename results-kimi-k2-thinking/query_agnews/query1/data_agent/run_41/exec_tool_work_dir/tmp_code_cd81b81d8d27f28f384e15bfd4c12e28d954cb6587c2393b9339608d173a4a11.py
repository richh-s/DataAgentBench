code = """import json
import os
import re

# Try to load the articles from the JSON file
articles = []

# Check if the file exists at the expected location
expected_file = '/tmp/query_result_articles_database.json'
if os.path.exists(expected_file):
    with open(expected_file, 'r') as f:
        articles = json.load(f)
    print(f"Loaded {len(articles)} articles from {expected_file}")
else:
    # Try to find any JSON file with articles
    import glob
    for file_path in glob.glob('/tmp/*.json'):
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                if isinstance(data, list) and len(data) > 0:
                    if any('title' in item and 'description' in item for item in data[:5]):
                        articles = data
                        print(f"Loaded {len(articles)} articles from {file_path}")
                        break
        except:
            continue

if not articles:
    print("Failed to load articles")
    result = "Failed to load articles"
else:
    # Enhanced sports keyword detection
    sports_patterns = [
        r'\bolympic\b', r'\bolympics\b', r'\bmedal\b', r'\bworld cup\b',
        r'\bchampionship\b', r'\bchampion\b', r'\btournament\b', r'\bcoach\b',
        r'\bteam\b', r'\bplayer\b', r'\bquarterfinal\b', r'\bsemifinal\b',
        r'\bfinal\b', r'\bscore\b', r'\bgame\b', r'\bsport\b', r'\bsports\b',
        r'\bfootball\b', r'\bsoccer\b', r'\bbasketball\b', r'\bbaseball\b',
        r'\btennis\b', r'\bgolf\b', r'\bhockey\b', r'\bcricket\b',
        r'\brugby\b', r'\bboxing\b', r'\bswimm\b', r'\bathlet\b',
        r'\bmarathon\b', r'\brace\b', r'\bracing\b', r'\bski\b',
        r'\bskating\b', r'\bvolleyball\b', r'\bbadminton\b',
        r'\bcycling\b', r'\bwrestling\b', r'\bmatch\b'
    ]
    
    compiled_pattern = re.compile('|'.join(sports_patterns), re.IGNORECASE)
    
    sports_articles = []
    for article in articles:
        title = article.get('title', '')
        description = article.get('description', '')
        
        if compiled_pattern.search(title) or compiled_pattern.search(description):
            sports_articles.append({
                'title': title,
                'description': description,
                'desc_length': len(description)
            })
    
    if sports_articles:
        # Find the article with the longest description
        longest_article = max(sports_articles, key=lambda x: x['desc_length'])
        result = longest_article['title']
    else:
        result = "No sports articles found"

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': 'No sports articles found in the dataset', 'var_functions.execute_python:6': 'No sports articles found', 'var_functions.execute_python:8': 'Found 2 articles to analyze', 'var_functions.execute_python:10': 'No sports articles found', 'var_functions.query_db:12': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:14': 'No sports articles found in the available data', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': 'No articles loaded'}

exec(code, env_args)
