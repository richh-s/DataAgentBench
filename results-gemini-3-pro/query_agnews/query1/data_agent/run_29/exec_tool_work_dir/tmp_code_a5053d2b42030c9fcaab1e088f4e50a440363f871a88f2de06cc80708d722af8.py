code = """import json
import re

file_path = locals()['var_function-call-4669942154469182092']

with open(file_path, 'r') as f:
    articles = json.load(f)

# Same keywords and logic
sports_kws = {
    'sport', 'sports', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'hockey', 'olympic', 'olympics', 
    'athens', 'medal', 'medals', 'gold', 'silver', 'bronze', 'champion', 'champions', 'championship', 'tournament', 
    'cup', 'league', 'game', 'games', 'match', 'matches', 'score', 'scores', 'team', 'teams', 'coach', 'coaches', 
    'athlete', 'athletes', 'nfl', 'nba', 'mlb', 'nhl', 'fifa', 'wta', 'atp', 'pga', 'racing', 'f1', 'nascar', 
    'boxing', 'swim', 'swimming', 'swimmer', 'run', 'runner', 'running', 'marathon', 'wrestling', 'gymnastics', 
    'volleyball', 'rugby', 'cricket', 'doping', 'record', 'records', 'red sox', 'yankees', 'lakers', 'patriots', 
    'united', 'real madrid', 'arsenal', 'chelsea', 'liverpool', 'milan', 'juventus', 'barcelona', 'cowboys', 
    '49ers', 'giants', 'jets', 'mets', 'rangers', 'knicks', 'bulls', 'pistons', 'pacers', 'heat', 'magic', 'suns', 
    'spurs', 'rockets', 'mavericks', 'stars', 'lightning', 'flames', 'oilers', 'canucks', 'leafs', 'canadiens', 
    'senators', 'eagles', 'steelers', 'bengals', 'browns', 'ravens', 'titans', 'colts', 'jaguars', 'texans', 
    'bills', 'dolphins', 'saints', 'falcons', 'panthers', 'buccaneers', 'vikings', 'packers', 'lions', 'bears', 
    'seahawks', 'rams', 'cardinals', 'raiders', 'broncos', 'chiefs', 'chargers', 'redskins', 'wizards', 'nationals', 
    'orioles', 'phillies', 'braves', 'marlins', 'twins', 'tigers', 'indians', 'royals', 'white sox', 'angels', 
    'athletics', 'mariners', 'blue jays', 'devil rays', 'diamondbacks', 'rockies', 'padres', 'dodgers', 'pirates', 
    'reds', 'cubs', 'astros', 'brewers', 'grand prix', 'super bowl', 'world series', 'stanley cup', 'wimbledon', 
    'us open', 'french open', 'australian open', 'masters'
}

def clean_and_tokenize(text):
    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text.lower())
    return set(text.split())

def is_sports(title, desc):
    text = title + " " + desc
    tokens = clean_and_tokenize(text)
    
    s_score = len(tokens.intersection(sports_kws))
    
    if 'olympic' in tokens or 'olympics' in tokens: s_score += 5
    if 'athens' in tokens: s_score += 3
    if 'medal' in tokens: s_score += 2
    
    # Penalties
    if 'stock' in tokens or 'market' in tokens or 'economy' in tokens: s_score -= 10
    if 'software' in tokens or 'computer' in tokens or 'java' in tokens: s_score -= 10
    if 'iraq' in tokens or 'war' in tokens: s_score -= 10
    
    return s_score

candidates = []
for a in articles:
    score = is_sports(a['title'], a['description'])
    if score >= 3: # Threshold
        candidates.append(a)

if candidates:
    # Sort by description length descending
    candidates.sort(key=lambda x: len(x['description']), reverse=True)
    best = candidates[0]
    result = {
        "title": best['title'],
        "desc_len": len(best['description']),
        "description": best['description'],
        "score": is_sports(best['title'], best['description'])
    }
else:
    result = {"error": "No candidates"}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-17957500709340990638': ['articles'], 'var_function-call-17957500709340988297': ['authors', 'article_metadata'], 'var_function-call-16327477412725333731': [{'_id': '6944784ccb63a7dc9ff11c96', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944784ccb63a7dc9ff11c97', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944784ccb63a7dc9ff11c98', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944784ccb63a7dc9ff11c99', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944784ccb63a7dc9ff11c9a', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}, {'_id': '6944784ccb63a7dc9ff11c9b', 'article_id': '5', 'title': 'Stocks End Up, But Near Year Lows (Reuters)', 'description': 'Reuters - Stocks ended slightly higher on Friday\\but stayed near lows for the year as oil prices surged past  #36;46\\a barrel, offsetting a positive outlook from computer maker\\Dell Inc. (DELL.O)'}, {'_id': '6944784ccb63a7dc9ff11c9c', 'article_id': '6', 'title': 'Money Funds Fell in Latest Week (AP)', 'description': "AP - Assets of the nation's retail money market mutual funds fell by  #36;1.17 billion in the latest week to  #36;849.98 trillion, the Investment Company Institute said Thursday."}, {'_id': '6944784ccb63a7dc9ff11c9d', 'article_id': '7', 'title': 'Fed minutes show dissent over inflation (USATODAY.com)', 'description': 'USATODAY.com - Retail sales bounced back a bit in July, and new claims for jobless benefits fell last week, the government said Thursday, indicating the economy is improving from a midsummer slump.'}, {'_id': '6944784ccb63a7dc9ff11c9e', 'article_id': '8', 'title': 'Safety Net (Forbes.com)', 'description': 'Forbes.com - After earning a PH.D. in Sociology, Danny Bazil Riley started to work as the general manager at a commercial real estate firm at an annual base salary of  #36;70,000. Soon after, a financial planner stopped by his desk to drop off brochures about insurance benefits available through his employer. But, at 32, "buying insurance was the furthest thing from my mind," says Riley.'}, {'_id': '6944784ccb63a7dc9ff11c9f', 'article_id': '9', 'title': 'Wall St. Bears Claw Back Into the Black', 'description': " NEW YORK (Reuters) - Short-sellers, Wall Street's dwindling  band of ultra-cynics, are seeing green again."}], 'var_function-call-16660690882308850022': [{'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-8419400322356387724': {'count_sports': 1, 'total_articles': 5, 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'desc_len': 94, 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, 'var_function-call-15737859402229921472': [{'_id': '6944784ccb63a7dc9ff11c96', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944784ccb63a7dc9ff11c97', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944784ccb63a7dc9ff11c98', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944784ccb63a7dc9ff11c99', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944784ccb63a7dc9ff11c9a', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-4669942154469182092': 'file_storage/function-call-4669942154469182092.json', 'var_function-call-6111710585321670497': {'title': 'RuntimeProperties... Reflection from System Properties', 'desc_len': 708, 'description': '\\\\Java developers often load system properties to customize the runtime behavior\\of their applications.\\\\For example a develoepr could define a \'max_connections\' system property to\\define the maximum number of TCP connections that their application server can\\support.  While nice, this prevents all other applications from using this\\variable name.\\\\The first reaction to this would be to namespace your variable names.  Instead\\of using max_connections you would now use\\\'my.application.Server.MAX_CONNECTIONS\' as your property name.  This works of\\course but now you have to load this property on startup.\\\\public static int MAX_CONNECTIONS = Integer.parseInt( System.getProperty(\\"my.application.Se ...\\\\'}, 'var_function-call-10772560907913926086': {'title': 'Michael Phelps Wins Second Gold Medal (AP)', 'desc_len': 416, 'description': "AP - Michael Phelps, denied in his bid to win seven gold medals, picked up his second victory of the Athens Games by winning the 200-meter butterfly Tuesday night in Olympic-record time. Phelps fell just short of his own world record, holding off Takashi Yamamoto to win in 1 minute, 54.01 seconds. The hard-charging Japanese swimmer took silver in 1:54.56, while Great Britain's Stephen Parry won bronze in 1:55.22.", 'score': 20}}

exec(code, env_args)
