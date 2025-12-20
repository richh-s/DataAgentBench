code = """import json
import collections

# Load metadata
# Key for metadata file: var_function-call-16217748514118301059
# Wait, I need to check if I need to reload it or if it is still available.
# In the system, I can access previous results.
# But I should probably use the file path provided in the first step.
meta_file = locals()['var_function-call-16217748514118301059']
with open(meta_file, 'r') as f:
    metadata_list = json.load(f)

# Load articles
# Key for articles file: var_function-call-3496579977064904121
articles_file = locals()['var_function-call-3496579977064904121']
with open(articles_file, 'r') as f:
    articles_list = json.load(f)

# Create a dictionary for articles for fast lookup
articles_dict = {a['article_id']: a for a in articles_list}

# Keywords (heuristic)
# I will use sets for faster lookup
keywords = {
    'World': {'world', 'war', 'iraq', 'iran', 'syria', 'israel', 'palestine', 'president', 'minister', 'government', 'military', 'attack', 'bomb', 'peace', 'treaty', 'foreign', 'international', 'un', 'nato', 'eu', 'europe', 'china', 'russia', 'ukraine', 'korea', 'afghanistan', 'pakistan', 'protest', 'kill', 'dead', 'crash', 'hostage', 'refugee', 'terror', 'isis', 'al-qaeda', 'boko', 'haram', 'election', 'politic', 'parliament', 'senate', 'congress', 'law', 'legal', 'court', 'judge', 'prison', 'jail', 'police', 'crime', 'murder'},
    'Sports': {'sport', 'game', 'match', 'score', 'team', 'player', 'win', 'won', 'loss', 'lost', 'beat', 'cup', 'league', 'season', 'coach', 'olympic', 'football', 'soccer', 'baseball', 'basketball', 'tennis', 'cricket', 'golf', 'race', 'racing', 'champion', 'championship', 'medal', 'athlete', 'tournament', 'stadium', 'club', 'nfl', 'nba', 'mlb', 'nhl', 'fifa', 'uefa'},
    'Business': {'business', 'market', 'stock', 'share', 'price', 'company', 'corp', 'inc', 'profit', 'loss', 'earn', 'bank', 'economy', 'economic', 'trade', 'dollar', 'euro', 'yen', 'currency', 'oil', 'gas', 'energy', 'merger', 'acquisition', 'deal', 'ceo', 'cfo', 'executive', 'industry', 'finance', 'financial', 'tax', 'invest', 'investment', 'fund', 'wall', 'street', 'dow', 'nasdaq', 'inflation', 'rate', 'fed', 'federal', 'reserve'},
    'Sci/Tech': {'science', 'technology', 'tech', 'computer', 'software', 'hardware', 'internet', 'web', 'online', 'google', 'apple', 'microsoft', 'facebook', 'twitter', 'amazon', 'nasa', 'space', 'astronomy', 'planet', 'mars', 'moon', 'study', 'research', 'discovery', 'biology', 'physics', 'chemistry', 'medical', 'medicine', 'health', 'virus', 'disease', 'cancer', 'drug', 'phone', 'mobile', 'smartphone', 'app', 'device', 'robot', 'ai', 'artificial', 'intelligence', 'cyber', 'hacker', 'digital'}
}

def classify(text):
    text = text.lower()
    scores = {cat: 0 for cat in keywords}
    words = text.split() # Simple tokenization
    # Remove punctuation
    words = [''.join(c for c in w if c.isalnum()) for w in words]
    
    for word in words:
        for cat, kws in keywords.items():
            if word in kws:
                scores[cat] += 1
                
    # Prioritize categories if needed, but max score is standard
    # If tie, maybe look at specific strong keywords?
    # Let's just take max.
    best_cat = max(scores, key=scores.get)
    if scores[best_cat] == 0:
        return 'World' # Default fallback if nothing matches (news is often world/local)
    return best_cat

# Process
world_counts = collections.Counter()

for item in metadata_list:
    aid = str(item['article_id']) # Ensure string
    if aid in articles_dict:
        art = articles_dict[aid]
        # Combine title and description
        text = (art.get('title', '') + ' ' + art.get('description', ''))
        category = classify(text)
        
        if category == 'World':
            world_counts[item['region']] += 1

# Find max
if world_counts:
    top_region = world_counts.most_common(1)[0]
    result = {"region": top_region[0], "count": top_region[1]}
else:
    result = {"region": None, "count": 0}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-16217748514118301059': 'file_storage/function-call-16217748514118301059.json', 'var_function-call-15270387655535073245': 6696, 'var_function-call-17504268953086342137': [{'_id': '6944e84deb7dfcfa920beb63', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944e84deb7dfcfa920beb64', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944e84deb7dfcfa920beb65', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944e84deb7dfcfa920beb66', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944e84deb7dfcfa920beb67', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-7651061946173546542': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-17293771532660502536': 127570, 'var_function-call-3496579977064904121': 'file_storage/function-call-3496579977064904121.json'}

exec(code, env_args)
