code = """import json
import re

# Load metadata
with open(locals()['var_function-call-16473785254101418274'], 'r') as f:
    meta = json.load(f)

# Load articles
with open(locals()['var_function-call-16666979674709341157'], 'r') as f:
    articles = json.load(f)

# Map articles by ID
articles_map = {str(a['article_id']): a for a in articles}

# Keywords
business_keywords = {
    'market', 'markets', 'economy', 'economic', 'stocks', 'stock', 'wall', 'street', 
    'finance', 'financial', 'investment', 'investor', 'investors', 'profit', 'profits', 
    'revenue', 'loss', 'losses', 'earnings', 'quarter', 'quarterly', 
    'company', 'companies', 'corporation', 'corp', 'inc', 'share', 'shares', 
    'trade', 'trading', 'dollar', 'euro', 'yen', 'currency', 'currencies', 
    'bank', 'banks', 'banking', 'fed', 'federal', 'reserve', 'rates', 'rate', 
    'inflation', 'deflation', 'oil', 'crude', 'barrel', 'prices', 'price', 
    'imf', 'wto', 'treasury', 'bond', 'bonds', 'debt', 'loan', 'loans', 
    'nasdaq', 'dow', 'jones', 's&p', 'merger', 'acquisition', 'deal', 'buyout', 
    'ceo', 'cfo', 'executive', 'business', 'businesses', 'industry', 'sales', 
    'retail', 'consumer', 'spending', 'commodities', 'gold', 'futures', 'ipo', 
    'dividend', 'dividends', 'sector', 'growth', 'recession', 'forecast', 
    'analyst', 'analysts', 'beating', 'estimates', 'jobs', 'unemployment', 
    'hiring', 'wage', 'wages', 'deficit', 'budget', 'tax', 'taxes', 'tariff', 
    'tariffs', 'bankruptcy', 'bankrupt', 'audit', 'accounting'
}

world_keywords = {
    'war', 'wars', 'peace', 'election', 'elections', 'vote', 'voting', 'voters', 
    'president', 'presidency', 'minister', 'prime', 'parliament', 'senate', 'congress', 
    'legislation', 'law', 'bill', 'military', 'army', 'navy', 'air', 'force', 'troops', 
    'soldier', 'soldiers', 'guerrilla', 'rebel', 'rebels', 'militia', 
    'iraq', 'iraqi', 'iran', 'iranian', 'afghanistan', 'china', 'chinese', 
    'russia', 'russian', 'un', 'united', 'nations', 'eu', 'european', 'union', 
    'treaty', 'nuclear', 'atomic', 'weapon', 'weapons', 'bomb', 'bombing', 'blast', 
    'attack', 'attacks', 'killed', 'kill', 'dead', 'died', 'death', 'injured', 'wounded', 
    'crash', 'police', 'court', 'trial', 'judge', 'prison', 'jail', 'protest', 'protests', 
    'demonstration', 'riot', 'government', 'official', 'officials', 'diplomat', 
    'hurricane', 'storm', 'typhoon', 'earthquake', 'quake', 'tsunami', 'disaster', 
    'israel', 'israeli', 'palestinian', 'gaza', 'syria', 'syrian', 'korea', 'korean', 
    'security', 'terrorism', 'terrorist', 'qaeda', 'taliban', 'hostage', 'kidnap'
}

sports_keywords = {
    'sport', 'sports', 'football', 'soccer', 'basketball', 'baseball', 'hockey', 
    'tennis', 'golf', 'cricket', 'rugby', 'boxing', 'f1', 'formula', 'racing', 
    'team', 'teams', 'player', 'players', 'coach', 'manager', 'game', 'games', 
    'match', 'matches', 'tournament', 'championship', 'champion', 'cup', 'league', 
    'olympic', 'olympics', 'medal', 'medals', 'gold', 'silver', 'bronze', 
    'win', 'wins', 'winning', 'won', 'winner', 'loss', 'lost', 'losing', 
    'score', 'scores', 'season', 'club', 'clubs', 'fifa', 'uefa', 'nfl', 'nba', 
    'mlb', 'nhl', 'stadium', 'athlete', 'athletes'
}

tech_keywords = {
    'technology', 'tech', 'science', 'computer', 'computers', 'software', 'hardware', 
    'internet', 'web', 'online', 'cyberspace', 'digital', 'network', 'networks', 
    'google', 'microsoft', 'apple', 'intel', 'ibm', 'oracle', 'linux', 'windows', 
    'server', 'servers', 'chip', 'chips', 'processor', 'mobile', 'phone', 'phones', 
    'smartphone', 'wireless', 'wifi', 'broadband', 'satellite', 'space', 'nasa', 
    'shuttle', 'astronaut', 'astronomy', 'biology', 'genome', 'dna', 'stem', 'cell', 
    'research', 'study', 'scientist', 'scientists', 'virus', 'worm', 'spam', 'hacker', 
    'browser', 'search', 'engine', 'blog', 'blogger', 'email', 'ipod', 'mp3', 
    'video', 'gaming', 'console', 'nintendo', 'sony', 'xbox'
}

# Counters
yearly_counts = {y: 0 for y in range(2010, 2021)}

business_articles_count = 0
total_checked = 0

for m in meta:
    aid = str(m['article_id'])
    if aid in articles_map:
        total_checked += 1
        art = articles_map[aid]
        text = (art.get('title', '') + " " + art.get('description', '')).lower()
        
        # Tokenize (simple split by non-word char)
        tokens = re.findall(r'[a-z]+', text)
        
        scores = {'Business': 0, 'World': 0, 'Sports': 0, 'Tech': 0}
        
        for t in tokens:
            if t in business_keywords: scores['Business'] += 1
            if t in world_keywords: scores['World'] += 1
            if t in sports_keywords: scores['Sports'] += 1
            if t in tech_keywords: scores['Tech'] += 1
            
        # Determine category
        # If no keywords match, assume World (common default in news) or skip?
        # Let's verify ties.
        # Max score
        best_cat = max(scores, key=scores.get)
        
        # If score is 0, it's ambiguous. 
        # But let's stick to the max.
        if scores[best_cat] > 0 and best_cat == 'Business':
            y = int(m['publication_date'][:4])
            if 2010 <= y <= 2020:
                yearly_counts[y] += 1
                business_articles_count += 1
        elif scores[best_cat] == 0:
             # Fallback: Check title for specific strong indicators?
             # For now, ignore uncategorized or assume non-business.
             pass

# Calculate Average
avg_per_year = sum(yearly_counts.values()) / 11.0

print(f"Total Europe Articles Processed: {total_checked}")
print(f"Total Business Articles Found: {business_articles_count}")
print(f"Yearly Counts: {yearly_counts}")
print("__RESULT__:")
print(json.dumps(avg_per_year))"""

env_args = {'var_function-call-16473785254101418274': 'file_storage/function-call-16473785254101418274.json', 'var_function-call-5763965642417162801': 14860, 'var_function-call-16666979674709341157': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
