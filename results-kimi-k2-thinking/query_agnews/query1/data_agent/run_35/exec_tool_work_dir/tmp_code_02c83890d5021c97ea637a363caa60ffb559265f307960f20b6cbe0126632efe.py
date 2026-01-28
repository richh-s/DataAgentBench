code = """import json

# Load all articles from the file
all_articles_file = locals()['var_functions.query_db:24']

# Read all articles from file
with open(all_articles_file, 'r') as f:
    all_articles = json.load(f)

# Define comprehensive sports keywords (whole words only)
sports_terms = [
    'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf',
    'hockey', 'rugby', 'cricket', 'volleyball', 'swimming', 'boxing',
    'wrestling', 'running', 'marathon', 'sprint', 'race', 'racing',
    'olympics', 'olympic', 'athlete', 'athletes', 'athletic',
    'championship', 'tournament', 'league', 'coach', 'player', 'team',
    'medal', 'gold medal', 'silver medal', 'bronze medal',
    'nba', 'nfl', 'mlb', 'nhl', 'fifa', 'uefa', 'ncaa',
    'world cup', 'super bowl', 'playoff', 'playoffs'
]

# Function to check if text contains sports terms (as whole words)
def contains_sports(text):
    if not text:
        return False
    text_lower = text.lower()
    words = text_lower.split()
    
    # Check for multi-word phrases first
    if 'world cup' in text_lower or 'gold medal' in text_lower or 'silver medal' in text_lower or 'bronze medal' in text_lower:
        return True
    
    # Check for single words
    for term in sports_terms:
        if term in words:
            return True
    
    return False

# Filter sports articles and find the one with longest description
sports_articles = []
max_desc_length = -1
article_with_longest_desc = None

for article in all_articles:
    title = article.get('title', '')
    description = article.get('description', '')
    
    # Check if it's a sports article
    if contains_sports(title) or contains_sports(description):
        # Skip false positives
        if 'Windows' in title or 'Unix' in title or 'Microsoft' in title or 'IE' in title:
            continue
        if 'GameBoy' in title and 'micro-games' in description:
            continue
        if 'simulation' in description.lower() and 'football' in description.lower():
            # This is about football video game, count as sports
            pass
        
        desc_length = len(description)
        
        sports_articles.append({
            'title': title,
            'article_id': article.get('article_id'),
            'desc_length': desc_length,
            'description_preview': description[:100] + '...' if len(description) > 100 else description
        })
        
        if desc_length > max_desc_length:
            max_desc_length = desc_length
            article_with_longest_desc = {
                'title': title,
                'article_id': article.get('article_id'),
                'desc_length': desc_length
            }

print('__RESULT__:')
print(json.dumps({
    'total_sports_articles_found': len(sports_articles),
    'article_with_longest_description': article_with_longest_desc,
    'sample_sports_articles': sports_articles[:10] if len(sports_articles) > 10 else sports_articles
}))"""

env_args = {'var_functions.query_db:0': [{'_id': '69697811190e2e64cc8a20ea', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69697811190e2e64cc8a20eb', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697811190e2e64cc8a20ec', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697811190e2e64cc8a20ed', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697811190e2e64cc8a20ee', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:5': 'No sports articles found', 'var_functions.query_db:6': [{'_id': '69697811190e2e64cc8a20ea', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69697811190e2e64cc8a20eb', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697811190e2e64cc8a20ec', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697811190e2e64cc8a20ed', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697811190e2e64cc8a20ee', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:8': {'count': 5, 'articles': [{'_id': '69697811190e2e64cc8a20ea', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69697811190e2e64cc8a20eb', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697811190e2e64cc8a20ec', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697811190e2e64cc8a20ed', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697811190e2e64cc8a20ee', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}, 'var_functions.execute_python:10': {'total_articles': 5, 'articles': [{'index': 0, 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description_length': 94, 'first_words': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing..."}, {'index': 1, 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description_length': 214, 'first_words': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation...'}, {'index': 2, 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description_length': 184, 'first_words': 'Reuters - Soaring crude prices plus worries\\about the economy and...'}, {'index': 3, 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description_length': 195, 'first_words': 'Reuters - Authorities have halted oil export\\flows from the main...'}, {'index': 4, 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description_length': 160, 'first_words': 'AFP - Tearaway world oil prices, toppling records and straining...'}]}, 'var_functions.list_db:12': ['authors', 'article_metadata'], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'total_metadata_entries': 127600, 'min_article_id': 0, 'max_article_id': 127599, 'sample_article_ids': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'title': "Why Windows isn't Unix", 'article_id': '183', 'description_length': 708}, 'var_functions.query_db:22': [{'_id': '69697811190e2e64cc8a20f1', 'article_id': '7', 'title': 'Fed minutes show dissent over inflation (USATODAY.com)', 'description': 'USATODAY.com - Retail sales bounced back a bit in July, and new claims for jobless benefits fell last week, the government said Thursday, indicating the economy is improving from a midsummer slump.'}, {'_id': '69697811190e2e64cc8a20fa', 'article_id': '16', 'title': 'Kids Rule for Back-to-School', 'description': 'The purchasing power of kids is a big part of why the back-to-school season has become such a huge marketing phenomenon.'}, {'_id': '69697811190e2e64cc8a2107', 'article_id': '29', 'title': 'Chad seeks refugee aid from IMF', 'description': 'Chad asks the IMF for a loan to pay for looking after more than 100,000 refugees from conflict-torn Darfur in western Sudan.'}, {'_id': '69697811190e2e64cc8a2122', 'article_id': '56', 'title': 'Stoking the Steamroller', 'description': 'No other recording artist can channel American middle-class tastes quite like Chip Davis and his best-selling band'}, {'_id': '69697811190e2e64cc8a212f', 'article_id': '69', 'title': 'Autodesk tackles project collaboration', 'description': 'Autodesk  this week unwrapped an updated version of its hosted project collaboration service targeted at the construction and manufacturing industries. Autodesk Buzzsaw lets multiple, dispersed project participants -- including building owners, developers, architects, construction teams, and facility managers -- share and manage data throughout the life of a project, according to Autodesk officials.'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
