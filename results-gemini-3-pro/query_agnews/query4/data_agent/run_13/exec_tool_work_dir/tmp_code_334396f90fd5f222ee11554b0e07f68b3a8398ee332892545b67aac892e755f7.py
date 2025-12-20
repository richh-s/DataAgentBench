code = """import json
import re

# Load metadata
with open(locals()['var_function-call-517009556635827832'], 'r') as f:
    metadata_list = json.load(f)

article_region_map = {str(m['article_id']): m['region'] for m in metadata_list}

# Load articles
with open(locals()['var_function-call-815964868435706632'], 'r') as f:
    articles_list = json.load(f)

# Enhanced Keywords
world_keywords = [
    'war', 'peace', 'conflict', 'military', 'army', 'navy', 'air force', 'troops', 'soldier', 'rebel', 'militia', 'guerrilla', 'terror', 'terrorism', 'terrorist', 'bomb', 'blast', 'explosion', 'suicide', 'attack', 'kill', 'dead', 'death', 'injured', 'wound', 'casualty', 'hostage', 'kidnap', 'abduct',
    'president', 'prime minister', 'premier', 'chancellor', 'king', 'queen', 'prince', 'leader', 'official', 'spokesman', 'ambassador', 'diplomat', 'envoy', 'minister', 'secretary', 'senator', 'congressman', 'parliament', 'senate', 'congress', 'legislature', 'cabinet', 'government', 'administration', 'regime', 'authority',
    'election', 'vote', 'poll', 'ballot', 'campaign', 'candidate', 'voter', 'party', 'democrat', 'republican', 'conservative', 'liberal', 'socialist', 'communist',
    'united nations', 'un', 'un ', 'nato', 'eu', 'european union', 'asean', 'au', 'african union', 'imf', 'world bank', 'wto', 'who', 'red cross', 'ngo',
    'treaty', 'agreement', 'accord', 'deal', 'pact', 'truce', 'ceasefire', 'negotiation', 'talks', 'summit', 'conference', 'meeting',
    'court', 'trial', 'judge', 'jury', 'verdict', 'sentence', 'prison', 'jail', 'inmate', 'law', 'legal', 'legislation', 'bill', 'rights', 'human rights', 'justice',
    'police', 'officer', 'arrest', 'detain', 'suspect', 'investigation', 'probe', 'security', 'border', 'patrol', 'refugee', 'migrant', 'immigration', 'asylum',
    'crisis', 'disaster', 'emergency', 'aid', 'relief', 'rescue', 'hurricane', 'typhoon', 'earthquake', 'tsunami', 'flood', 'famine', 'drought',
    'nuclear', 'atomic', 'weapon', 'arms', 'missile', 'rocket', 'gun', 'fire', 'shoot',
    'protest', 'demonstration', 'rally', 'march', 'riot', 'clash', 'strike', 'unrest',
    'iraq', 'baghdad', 'iran', 'tehran', 'syria', 'damascus', 'israel', 'jerusalem', 'tel aviv', 'palestine', 'gaza', 'west bank', 'afghanistan', 'kabul', 'pakistan', 'islamabad', 'india', 'delhi', 'kashmir', 'china', 'beijing', 'russia', 'moscow', 'ukraine', 'kiev', 'crimea', 'chechnya', 'north korea', 'pyongyang', 'south korea', 'seoul', 'japan', 'tokyo', 'egypt', 'cairo', 'libya', 'tripoli', 'sudan', 'darfur', 'chad', 'nigeria', 'kenya', 'somalia', 'zimbabwe', 'south africa', 'venezuela', 'colombia', 'cuba', 'haiti', 'mexico', 'brazil', 'argentina', 'chile', 'peru', 'bolivia', 'turkey', 'cyprus', 'greece', 'balkans', 'serbia', 'bosnia', 'kosovo', 'france', 'germany', 'uk', 'britain', 'london', 'spain', 'italy', 'vatican', 'canada', 'australia', 'indonesia', 'malaysia', 'thailand', 'philippines', 'vietnam', 'myanmar', 'burma'
]

sports_keywords = [
    'sport', 'sports', 'game', 'match', 'tournament', 'championship', 'champion', 'cup', 'league', 'series', 'season', 'playoff', 'final', 'semifinal', 'quarterfinal',
    'team', 'club', 'squad', 'roster', 'player', 'athlete', 'coach', 'manager', 'referee', 'umpire',
    'win', 'won', 'winner', 'victory', 'lose', 'lost', 'loss', 'defeat', 'draw', 'tie', 'score', 'goal', 'point', 'run', 'touchdown', 'basket', 'medal', 'gold', 'silver', 'bronze', 'record',
    'olympic', 'olympics', 'athens', 'beijing', 'london',
    'football', 'soccer', 'fifa', 'uefa', 'world cup', 'premier league', 'bundesliga', 'la liga', 'serie a',
    'basketball', 'nba', 'fiba', 'baseball', 'mlb', 'world series', 'hockey', 'nhl', 'stanley cup',
    'tennis', 'wimbledon', 'open', 'grand slam', 'davis cup', 'golf', 'pga', 'masters', 'ryder cup', 'tiger woods',
    'cricket', 'rugby', 'boxing', 'wrestling', 'wwe', 'racing', 'f1', 'formula one', 'nascar', 'driver', 'grand prix', 'cycling', 'tour de france', 'doping', 'steroid',
    'stadium', 'arena', 'field', 'court'
]

business_keywords = [
    'business', 'economy', 'economic', 'finance', 'financial', 'market', 'stock', 'share', 'equity', 'bond', 'derivative', 'option', 'future', 'fund', 'mutual fund', 'hedge fund',
    'bank', 'banking', 'central bank', 'federal reserve', 'fed', 'interest rate', 'rate', 'loan', 'mortgage', 'credit', 'debt', 'default', 'bankruptcy',
    'company', 'corporation', 'corp', 'inc', 'ltd', 'firm', 'enterprise', 'startup', 'subsidiary', 'branch', 'headquarters',
    'industry', 'sector', 'manufacturing', 'retail', 'service', 'automotive', 'airline', 'telecom', 'utility',
    'trade', 'commerce', 'export', 'import', 'tariff', 'quota', 'deficit', 'surplus',
    'price', 'cost', 'value', 'revenue', 'sales', 'profit', 'earnings', 'loss', 'dividend', 'yield', 'margin',
    'invest', 'investment', 'investor', 'shareholder', 'stake', 'buy', 'sell', 'trading', 'exchange', 'wall street', 'nyse', 'nasdaq', 'dow', 's&p', 'ftse', 'nikkei',
    'deal', 'merger', 'acquisition', 'takeover', 'bid', 'offer', 'contract', 'agreement', 'partnership', 'joint venture',
    'ceo', 'cfo', 'coo', 'executive', 'chairman', 'president', 'director', 'manager', 'boss',
    'job', 'employment', 'unemployment', 'hiring', 'layoff', 'cut', 'wage', 'salary', 'bonus', 'pension', 'strike', 'union',
    'tax', 'taxation', 'budget', 'spending', 'fiscal', 'monetary', 'inflation', 'deflation', 'recession', 'depression', 'recovery', 'growth', 'gdp',
    'oil', 'gas', 'petroleum', 'energy', 'crude', 'barrel', 'opec', 'pipeline', 'refinery'
]

scitech_keywords = [
    'science', 'scientific', 'scientist', 'research', 'researcher', 'study', 'experiment', 'lab', 'laboratory', 'discovery', 'invention', 'innovation',
    'technology', 'tech', 'high-tech', 'engineering', 'engineer',
    'computer', 'computing', 'pc', 'laptop', 'desktop', 'server', 'mainframe', 'supercomputer', 'hardware', 'processor', 'chip', 'semiconductor', 'intel', 'amd',
    'software', 'program', 'application', 'app', 'code', 'coding', 'developer', 'programmer', 'algorithm', 'os', 'operating system', 'windows', 'linux', 'unix', 'mac', 'microsoft', 'oracle', 'sap',
    'internet', 'web', 'www', 'online', 'cyber', 'digital', 'virtual', 'network', 'wireless', 'wifi', 'broadband', 'dsl', 'modem', 'router', 'cloud',
    'mobile', 'phone', 'cellphone', 'smartphone', 'handset', 'tablet', 'nokia', 'motorola', 'samsung', 'apple', 'iphone', 'ipod', 'blackberry',
    'google', 'yahoo', 'search engine', 'email', 'spam', 'virus', 'worm', 'trojan', 'hacker', 'security', 'encryption', 'privacy',
    'space', 'nasa', 'esa', 'astronaut', 'satellite', 'rocket', 'launch', 'orbit', 'mission', 'shuttle', 'station', 'iss', 'mars', 'moon', 'planet', 'star', 'galaxy', 'universe', 'telescope', 'astronomy',
    'biology', 'biological', 'genetics', 'gene', 'dna', 'genome', 'stem cell', 'cloning', 'biotech', 'medicine', 'medical', 'drug', 'pharmaceutical', 'pharma', 'vaccine', 'virus', 'disease', 'cancer', 'aids', 'hiv', 'flu', 'health', 'hospital', 'doctor', 'patient',
    'physics', 'physicist', 'chemistry', 'chemist', 'climate', 'warming', 'environment', 'pollution', 'emissions'
]

categories = {
    "World": world_keywords,
    "Sports": sports_keywords,
    "Business": business_keywords,
    "Sci/Tech": scitech_keywords
}

region_counts = {}

def classify(text):
    text = text.lower()
    # Replace non-alphanumeric with space to help tokenization
    text = re.sub(r'[^a-z0-9]', ' ', text)
    tokens = set(text.split())
    
    scores = {cat: 0 for cat in categories}
    for cat, keywords in categories.items():
        for word in keywords:
            # Check for exact word match
            if word in tokens:
                scores[cat] += 1
            # For multi-word keywords (uncommon in my list except organizations)
            elif ' ' in word and word in text:
                scores[cat] += 1
                
    if max(scores.values()) == 0:
        return "Unknown"
    
    return max(scores, key=scores.get)

for article in articles_list:
    aid = str(article['article_id'])
    if aid in article_region_map:
        text = (article.get('title', '') + " " + article.get('description', '')).strip()
        category = classify(text)
        region = article_region_map[aid]
        
        if category == 'World':
            region_counts[region] = region_counts.get(region, 0) + 1

print("__RESULT__:")
print(json.dumps(region_counts))"""

env_args = {'var_function-call-517009556635827832': 'file_storage/function-call-517009556635827832.json', 'var_function-call-5428732152861875432': 6696, 'var_function-call-2587877961923239291': 'file_storage/function-call-2587877961923239291.json', 'var_function-call-9785334966898514267': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-815964868435706632': 'file_storage/function-call-815964868435706632.json', 'var_function-call-9731091633143192176': {'Asia': 470, 'South America': 475, 'Europe': 456, 'North America': 450, 'Africa': 462}}

exec(code, env_args)
