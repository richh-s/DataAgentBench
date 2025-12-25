code = """import json
import collections

# Load metadata
with open(locals()['var_function-call-13980908279818660914'], 'r') as f:
    metadata_list = json.load(f)

# Create map: article_id (int) -> year (int)
# Also filter for years 2010-2020 just in case the previous query wasn't perfect (it was, but good to be safe)
article_year_map = {}
for item in metadata_list:
    try:
        aid = int(item['article_id'])
        date_str = item['publication_date']
        year = int(date_str.split('-')[0])
        if 2010 <= year <= 2020:
            article_year_map[aid] = year
    except ValueError:
        continue

# Load articles
with open(locals()['var_function-call-7010050511293703345'], 'r') as f:
    articles_list = json.load(f)

print(f"Loaded {len(articles_list)} articles.")

# Keywords (simplified but extensive)
business_keywords = {
    'market', 'stock', 'share', 'wall street', 'profit', 'loss', 'revenue', 'invest', 
    'finance', 'financial', 'bank', 'federal reserve', 'fed', 'rate', 'inflation', 
    'dollar', 'euro', 'yen', 'currency', 'trade', 'tariff', 'deficit', 'budget', 'tax', 
    'price', 'oil', 'gas', 'gold', 'merge', 'acquisition', 'deal', 'company', 'corp', 
    'inc', 'plc', 'ltd', 'ceo', 'cfo', 'sales', 'retail', 'industry', 'factory', 
    'production', 'job', 'unemployment', 'nasdaq', 'dow', 's&p', 'commodity', 'audit', 
    'accounting', 'loan', 'credit', 'mortgage', 'recession', 'gdp', 'ipo', 'economy',
    'sector', 'growth', 'spending', 'cost', 'earnings', 'quarter', 'forecast', 'analyst'
}

sports_keywords = {
    'sport', 'game', 'match', 'cup', 'win', 'lose', 'score', 'team', 'league', 'season', 
    'player', 'athlete', 'olympic', 'medal', 'championship', 'champion', 'football', 
    'soccer', 'baseball', 'basketball', 'hockey', 'tennis', 'golf', 'coach', 'stadium', 
    'race', 'racing', 'tournament', 'f1', 'cricket', 'rugby', 'nfl', 'nba', 'mlb', 'nhl'
}

scitech_keywords = {
    'technology', 'tech', 'science', 'computer', 'software', 'hardware', 'internet', 
    'web', 'online', 'net', 'google', 'microsoft', 'apple', 'ibm', 'intel', 'chip', 
    'processor', 'server', 'virus', 'hacker', 'security', 'space', 'nasa', 'astronomy', 
    'biology', 'physics', 'chemistry', 'research', 'study', 'scientist', 'mobile', 
    'phone', 'wireless', 'network', 'satellite', 'robot', 'gadget', 'device', 'app', 'browser'
}

world_keywords = {
    'world', 'war', 'peace', 'conflict', 'army', 'military', 'troop', 'soldier', 'police', 
    'crime', 'court', 'trial', 'judge', 'prison', 'government', 'politic', 'election', 
    'vote', 'president', 'minister', 'senate', 'congress', 'parliament', 'official', 
    'diplomat', 'treaty', 'un', 'united nations', 'eu', 'european union', 'nato', 'bomb', 
    'blast', 'attack', 'terror', 'crisis', 'disaster', 'quake', 'flood', 'storm', 'hurricane',
    'killing', 'killed', 'nuclear', 'protest', 'strike', 'prime minister'
}

def classify(text):
    text = text.lower()
    tokens = text.split()
    scores = {'Business': 0, 'Sports': 0, 'Sci/Tech': 0, 'World': 0}
    
    for token in tokens:
        # Simple token matching, removing punctuation
        clean_token = ''.join(c for c in token if c.isalnum())
        if clean_token in business_keywords: scores['Business'] += 1
        if clean_token in sports_keywords: scores['Sports'] += 1
        if clean_token in scitech_keywords: scores['Sci/Tech'] += 1
        if clean_token in world_keywords: scores['World'] += 1
    
    # Priority handling or just max
    # Oil/Gas prices usually Business, but could be World. Business keywords often overlap.
    # Let's use max.
    best_cat = max(scores, key=scores.get)
    if scores[best_cat] == 0:
        return 'Unsure' # Default or Handle
    return best_cat

business_counts = collections.defaultdict(int)

for article in articles_list:
    try:
        aid = int(article.get('article_id', -1))
    except:
        continue
        
    if aid in article_year_map:
        title = article.get('title', '')
        desc = article.get('description', '')
        full_text = title + " " + desc
        
        category = classify(full_text)
        
        if category == 'Business':
            year = article_year_map[aid]
            business_counts[year] += 1

# Calculate average
total_business = sum(business_counts.values())
years_count = 11 # 2010 to 2020 inclusive
average = total_business / years_count

print("__RESULT__:")
print(json.dumps({
    "business_counts_by_year": business_counts,
    "total_business": total_business,
    "average": average
}))"""

env_args = {'var_function-call-13980908279818660914': 'file_storage/function-call-13980908279818660914.json', 'var_function-call-9650828071725481158': 'file_storage/function-call-9650828071725481158.json', 'var_function-call-9975019705778292036': [{'_id': '6944d514bfa2adeadebcf6b4', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944d514bfa2adeadebcf6b5', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944d514bfa2adeadebcf6b6', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944d514bfa2adeadebcf6b7', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944d514bfa2adeadebcf6b8', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-4774409130676372759': [{'_id': '6944d514bfa2adeadebcf6b4', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944d514bfa2adeadebcf6b5', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944d514bfa2adeadebcf6b6', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944d514bfa2adeadebcf6b7', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944d514bfa2adeadebcf6b8', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-7010050511293703345': 'file_storage/function-call-7010050511293703345.json'}

exec(code, env_args)
