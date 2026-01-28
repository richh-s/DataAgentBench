code = """import json
import os
import pandas as pd

# Find the articles file
possible_file = '/tmp/query_result_articles_database.json'

if os.path.exists(possible_file):
    with open(possible_file, 'r') as f:
        articles = json.load(f)
else:
    # Try to find any JSON file that might contain articles
    import glob
    json_files = glob.glob('/tmp/*.json')
    articles = []
    for file in json_files:
        try:
            with open(file, 'r') as f:
                data = json.load(f)
                if isinstance(data, list) and len(data) > 0:
                    if 'title' in data[0] and 'description' in data[0]:
                        articles = data
                        break
        except:
            continue

# If we found articles, process them
if articles:
    # Create a DataFrame for easier analysis
    df = pd.DataFrame(articles)
    
    # Sports-related keywords
    sports_terms = [
        'olympic', 'olympics', 'gold medal', 'silver medal', 'bronze medal', 'medal',
        'world cup', 'championship', 'champion', 'tournament', 'coach',
        'team', 'player', 'quarterfinal', 'semifinal', 'final', 'score',
        'game', 'games', 'sport', 'sports', 'football', 'soccer', 'basketball',
        'baseball', 'tennis', 'golf', 'hockey', 'cricket', 'rugby', 'boxing',
        'swimming', 'athlete', 'athletes', 'marathon', 'race', 'racing'
    ]
    
    # Find sports articles
    sports_mask = df['title'].str.lower().str.contains('|'.join(sports_terms)) | \
                  df['description'].str.lower().str.contains('|'.join(sports_terms))
    
    sports_articles = df[sports_mask].copy()
    
    if not sports_articles.empty:
        # Calculate description lengths
        sports_articles['desc_length'] = sports_articles['description'].str.len()
        
        # Find article with longest description
        longest_article = sports_articles.loc[sports_articles['desc_length'].idxmax()]
        result = longest_article['title']
    else:
        result = "No sports articles found"
else:
    result = "No articles loaded"

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': 'No sports articles found in the dataset', 'var_functions.execute_python:6': 'No sports articles found', 'var_functions.execute_python:8': 'Found 2 articles to analyze', 'var_functions.execute_python:10': 'No sports articles found', 'var_functions.query_db:12': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:14': 'No sports articles found in the available data', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
