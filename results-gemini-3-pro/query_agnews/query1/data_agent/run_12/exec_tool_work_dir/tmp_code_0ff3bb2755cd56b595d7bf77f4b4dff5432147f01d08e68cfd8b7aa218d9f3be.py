code = """import json
import string

file_path = locals()['var_function-call-7359036917075943210']
with open(file_path, 'r') as f:
    articles = json.load(f)

sports_keywords = {
    'sport', 'sports', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'hockey', 'cricket', 'rugby', 
    'olympic', 'olympics', 'medal', 'gold', 'silver', 'bronze', 'athlete', 'athletes', 'coach', 'team', 'teams', 
    'league', 'cup', 'championship', 'tournament', 'game', 'match', 'score', 'scores', 'win', 'won', 'loss', 'lost', 
    'victory', 'defeat', 'player', 'players', 'quarterback', 'pitcher', 'batter', 'touchdown', 'goal', 'basket', 
    'nfl', 'nba', 'mlb', 'nhl', 'fifa', 'uefa', 'wimbledon', 'grand slam', 'world cup', 'super bowl', 'playoff', 
    'race', 'racing', 'f1', 'formula one', 'nascar', 'driver', 'marathon', 'sprint', 'relay', 'swimming', 'gymnastics',
    'boxing', 'wrestling', 'stadium', 'arena', 'athens', 'greece', 'red sox', 'yankees', 'mets', 'dodgers', 'lakers',
    'bulls', 'celtics', 'knicks', 'rangers', 'eagles', 'patriots', 'steelers', 'packers', 'cowboys', '49ers', 'raiders',
    'arsenal', 'chelsea', 'liverpool', 'manchester', 'real madrid', 'barcelona', 'ac milan', 'juventus', 'inter milan',
    'bayern munich', 'dortmund', 'paris st germain', 'psg', 'davis cup', 'ryder cup', 'masters', 'us open', 'australian open',
    'french open', 'pga', 'lpga', 'tour de france', 'armstrong', 'schumacher', 'woods', 'federer', 'roddick', 'williams',
    'sharapova', 'kobe', 'shaq', 'lebron', 'jordan', 'beckham', 'ronaldo', 'zidane', 'owens', 'manning', 'brady', 'favre'
}

business_keywords = {
    'business', 'market', 'markets', 'stock', 'stocks', 'share', 'shares', 'economy', 'economic', 'finance', 'financial',
    'invest', 'investment', 'investor', 'bank', 'banks', 'dollar', 'euro', 'yen', 'currency', 'oil', 'price', 'prices',
    'profit', 'loss', 'quarter', 'revenue', 'earnings', 'ipo', 'merger', 'acquisition', 'deal', 'company', 'companies',
    'corp', 'inc', 'ltd', 'ceo', 'cfo', 'fed', 'federal reserve', 'rates', 'inflation', 'trade', 'deficit', 'surplus',
    'wall', 'street', 'dow', 'nasdaq', 'bond', 'bonds', 'reuters', 'bloomberg', 'nyse', 'amex'
}

scitech_keywords = {
    'science', 'technology', 'tech', 'computer', 'computers', 'software', 'hardware', 'internet', 'web', 'online',
    'google', 'microsoft', 'apple', 'ibm', 'intel', 'linux', 'windows', 'virus', 'worm', 'security', 'hacker',
    'space', 'nasa', 'shuttle', 'mars', 'moon', 'orbit', 'astronomy', 'biology', 'physics', 'chemistry', 'research',
    'study', 'scientist', 'scientists', 'lab', 'laboratory', 'cell', 'gene', 'genome', 'medical', 'medicine', 'drug',
    'cancer', 'disease', 'health', 'mobile', 'phone', 'wireless', 'broadband', 'chip', 'processor', 'spam', 'search engine',
    'browser', 'server', 'network', 'satellite', 'telescope', 'robot', 'robotics', 'nanotech', 'stem cell'
}

world_keywords = {
    'world', 'international', 'politics', 'government', 'president', 'prime minister', 'minister', 'official',
    'election', 'vote', 'voters', 'campaign', 'candidate', 'war', 'peace', 'military', 'army', 'troops', 'soldier',
    'soldiers', 'iraq', 'iran', 'afghanistan', 'israel', 'palestine', 'china', 'russia', 'usa', 'un', 'united nations',
    'treaty', 'agreement', 'nuclear', 'bomb', 'blast', 'explosion', 'attack', 'terror', 'terrorist', 'terrorism',
    'rebel', 'rebels', 'police', 'court', 'trial', 'judge', 'law', 'legal', 'congress', 'senate', 'parliament',
    'baghdad', 'korea', 'darfur', 'sudan', 'gaza', 'fallujah', 'kabul', 'tehran', 'moscow', 'beijing', 'washington',
    'london', 'madrid', 'paris', 'berlin', 'tokyo', 'premier', 'governor', 'democrat', 'republican', 'bush', 'kerry',
    'putin', 'blair', 'chirac', 'schroeder', 'koizumi', 'arose', 'hostage', 'kidnap', 'sanctions'
}

def classify(text):
    text = text.lower()
    # Replace punctuation with space
    for char in string.punctuation:
        text = text.replace(char, ' ')
    tokens = set(text.split())
    
    scores = {
        'Sports': len(tokens.intersection(sports_keywords)),
        'Business': len(tokens.intersection(business_keywords)),
        'Sci/Tech': len(tokens.intersection(scitech_keywords)),
        'World': len(tokens.intersection(world_keywords))
    }
    
    if sum(scores.values()) == 0:
        return None
    
    return max(scores, key=scores.get)

sports_candidates = []
for art in articles:
    content = (art.get('title', '') + " " + art.get('description', ''))
    if classify(content) == 'Sports':
        sports_candidates.append(art)

# Sort by description length descending
sports_candidates.sort(key=lambda x: len(x.get('description', '')), reverse=True)

# Get top result
if sports_candidates:
    top = sports_candidates[0]
    res = {
        "title": top['title'],
        "len": len(top['description']),
        "desc": top['description']
    }
else:
    res = {"error": "No sports articles found"}

print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_function-call-14460016368639222028': ['articles'], 'var_function-call-14460016368639224981': ['authors', 'article_metadata'], 'var_function-call-14109477459473775675': [{'_id': '69446beedd796e99613ec2ac', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69446beedd796e99613ec2ad', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69446beedd796e99613ec2ae', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69446beedd796e99613ec2af', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69446beedd796e99613ec2b0', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-14109477459473772956': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'author_id': '992', 'region': 'North America', 'publication_date': '2004-03-20'}, {'article_id': '2', 'author_id': '820', 'region': 'South America', 'publication_date': '2021-02-04'}, {'article_id': '3', 'author_id': '478', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '4', 'author_id': '39', 'region': 'Africa', 'publication_date': '2012-02-01'}], 'var_function-call-12709903721171023210': [{'_id': '69446beedd796e99613ec2ac', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69446beedd796e99613ec2ad', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69446beedd796e99613ec2ae', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69446beedd796e99613ec2af', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69446beedd796e99613ec2b0', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-11205666105338504994': [{'_id': '69446beedd796e99613ec2ac', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69446beedd796e99613ec2ad', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69446beedd796e99613ec2ae', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69446beedd796e99613ec2af', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69446beedd796e99613ec2b0', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-14554890964508606111': 5, 'var_function-call-3474523854322095635': 'file_storage/function-call-3474523854322095635.json', 'var_function-call-2315724581832008923': {'error': 'No sports articles found'}, 'var_function-call-17104906858817236311': [{'_id': '69446beedd796e99613ec2ac', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69446beedd796e99613ec2ad', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69446beedd796e99613ec2ae', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69446beedd796e99613ec2af', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69446beedd796e99613ec2b0', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-5729926315226506181': [{'_id': '69446beedd796e99613ee9bd', 'article_id': '10001', 'title': 'Jacobsen Skips Hartford to Play Tradition (AP)', 'description': 'AP - Last year, Peter Jacobsen was too young to play in the Tradition. This year, he has already won a major on the Champions Tour as he readies for his debut in the tournament he helped bring to his home state.'}, {'_id': '69446beedd796e99613ee9be', 'article_id': '10002', 'title': 'Alta prison bans pedophile from socials with kids that fuel his fantasies (Canadian Press)', 'description': "Canadian Press - WINNIPEG (CP) - A medium-security prison in Alberta has banned a Manitoba pedophile from social functions with the children of other inmates following the man's admission that the events fuel his sexual fantasies."}, {'_id': '69446beedd796e99613ee9bf', 'article_id': '10003', 'title': "Olympics: Fame But Questions for Greece's New Heroine", 'description': " ATHENS (Reuters) - Fani Halkia hurtled from virtual  obscurity to become Olympic women's 400 meters hurdles champion  on Wednesday, giving Greece a new sports diva to hail but  sparking a barrage of questions over her rise to prominence."}, {'_id': '69446beedd796e99613ee9c0', 'article_id': '10004', 'title': 'U.S. Expresses Concern About UAL Pensions', 'description': ' WASHINGTON (Reuters) - The Bush administration expressed  fresh concern on Wednesday about the possibility bankrupt  United Airlines &lt;A HREF="http://www.investor.reuters.com/FullQuote.aspx?ticker=UALAQ.OB target=/stocks/quickinfo/fullquote"&gt;UALAQ.OB&lt;/A&gt; might scrap its employee pension  plans, which would shift the burden of paying benefits to the  government.'}, {'_id': '69446beedd796e99613ee9c1', 'article_id': '10005', 'title': 'Nikkei Seen Firming After 11,000 Cleared', 'description': " TOKYO (Reuters) - Japan's Nikkei average is expected to  extend gains on Thursday as investors keep a healthy appetite  for blue-chip exporters after a fall in oil prices boosted  confidence over the U.S. economy and lifted Wall Street stocks."}], 'var_function-call-7359036917075943210': 'file_storage/function-call-7359036917075943210.json', 'var_function-call-2248939482407386105': 127600, 'var_function-call-476224062517708366': [], 'var_function-call-17779117529654483044': [{'_id': '69446beedd796e99613ec2ac', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69446beedd796e99613ec2ad', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69446beedd796e99613ec2ae', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}], 'var_function-call-9423884618101550442': {'title': "Olympics: Fame But Questions for Greece's New Heroine", 'intersection': []}, 'var_function-call-13208182005589552156': {'tokens_preview': [], 'has_olympics': False, 'has_Olympics': False, 'text_preview': "olympics: fame but questions for greece's new heroine  athens (reuters) - fani halkia hurtled from virtual  obscurity to become olympic women's 400 meters hurdles champion  on wednesday, giving greece a new sports diva to hail but  sparking a barrage of questions over her rise to prominence."}}

exec(code, env_args)
