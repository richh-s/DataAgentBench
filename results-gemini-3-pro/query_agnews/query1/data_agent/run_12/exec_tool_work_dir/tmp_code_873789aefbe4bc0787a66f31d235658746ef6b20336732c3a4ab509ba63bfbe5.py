code = """import json
import re

# Load the data
file_path = locals()['var_function-call-3474523854322095635']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Define keywords
sports_keywords = {
    'sport', 'sports', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'hockey', 'cricket', 'rugby', 
    'olympic', 'olympics', 'medal', 'gold', 'silver', 'bronze', 'athlete', 'athletes', 'coach', 'team', 'teams', 
    'league', 'cup', 'championship', 'tournament', 'game', 'match', 'score', 'scores', 'win', 'won', 'loss', 'lost', 
    'victory', 'defeat', 'player', 'players', 'quarterback', 'pitcher', 'batter', 'touchdown', 'goal', 'basket', 
    'nfl', 'nba', 'mlb', 'nhl', 'fifa', 'uefa', 'wimbledon', 'grand slam', 'world cup', 'super bowl', 'playoff', 
    'race', 'racing', 'f1', 'formula one', 'nascar', 'driver', 'marathon', 'sprint', 'relay', 'swimming', 'gymnastics',
    'boxing', 'wrestling', 'stadium', 'arena', 'athens', 'greece' # Athens 2004 Olympics might be in the dataset given the dates 2004
}

business_keywords = {
    'business', 'market', 'markets', 'stock', 'stocks', 'share', 'shares', 'economy', 'economic', 'finance', 'financial',
    'invest', 'investment', 'investor', 'bank', 'banks', 'dollar', 'euro', 'yen', 'currency', 'oil', 'price', 'prices',
    'profit', 'loss', 'quarter', 'revenue', 'earnings', 'ipo', 'merger', 'acquisition', 'deal', 'company', 'companies',
    'corp', 'inc', 'ltd', 'ceo', 'cfo', 'fed', 'federal reserve', 'rates', 'inflation', 'trade', 'deficit', 'surplus',
    'wall st', 'wall street', 'dow', 'nasdaq', 's&p', 'bond', 'bonds', 'reuters'
}

scitech_keywords = {
    'science', 'technology', 'tech', 'computer', 'computers', 'software', 'hardware', 'internet', 'web', 'online',
    'google', 'microsoft', 'apple', 'ibm', 'intel', 'linux', 'windows', 'virus', 'worm', 'security', 'hacker',
    'space', 'nasa', 'shuttle', 'mars', 'moon', 'orbit', 'astronomy', 'biology', 'physics', 'chemistry', 'research',
    'study', 'scientist', 'scientists', 'lab', 'laboratory', 'cell', 'gene', 'genome', 'medical', 'medicine', 'drug',
    'cancer', 'disease', 'health', 'mobile', 'phone', 'wireless', 'broadband', 'chip', 'processor', 'spam', 'search engine'
}

world_keywords = {
    'world', 'international', 'politics', 'government', 'president', 'prime minister', 'minister', 'official',
    'election', 'vote', 'voters', 'campaign', 'candidate', 'war', 'peace', 'military', 'army', 'troops', 'soldier',
    'soldiers', 'iraq', 'iran', 'afghanistan', 'israel', 'palestine', 'china', 'russia', 'usa', 'un', 'united nations',
    'treaty', 'agreement', 'nuclear', 'bomb', 'blast', 'explosion', 'attack', 'terror', 'terrorist', 'terrorism',
    'rebel', 'rebels', 'police', 'court', 'trial', 'judge', 'law', 'legal', 'congress', 'senate', 'parliament',
    'baghdad', 'korea', 'darfur', 'sudan', 'gaza'
}

def classify(text):
    text = text.lower()
    # Simple tokenization
    tokens = set(re.findall(r'\b\w+\b', text))
    
    scores = {
        'Sports': len(tokens.intersection(sports_keywords)),
        'Business': len(tokens.intersection(business_keywords)),
        'Sci/Tech': len(tokens.intersection(scitech_keywords)),
        'World': len(tokens.intersection(world_keywords))
    }
    
    # Logic to handle ties or zeros
    # If all zero, default to 'World' or handle?
    if sum(scores.values()) == 0:
        return None
    
    return max(scores, key=scores.get)

sports_articles = []
for art in articles:
    content = (art.get('title', '') + " " + art.get('description', ''))
    category = classify(content)
    if category == 'Sports':
        sports_articles.append(art)

# Find the one with max description length
max_len = -1
target_article = None

for art in sports_articles:
    desc = art.get('description', '')
    if len(desc) > max_len:
        max_len = len(desc)
        target_article = art

print("__RESULT__:")
if target_article:
    print(json.dumps({"title": target_article['title'], "len": max_len, "desc": target_article['description']}))
else:
    print(json.dumps({"error": "No sports articles found"}))"""

env_args = {'var_function-call-14460016368639222028': ['articles'], 'var_function-call-14460016368639224981': ['authors', 'article_metadata'], 'var_function-call-14109477459473775675': [{'_id': '69446beedd796e99613ec2ac', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69446beedd796e99613ec2ad', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69446beedd796e99613ec2ae', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69446beedd796e99613ec2af', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69446beedd796e99613ec2b0', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-14109477459473772956': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'author_id': '992', 'region': 'North America', 'publication_date': '2004-03-20'}, {'article_id': '2', 'author_id': '820', 'region': 'South America', 'publication_date': '2021-02-04'}, {'article_id': '3', 'author_id': '478', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '4', 'author_id': '39', 'region': 'Africa', 'publication_date': '2012-02-01'}], 'var_function-call-12709903721171023210': [{'_id': '69446beedd796e99613ec2ac', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69446beedd796e99613ec2ad', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69446beedd796e99613ec2ae', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69446beedd796e99613ec2af', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69446beedd796e99613ec2b0', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-11205666105338504994': [{'_id': '69446beedd796e99613ec2ac', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69446beedd796e99613ec2ad', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69446beedd796e99613ec2ae', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69446beedd796e99613ec2af', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69446beedd796e99613ec2b0', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-14554890964508606111': 5, 'var_function-call-3474523854322095635': 'file_storage/function-call-3474523854322095635.json'}

exec(code, env_args)
