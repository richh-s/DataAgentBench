code = """import json

# Read the full result from the file
file_path = locals()['var_functions.query_db:12']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Define a comprehensive set of sports keywords
sports_keywords = [
    'sport', 'sports', 'game', 'games', 'football', 'basketball', 'baseball',
    'soccer', 'tennis', 'golf', 'hockey', 'cricket', 'rugby', 'volleyball',
    'badminton', 'squash', 'athlete', 'athletes', 'olympic', 'olympics',
    'championship', 'championships', 'tournament', 'tournaments', 'league',
    'playoffs', 'finals', 'coach', 'coaching', 'player', 'players',
    'team', 'teams', 'match', 'matches', 'nba', 'nfl', 'mlb', 'nhl',
    'world cup', 'super bowl', 'world series', 'race', 'racing', 'marathon',
    'boxing', 'wrestling', 'swimming', 'cycling', 'ski', 'skating',
    'sailing', 'fencing', 'judo', 'karate', 'mma', 'ufc', 'fifa', 'ncaa',
    'competition', 'competitor', 'competitors'
]

sports_articles = []

for article in articles:
    title_lower = article['title'].lower()
    desc_lower = article['description'].lower()
    
    # Check if it's a sports article
    is_sports = False
    for keyword in sports_keywords:
        if keyword in title_lower or keyword in desc_lower:
            is_sports = True
            break
    
    if is_sports:
        sports_articles.append({
            'article_id': article['article_id'],
            'title': article['title'],
            'description': article['description'],
            'description_length': len(article['description'])
        })

# Sort by description length descending
sports_articles_sorted = sorted(sports_articles, key=lambda x: x['description_length'], reverse=True)

# Get the top 5 to verify
if sports_articles_sorted:
    top_5 = sports_articles_sorted[:5]
    result = json.dumps(top_5)
else:
    result = json.dumps([])

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': [{'_id': '696963af5c1273d15c5e3718', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '696963af5c1273d15c5e3719', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '696963af5c1273d15c5e371a', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '696963af5c1273d15c5e371b', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '696963af5c1273d15c5e371c', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:2': [{'_id': '696963af5c1273d15c5e3718', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '696963af5c1273d15c5e3719', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '696963af5c1273d15c5e371a', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '696963af5c1273d15c5e371b', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '696963af5c1273d15c5e371c', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:5': [{'_id': '696963af5c1273d15c5e3718', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '696963af5c1273d15c5e3719', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '696963af5c1273d15c5e371a', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '696963af5c1273d15c5e371b', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '696963af5c1273d15c5e371c', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:6': [{'_id': '696963af5c1273d15c5e3718', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '696963af5c1273d15c5e3719', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '696963af5c1273d15c5e371a', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '696963af5c1273d15c5e371b', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '696963af5c1273d15c5e371c', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:18': ["Why Windows isn't Unix"], 'var_functions.list_db:20': ['authors', 'article_metadata'], 'var_functions.query_db:22': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'author_id': '992', 'region': 'North America', 'publication_date': '2004-03-20'}, {'article_id': '2', 'author_id': '820', 'region': 'South America', 'publication_date': '2021-02-04'}, {'article_id': '3', 'author_id': '478', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '4', 'author_id': '39', 'region': 'Africa', 'publication_date': '2012-02-01'}, {'article_id': '5', 'author_id': '802', 'region': 'Africa', 'publication_date': '2011-02-21'}, {'article_id': '6', 'author_id': '156', 'region': 'North America', 'publication_date': '2017-09-20'}, {'article_id': '7', 'author_id': '570', 'region': 'Europe', 'publication_date': '2022-12-23'}, {'article_id': '8', 'author_id': '272', 'region': 'Africa', 'publication_date': '2011-03-30'}, {'article_id': '9', 'author_id': '399', 'region': 'Europe', 'publication_date': '2016-05-24'}], 'var_functions.query_db:24': [{'_id': '696963af5c1273d15c5e37f2', 'article_id': '218', 'title': 'GAO Calls Stryker Too Heavy for Transport', 'description': "The Army's new medium-weight armored vehicle, the Stryker, weighs so much that it curtails the range of C-130 military cargo aircraft that carry it and under certain conditions make it impossible for the planes to take off, a new report for Congress found."}, {'_id': '696963af5c1273d15c5e381c', 'article_id': '260', 'title': 'Ancient Olympics Mixed Naked Sports, Pagan Partying', 'description': 'Nude athletes, performance-enhancing lizard meat, and animal sacrifices are just a few of the things that separate the ancient Olympics from the modern games, says the author of &lt;i&gt;The Naked Olympics.&lt;/i&gt;'}, {'_id': '696963af5c1273d15c5e39f9', 'article_id': '737', 'title': 'Space-age sport ', 'description': "GPS is invading recreational sports. Under clear skies, those signals beaming to earth from satellites can find you on a hilly running trail, in a kayak on the ocean, or on a green fairway where you're trying to fade a 230-yard drive into the wind."}, {'_id': '696963af5c1273d15c5e3a92', 'article_id': '890', 'title': 'Briefly: AOL kicks off free fantasy sports', 'description': "roundup Plus: HP partners with 3G gear maker...AMD starts shipping 90-nanometer chips...ABC.com to air on Real's SuperPass."}, {'_id': '696963af5c1273d15c5e3ba9', 'article_id': '1169', 'title': "Catching 'phishers' a WholeSecurity sport", 'description': 'Tool that identifies sites pretending to be connected to banks, eBay and more could help leave "phishing" scammers dead in the water.'}]}

exec(code, env_args)
