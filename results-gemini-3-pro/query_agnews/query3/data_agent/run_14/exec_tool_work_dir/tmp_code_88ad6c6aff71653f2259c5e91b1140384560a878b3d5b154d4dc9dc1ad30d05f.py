code = """import json
import re
from collections import Counter

# Load data
meta_var = locals()['var_function-call-12987280970809318212']
with open(meta_var, 'r') as f:
    meta_list = json.load(f)

art_var = locals()['var_function-call-10227214225653299707']
with open(art_var, 'r') as f:
    art_list = json.load(f)

# ID to Year mapping
id_to_year = {}
for m in meta_list:
    aid = int(m['article_id'])
    date = m['publication_date']
    year = int(date[:4])
    if 2010 <= year <= 2020:
        id_to_year[aid] = year

# Keywords
categories = {
    'Business': [
        'business', 'economy', 'market', 'markets', 'stock', 'stocks', 'share', 'shares', 
        'trade', 'trading', 'financial', 'finance', 'investment', 'investor', 'invest', 
        'bank', 'banking', 'banks', 'money', 'currency', 'dollar', 'euro', 'yen', 'price', 'prices', 
        'profit', 'profits', 'loss', 'losses', 'earnings', 'revenue', 'debt', 'bond', 'bonds', 
        'loan', 'loans', 'rate', 'rates', 'interest', 'tax', 'taxes', 'budget', 'deficit', 
        'inflation', 'recession', 'growth', 'gdp', 'ceo', 'cfo', 'executive', 'manager', 
        'company', 'companies', 'firm', 'firms', 'corp', 'corporate', 'industry', 'industrial', 
        'commercial', 'retail', 'sales', 'sale', 'deal', 'merger', 'acquisition', 'bid', 'buyout', 
        'wall st', 'wall street', 'dow', 'nasdaq', 'nyse', 'fed', 'federal reserve', 'treasury', 
        'imf', 'wto', 'opec', 'oil', 'gas', 'energy', 'crude', 'barrel', 'airline', 'airlines', 
        'automaker', 'manufacturing', 'manufacturer', 'production', 'output', 'job', 'jobs', 
        'unemployment', 'employment', 'hiring', 'labor', 'strike', 'union', 'audit', 'accounting'
    ],
    'Sports': [
        'sport', 'sports', 'game', 'games', 'match', 'matches', 'team', 'teams', 'player', 'players', 
        'coach', 'coaches', 'win', 'wins', 'won', 'winner', 'loss', 'lost', 'score', 'scores', 
        'goal', 'goals', 'cup', 'league', 'championship', 'champion', 'tournament', 'season', 
        'olympic', 'olympics', 'medal', 'football', 'soccer', 'baseball', 'basketball', 'tennis', 
        'golf', 'hockey', 'cricket', 'rugby', 'racing', 'race', 'driver', 'f1', 'formula one', 
        'nfl', 'nba', 'mlb', 'nhl', 'fifa', 'uefa', 'stadium', 'club'
    ],
    'SciTech': [
        'science', 'technology', 'tech', 'computer', 'computers', 'software', 'hardware', 'internet', 
        'web', 'online', 'digital', 'network', 'broadband', 'wireless', 'mobile', 'phone', 'smartphone', 
        'app', 'data', 'cyber', 'security', 'hacker', 'virus', 'microsoft', 'google', 'apple', 'intel', 
        'ibm', 'linux', 'windows', 'browser', 'server', 'chip', 'space', 'nasa', 'astronomy', 'planet', 
        'mars', 'moon', 'orbit', 'satellite', 'launch', 'shuttle', 'robot', 'robotics', 'biotech', 
        'biology', 'physics', 'chemistry', 'study', 'research', 'researcher', 'scientist', 'discovery', 
        'experiment', 'drug', 'medical', 'medicine', 'disease', 'cancer', 'health'
    ],
    'World': [
        'world', 'international', 'nation', 'nations', 'country', 'countries', 'state', 'government', 
        'politics', 'political', 'politician', 'president', 'minister', 'premier', 'leader', 'official', 
        'officials', 'parliament', 'senate', 'congress', 'election', 'vote', 'voters', 'poll', 'polls', 
        'party', 'democrat', 'republican', 'conservative', 'liberal', 'war', 'military', 'army', 'troops', 
        'soldier', 'soldiers', 'conflict', 'fight', 'fighting', 'attack', 'attacks', 'bomb', 'bombing', 
        'blast', 'explosion', 'kill', 'killed', 'death', 'dead', 'casualty', 'hostage', 'terror', 'terrorist', 
        'rebel', 'rebels', 'insurgent', 'iraq', 'iran', 'afghanistan', 'palestinian', 'israel', 'syria', 
        'russia', 'china', 'uk', 'britain', 'france', 'germany', 'europe', 'eu', 'un', 'united nations', 
        'treaty', 'accord', 'deal', 'talks', 'peace', 'summit', 'protest', 'riot', 'police', 'court', 'judge', 
        'trial', 'prison', 'jail', 'law', 'legal', 'ban', 'rights', 'refugee', 'aid', 'crisis'
    ]
}

# Compile regex for speed
cat_regex = {}
for cat, kws in categories.items():
    # Sort by length desc to match longer phrases first
    kws.sort(key=len, reverse=True)
    pattern = r'\b(' + '|'.join(map(re.escape, kws)) + r')\b'
    cat_regex[cat] = re.compile(pattern)

year_counts = Counter()
processed_count = 0
business_count = 0

for art in art_list:
    aid = int(art['article_id'])
    if aid in id_to_year:
        title = art.get('title', '') or ''
        desc = art.get('description', '') or ''
        text = (title + " " + desc).lower()
        
        scores = {}
        for cat, regex in cat_regex.items():
            matches = regex.findall(text)
            scores[cat] = len(matches)
        
        # Determine category
        # Heuristic: Max score. If tie, prefer Business > World > SciTech > Sports?
        # Or just Business vs others.
        
        # If Business score is highest (strictly or >=?)
        # Let's verify with ties.
        if not scores:
            best_cat = 'World'
        else:
            # Find max score
            max_score = max(scores.values())
            if max_score == 0:
                best_cat = 'World' # Default
            else:
                # Get all cats with max_score
                candidates = [c for c, s in scores.items() if s == max_score]
                if len(candidates) == 1:
                    best_cat = candidates[0]
                else:
                    # Tie breaking
                    if 'Business' in candidates:
                        best_cat = 'Business'
                    elif 'World' in candidates:
                        best_cat = 'World'
                    else:
                        best_cat = candidates[0]

        if best_cat == 'Business':
            y = id_to_year[aid]
            year_counts[y] += 1
            business_count += 1
        
        processed_count += 1

# Calculate average
avg = business_count / 11.0 if processed_count > 0 else 0

result = {
    "year_counts": dict(year_counts),
    "processed": processed_count,
    "total_business": business_count,
    "average": avg
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-12987280970809318212': 'file_storage/function-call-12987280970809318212.json', 'var_function-call-3327544021322435934': 'file_storage/function-call-3327544021322435934.json', 'var_function-call-5544368014430609247': {'min': 3, 'max': 127583, 'count': 14860}, 'var_function-call-11134278749745899859': [{'_id': '6944cce21659048c9db08bdd', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944cce21659048c9db08bde', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944cce21659048c9db08bdf', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944cce21659048c9db08be0', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944cce21659048c9db08be1', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-1079264442624552925': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-10815997547170822222': {'year_counts': {'2010': 0, '2011': 0, '2012': 0, '2013': 0, '2014': 0, '2015': 0, '2016': 0, '2017': 0, '2018': 0, '2019': 0, '2020': 0}, 'processed': 1, 'total_business': 0}, 'var_function-call-10227214225653299707': 'file_storage/function-call-10227214225653299707.json', 'var_function-call-16728244327291461152': {'year_counts': {'2010': 0, '2011': 0, '2012': 0, '2013': 0, '2014': 0, '2015': 0, '2016': 0, '2017': 0, '2018': 0, '2019': 0, '2020': 0}, 'processed': 14860, 'total_business': 0, 'average': 0.0}, 'var_function-call-18282204154223833578': [{'id': 3, 'text': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters) Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could ', 'scores': {'Business': 1, 'Sports': 0, 'SciTech': 0, 'World': 1}}, {'id': 9, 'text': "Wall St. Bears Claw Back Into the Black  NEW YORK (Reuters) - Short-sellers, Wall Street's dwindling  band of ultra-cynics, are seeing green again.", 'scores': {'Business': 1, 'Sports': 1, 'SciTech': 0, 'World': 1}}, {'id': 13, 'text': "Google IPO Auction Off to Rocky Start  WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web searc", 'scores': {'Business': 0, 'Sports': 0, 'SciTech': 2, 'World': 0}}, {'id': 14, 'text': "Dollar Falls Broadly on Record Trade Gap  NEW YORK (Reuters) - The dollar tumbled broadly on Friday  after data showing a record U.S. trade deficit in June cast  fresh doubts on the economy's recovery", 'scores': {'Business': 3, 'Sports': 1, 'SciTech': 0, 'World': 0}}, {'id': 21, 'text': 'Eurozone economy keeps growing Official figures show the 12-nation eurozone economy continues to grow, but there are warnings it may slow down later in the year.', 'scores': {'Business': 3, 'Sports': 1, 'SciTech': 0, 'World': 1}}, {'id': 27, 'text': 'HP shares tumble on profit news Hewlett-Packard shares fall after disappointing third-quarter profits, while the firm warns the final quarter will also fall short of expectations.', 'scores': {'Business': 2, 'Sports': 0, 'SciTech': 0, 'World': 1}}, {'id': 43, 'text': 'Grant to aid Lynn Central Square Central Square in Lynn should be looking a bit brighter. New sidewalks, curbs, fences, lights, landscaping, and road improvements are planned for the Gateway Artisan B', 'scores': {'Business': 1, 'Sports': 0, 'SciTech': 0, 'World': 0}}, {'id': 60, 'text': 'Oldsmobile: The final parking lot Why General Motors dropped the Oldsmobile. The four brand  paradoxes GM had to face - the name, the product, image re-positioning, and the consumer - all added up to ', 'scores': {'Business': 0, 'Sports': 0, 'SciTech': 1, 'World': 0}}, {'id': 62, 'text': "Downhome Pinoy Blues, Intersecting Life Paths, and Heartbreak Songs The Blues is alive and well in the Philippines, as evidenced by this appreciation of the Pinoy Blues band 'Lampano Alley', penned by", 'scores': {'Business': 2, 'Sports': 0, 'SciTech': 0, 'World': 0}}, {'id': 63, 'text': 'The Real Time Modern Manila Blues: Bill Monroe Meets Muddy Waters in the Orient Globalization does strange things to people. A day in the life of a Manila Philippines based business consultant - provi', 'scores': {'Business': 1, 'Sports': 0, 'SciTech': 0, 'World': 0}}]}

exec(code, env_args)
