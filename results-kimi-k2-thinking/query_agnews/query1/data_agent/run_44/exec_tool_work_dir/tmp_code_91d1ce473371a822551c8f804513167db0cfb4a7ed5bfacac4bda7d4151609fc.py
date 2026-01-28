code = """import json, os, re
file_path = locals().get('var_functions.query_db:4')
if not file_path or not os.path.exists(file_path):
    raise FileNotFoundError('File not found')
with open(file_path, 'r') as f:
    articles = json.load(f)

print('Total articles:', len(articles))

# Let's first look for obviously sports-related articles
sports_keywords = ['football', 'basketball', 'basket', 'nba', 'nfl', 'baseball', 'mlb', 'soccer', 'fifa', 'world cup', 'hockey', 'nhl', 'tennis', 'wimbledon', 'golf', 'pga', 'cricket', 'rugby', 'volleyball', 'olympics', 'olympic', 'gold medal', 'silver medal', 'bronze medal', 'coach', 'quarterback', 'pitcher', 'goalkeeper', 'player', 'team', 'league', 'stadium', 'arena', 'quarterfinal', 'semifinal', 'final', 'championship', 'tournament', 'match', 'game', 'score', 'points', 'goal', 'touchdown', 'home run', 'win', 'lose', 'defeat', 'victory', 'champion', 'title', 'season', 'playoff', 'playoffs']

def is_sports(text):
    if not text:
        return False
    lower = text.lower()
    # Look for whole word matches to avoid false positives
    for kw in sports_keywords:
        if re.search(r'\b' + re.escape(kw) + r'\b', lower):
            return True
    return False

sports_articles = []
for a in articles:
    combined = a.get('title', '') + ' ' + a.get('description', '')
    if is_sports(combined):
        sports_articles.append(a)

print('Sports articles found using keywords:', len(sports_articles))

if len(sports_articles) == 0:
    print('No sports articles found with strict keywords.')
    print('Let me manually scan for sports articles...')
    # Let's manually scan by looking at titles
    candidate_titles = []
    for i, a in enumerate(articles):
        title_lower = a.get('title', '').lower()
        if any(word in title_lower for word in ['olympic', 'olympics', 'nba ', 'nfl ', 'world cup', 'golf', 'tennis', 'football', 'soccer', 'basketball', 'baseball', 'hockey', 'cricket']):
            candidate_titles.append((i, a.get('title')))
    
    print('Candidate titles containing sports words:')
    for idx, title in candidate_titles[:20]:
        print(f"{idx}: {title}")

# If we found sports articles, find the one with longest description
if sports_articles:
    max_len = -1
    max_article = None
    for a in sports_articles:
        desc_len = len(a.get('description', ''))
        if desc_len > max_len:
            max_len = desc_len
            max_article = a
    
    if max_article:
        print('\nLongest sports article description:')
        print('Title:', max_article.get('title'))
        print('Description length:', max_len)
        print('Description:', max_article.get('description'))
        result_title = max_article.get('title')
    else:
        result_title = None
else:
    # Let's try a broader search to find ANY sports articles
    print('\nTrying broader search...')
    broader_keywords = ['football', 'basketball', 'soccer', 'tennis', 'golf', 'olympic', 'world cup', 'nba', 'nfl', 'mlb', 'hockey']
    candidate_articles = []
    for a in articles:
        title = a.get('title', '').lower()
        if any(kw in title for kw in broader_keywords):
            candidate_articles.append(a)
    
    print(f'Found {len(candidate_articles)} candidate articles with sports keywords in title')
    
    if candidate_articles:
        max_len = -1
        max_article = None
        for a in candidate_articles:
            desc_len = len(a.get('description', ''))
            if desc_len > max_len:
                max_len = desc_len
                max_article = a
        
        if max_article:
            print('\nLongest description among candidates:')
            print('Title:', max_article.get('title'))
            print('Description length:', max_len)
            result_title = max_article.get('title')
        else:
            result_title = None
    else:
        result_title = None
        print('No candidate sports articles found.')

print('__RESULT__:')
print(json.dumps(result_title))"""

env_args = {'var_functions.query_db:0': [{'_id': '69697f31f785858cca58a7cf', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69697f31f785858cca58a7d0', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697f31f785858cca58a7d1', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697f31f785858cca58a7d2', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697f31f785858cca58a7d3', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}, {'_id': '69697f31f785858cca58a7d4', 'article_id': '5', 'title': 'Stocks End Up, But Near Year Lows (Reuters)', 'description': 'Reuters - Stocks ended slightly higher on Friday\\but stayed near lows for the year as oil prices surged past  #36;46\\a barrel, offsetting a positive outlook from computer maker\\Dell Inc. (DELL.O)'}, {'_id': '69697f31f785858cca58a7d5', 'article_id': '6', 'title': 'Money Funds Fell in Latest Week (AP)', 'description': "AP - Assets of the nation's retail money market mutual funds fell by  #36;1.17 billion in the latest week to  #36;849.98 trillion, the Investment Company Institute said Thursday."}, {'_id': '69697f31f785858cca58a7d6', 'article_id': '7', 'title': 'Fed minutes show dissent over inflation (USATODAY.com)', 'description': 'USATODAY.com - Retail sales bounced back a bit in July, and new claims for jobless benefits fell last week, the government said Thursday, indicating the economy is improving from a midsummer slump.'}, {'_id': '69697f31f785858cca58a7d7', 'article_id': '8', 'title': 'Safety Net (Forbes.com)', 'description': 'Forbes.com - After earning a PH.D. in Sociology, Danny Bazil Riley started to work as the general manager at a commercial real estate firm at an annual base salary of  #36;70,000. Soon after, a financial planner stopped by his desk to drop off brochures about insurance benefits available through his employer. But, at 32, "buying insurance was the furthest thing from my mind," says Riley.'}, {'_id': '69697f31f785858cca58a7d8', 'article_id': '9', 'title': 'Wall St. Bears Claw Back Into the Black', 'description': " NEW YORK (Reuters) - Short-sellers, Wall Street's dwindling  band of ultra-cynics, are seeing green again."}], 'var_functions.query_db:2': [{'_id': '69697f31f785858cca58a7cf', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69697f31f785858cca58a7d0', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697f31f785858cca58a7d1', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697f31f785858cca58a7d2', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697f31f785858cca58a7d3', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:6': 'AMD starts shipping 90-nanometer chips to customers', 'var_functions.execute_python:8': 'AMD starts shipping 90-nanometer chips to customers', 'var_functions.list_db:10': ['authors', 'article_metadata'], 'var_functions.query_db:12': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'author_id': '992', 'region': 'North America', 'publication_date': '2004-03-20'}, {'article_id': '2', 'author_id': '820', 'region': 'South America', 'publication_date': '2021-02-04'}, {'article_id': '3', 'author_id': '478', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '4', 'author_id': '39', 'region': 'Africa', 'publication_date': '2012-02-01'}]}

exec(code, env_args)
