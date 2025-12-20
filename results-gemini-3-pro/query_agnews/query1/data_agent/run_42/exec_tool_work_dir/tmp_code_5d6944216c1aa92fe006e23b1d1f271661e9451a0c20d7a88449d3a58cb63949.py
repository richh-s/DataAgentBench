code = """import json
import re

file_path = locals()['var_function-call-14251754240139237620']

with open(file_path, 'r') as f:
    articles = json.load(f)

# Define keywords
# Use sets for faster lookup if tokenizing, but regex is good for phrases
# Let's use word tokenization and set intersection for single words.

keywords_map = {
    'Business': {'oil', 'price', 'prices', 'stock', 'stocks', 'economy', 'market', 'markets', 'company', 'companies', 'profit', 'profits', 'dollar', 'bank', 'banks', 'trade', 'business', 'ipo', 'fed', 'inflation', 'investor', 'investors', 'sales', 'corp', 'inc', 'revenue', 'deal', 'merger', 'acquisition', 'bond', 'bonds', 'fund', 'funds', 'rate', 'rates', 'ceo', 'cfo', 'executive', 'share', 'shares'},
    'Sci/Tech': {'computer', 'computers', 'software', 'technology', 'internet', 'microsoft', 'google', 'intel', 'space', 'nasa', 'web', 'virus', 'linux', 'science', 'tech', 'online', 'pc', 'apple', 'ibm', 'chip', 'chips', 'digital', 'network', 'wireless', 'broadband', 'server', 'browser', 'code', 'java', 'programming', 'developer', 'developers', 'app', 'application', 'system', 'systems', 'mobile', 'phone', 'cellular', 'satellite', 'robot', 'spam', 'hacker', 'security', 'windows', 'search', 'engine'},
    'World': {'iraq', 'war', 'president', 'government', 'minister', 'palestinian', 'israel', 'bomb', 'official', 'officials', 'un', 'peace', 'troops', 'country', 'countries', 'world', 'baghdad', 'gaza', 'leader', 'leaders', 'election', 'elections', 'politics', 'party', 'vote', 'voters', 'military', 'army', 'navy', 'nuclear', 'weapon', 'weapons', 'strike', 'attack', 'attacks', 'killed', 'died', 'injured', 'police', 'security', 'court', 'trial', 'judge', 'law'},
    'Sports': {'olympic', 'olympics', 'athens', 'medal', 'medals', 'gold', 'silver', 'bronze', 'team', 'teams', 'game', 'games', 'win', 'wins', 'winning', 'won', 'winner', 'cup', 'coach', 'sport', 'sports', 'football', 'baseball', 'basketball', 'soccer', 'tennis', 'hockey', 'champion', 'champions', 'championship', 'athlete', 'athletes', 'player', 'players', 'sox', 'yankees', 'mets', 'bulls', 'lakers', 'nfl', 'nba', 'mlb', 'nhl', 'rugby', 'cricket', 'race', 'racing', 'victory', 'defeat', 'score', 'scores', 'scoring', 'tournament', 'match', 'matches', 'f1', 'golf', 'tiger', 'woods', 'armstrong', 'cycling', 'boxing', 'swim', 'swimming', 'track', 'field', 'marathon', 'relay', 'gymnastics', 'volleyball', 'handball', 'stadium', 'league'}
}

def classify_article(title, desc):
    text = (title + " " + desc).lower()
    # Replace non-alphanumeric with space
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    tokens = text.split()
    token_set = set(tokens)
    
    scores = {}
    for cat, kws in keywords_map.items():
        # count how many keywords are present
        # intersection count
        common = token_set.intersection(kws)
        scores[cat] = len(common)
    
    # Heuristic: if "olympic" or "athens" is present, it's likely sports (given the timeframe)
    if 'olympic' in token_set or 'olympics' in token_set or 'athens' in token_set:
        scores['Sports'] += 5
        
    # Pick max
    best_cat = max(scores, key=scores.get)
    if scores[best_cat] == 0:
        return 'Unknown', 0
    return best_cat, scores[best_cat]

sports_candidates = []

for art in articles:
    cat, score = classify_article(art.get('title', ''), art.get('description', ''))
    if cat == 'Sports':
        sports_candidates.append(art)

# Sort by description length
sports_candidates.sort(key=lambda x: len(x.get('description', '')), reverse=True)

# Print top 3 to verify
top_results = []
for art in sports_candidates[:3]:
    top_results.append({
        "title": art['title'],
        "description_length": len(art['description']),
        "description_preview": art['description'][:100]
    })

print("__RESULT__:")
print(json.dumps(top_results))"""

