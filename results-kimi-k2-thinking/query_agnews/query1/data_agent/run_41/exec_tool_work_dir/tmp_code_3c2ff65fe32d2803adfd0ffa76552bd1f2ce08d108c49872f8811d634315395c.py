code = """import json
import os
import re
import glob

# Let's explore what files we have available
print("Looking for article files...")

tmp_files = glob.glob('/tmp/*')
print(f"Files in /tmp: {tmp_files}")

# Look specifically for query result files
query_files = glob.glob('/tmp/query_result*.json')
print(f"Query result files: {query_files}")

# Try to load articles from any file that looks right
articles = []
loaded_from = None

for file_path in query_files:
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            if isinstance(data, list) and len(data) > 0:
                if isinstance(data[0], dict) and 'title' in data[0]:
                    articles = data
                    loaded_from = file_path
                    break
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        continue

print(f"Loaded {len(articles)} articles from {loaded_from}")

if articles:
    # Look for sports articles
    sports_indicators = [
        'olympics', 'olympic', 'medal', 'world cup', 'championship', 'tournament',
        'team', 'player', 'coach', 'final', 'semifinal', 'quarterfinal', 'score',
        'sport', 'football', 'soccer', 'basketball', 'baseball', 'tennis',
        'hockey', 'golf', 'cricket', 'rugby', 'boxing', 'swimming', 'athlete',
        'marathon', 'race', 'competition', 'match', 'game', 'stadium', 'league'
    ]
    
    pattern = re.compile('|'.join([f'\\b{term}\\b' for term in sports_indicators]), re.IGNORECASE)
    
    sports_articles = []
    for idx, article in enumerate(articles):
        title = article.get('title', '')
        desc = article.get('description', '')
        
        if pattern.search(title) or pattern.search(desc):
            sports_articles.append({
                'index': idx,
                'title': title,
                'length': len(desc)
            })
    
    print(f"Found {len(sports_articles)} sports articles")
    
    if sports_articles:
        # Find the one with longest description
        longest = max(sports_articles, key=lambda x: x['length'])
        result = longest['title']
        print(f"Sports article with longest description: {result}")
    else:
        result = "No sports articles found"
        
        # Debug: Show first few article titles
        print("\\nFirst 10 article titles:")
        for i, article in enumerate(articles[:10]):
            print(f"{i}: {article.get('title', '')}")
else:
    result = "No articles loaded"

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': 'No sports articles found in the dataset', 'var_functions.execute_python:6': 'No sports articles found', 'var_functions.execute_python:8': 'Found 2 articles to analyze', 'var_functions.execute_python:10': 'No sports articles found', 'var_functions.query_db:12': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:14': 'No sports articles found in the available data', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': 'No articles loaded', 'var_functions.execute_python:22': 'Failed to load articles', 'var_functions.execute_python:24': 'No articles found to analyze', 'var_functions.execute_python:26': 'Failed to load articles', 'var_functions.execute_python:28': 'No sports articles found', 'var_functions.execute_python:30': 'Failed to load articles'}

exec(code, env_args)
