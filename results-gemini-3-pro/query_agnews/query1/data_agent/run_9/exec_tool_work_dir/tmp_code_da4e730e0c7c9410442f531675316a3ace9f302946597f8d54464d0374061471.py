code = """import json
import re

file_path = locals()['var_function-call-1631278526276499272']
with open(file_path, 'r') as f:
    articles = json.load(f)

keywords = [
    'olympic', 'olympics', 'athens', 'games',
    'football', 'basketball', 'baseball', 'soccer', 'tennis', 'golf', 'hockey', 'cricket', 'rugby',
    'nfl', 'nba', 'mlb', 'nhl', 'fifa', 'uefa', 
    'wimbledon', 'us open', 'australian open', 'french open', 
    'championship', 'tournament', 'world cup', 'super bowl', 'stanley cup', 'world series',
    'gold medal', 'silver medal', 'bronze medal', 'medalist',
    'athlete', 'coach', 'quarterback', 'touchdown', 'goal', 'score', 
    'red sox', 'yankees', 'lakers', 'pistons', 'spurs', 'heat', 'knicks', 'rangers',
    'manchester united', 'real madrid', 'arsenal', 'chelsea', 'liverpool',
    'formula one', 'f1', 'nascar', 'racing', 'grand prix',
    'swimming', 'gymnastics', 'marathon', 'track and field', 'volleyball',
    'sport', 'sports'
]

# Compile regex for efficiency: look for whole words
regex = re.compile(r'\b(' + '|'.join(map(re.escape, keywords)) + r')\b', re.IGNORECASE)

candidates = []
for art in articles:
    # Check title and description
    # Check if title is clearly sports?
    # Or just check if regex matches anywhere.
    text = (art.get('title', '') + ' ' + art.get('description', ''))
    match = regex.search(text)
    if match:
        candidates.append({
            'title': art['title'],
            'description': art['description'],
            'desc_len': len(art['description']),
            'matched_keyword': match.group(0)
        })

# Sort by description length descending
candidates.sort(key=lambda x: x['desc_len'], reverse=True)

# Print top 10
print("__RESULT__:")
print(json.dumps(candidates[:10]))"""

env_args = {'var_function-call-3405305575496258850': ['articles'], 'var_function-call-8922034183929127080': [{'_id': '694469dae6ccbefbf4774406', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694469dae6ccbefbf4774407', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694469dae6ccbefbf4774408', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694469dae6ccbefbf4774409', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694469dae6ccbefbf477440a', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-2370693320005028959': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'author_id': '992', 'region': 'North America', 'publication_date': '2004-03-20'}, {'article_id': '2', 'author_id': '820', 'region': 'South America', 'publication_date': '2021-02-04'}, {'article_id': '3', 'author_id': '478', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '4', 'author_id': '39', 'region': 'Africa', 'publication_date': '2012-02-01'}], 'var_function-call-8758874876893031559': [{'_id': '694469dae6ccbefbf4774406', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694469dae6ccbefbf4774407', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694469dae6ccbefbf4774408', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694469dae6ccbefbf4774409', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694469dae6ccbefbf477440a', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-10390619581974537303': {'count': 5, 'sample_titles': ['Wall St. Bears Claw Back Into the Black (Reuters)', 'Carlyle Looks Toward Commercial Aerospace (Reuters)', "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'Oil prices soar to all-time record, posing new menace to US economy (AFP)']}, 'var_function-call-3430141558639675251': 'file_storage/function-call-3430141558639675251.json', 'var_function-call-2308637426162186490': 1000, 'var_function-call-1631278526276499272': 'file_storage/function-call-1631278526276499272.json', 'var_function-call-3706159196123938955': [{'title': 'Cavaliers, Hokies Play Host', 'desc_len': 773, 'preview': 'Akron at No. 12 Virginia &lt;br&gt;   Where:  Scot'}, {'title': 'Area College Football Capsules', 'desc_len': 761, 'preview': 'Navy at Tulsa &lt;br&gt;   Where:  Skelly Stadium '}, {'title': 'FBI Probing Suspected Israeli Spy at Pentagon', 'desc_len': 696, 'preview': 'Reuters, CNN, CBS news, and the Washington Post ar'}, {'title': 'THECHAT', 'desc_len': 631, 'preview': '&lt;em&gt; Dean Cain has spent much of his life in'}, {'title': 'The Rundown', 'desc_len': 614, 'preview': '5 LSU at 14 Auburn  3:30 p.m., WUSA-9, WJZ-13 &lt;'}, {'title': 'China Begins Countdown for Next Manned Space Flight', 'desc_len': 580, 'preview': 'By ELAINE KURTENBACH    SHANGHAI, China (AP) -- Ch'}, {'title': 'The Decline and Fall of Canada?', 'desc_len': 567, 'preview': 'The New York Times has recently run a piece ponder'}, {'title': 'Netflix, TiVo to Develop Internet Movie Product', 'desc_len': 545, 'preview': ' NEW YORK/LOS ANGELES (Reuters) - Online DVD renta'}, {'title': 'Sprint certifies QuickTime, Xserve G5 for phone media (MacCentral)', 'desc_len': 539, 'preview': 'MacCentral - Telecommunications company Sprint on '}, {'title': 'U.S. Bounces Back to Beat Greece 77-71', 'desc_len': 532, 'preview': 'ATHENS, Greece - Lamar Odom made a key defensive p'}]}

exec(code, env_args)
