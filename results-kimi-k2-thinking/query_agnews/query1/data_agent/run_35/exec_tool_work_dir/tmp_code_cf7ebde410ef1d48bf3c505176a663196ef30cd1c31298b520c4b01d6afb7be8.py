code = """import json

# Load all articles from the file
all_articles_file = locals()['var_functions.query_db:24']

# Read all articles from file
with open(all_articles_file, 'r') as f:
    all_articles = json.load(f)

# Comprehensive sports keywords
sports_keywords = [
    'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf',
    'hockey', 'rugby', 'cricket', 'volleyball', 'swimming', 'boxing',
    'wrestling', 'running', 'marathon', 'sprint', 'race', 
    'olympics', 'olympic', 'athlete', 'athletes', 'athletic',
    'championship', 'tournament', 'league', 'coach', 'player', 'team',
    'medal', 'nba', 'nfl', 'mlb', 'nhl', 'fifa', 'uefa', 'ncaa',
    'world cup', 'super bowl', 'playoff', 'playoffs'
]

# False positive keywords to exclude
false_positives = [
    'rocket', 'space', 'launch', 'satellite', 'nasa',
    'windows', 'unix', 'microsoft', 'software',
    'steamroller', 'band', 'music', 'recording',
    'project collaboration', 'autodesk', 'construction'
]

# Check if text contains sports terms
def is_sports_article(title, description):
    title_lower = title.lower() if title else ''
    desc_lower = description.lower() if description else ''
    text_lower = title_lower + ' ' + desc_lower
    
    # Check for false positives first
    for fp in false_positives:
        if fp in text_lower:
            return False
    
    # Check for sports terms
    for keyword in sports_keywords:
        if keyword in text_lower:
            return True
    
    return False

# Find sports articles with longest description
max_desc_length = -1
longest_desc_sports_article = None
sports_articles_count = 0

for article in all_articles:
    title = article.get('title', '')
    description = article.get('description', '')
    article_id = article.get('article_id')
    
    if is_sports_article(title, description):
        sports_articles_count += 1
        desc_length = len(description)
        
        if desc_length > max_desc_length:
            max_desc_length = desc_length
            longest_desc_sports_article = {
                'title': title,
                'article_id': article_id,
                'description_length': desc_length,
                'description_preview': description[:150] + '...' if len(description) > 150 else description
            }

print('__RESULT__:')
print(json.dumps({
    'total_articles_processed': len(all_articles),
    'sports_articles_found': sports_articles_count,
    'article_with_longest_description': longest_desc_sports_article
}))"""

