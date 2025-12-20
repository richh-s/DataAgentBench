code = """import json
import collections

# Load metadata
with open(locals()['var_function-call-15785121732506884524'], 'r') as f:
    metadata_list = json.load(f)

# Create a map article_id -> year for Europe articles
# Filter year 2010-2020 is already done in SQL, but good to be sure.
meta_map = {}
for m in metadata_list:
    aid = str(m['article_id'])
    date = m['publication_date'] # "YYYY-MM-DD"
    year = int(date[:4])
    if 2010 <= year <= 2020:
        meta_map[aid] = year

# Load articles
with open(locals()['var_function-call-11595286939562233516'], 'r') as f:
    articles_list = json.load(f)

# Keywords
categories = {
    'Business': ['business', 'economy', 'market', 'stock', 'trade', 'finance', 'financial', 'corporate', 'company', 'companies', 'investment', 'investor', 'bank', 'banking', 'profit', 'loss', 'revenue', 'dollar', 'euro', 'currency', 'inflation', 'rate', 'price', 'oil', 'shares', 'nasdaq', 'dow', 'wall street', 'ipo', 'merger', 'acquisition', 'deal', 'ceo', 'federal reserve', 'fed', 'treasury', 'yield', 'bond', 'crude', 'barrel', 'opec'],
    'Sports': ['sport', 'olympic', 'game', 'match', 'team', 'win', 'won', 'loss', 'lost', 'score', 'player', 'coach', 'league', 'cup', 'medal', 'champion', 'championship', 'football', 'baseball', 'basketball', 'soccer', 'tennis', 'golf', 'hockey', 'athlete', 'race', 'racing', 'tournament'],
    'Sci/Tech': ['technology', 'tech', 'science', 'computer', 'software', 'hardware', 'internet', 'web', 'net', 'online', 'google', 'microsoft', 'apple', 'intel', 'ibm', 'linux', 'windows', 'server', 'mobile', 'phone', 'wireless', 'space', 'nasa', 'astronomy', 'biology', 'physics', 'chip', 'processor', 'digital', 'network', 'satellite', 'robot'],
    'World': ['world', 'international', 'president', 'minister', 'prime minister', 'iraq', 'iran', 'afghanistan', 'palestinian', 'israel', 'war', 'peace', 'military', 'army', 'police', 'government', 'election', 'vote', 'party', 'official', 'united nations', 'un', 'country', 'countries', 'blast', 'attack', 'kill', 'killed', 'bomb', 'terror', 'rebel', 'troops', 'leader', 'hostage']
}

business_counts_by_year = collections.defaultdict(int)

# Check matches
match_count = 0
for art in articles_list:
    aid = str(art['article_id'])
    if aid in meta_map:
        title = art.get('title', '').lower()
        desc = art.get('description', '').lower()
        text = title + " " + desc
        
        scores = {cat: 0 for cat in categories}
        for cat, keywords in categories.items():
            for kw in keywords:
                if kw in text:
                    scores[cat] += 1
        
        # Determine category with max score
        # If tie, prioritize Business > others? Or just pick one.
        # If all 0, maybe "World" default? Or ignore.
        
        best_cat = None
        max_score = -1
        for cat, score in scores.items():
            if score > max_score:
                max_score = score
                best_cat = cat
            elif score == max_score:
                # Tie breaking preference?
                # "Oil prices" has "oil" (Business) and maybe "prices" (Business).
                # "War in Iraq" has "war" (World) and "iraq" (World).
                pass
        
        if max_score > 0 and best_cat == 'Business':
            year = meta_map[aid]
            business_counts_by_year[year] += 1
            match_count += 1

print("__RESULT__:")
print(json.dumps({'business_counts': business_counts_by_year, 'total_business': match_count}))"""

env_args = {'var_function-call-15785121732506884524': 'file_storage/function-call-15785121732506884524.json', 'var_function-call-1168963100996389455': {'count': 14860, 'sample_ids': [3, 9, 13, 14, 21]}, 'var_function-call-78814616678511644': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-3419358495876270710': {'article_count': 5}, 'var_function-call-11595286939562233516': 'file_storage/function-call-11595286939562233516.json'}

exec(code, env_args)
