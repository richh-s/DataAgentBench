code = """import json
import os
import re
import glob

# Find all query result files
files = glob.glob('/tmp/query_result_*.json')

articles = []
# Load the largest file
for file_path in sorted(files):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            if len(data) > len(articles):
                articles = data
    except:
        continue

result = "No articles found"
if articles:
    # Sports keywords
    sports_keywords = ['football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf',
                      'hockey', 'cricket', 'rugby', 'boxing', 'wrestling', 'volleyball',
                      'badminton', 'olympics', 'medal', 'world cup', 'championship',
                      'tournament', 'coach', 'team', 'player', 'nba', 'nfl', 'mlb', 'nhl',
                      'athlete', 'marathon', 'race', 'season', 'league', 'game', 'match']
    
    pattern = re.compile('|'.join(['\\b' + k + '\\b' for k in sports_keywords]), re.IGNORECASE)
    
    sports_articles = []
    for article in articles:
        title = article.get('title', '').lower()
        desc = article.get('description', '').lower()
        
        if pattern.search(title) or pattern.search(desc):
            sports_count = sum(1 for word in sports_keywords if word in title or word in desc)
            if sports_count >= 2:
                sports_articles.append({
                    'title': article.get('title'),
                    'length': len(article.get('description', ''))
                })
    
    if sports_articles:
        longest = max(sports_articles, key=lambda x: x['length'])
        result = longest['title']
    else:
        result = "No sports articles found"

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': 'No sports articles found in the dataset', 'var_functions.execute_python:6': 'No sports articles found', 'var_functions.execute_python:8': 'Found 2 articles to analyze', 'var_functions.execute_python:10': 'No sports articles found', 'var_functions.query_db:12': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:14': 'No sports articles found in the available data', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': 'No articles loaded', 'var_functions.execute_python:22': 'Failed to load articles', 'var_functions.execute_python:24': 'No articles found to analyze', 'var_functions.execute_python:26': 'Failed to load articles', 'var_functions.execute_python:28': 'No sports articles found', 'var_functions.execute_python:30': 'Failed to load articles', 'var_functions.execute_python:32': 'No articles loaded', 'var_functions.query_db:34': [{'article_id': '56', 'title': 'Stoking the Steamroller', 'description': 'No other recording artist can channel American middle-class tastes quite like Chip Davis and his best-selling band'}, {'article_id': '69', 'title': 'Autodesk tackles project collaboration', 'description': 'Autodesk  this week unwrapped an updated version of its hosted project collaboration service targeted at the construction and manufacturing industries. Autodesk Buzzsaw lets multiple, dispersed project participants -- including building owners, developers, architects, construction teams, and facility managers -- share and manage data throughout the life of a project, according to Autodesk officials.'}, {'article_id': '78', 'title': "'Madden,' 'ESPN' Football Score in Different Ways (Reuters)", 'description': 'Reuters - Was absenteeism a little high\\on Tuesday among the guys at the office? EA Sports would like\\to think it was because "Madden NFL 2005" came out that day,\\and some fans of the football simulation are rabid enough to\\take a sick day to play it.'}, {'article_id': '109', 'title': 'New NASA Supercomputer to Aid Theorists and Shuttle Engineers (SPACE.com)', 'description': "SPACE.com - NASA researchers have teamed up with a pair of Silicon Valley firms to build \\  a supercomputer that ranks alongside the world's largest Linux-based systems."}, {'article_id': '126', 'title': 'The Next Great Space Race: SpaceShipOne and Wild Fire to Go For the Gold (SPACE.com)', 'description': 'SPACE.com - A piloted rocket ship race to claim a  #36;10 million Ansari X Prize purse for privately financed flight to the edge of space is heating up.'}], 'var_functions.query_db:44': [{'article_id': '7', 'title': 'Fed minutes show dissent over inflation (USATODAY.com)', 'description': 'USATODAY.com - Retail sales bounced back a bit in July, and new claims for jobless benefits fell last week, the government said Thursday, indicating the economy is improving from a midsummer slump.'}, {'article_id': '29', 'title': 'Chad seeks refugee aid from IMF', 'description': 'Chad asks the IMF for a loan to pay for looking after more than 100,000 refugees from conflict-torn Darfur in western Sudan.'}, {'article_id': '39', 'title': 'Microsoft Corp. 2.0: a kinder corporate culture', 'description': 'Even a genius can mess up. Bill Gates was a brilliant technologist when he cofounded Microsoft , but as he guided it to greatness in both size and historical consequence, he blundered. He terrorized underlings with his temper and parceled out praise like Scrooge gave to charity. Only the lash inspired the necessary aggressiveness to beat the competition, he thought.'}, {'article_id': '56', 'title': 'Stoking the Steamroller', 'description': 'No other recording artist can channel American middle-class tastes quite like Chip Davis and his best-selling band'}, {'article_id': '69', 'title': 'Autodesk tackles project collaboration', 'description': 'Autodesk  this week unwrapped an updated version of its hosted project collaboration service targeted at the construction and manufacturing industries. Autodesk Buzzsaw lets multiple, dispersed project participants -- including building owners, developers, architects, construction teams, and facility managers -- share and manage data throughout the life of a project, according to Autodesk officials.'}], 'var_functions.query_db:46': [{'article_id': '7', 'title': 'Fed minutes show dissent over inflation (USATODAY.com)', 'description': 'USATODAY.com - Retail sales bounced back a bit in July, and new claims for jobless benefits fell last week, the government said Thursday, indicating the economy is improving from a midsummer slump.'}, {'article_id': '16', 'title': 'Kids Rule for Back-to-School', 'description': 'The purchasing power of kids is a big part of why the back-to-school season has become such a huge marketing phenomenon.'}, {'article_id': '19', 'title': "Shell 'could be target for Total'", 'description': 'Oil giant Shell could be bracing itself for a takeover attempt, possibly from French rival Total, a  press report claims.'}, {'article_id': '29', 'title': 'Chad seeks refugee aid from IMF', 'description': 'Chad asks the IMF for a loan to pay for looking after more than 100,000 refugees from conflict-torn Darfur in western Sudan.'}, {'article_id': '56', 'title': 'Stoking the Steamroller', 'description': 'No other recording artist can channel American middle-class tastes quite like Chip Davis and his best-selling band'}], 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.execute_python:52': 'No sports articles found', 'var_functions.query_db:54': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