env_args = {'var_function-call-421718428905845327': [{'_id': '694484ac1eb216d85781ec21', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694484ac1eb216d85781ec22', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694484ac1eb216d85781ec23', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694484ac1eb216d85781ec24', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694484ac1eb216d85781ec25', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}, {'_id': '694484ac1eb216d85781ec26', 'article_id': '5', 'title': 'Stocks End Up, But Near Year Lows (Reuters)', 'description': 'Reuters - Stocks ended slightly higher on Friday\\but stayed near lows for the year as oil prices surged past  #36;46\\a barrel, offsetting a positive outlook from computer maker\\Dell Inc. (DELL.O)'}, {'_id': '694484ac1eb216d85781ec27', 'article_id': '6', 'title': 'Money Funds Fell in Latest Week (AP)', 'description': "AP - Assets of the nation's retail money market mutual funds fell by  #36;1.17 billion in the latest week to  #36;849.98 trillion, the Investment Company Institute said Thursday."}, {'_id': '694484ac1eb216d85781ec28', 'article_id': '7', 'title': 'Fed minutes show dissent over inflation (USATODAY.com)', 'description': 'USATODAY.com - Retail sales bounced back a bit in July, and new claims for jobless benefits fell last week, the government said Thursday, indicating the economy is improving from a midsummer slump.'}, {'_id': '694484ac1eb216d85781ec29', 'article_id': '8', 'title': 'Safety Net (Forbes.com)', 'description': 'Forbes.com - After earning a PH.D. in Sociology, Danny Bazil Riley started to work as the general manager at a commercial real estate firm at an annual base salary of  #36;70,000. Soon after, a financial planner stopped by his desk to drop off brochures about insurance benefits available through his employer. But, at 32, "buying insurance was the furthest thing from my mind," says Riley.'}, {'_id': '694484ac1eb216d85781ec2a', 'article_id': '9', 'title': 'Wall St. Bears Claw Back Into the Black', 'description': " NEW YORK (Reuters) - Short-sellers, Wall Street's dwindling  band of ultra-cynics, are seeing green again."}], 'var_function-call-5747374927598452492': [{'_id': '694484ac1eb216d85781ec21', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694484ac1eb216d85781ec22', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694484ac1eb216d85781ec23', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694484ac1eb216d85781ec24', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694484ac1eb216d85781ec25', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-9425809562068439331': [{'_id': '694484ac1eb216d85781ec21', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694484ac1eb216d85781ec22', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694484ac1eb216d85781ec23', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694484ac1eb216d85781ec24', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694484ac1eb216d85781ec25', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-14907584402056121809': 5, 'var_function-call-14251754240139237620': 'file_storage/function-call-14251754240139237620.json', 'var_function-call-8001037114528835732': {'title': 'Pretty Log4J', 'length': 708, 'description': '\\\\I\'ve been a big fan of Log4J  for a while now but haven\'t migrated any code\\over for one central reason.  The following line of code:\\\\    final static Logger logger = Logger.getLogger( "some.name" );\\\\... is amazingly ugly and difficult to work with.\\\\Most people use Log4J with a logger based on the classname:\\\\So we would probably see:\\\\    static Logger logger = Logger.getLogger( "org.apache.commons.feedparser.locate.FeedLocator" );\\\\Which is amazingly verbose.  A lot of developers shorten this to:\\\\    static Logger logger = Logger.getLogger( FeedLocator.class );\\\\But this still leaves us with cut and paste errors.\\\\What if we could just reduce it to:\\\\    static Logger logger = Logger.g ...\\\\'}, 'var_function-call-5668352130803893922': [{'region': 'Asia'}, {'region': 'North America'}, {'region': 'South America'}, {'region': 'Europe'}, {'region': 'Africa'}]}

exec(code, env_args)
