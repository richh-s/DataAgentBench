code = """import json

# Access the data
data = locals()['var_function-call-16660690882308850022']

# If data is a string (file path), load it
if isinstance(data, str):
    with open(data, 'r') as f:
        articles = json.load(f)
else:
    articles = data

# Define keywords
keywords = {
    'Sports': ['sport', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'hockey', 'olympic', 'athens', 'medal', 'gold', 'silver', 'bronze', 'champion', 'tournament', 'cup', 'league', 'game', 'match', 'score', 'team', 'coach', 'athlete', 'nfl', 'nba', 'mlb', 'nhl', 'fifa', 'wta', 'atp', 'pga', 'racing', 'f1', 'nascar', 'boxing', 'swim', 'run', 'marathon', 'wrestling', 'gymnastics', 'volleyball', 'rugby', 'cricket', 'doping', 'record', 'red sox', 'yankees', 'lakers', 'patriots', 'united', 'real madrid', 'arsenal', 'chelsea', 'liverpool', 'milan', 'juventus', 'barcelona', 'cowboys', '49ers', 'giants', 'jets', 'mets', 'rangers', 'knicks', 'bulls', 'pistons', 'pacers', 'heat', 'magic', 'suns', 'spurs', 'rockets', 'mavericks', 'stars', 'lightning', 'flames', 'oilers', 'canucks', 'leafs', 'canadiens', 'senators', 'eagles', 'steelers', 'bengals', 'browns', 'ravens', 'titans', 'colts', 'jaguars', 'texans', 'bills', 'dolphins', 'saints', 'falcons', 'panthers', 'buccaneers', 'vikings', 'packers', 'lions', 'bears', 'seahawks', 'rams', 'cardinals', 'raiders', 'broncos', 'chiefs', 'chargers', 'redskins', 'wizards', 'nationals', 'orioles', 'phillies', 'braves', 'marlins', 'twins', 'tigers', 'indians', 'royals', 'white sox', 'angels', 'athletics', 'mariners', 'blue jays', 'devil rays', 'diamondbacks', 'rockies', 'padres', 'dodgers', 'pirates', 'reds', 'cubs', 'astros', 'brewers'],
    'Business': ['oil', 'price', 'stock', 'market', 'wall st', 'profit', 'loss', 'earn', 'share', 'dollar', 'euro', 'yen', 'bank', 'fed', 'rate', 'inflation', 'economy', 'job', 'sale', 'deal', 'merger', 'acquisition', 'corp', 'company', 'inc', 'ltd', 'ceo', 'cfo', 'google', 'ipo', 'airline', 'boeing', 'airbus', 'wal-mart', 'exxon', 'gm', 'ford', 'toyota', 'microsoft', 'intel', 'ibm', 'oracle', 'cisco', 'dell', 'hp', 'nyse', 'nasdaq', 'dow', 's&p', 'bond', 'fund', 'invest'],
    'Sci/Tech': ['computer', 'software', 'microsoft', 'intel', 'internet', 'web', 'virus', 'worm', 'space', 'nasa', 'moon', 'mars', 'orbit', 'science', 'study', 'research', 'phone', 'mobile', 'wireless', 'tech', 'chip', 'linux', 'apple', 'ipod', 'digital', 'camera', 'game', 'video', 'sony', 'nintendo', 'console', 'browser', 'search', 'email', 'spam', 'hacker', 'security', 'biotech', 'genome', 'cloning', 'stem cell', 'drug', 'fda', 'health', 'disease', 'cancer', 'aids', 'hiv'],
    'World': ['iraq', 'iran', 'palestine', 'israel', 'bush', 'kerry', 'election', 'president', 'minister', 'prime', 'official', 'police', 'kill', 'bomb', 'blast', 'war', 'truce', 'treaty', 'un', 'nation', 'country', 'china', 'russia', 'darfur', 'sudan', 'gaza', 'baghdad', 'najaf', 'korea', 'afghanistan', 'pakistan', 'india', 'terror', 'qaeda', 'bin laden', 'military', 'army', 'troop', 'soldier', 'rebel', 'guerrilla', 'kidnap', 'hostage', 'crash', 'storm', 'hurricane', 'typhoon', 'quake', 'flood']
}

# Note: 'game' is in both Sports and Sci/Tech (video games). I should check context or prioritize.
# Note: 'microsoft', 'intel' etc. are in both Business and Sci/Tech.

def classify(text):
    text = text.lower()
    scores = {cat: 0 for cat in keywords}
    for cat, words in keywords.items():
        for word in words:
            if word in text:
                scores[cat] += 1
    
    # Heuristics to resolve ties or common words
    # 'game' is tricky. If 'video' or 'console' or 'software' appears, it's Tech. If 'team' or 'score' or 'win' appears, it's Sports.
    
    if scores['Sports'] > 0 and scores['Sci/Tech'] > 0:
        if any(w in text for w in ['video', 'console', 'nintendo', 'sony', 'xbox', 'ps2', 'doom', 'quake', 'software']):
             scores['Sci/Tech'] += 2
        if any(w in text for w in ['team', 'coach', 'medal', 'olympic', 'stadium', 'ball']):
             scores['Sports'] += 2
             
    # Pick max
    return max(scores, key=scores.get)

sports_articles = []
for article in articles:
    text = article['title'] + " " + article['description']
    cat = classify(text)
    if cat == 'Sports':
        sports_articles.append(article)

# Find the one with max description length
if sports_articles:
    longest_sports_article = max(sports_articles, key=lambda x: len(x['description']))
    result = {
        "count_sports": len(sports_articles),
        "total_articles": len(articles),
        "title": longest_sports_article['title'],
        "desc_len": len(longest_sports_article['description']),
        "description": longest_sports_article['description'] # Printing description to verify
    }
else:
    result = {"count_sports": 0, "total_articles": len(articles)}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-17957500709340990638': ['articles'], 'var_function-call-17957500709340988297': ['authors', 'article_metadata'], 'var_function-call-16327477412725333731': [{'_id': '6944784ccb63a7dc9ff11c96', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944784ccb63a7dc9ff11c97', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944784ccb63a7dc9ff11c98', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944784ccb63a7dc9ff11c99', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944784ccb63a7dc9ff11c9a', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}, {'_id': '6944784ccb63a7dc9ff11c9b', 'article_id': '5', 'title': 'Stocks End Up, But Near Year Lows (Reuters)', 'description': 'Reuters - Stocks ended slightly higher on Friday\\but stayed near lows for the year as oil prices surged past  #36;46\\a barrel, offsetting a positive outlook from computer maker\\Dell Inc. (DELL.O)'}, {'_id': '6944784ccb63a7dc9ff11c9c', 'article_id': '6', 'title': 'Money Funds Fell in Latest Week (AP)', 'description': "AP - Assets of the nation's retail money market mutual funds fell by  #36;1.17 billion in the latest week to  #36;849.98 trillion, the Investment Company Institute said Thursday."}, {'_id': '6944784ccb63a7dc9ff11c9d', 'article_id': '7', 'title': 'Fed minutes show dissent over inflation (USATODAY.com)', 'description': 'USATODAY.com - Retail sales bounced back a bit in July, and new claims for jobless benefits fell last week, the government said Thursday, indicating the economy is improving from a midsummer slump.'}, {'_id': '6944784ccb63a7dc9ff11c9e', 'article_id': '8', 'title': 'Safety Net (Forbes.com)', 'description': 'Forbes.com - After earning a PH.D. in Sociology, Danny Bazil Riley started to work as the general manager at a commercial real estate firm at an annual base salary of  #36;70,000. Soon after, a financial planner stopped by his desk to drop off brochures about insurance benefits available through his employer. But, at 32, "buying insurance was the furthest thing from my mind," says Riley.'}, {'_id': '6944784ccb63a7dc9ff11c9f', 'article_id': '9', 'title': 'Wall St. Bears Claw Back Into the Black', 'description': " NEW YORK (Reuters) - Short-sellers, Wall Street's dwindling  band of ultra-cynics, are seeing green again."}], 'var_function-call-16660690882308850022': [{'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
