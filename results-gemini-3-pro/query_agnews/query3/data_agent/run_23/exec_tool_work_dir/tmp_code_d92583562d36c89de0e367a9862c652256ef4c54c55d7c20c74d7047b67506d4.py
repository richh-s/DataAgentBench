code = """import json
import re

# Load SQL data
with open(locals()['var_function-call-18349184007638640037'], 'r') as f:
    sql_data = json.load(f)

# Map article_id (int) to year (str)
id_year_map = {}
for row in sql_data:
    aid = int(row['article_id'])
    year = row['publication_date'][:4]
    id_year_map[aid] = year

# Load Mongo data
with open(locals()['var_function-call-5591043477264276046'], 'r') as f:
    mongo_data = json.load(f)

# Keywords
business_keywords = [
    'business', 'economy', 'economic', 'market', 'stock', 'share', 'invest', 'finance', 'financial', 
    'money', 'bank', 'trade', 'profit', 'revenue', 'sale', 'price', 'cost', 'rate', 'interest', 
    'inflation', 'dollar', 'euro', 'currency', 'exchange', 'capital', 'fund', 'asset', 'debt', 
    'budget', 'tax', 'company', 'firm', 'corp', 'inc', 'industry', 'commercial', 'corporate', 
    'ceo', 'executive', 'job', 'employment', 'labor', 'strike', 'union', 'merger', 'acquisition', 
    'deal', 'contract', 'bid', 'ipo', 'supply', 'demand', 'export', 'import', 'oil', 'gas', 'energy', 
    'fuel', 'commodity', 'gold', 'futures', 'loan', 'credit', 'mortgage', 'insurance', 'retail', 
    'consumer', 'earning', 'quarter', 'fiscal', 'recession', 'growth', 'deficit', 'surplus', 
    'wall st', 'treasury', 'fed', 'reserve', 'imf', 'wto', 'opec', 'nasdaq', 'dow jones', 's&p'
]

# Simple scorer
def is_business(title, desc):
    text = (title + " " + desc).lower()
    score = 0
    for kw in business_keywords:
        if kw in text:
            score += 1
    # Heuristic: if score >= 1, likely business? 
    # But "World" news might mention "oil" or "money".
    # Let's try to exclude if other stronger keywords are present?
    # For now, let's assume if it hits business keywords it's business.
    # The hint implies disjoint categories.
    return score >= 1

# Actually, I should probably check for competition.
# But let's start with this.
business_counts = {}
years = range(2010, 2021) # 2010 to 2020
for y in years:
    business_counts[str(y)] = 0

processed_count = 0
business_found = 0

for art in mongo_data:
    aid = int(art['article_id'])
    if aid in id_year_map:
        processed_count += 1
        title = art.get('title', '')
        desc = art.get('description', '')
        
        # Check specific strong indicators in title for other categories
        text = (title + " " + desc).lower()
        
        # Sports
        is_sport = any(k in text for k in ['sport', 'game', 'match', 'cup', 'league', 'olympic', 'medal', 'team', 'player', 'coach', 'score', 'win', 'defeat', 'soccer', 'football', 'tennis', 'baseball', 'basketball', 'hockey', 'golf'])
        
        # Sci/Tech
        is_tech = any(k in text for k in ['software', 'hardware', 'computer', 'internet', 'web', 'technology', 'science', 'space', 'nasa', 'microsoft', 'google', 'apple', 'linux', 'virus', 'study', 'research'])
        
        # World
        is_world = any(k in text for k in ['war', 'peace', 'president', 'minister', 'bomb', 'attack', 'kill', 'military', 'army', 'government', 'police', 'election', 'vote', 'iraq', 'iran', 'afghanistan', 'palestinian', 'israel', 'un', 'official'])
        
        # Business (re-eval)
        is_biz = any(k in text for k in business_keywords)
        
        # Priority resolution
        # Usually: Sports is distinct. Tech is distinct.
        # Business vs World is tricky. "Oil prices" is Business. "Iraq war oil" is World.
        # If it has strong Business keywords like "stock", "market", "economy", "profit", "euro", "dollar" -> Business.
        
        category = 'Other'
        scores = {'Business': 0, 'Sports': 0, 'Sci/Tech': 0, 'World': 0}
        
        # Count keyword matches
        for k in business_keywords: 
            if k in text: scores['Business'] += 1
        
        # Refined other lists
        sport_kws = ['sport', 'game', 'match', 'cup', 'league', 'olympic', 'medal', 'team', 'player', 'coach', 'score', 'soccer', 'football', 'tennis', 'baseball', 'basketball', 'hockey', 'golf', 'athlete']
        for k in sport_kws:
            if k in text: scores['Sports'] += 1
            
        tech_kws = ['software', 'hardware', 'computer', 'internet', 'web', 'technology', 'science', 'space', 'nasa', 'microsoft', 'google', 'apple', 'linux', 'virus', 'study', 'research', 'biology', 'astronomy']
        for k in tech_kws:
            if k in text: scores['Sci/Tech'] += 1
            
        world_kws = ['war', 'peace', 'president', 'minister', 'bomb', 'attack', 'kill', 'military', 'army', 'government', 'police', 'election', 'vote', 'iraq', 'iran', 'afghanistan', 'palestinian', 'israel', 'un', 'official', 'blast', 'troops', 'rebel']
        for k in world_kws:
            if k in text: scores['World'] += 1
            
        # Determine max
        max_cat = max(scores, key=scores.get)
        if scores[max_cat] > 0:
            if max_cat == 'Business':
                year = id_year_map[aid]
                business_counts[year] += 1
                business_found += 1
        else:
            # If no keywords, maybe default? Or ignore.
            pass

print(f"Processed {processed_count} articles.")
print(f"Business articles found: {business_found}")
print(f"Counts per year: {business_counts}")

# Calculate average
total_business = sum(business_counts.values())
average = total_business / 11.0 # 2010 to 2020 inclusive is 11 years

print("__RESULT__:")
print(json.dumps({"average": average, "counts": business_counts}))"""

env_args = {'var_function-call-18349184007638640037': 'file_storage/function-call-18349184007638640037.json', 'var_function-call-13314577976510498220': 'file_storage/function-call-13314577976510498220.json', 'var_function-call-15338869438340783850': [{'_id': '6944d56f1edb9f0b9c16c37b', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944d56f1edb9f0b9c16c37c', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944d56f1edb9f0b9c16c37d', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944d56f1edb9f0b9c16c37e', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944d56f1edb9f0b9c16c37f', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-7013472605511009319': {'min': 3, 'max': 127583, 'count': 14860}, 'var_function-call-3049339074989705586': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-5591043477264276046': 'file_storage/function-call-5591043477264276046.json'}

exec(code, env_args)
