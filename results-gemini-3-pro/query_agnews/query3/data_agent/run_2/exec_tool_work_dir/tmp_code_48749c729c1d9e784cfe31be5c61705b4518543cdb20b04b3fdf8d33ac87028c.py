code = """import json
import re

# Load Metadata
meta_file = locals()['var_function-call-18399428532014092056']
with open(meta_file, 'r') as f:
    meta_data = json.load(f)

# Map article_id to year for Europe articles
id_to_year = {}
for r in meta_data:
    year = int(r['publication_date'].split('-')[0])
    id_to_year[int(r['article_id'])] = year

# Load Articles
articles_file = locals()['var_function-call-15183395177982916963']
with open(articles_file, 'r') as f:
    articles_data = json.load(f)

# Keywords
kw_business = set(['business', 'economy', 'economic', 'market', 'finance', 'financial', 'stock', 'share', 'shares', 'trade', 'investment', 'investor', 'bank', 'banking', 'money', 'profit', 'loss', 'revenue', 'tax', 'inflation', 'dollar', 'euro', 'yen', 'rate', 'rates', 'interest', 'price', 'cost', 'oil', 'gas', 'energy', 'budget', 'deficit', 'growth', 'recession', 'crisis', 'debt', 'loan', 'credit', 'bond', 'corporate', 'company', 'firm', 'industry', 'sector', 'retail', 'sale', 'sales', 'consumer', 'spending', 'job', 'unemployment', 'wage', 'wall st', 'nasdaq', 'dow', 'ipo', 'merger', 'acquisition', 'deal', 'export', 'import', 'commerce', 'commercial', 'manager', 'executive', 'ceo', 'cfo', 'fed', 'federal reserve', 'central bank', 'treasury'])

kw_tech = set(['technology', 'tech', 'science', 'computer', 'internet', 'software', 'hardware', 'web', 'website', 'online', 'phone', 'mobile', 'wireless', 'space', 'nasa', 'chip', 'processor', 'virus', 'microsoft', 'google', 'apple', 'intel', 'ibm', 'linux', 'digital', 'network', 'broadband', 'server', 'data', 'robot', 'electronic', 'gadget', 'device', 'screen', 'monitor', 'browser', 'search engine', 'email', 'spam', 'hacker', 'satellite', 'orbit', 'astronomy', 'biology', 'physics', 'research', 'scientist'])

kw_sports = set(['sport', 'sports', 'game', 'team', 'player', 'athlete', 'win', 'won', 'winner', 'lose', 'lost', 'loss', 'score', 'match', 'cup', 'league', 'season', 'coach', 'champion', 'championship', 'olympic', 'football', 'soccer', 'baseball', 'basketball', 'hockey', 'tennis', 'golf', 'cricket', 'rugby', 'boxing', 'racing', 'driver', 'medal', 'gold', 'silver', 'bronze', 'tournament', 'stadium', 'club', 'nba', 'nfl', 'mlb', 'nhl', 'fifa'])

kw_world = set(['world', 'international', 'government', 'president', 'minister', 'prime minister', 'official', 'leader', 'war', 'peace', 'military', 'army', 'troop', 'soldier', 'attack', 'bomb', 'blast', 'kill', 'killed', 'death', 'dead', 'die', 'election', 'vote', 'voter', 'poll', 'campaign', 'candidate', 'country', 'nation', 'state', 'police', 'law', 'court', 'trial', 'judge', 'prison', 'jail', 'crime', 'criminal', 'iraq', 'iran', 'china', 'russia', 'usa', 'america', 'britain', 'uk', 'germany', 'france', 'europe', 'asia', 'africa', 'un', 'united nations', 'security', 'terror', 'terrorism', 'terrorist', 'rebel', 'protest', 'strike', 'treaty', 'agreement', 'nuclear', 'weapon'])

# Counters
counts_per_year = {y: 0 for y in range(2010, 2021)}

for art in articles_data:
    aid = int(art.get('article_id', -1))
    if aid in id_to_year:
        text = (art.get('title', '') + ' ' + art.get('description', '')).lower()
        # Tokenize simply
        words = set(re.findall(r'\w+', text))
        
        # Count overlaps
        score_bus = len(words.intersection(kw_business))
        score_tech = len(words.intersection(kw_tech))
        score_spo = len(words.intersection(kw_sports))
        score_wor = len(words.intersection(kw_world))
        
        # Determine category
        # Priority: If Business is max or tied for max, check carefully.
        # But simple max is usually fine.
        scores = {'Business': score_bus, 'Tech': score_tech, 'Sports': score_spo, 'World': score_wor}
        max_score = max(scores.values())
        
        if max_score > 0:
            # Get categories with max score
            cats = [k for k, v in scores.items() if v == max_score]
            # If Business is in the top categories
            if 'Business' in cats:
                # Tie breaking? 
                # If tied with World (e.g. Oil war), usually Business if it mentions price/market.
                # If tied with Tech (e.g. Google IPO), usually Business.
                # If tied with Sports? Unlikely, but "Win contract" vs "Win game".
                # I will default to Business if it is one of the max.
                counts_per_year[id_to_year[aid]] += 1

# Calculate average
total_business = sum(counts_per_year.values())
average = total_business / 11.0

print("__RESULT__:")
print(json.dumps({"counts": counts_per_year, "average": average}))"""

env_args = {'var_function-call-12102129638019306028': ['authors', 'article_metadata'], 'var_function-call-12102129638019306837': ['articles'], 'var_function-call-18399428532014092056': 'file_storage/function-call-18399428532014092056.json', 'var_function-call-3700738106977438282': 14860, 'var_function-call-80233190844241043': [{'_id': '6944c1d66aebb4a355b6ecab', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944c1d66aebb4a355b6ecac', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944c1d66aebb4a355b6ecad', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944c1d66aebb4a355b6ecae', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944c1d66aebb4a355b6ecaf', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-13560034224583890199': {'min': 3, 'max': 127583, 'count': 14860, 'unique': 14860}, 'var_function-call-17951918547354542984': [{'_id': '6944c1d66aebb4a355b6ecae', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944c1d66aebb4a355b6ecaf', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}, {'_id': '6944c1d66aebb4a355b6ecb0', 'article_id': '5', 'title': 'Stocks End Up, But Near Year Lows (Reuters)', 'description': 'Reuters - Stocks ended slightly higher on Friday\\but stayed near lows for the year as oil prices surged past  #36;46\\a barrel, offsetting a positive outlook from computer maker\\Dell Inc. (DELL.O)'}, {'_id': '6944c1d66aebb4a355b6ecb1', 'article_id': '6', 'title': 'Money Funds Fell in Latest Week (AP)', 'description': "AP - Assets of the nation's retail money market mutual funds fell by  #36;1.17 billion in the latest week to  #36;849.98 trillion, the Investment Company Institute said Thursday."}, {'_id': '6944c1d66aebb4a355b6ecb2', 'article_id': '7', 'title': 'Fed minutes show dissent over inflation (USATODAY.com)', 'description': 'USATODAY.com - Retail sales bounced back a bit in July, and new claims for jobless benefits fell last week, the government said Thursday, indicating the economy is improving from a midsummer slump.'}], 'var_function-call-10942473709632976765': 5, 'var_function-call-15183395177982916963': 'file_storage/function-call-15183395177982916963.json'}

exec(code, env_args)
