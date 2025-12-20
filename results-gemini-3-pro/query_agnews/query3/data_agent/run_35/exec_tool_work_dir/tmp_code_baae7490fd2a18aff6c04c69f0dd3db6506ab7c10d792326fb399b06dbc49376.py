code = """import json
import re

# Load metadata
# Key for metadata file
metadata_key = 'var_function-call-3785327814520365478'
metadata_file = locals()[metadata_key]
with open(metadata_file, 'r') as f:
    metadata_list = json.load(f)

# Create a map of article_id -> year for relevant articles
# Also filter by Europe and date range (already done in SQL, but double checking date doesn't hurt, though SQL is reliable)
article_years = {}
for entry in metadata_list:
    aid = str(entry['article_id'])
    pub_date = entry['publication_date']
    year = int(pub_date.split('-')[0])
    article_years[aid] = year

# Load articles
# Key for articles file
articles_key = 'var_function-call-10461147015258945080'
articles_file = locals()[articles_key]
with open(articles_file, 'r') as f:
    articles_list = json.load(f)

# Keywords
business_keywords = {
    'market', 'markets', 'stock', 'stocks', 'wall street', 'dow', 'nasdaq', 'nyse', 
    'economy', 'economic', 'financial', 'finance', 'business', 'invest', 'investment', 
    'investor', 'bank', 'banks', 'banking', 'interest rate', 'fed', 'federal reserve', 
    'inflation', 'dollar', 'euro', 'currency', 'trade', 'deficit', 'surplus', 'profit', 
    'profits', 'earnings', 'revenue', 'loss', 'losses', 'quarterly', 'share', 'shares', 
    'company', 'companies', 'corp', 'corporation', 'inc', 'merger', 'acquisition', 'deal', 
    'buyout', 'ipo', 'ceo', 'oil', 'crude', 'prices', 'barrel', 'gasoline', 'energy', 'imf', 'wto',
    'bonds', 'treasury', 'yield', 'loan', 'credit', 'mortgage', 'sales', 'retail', 'consumer'
}

scitech_keywords = {
    'technology', 'tech', 'science', 'computer', 'computers', 'software', 'hardware', 
    'internet', 'web', 'online', 'net', 'telecom', 'wireless', 'mobile', 'cellphone', 
    'phone', 'broadband', 'satellite', 'space', 'nasa', 'astronomy', 'biology', 'physics', 
    'research', 'microsoft', 'google', 'apple', 'ibm', 'intel', 'linux', 'windows', 'virus', 
    'hacker', 'spam', 'search engine', 'chip', 'processor', 'digital', 'electronic', 'gadget'
}

sports_keywords = {
    'sport', 'sports', 'baseball', 'basketball', 'football', 'soccer', 'hockey', 'tennis', 
    'golf', 'rugby', 'cricket', 'game', 'games', 'match', 'tournament', 'cup', 'league', 
    'team', 'teams', 'player', 'players', 'coach', 'champion', 'championship', 'olympics', 
    'olympic', 'medal', 'gold', 'score', 'win', 'won', 'loss', 'lost', 'victory', 'defeat', 
    'season', 'nfl', 'nba', 'mlb', 'nhl', 'fifa', 'athlete', 'athletics'
}

world_keywords = {
    'world', 'international', 'politics', 'political', 'government', 'president', 'premier', 
    'minister', 'official', 'officials', 'election', 'vote', 'voters', 'campaign', 'war', 
    'military', 'army', 'troops', 'soldiers', 'peace', 'treaty', 'accord', 'un', 'united nations', 
    'iraq', 'iran', 'palestine', 'israel', 'afghanistan', 'syria', 'attack', 'bomb', 'blast', 
    'kill', 'killed', 'police', 'court', 'trial', 'judge', 'prison', 'protest', 'riot', 'crisis', 
    'disaster', 'parliament', 'senate', 'congress', 'law', 'legal'
}

def classify(text):
    text = text.lower()
    # Simple tokenization
    tokens = set(re.findall(r'\b\w+\b', text))
    
    # Also check for phrases in keywords if any (most are single words in my list, 'wall street', 'interest rate' need care)
    # For simplicity, let's stick to single words or simple checking
    
    scores = {'Business': 0, 'Sci/Tech': 0, 'Sports': 0, 'World': 0}
    
    # Check Business
    for kw in business_keywords:
        if kw in text: # simple substring check for phrases like "wall street"
            scores['Business'] += 1
            
    # Check Sci/Tech
    for kw in scitech_keywords:
        if kw in text:
            scores['Sci/Tech'] += 1
            
    # Check Sports
    for kw in sports_keywords:
        if kw in text:
            scores['Sports'] += 1
            
    # Check World
    for kw in world_keywords:
        if kw in text:
            scores['World'] += 1
            
    # Determine max
    max_cat = max(scores, key=scores.get)
    if scores[max_cat] == 0:
        return 'Unknown' # or default?
    return max_cat

# Count business articles per year
yearly_counts = {y: 0 for y in range(2010, 2021)}

for article in articles_list:
    aid = str(article['article_id'])
    if aid in article_years:
        year = article_years[aid]
        # Combine title and description
        text = (article.get('title', '') + " " + article.get('description', ''))
        category = classify(text)
        if category == 'Business':
            yearly_counts[year] += 1

# Calculate average
total_business = sum(yearly_counts.values())
num_years = 11 # 2010 to 2020 inclusive
average = total_business / num_years

result = {
    "yearly_counts": yearly_counts,
    "average": average
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-3785327814520365478': 'file_storage/function-call-3785327814520365478.json', 'var_function-call-10425828837385434801': 14860, 'var_function-call-14030611635613635526': ['articles'], 'var_function-call-14105563126826159578': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-8122656162104347158': 5, 'var_function-call-10461147015258945080': 'file_storage/function-call-10461147015258945080.json'}

exec(code, env_args)
