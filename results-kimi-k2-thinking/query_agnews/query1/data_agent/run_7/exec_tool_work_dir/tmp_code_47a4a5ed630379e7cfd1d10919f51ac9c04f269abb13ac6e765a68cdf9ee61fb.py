code = """import json
import os

# Load articles data
articles = locals()['var_functions.query_db:2']
if isinstance(articles, str):
    with open(articles, 'r') as f:
        articles = json.load(f)

# Define sports keywords for identification
sports_keywords = [
    'football', 'basketball', 'baseball', 'soccer', 'tennis', 'golf',
    'cricket', 'hockey', 'rugby', 'volleyball', 'boxing', 'wrestling',
    'athlete', 'olympics', 'olympic', 'marathon', 'championship', 
    'tournament', 'competition', 'medal', 'nba', 'nfl', 'mlb', 'nhl'
]

sports_articles = []

# Find sports articles based on keywords
for article in articles:
    title_lower = article.get('title', '').lower()
    desc_lower = article.get('description', '').lower()
    
    # Check if any sports keyword appears
    for keyword in sports_keywords:
        if keyword in title_lower or keyword in desc_lower:
            # Add to sports list with description length
            sports_articles.append({
                'title': article.get('title'),
                'description': article.get('description'),
                'desc_length': len(article.get('description', ''))
            })
            break

# Sort sports articles by description length (longest first)
sports_articles.sort(key=lambda x: x['desc_length'], reverse=True)

# Get the title of the sports article with the longest description
if sports_articles:
    result = sports_articles[0]['title']
else:
    result = 'No sports articles found'

# Output in required format
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:18': "Why Windows isn't Unix", 'var_functions.execute_python:20': 'AMD starts shipping 90-nanometer chips to customers', 'var_functions.list_db:22': ['authors', 'article_metadata'], 'var_functions.execute_python:26': "Why Windows isn't Unix", 'var_functions.query_db:28': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'author_id': '992', 'region': 'North America', 'publication_date': '2004-03-20'}, {'article_id': '2', 'author_id': '820', 'region': 'South America', 'publication_date': '2021-02-04'}, {'article_id': '3', 'author_id': '478', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '4', 'author_id': '39', 'region': 'Africa', 'publication_date': '2012-02-01'}], 'var_functions.query_db:30': [{'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}, {'title': 'Stocks End Up, But Near Year Lows (Reuters)', 'description': 'Reuters - Stocks ended slightly higher on Friday\\but stayed near lows for the year as oil prices surged past  #36;46\\a barrel, offsetting a positive outlook from computer maker\\Dell Inc. (DELL.O)'}, {'title': 'Money Funds Fell in Latest Week (AP)', 'description': "AP - Assets of the nation's retail money market mutual funds fell by  #36;1.17 billion in the latest week to  #36;849.98 trillion, the Investment Company Institute said Thursday."}, {'title': 'Fed minutes show dissent over inflation (USATODAY.com)', 'description': 'USATODAY.com - Retail sales bounced back a bit in July, and new claims for jobless benefits fell last week, the government said Thursday, indicating the economy is improving from a midsummer slump.'}, {'title': 'Safety Net (Forbes.com)', 'description': 'Forbes.com - After earning a PH.D. in Sociology, Danny Bazil Riley started to work as the general manager at a commercial real estate firm at an annual base salary of  #36;70,000. Soon after, a financial planner stopped by his desk to drop off brochures about insurance benefits available through his employer. But, at 32, "buying insurance was the furthest thing from my mind," says Riley.'}, {'title': 'Wall St. Bears Claw Back Into the Black', 'description': " NEW YORK (Reuters) - Short-sellers, Wall Street's dwindling  band of ultra-cynics, are seeing green again."}], 'var_functions.execute_python:34': 'China Begins Countdown for Next Manned Space Flight', 'var_functions.execute_python:36': 'China Begins Countdown for Next Manned Space Flight', 'var_functions.query_db:40': [{'title': 'Stoking the Steamroller', 'description': 'No other recording artist can channel American middle-class tastes quite like Chip Davis and his best-selling band'}, {'title': "'Madden,' 'ESPN' Football Score in Different Ways (Reuters)", 'description': 'Reuters - Was absenteeism a little high\\on Tuesday among the guys at the office? EA Sports would like\\to think it was because "Madden NFL 2005" came out that day,\\and some fans of the football simulation are rabid enough to\\take a sick day to play it.'}, {'title': 'Invasive Purple Weed May Meet Its Match (AP)', 'description': 'AP - They burned it, mowed it, sprayed it and flooded it. But nothing killed the purple loosestrife weed, which has become a regional plague, until officials at the Parker River National Wildlife Refuge set a European beetle loose on it.'}, {'title': 'The Next Great Space Race: SpaceShipOne and Wild Fire to Go For the Gold (SPACE.com)', 'description': 'SPACE.com - A piloted rocket ship race to claim a  #36;10 million Ansari X Prize purse for privately financed flight to the edge of space is heating up.'}, {'title': "Wash. State Team's Private Rocket Explodes (AP)", 'description': 'AP - A team taking a low-budget stab at the  #36;10 million Ansari X Prize for private manned spaceflight suffered a setback Sunday, when their rocket malfunctioned and exploded after shooting less than 1,000 feet in the air.'}], 'var_functions.execute_python:42': 'Technology as Fashion', 'var_functions.execute_python:46': "Why Windows isn't Unix"}

exec(code, env_args)