env_args = {'var_functions.query_db:0': [{'_id': '69697811190e2e64cc8a20ea', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69697811190e2e64cc8a20eb', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697811190e2e64cc8a20ec', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697811190e2e64cc8a20ed', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697811190e2e64cc8a20ee', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:5': 'No sports articles found', 'var_functions.query_db:6': [{'_id': '69697811190e2e64cc8a20ea', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69697811190e2e64cc8a20eb', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697811190e2e64cc8a20ec', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697811190e2e64cc8a20ed', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697811190e2e64cc8a20ee', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:8': {'count': 5, 'articles': [{'_id': '69697811190e2e64cc8a20ea', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69697811190e2e64cc8a20eb', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697811190e2e64cc8a20ec', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697811190e2e64cc8a20ed', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697811190e2e64cc8a20ee', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}, 'var_functions.execute_python:10': {'total_articles': 5, 'articles': [{'index': 0, 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description_length': 94, 'first_words': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing..."}, {'index': 1, 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description_length': 214, 'first_words': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation...'}, {'index': 2, 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description_length': 184, 'first_words': 'Reuters - Soaring crude prices plus worries\\about the economy and...'}, {'index': 3, 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description_length': 195, 'first_words': 'Reuters - Authorities have halted oil export\\flows from the main...'}, {'index': 4, 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description_length': 160, 'first_words': 'AFP - Tearaway world oil prices, toppling records and straining...'}]}, 'var_functions.list_db:12': ['authors', 'article_metadata'], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'total_metadata_entries': 127600, 'min_article_id': 0, 'max_article_id': 127599, 'sample_article_ids': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'title': "Why Windows isn't Unix", 'article_id': '183', 'description_length': 708}, 'var_functions.query_db:22': [{'_id': '69697811190e2e64cc8a20f1', 'article_id': '7', 'title': 'Fed minutes show dissent over inflation (USATODAY.com)', 'description': 'USATODAY.com - Retail sales bounced back a bit in July, and new claims for jobless benefits fell last week, the government said Thursday, indicating the economy is improving from a midsummer slump.'}, {'_id': '69697811190e2e64cc8a20fa', 'article_id': '16', 'title': 'Kids Rule for Back-to-School', 'description': 'The purchasing power of kids is a big part of why the back-to-school season has become such a huge marketing phenomenon.'}, {'_id': '69697811190e2e64cc8a2107', 'article_id': '29', 'title': 'Chad seeks refugee aid from IMF', 'description': 'Chad asks the IMF for a loan to pay for looking after more than 100,000 refugees from conflict-torn Darfur in western Sudan.'}, {'_id': '69697811190e2e64cc8a2122', 'article_id': '56', 'title': 'Stoking the Steamroller', 'description': 'No other recording artist can channel American middle-class tastes quite like Chip Davis and his best-selling band'}, {'_id': '69697811190e2e64cc8a212f', 'article_id': '69', 'title': 'Autodesk tackles project collaboration', 'description': 'Autodesk  this week unwrapped an updated version of its hosted project collaboration service targeted at the construction and manufacturing industries. Autodesk Buzzsaw lets multiple, dispersed project participants -- including building owners, developers, architects, construction teams, and facility managers -- share and manage data throughout the life of a project, according to Autodesk officials.'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'total_sports_articles_found': 849, 'article_with_longest_description': {'title': 'Canadian Ansari X Prize Entrant Takes the Plunge in Test (SPACE.com)', 'article_id': '1133', 'desc_length': 552}, 'sample_sports_articles': [{'title': 'Japan nuclear firm shuts plants', 'article_id': '30', 'desc_length': 114, 'description_preview': 'The company running the Japanese nuclear plant hit by a fatal accident is to close its reactors for ...'}, {'title': 'HP to Buy Synstar', 'article_id': '74', 'desc_length': 207, 'description_preview': 'Hewlett-Packard will pay \\$297 million for the British company. Also: TiVo goes all out to attract c...'}, {'title': "'Madden,' 'ESPN' Football Score in Different Ways (Reuters)", 'article_id': '78', 'desc_length': 251, 'description_preview': 'Reuters - Was absenteeism a little high\\on Tuesday among the guys at the office? EA Sports would lik...'}, {'title': 'The Next Great Space Race: SpaceShipOne and Wild Fire to Go For the Gold (SPACE.com)', 'article_id': '126', 'desc_length': 152, 'description_preview': 'SPACE.com - A piloted rocket ship race to claim a  #36;10 million Ansari X Prize purse for privately...'}, {'title': "Wash. State Team's Private Rocket Explodes (AP)", 'article_id': '139', 'desc_length': 225, 'description_preview': 'AP - A team taking a low-budget stab at the  #36;10 million Ansari X Prize for private manned spacef...'}, {'title': 'Canadian Team Joins Rocket Launch Contest (AP)', 'article_id': '156', 'desc_length': 267, 'description_preview': 'AP - The  #36;10 million competition to send a private manned rocket into space started looking more...'}, {'title': 'Wireless net to get speed boost', 'article_id': '190', 'desc_length': 82, 'description_preview': 'Wireless computer networks could soon be running 10 times faster than they do now.'}, {'title': "'Invisible' technology for Olympics", 'article_id': '197', 'desc_length': 77, 'description_preview': 'Getting the technology in place for Athens 2004 is an Olympic task in itself.'}, {'title': 'Satellite boosts Olympic security', 'article_id': '198', 'desc_length': 109, 'description_preview': 'An enhanced satellite location system aims to help Olympic security guards react more quickly to eme...'}, {'title': "'Madden,' 'ESPN' Football Score in Different Ways", 'article_id': '203', 'desc_length': 275, 'description_preview': ' PROVIDENCE, R.I. (Reuters) - Was absenteeism a little high  on Tuesday among the guys at the office...'}]}, 'var_functions.query_db:28': [], 'var_functions.query_db:30': [{'_id': '69697811190e2e64cc8a20f1', 'article_id': '7', 'title': 'Fed minutes show dissent over inflation (USATODAY.com)', 'description': 'USATODAY.com - Retail sales bounced back a bit in July, and new claims for jobless benefits fell last week, the government said Thursday, indicating the economy is improving from a midsummer slump.'}, {'_id': '69697811190e2e64cc8a2107', 'article_id': '29', 'title': 'Chad seeks refugee aid from IMF', 'description': 'Chad asks the IMF for a loan to pay for looking after more than 100,000 refugees from conflict-torn Darfur in western Sudan.'}, {'_id': '69697811190e2e64cc8a2122', 'article_id': '56', 'title': 'Stoking the Steamroller', 'description': 'No other recording artist can channel American middle-class tastes quite like Chip Davis and his best-selling band'}, {'_id': '69697811190e2e64cc8a212f', 'article_id': '69', 'title': 'Autodesk tackles project collaboration', 'description': 'Autodesk  this week unwrapped an updated version of its hosted project collaboration service targeted at the construction and manufacturing industries. Autodesk Buzzsaw lets multiple, dispersed project participants -- including building owners, developers, architects, construction teams, and facility managers -- share and manage data throughout the life of a project, according to Autodesk officials.'}, {'_id': '69697811190e2e64cc8a2138', 'article_id': '78', 'title': "'Madden,' 'ESPN' Football Score in Different Ways (Reuters)", 'description': 'Reuters - Was absenteeism a little high\\on Tuesday among the guys at the office? EA Sports would like\\to think it was because "Madden NFL 2005" came out that day,\\and some fans of the football simulation are rabid enough to\\take a sick day to play it.'}]}

exec(code, env_args)
