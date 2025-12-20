code = """import json
import re

# Load metadata
with open(locals()['var_function-call-13727892763181911756'], 'r') as f:
    metadata_list = json.load(f)

# Load articles
with open(locals()['var_function-call-17115613930582186539'], 'r') as f:
    articles_list = json.load(f)

# Create meta_map: article_id (str) -> year (int)
meta_map = {}
for item in metadata_list:
    aid = str(item['article_id'])
    y = int(item['publication_date'][:4])
    meta_map[aid] = y

# Intersection check
article_ids_in_db = set(str(a['article_id']) for a in articles_list)
meta_ids = set(meta_map.keys())
intersection = meta_ids.intersection(article_ids_in_db)
print(f"Intersection count: {len(intersection)}")

# Define keywords
keywords = {
    "Business": [
        'business', 'market', 'stock', 'trade', 'economy', 'financial', 'finance', 'invest', 
        'bank', 'profit', 'company', 'corp', 'money', 'price', 'oil', 'dollar', 'euro', 
        'gold', 'sale', 'deal', 'revenue', 'earning', 'share', 'cost', 'bid', 'merger', 
        'acquire', 'acquisition', 'growth', 'fund', 'inflation', 'rate', 'budget', 'deficit', 
        'ceo', 'cfo', 'executive', 'manager', 'industry', 'sector', 'wall street', 'nasdaq', 
        'dow', 's&p', 'ltd', 'inc', 'commodity', 'treasury', 'fed', 'federal reserve', 'imf', 'wto'
    ],
    "Sports": [
        'sport', 'game', 'team', 'cup', 'player', 'match', 'win', 'loss', 'score', 'season', 
        'league', 'club', 'champion', 'olympic', 'medal', 'coach', 'athlete', 'football', 
        'soccer', 'basketball', 'baseball', 'tennis', 'hockey', 'golf', 'race', 'racing', 
        'final', 'round', 'stadium', 'tournament', 'f1', 'nfl', 'nba', 'mlb', 'nhl', 'rugby', 
        'cricket', 'victory', 'defeat', 'title', 'standings'
    ],
    "SciTech": [
        'technology', 'tech', 'science', 'computer', 'software', 'internet', 'web', 'online', 
        'phone', 'mobile', 'chip', 'processor', 'microsoft', 'google', 'apple', 'ibm', 'intel', 
        'linux', 'virus', 'security', 'space', 'nasa', 'orbit', 'launch', 'moon', 'research', 
        'study', 'drug', 'cancer', 'health', 'biology', 'physics', 'server', 'network', 
        'wireless', 'satellite', 'robot', 'astronomy', 'genetics', 'browser', 'spam', 'hacker'
    ],
    "World": [
        'world', 'government', 'president', 'minister', 'prime', 'official', 'state', 'country', 
        'nation', 'police', 'military', 'army', 'war', 'troop', 'iraq', 'iran', 'afghanistan', 
        'palestinian', 'israel', 'china', 'russia', 'bomb', 'blast', 'attack', 'kill', 'die', 
        'dead', 'storm', 'hurricane', 'quake', 'flood', 'election', 'vote', 'poll', 'party', 
        'un', 'united nations', 'treaty', 'talks', 'peace', 'court', 'trial', 'judge', 'prison', 
        'protest', 'strike', 'terror', 'korea', 'nuclear', 'politics'
    ]
}

yearly_counts = {y: 0 for y in range(2010, 2021)}

def classify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]', ' ', text)
    words = set(text.split())
    
    scores = {cat: 0 for cat in keywords}
    for cat, kws in keywords.items():
        for kw in kws:
            if ' ' in kw:
                if kw in text:
                    scores[cat] += 1
            else:
                if kw in words:
                    scores[cat] += 1
    
    max_score = -1
    best_cat = None
    for cat, score in scores.items():
        if score > max_score:
            max_score = score
            best_cat = cat
        elif score == max_score:
             # Tie handling
             pass
             
    if max_score == 0:
        return "Unknown"
    
    return best_cat

count = 0
for art in articles_list:
    aid = str(art.get('article_id'))
    if aid in intersection:
        title = art.get('title', '')
        desc = art.get('description', '')
        full_text = title + " " + desc
        
        category = classify(full_text)
        
        if category == "Business":
            y = meta_map[aid]
            if 2010 <= y <= 2020:
                yearly_counts[y] += 1
                count += 1

avg = sum(yearly_counts.values()) / 11.0

print("__RESULT__:")
print(json.dumps({
    "yearly_counts": yearly_counts,
    "average": avg,
    "total_business_found": count,
    "intersection_count": len(intersection)
}))"""

env_args = {'var_function-call-13727892763181911756': 'file_storage/function-call-13727892763181911756.json', 'var_function-call-14710500662845567092': 'file_storage/function-call-14710500662845567092.json', 'var_function-call-1777077423156184413': 14860, 'var_function-call-6622063249663007819': [{'_id': '6944e1bb7940ea7e4567e403', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944e1bb7940ea7e4567e404', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944e1bb7940ea7e4567e405', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944e1bb7940ea7e4567e406', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944e1bb7940ea7e4567e407', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-15317023739032041550': {'yearly_counts': {'2010': 0, '2011': 0, '2012': 0, '2013': 0, '2014': 0, '2015': 0, '2016': 0, '2017': 0, '2018': 0, '2019': 0, '2020': 0}, 'average': 0.0, 'total_business_found': 0}, 'var_function-call-4974995669331338744': {'meta_count': 14860, 'articles_count': 5, 'intersection_count': 1, 'sample_meta_id': '95893', 'sample_article_id': '4'}, 'var_function-call-17115613930582186539': 'file_storage/function-call-17115613930582186539.json'}

exec(code, env_args)
