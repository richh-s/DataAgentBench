code = """import json
import re

# Load metadata
with open(locals()['var_function-call-517009556635827832'], 'r') as f:
    metadata_list = json.load(f)

# Create a map of article_id -> region for 2015 articles
article_region_map = {str(m['article_id']): m['region'] for m in metadata_list}

# Load articles
with open(locals()['var_function-call-9785334966898514267'], 'r') as f:
    articles_list = json.load(f)

# Keywords
categories = {
    "World": ['war', 'peace', 'election', 'minister', 'president', 'government', 'military', 'army', 'troops', 'rebel', 'attack', 'bomb', 'blast', 'kill', 'dead', 'injured', 'crash', 'police', 'protest', 'riot', 'crisis', 'nuclear', 'weapon', 'treaty', 'agreement', 'talks', 'summit', 'united nations', 'un', 'nato', 'eu', 'european union', 'parliament', 'court', 'trial', 'judge', 'prison', 'jail', 'rights', 'human rights', 'refugee', 'migrant', 'border', 'security', 'terror', 'terrorism', 'iraq', 'iran', 'syria', 'afghanistan', 'pakistan', 'india', 'china', 'russia', 'ukraine', 'israel', 'palestine', 'gaza', 'egypt', 'libya', 'africa', 'asia', 'europe', 'latin america', 'south america', 'north america', 'australia'],
    "Sports": ['sport', 'game', 'match', 'cup', 'league', 'team', 'club', 'player', 'coach', 'manager', 'win', 'lose', 'draw', 'score', 'goal', 'point', 'run', 'basket', 'touchdown', 'medal', 'champion', 'championship', 'tournament', 'olympic', 'olympics', 'fifa', 'uefa', 'nfl', 'nba', 'mlb', 'nhl', 'ncaa', 'football', 'soccer', 'basketball', 'baseball', 'hockey', 'tennis', 'golf', 'cricket', 'rugby', 'racing', 'f1', 'nascar', 'boxing', 'wrestling', 'athlete', 'stadium'],
    "Business": ['business', 'company', 'corporation', 'corp', 'inc', 'firm', 'industry', 'market', 'stock', 'share', 'trade', 'exchange', 'wall street', 'dow jones', 'nasdaq', 'price', 'cost', 'profit', 'loss', 'revenue', 'earning', 'dividend', 'bank', 'finance', 'financial', 'economy', 'economic', 'currency', 'dollar', 'euro', 'yen', 'oil', 'gas', 'energy', 'invest', 'investment', 'investor', 'merger', 'acquisition', 'deal', 'contract', 'sales', 'retail', 'consumer', 'ceo', 'cfo', 'chairman', 'job', 'unemployment', 'rate', 'tax', 'budget', 'debt'],
    "Sci/Tech": ['science', 'technology', 'tech', 'computer', 'computing', 'software', 'hardware', 'internet', 'web', 'online', 'digital', 'mobile', 'phone', 'smartphone', 'tablet', 'app', 'application', 'network', 'wireless', 'wifi', 'data', 'server', 'cloud', 'cyber', 'virus', 'hacker', 'security', 'space', 'nasa', 'astronomy', 'universe', 'planet', 'mars', 'moon', 'robot', 'robotics', 'ai', 'artificial intelligence', 'google', 'microsoft', 'apple', 'amazon', 'facebook', 'twitter', 'intel', 'ibm', 'chip', 'processor', 'research', 'study', 'experiment', 'biology', 'physics', 'chemistry', 'medicine', 'medical', 'drug', 'health', 'disease']
}

region_counts = {}

def classify(text):
    text = text.lower()
    scores = {cat: 0 for cat in categories}
    for cat, keywords in categories.items():
        for word in keywords:
            # Simple substring match might be too noisy, lets try word boundary
            if re.search(r'\b' + re.escape(word) + r'\b', text):
                scores[cat] += 1
    
    # Heuristic: if max score is 0, classify as World? Or Unknown.
    # The prompt implies all belong to one.
    if max(scores.values()) == 0:
        return "Unknown"
    
    return max(scores, key=scores.get)

count_world = 0
debug_samples = []

for article in articles_list:
    aid = str(article['article_id'])
    if aid in article_region_map:
        text = (article.get('title', '') + " " + article.get('description', '')).strip()
        category = classify(text)
        region = article_region_map[aid]
        
        if category == 'World':
            region_counts[region] = region_counts.get(region, 0) + 1
            if len(debug_samples) < 5:
                debug_samples.append((text[:50], region))

print("__RESULT__:")
print(json.dumps(region_counts))
print("DEBUG:", debug_samples)"""

env_args = {'var_function-call-517009556635827832': 'file_storage/function-call-517009556635827832.json', 'var_function-call-5428732152861875432': 6696, 'var_function-call-2587877961923239291': 'file_storage/function-call-2587877961923239291.json', 'var_function-call-9785334966898514267': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
