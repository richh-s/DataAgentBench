code = """import json
import re

# Load metadata
metadata_key = 'var_function-call-3785327814520365478'
metadata_file = locals()[metadata_key]
with open(metadata_file, 'r') as f:
    metadata_list = json.load(f)

article_years = {}
for entry in metadata_list:
    aid = str(entry['article_id'])
    pub_date = entry['publication_date']
    year = int(pub_date.split('-')[0])
    article_years[aid] = year

# Load articles
articles_key = 'var_function-call-10461147015258945080'
articles_file = locals()[articles_key]
with open(articles_file, 'r') as f:
    articles_list = json.load(f)

# Keywords
business_keywords = [
    'market', 'markets', 'stock', 'stocks', 'wall street', 'dow', 'nasdaq', 'nyse', 
    'economy', 'economic', 'financial', 'finance', 'business', 'invest', 'investment', 
    'investor', 'bank', 'banks', 'banking', 'interest rate', 'fed', 'federal reserve', 
    'inflation', 'dollar', 'euro', 'currency', 'trade', 'deficit', 'surplus', 'profit', 
    'profits', 'earnings', 'revenue', 'loss', 'losses', 'quarterly', 'share', 'shares', 
    'company', 'companies', 'corp', 'corporation', 'inc', 'merger', 'acquisition', 'deal', 
    'buyout', 'ipo', 'ceo', 'oil', 'crude', 'prices', 'barrel', 'gasoline', 'energy', 'imf', 'wto',
    'bonds', 'treasury', 'yield', 'loan', 'credit', 'mortgage', 'sales', 'retail', 'consumer'
]

scitech_keywords = [
    'technology', 'tech', 'science', 'computer', 'computers', 'software', 'hardware', 
    'internet', 'web', 'online', 'net', 'telecom', 'wireless', 'mobile', 'cellphone', 
    'phone', 'broadband', 'satellite', 'space', 'nasa', 'astronomy', 'biology', 'physics', 
    'research', 'microsoft', 'google', 'apple', 'ibm', 'intel', 'linux', 'windows', 'virus', 
    'hacker', 'spam', 'search engine', 'chip', 'processor', 'digital', 'electronic', 'gadget'
]

sports_keywords = [
    'sport', 'sports', 'baseball', 'basketball', 'football', 'soccer', 'hockey', 'tennis', 
    'golf', 'rugby', 'cricket', 'game', 'games', 'match', 'tournament', 'cup', 'league', 
    'team', 'teams', 'player', 'players', 'coach', 'champion', 'championship', 'olympics', 
    'olympic', 'medal', 'gold', 'score', 'win', 'won', 'loss', 'lost', 'victory', 'defeat', 
    'season', 'nfl', 'nba', 'mlb', 'nhl', 'fifa', 'athlete', 'athletics'
]

world_keywords = [
    'world', 'international', 'politics', 'political', 'government', 'president', 'premier', 
    'minister', 'official', 'officials', 'election', 'vote', 'voters', 'campaign', 'war', 
    'military', 'army', 'troops', 'soldiers', 'peace', 'treaty', 'accord', 'un', 'united nations', 
    'iraq', 'iran', 'palestine', 'israel', 'afghanistan', 'syria', 'attack', 'bomb', 'blast', 
    'kill', 'killed', 'police', 'court', 'trial', 'judge', 'prison', 'protest', 'riot', 'crisis', 
    'disaster', 'parliament', 'senate', 'congress', 'law', 'legal'
]

def count_keywords(text, keywords):
    count = 0
    # Prepare text
    text_lower = text.lower()
    for kw in keywords:
        # Check if kw is a phrase (contains space)
        if ' ' in kw:
            if kw in text_lower:
                count += 1
        else:
            # Check distinct word
            # Regex \bkw\b
            if re.search(r'\b' + re.escape(kw) + r'\b', text_lower):
                count += 1
    return count

# Count business articles per year
yearly_counts = {y: 0 for y in range(2010, 2021)}

for article in articles_list:
    aid = str(article['article_id'])
    if aid in article_years:
        year = article_years[aid]
        # Combine title and description
        text = (article.get('title', '') + " " + article.get('description', ''))
        
        c_bus = count_keywords(text, business_keywords)
        c_sci = count_keywords(text, scitech_keywords)
        c_spo = count_keywords(text, sports_keywords)
        c_wor = count_keywords(text, world_keywords)
        
        scores = {'Business': c_bus, 'Sci/Tech': c_sci, 'Sports': c_spo, 'World': c_wor}
        
        max_score = max(scores.values())
        if max_score > 0:
            # Get categories with max score
            top_cats = [k for k, v in scores.items() if v == max_score]
            # Tie breaking? 
            # If 'Business' is in top_cats, we can count it, or prioritize?
            # Standard classifiers usually just pick one.
            # If it's ambiguous, maybe look at title keywords?
            # For this exercise, let's say if it's tied, we pick the first one in a priority list or just Business if present.
            # Let's check if Business is the unique winner or tied.
            
            # Simple tie break: Business > World > Sci/Tech > Sports (arbitrary but Business is target)
            # Actually, "Google IPO" has Google (Tech) and IPO (Business). Usually categorized as Business.
            # "Microsoft earnings" -> Tech + Business -> Business.
            # So if Business is tied with Tech, it's often Business.
            if 'Business' in top_cats:
                category = 'Business'
            else:
                category = top_cats[0]
                
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

env_args = {'var_function-call-3785327814520365478': 'file_storage/function-call-3785327814520365478.json', 'var_function-call-10425828837385434801': 14860, 'var_function-call-14030611635613635526': ['articles'], 'var_function-call-14105563126826159578': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-8122656162104347158': 5, 'var_function-call-10461147015258945080': 'file_storage/function-call-10461147015258945080.json', 'var_function-call-16342635927272023977': {'yearly_counts': {'2010': 50, '2011': 68, '2012': 47, '2013': 61, '2014': 59, '2015': 55, '2016': 63, '2017': 62, '2018': 73, '2019': 51, '2020': 64}, 'average': 59.36363636363637}}

exec(code, env_args)
