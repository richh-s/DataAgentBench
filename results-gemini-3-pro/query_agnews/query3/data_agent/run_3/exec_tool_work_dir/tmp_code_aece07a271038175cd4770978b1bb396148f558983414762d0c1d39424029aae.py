code = """import json
import re
from collections import Counter

# Load metadata
with open(locals()['var_function-call-7230959688738805590'], 'r') as f:
    metadata_list = json.load(f)

# Load articles
with open(locals()['var_function-call-16295593414804423020'], 'r') as f:
    articles_list = json.load(f)

# Convert articles to a dict for fast lookup
articles_dict = {str(item['article_id']): item for item in articles_list}

# Keywords
business_keywords = {
    'market', 'markets', 'stock', 'stocks', 'trade', 'trading', 'economy', 'economic', 'business', 
    'company', 'companies', 'profit', 'profits', 'bank', 'banks', 'financial', 'finance', 'invest', 
    'investment', 'investor', 'investors', 'fund', 'funds', 'dollar', 'euro', 'yen', 'currency', 
    'oil', 'price', 'prices', 'cost', 'costs', 'rate', 'rates', 'inflation', 'fed', 'federal reserve', 
    'wall st', 'wall street', 'nasdaq', 'dow', 'ipo', 'revenue', 'revenues', 'deal', 'merger', 
    'acquisition', 'ceo', 'cfo', 'manager', 'corporate', 'share', 'shares', 'dividend', 'bond', 
    'bonds', 'debt', 'loan', 'credit', 'budget', 'tax', 'taxes', 'sales', 'retail', 'spending', 
    'growth', 'forecast', 'analyst', 'analysts', 'sector', 'industry'
}
sports_keywords = {
    'sport', 'sports', 'game', 'games', 'team', 'teams', 'match', 'matches', 'cup', 'win', 'wins', 
    'winner', 'loss', 'lost', 'score', 'scores', 'player', 'players', 'coach', 'olympic', 'olympics', 
    'medal', 'football', 'soccer', 'basketball', 'baseball', 'hockey', 'tennis', 'golf', 'race', 
    'racing', 'prix', 'champion', 'championship', 'league', 'tournament', 'athlete', 'athletes', 
    'stadium', 'club', 'nfl', 'nba', 'mlb', 'nhl', 'fifa', 'uefa', 'season', 'playoff', 'final'
}
tech_keywords = {
    'technology', 'tech', 'science', 'computer', 'computers', 'software', 'hardware', 'internet', 
    'web', 'website', 'online', 'digital', 'mobile', 'phone', 'phones', 'cellphone', 'smartphone', 
    'chip', 'chips', 'processor', 'server', 'wireless', 'network', 'networks', 'space', 'nasa', 
    'satellite', 'virus', 'malware', 'microsoft', 'google', 'intel', 'apple', 'linux', 'windows', 
    'gadget', 'device', 'research', 'scientist', 'scientists', 'lab', 'browser', 'search engine', 
    'cyber', 'robot', 'robotics', 'broadband', 'telecom', 'carrier'
}
world_keywords = {
    'world', 'government', 'governments', 'president', 'minister', 'ministers', 'prime minister', 
    'election', 'elections', 'vote', 'voters', 'war', 'wars', 'military', 'army', 'troops', 'soldier', 
    'soldiers', 'police', 'killed', 'kill', 'dead', 'death', 'bomb', 'bombing', 'attack', 'attacks', 
    'blast', 'iraq', 'iraqi', 'iran', 'afghanistan', 'palestin', 'palestinian', 'israel', 'israeli', 
    'un', 'united nations', 'treaty', 'nuclear', 'protest', 'protests', 'court', 'law', 'legal', 
    'crime', 'criminal', 'disaster', 'storm', 'hurricane', 'quake', 'earthquake', 'tsunami', 'flood', 
    'hostage', 'terror', 'terrorism', 'terrorist', 'rebel', 'rebels', 'politic', 'politics', 'party'
}

def classify(title, description):
    text = (title + " " + description).lower()
    # Simple tokenizer
    tokens = re.findall(r'\b\w+\b', text)
    
    counts = {'business': 0, 'sports': 0, 'tech': 0, 'world': 0}
    
    for token in tokens:
        if token in business_keywords: counts['business'] += 1
        if token in sports_keywords: counts['sports'] += 1
        if token in tech_keywords: counts['tech'] += 1
        if token in world_keywords: counts['world'] += 1
        
    # Heuristic adjustments:
    # "Oil" is tricky. If "prices" or "barrel" -> Business. If "pipeline" or "supply" -> Business/World.
    # "Google", "Microsoft" -> Tech usually, but if "ipo" or "shares" -> Business.
    # Let's trust the max count.
    
    # Priority handling for ties or specific phrases could be added, but let's stick to max.
    # If Business ties with others, maybe prefer Business if "stocks" or "market" is present?
    
    best_cat = max(counts, key=counts.get)
    if counts[best_cat] == 0:
        return 'unknown' # Default or unknown
    return best_cat

business_counts_per_year = Counter()
years = range(2010, 2021) # 2010 to 2020 inclusive

for entry in metadata_list:
    aid = str(entry['article_id'])
    pub_date = entry['publication_date']
    year = int(pub_date.split('-')[0])
    
    if aid in articles_dict:
        art = articles_dict[aid]
        cat = classify(art.get('title', ''), art.get('description', ''))
        if cat == 'business':
            business_counts_per_year[year] += 1

# Calculate average
total_business_articles = sum(business_counts_per_year.values())
# We must consider all years 2010-2020.
num_years = 11
average = total_business_articles / num_years

print("__RESULT__:")
print(json.dumps({
    "counts_per_year": dict(business_counts_per_year),
    "total": total_business_articles,
    "average": average
}))"""

env_args = {'var_function-call-7230959688738805590': 'file_storage/function-call-7230959688738805590.json', 'var_function-call-10820393096766796138': {'count': 14860, 'sample_ids': [3, 9, 13, 14, 21, 27, 43, 60, 62, 63], 'file_path_used': 'file_storage/function-call-7230959688738805590.json'}, 'var_function-call-1252885495403344339': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-7038289333483106192': 5, 'var_function-call-15983958513975732915': ['articles'], 'var_function-call-7425021987037564653': [{'_id': '6944c26316c3efdda9fc9184', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944c26316c3efdda9fc918a', 'article_id': '9', 'title': 'Wall St. Bears Claw Back Into the Black', 'description': " NEW YORK (Reuters) - Short-sellers, Wall Street's dwindling  band of ultra-cynics, are seeing green again."}, {'_id': '6944c26316c3efdda9fc918e', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}], 'var_function-call-14402555524284394332': {'min': 3, 'max': 127583, 'count': 14860}, 'var_function-call-16295593414804423020': 'file_storage/function-call-16295593414804423020.json'}

exec(code, env_args)
