code = """import json
import re

# Load the articles data
query_result = locals()['var_functions.query_db:10']

# If the result is a file path, read the file
if isinstance(query_result, str) and query_result.endswith('.json'):
    with open(query_result, 'r') as f:
        articles = json.load(f)
else:
    articles = query_result

# Define more specific sports keywords
sports_keywords = [
    'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 
    'olympic', 'olympics', 'athlete', 'athletes',
    'nba', 'nfl', 'mlb', 'nhl', 'racing', 'marathon', 'boxing',
    'hockey', 'world cup', 'league', 'match', 'game', 'player',
    'championship', 'tournament', 'cup', 'coach', 'team', 'sport'
]

# Define anti-keywords to exclude non-sports
anti_keywords = ['video game', 'computer game', 'gaming', 'stock market', 'business', 'political game', 'economic']

# Find sports articles
sports_articles = []

for article in articles:
    title = article['title'].lower()
    description = article['description'].lower()
    
    # Skip if contains anti-keywords
    skip = False
    for anti in anti_keywords:
        if anti in title or anti in description:
            skip = True
            break
    
    if skip:
        continue
    
    # Check for sports keywords
    for keyword in sports_keywords:
        if keyword in title or keyword in description:
            sports_articles.append(article)
            break

# Among sports articles, find the one with the longest description
max_length = 0
longest_sports_article = None

for article in sports_articles:
    desc_length = len(article['description'])
    if desc_length > max_length:
        max_length = desc_length
        longest_sports_article = article

# Print results
result = {
    "total_sports_articles": len(sports_articles),
    "max_description_length": max_length,
    "longest_sports_article": longest_sports_article
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': [{'_id': '6969800f3524e9056f8f7620', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969800f3524e9056f8f7621', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969800f3524e9056f8f7622', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969800f3524e9056f8f7623', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969800f3524e9056f8f7624', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}, {'_id': '6969800f3524e9056f8f7625', 'article_id': '5', 'title': 'Stocks End Up, But Near Year Lows (Reuters)', 'description': 'Reuters - Stocks ended slightly higher on Friday\\but stayed near lows for the year as oil prices surged past  #36;46\\a barrel, offsetting a positive outlook from computer maker\\Dell Inc. (DELL.O)'}, {'_id': '6969800f3524e9056f8f7626', 'article_id': '6', 'title': 'Money Funds Fell in Latest Week (AP)', 'description': "AP - Assets of the nation's retail money market mutual funds fell by  #36;1.17 billion in the latest week to  #36;849.98 trillion, the Investment Company Institute said Thursday."}, {'_id': '6969800f3524e9056f8f7627', 'article_id': '7', 'title': 'Fed minutes show dissent over inflation (USATODAY.com)', 'description': 'USATODAY.com - Retail sales bounced back a bit in July, and new claims for jobless benefits fell last week, the government said Thursday, indicating the economy is improving from a midsummer slump.'}, {'_id': '6969800f3524e9056f8f7628', 'article_id': '8', 'title': 'Safety Net (Forbes.com)', 'description': 'Forbes.com - After earning a PH.D. in Sociology, Danny Bazil Riley started to work as the general manager at a commercial real estate firm at an annual base salary of  #36;70,000. Soon after, a financial planner stopped by his desk to drop off brochures about insurance benefits available through his employer. But, at 32, "buying insurance was the furthest thing from my mind," says Riley.'}, {'_id': '6969800f3524e9056f8f7629', 'article_id': '9', 'title': 'Wall St. Bears Claw Back Into the Black', 'description': " NEW YORK (Reuters) - Short-sellers, Wall Street's dwindling  band of ultra-cynics, are seeing green again."}], 'var_functions.query_db:2': [{'_id': '6969800f3524e9056f8f7620', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969800f3524e9056f8f7621', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969800f3524e9056f8f7622', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969800f3524e9056f8f7623', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969800f3524e9056f8f7624', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:8': [{'_id': '6969800f3524e9056f8f7620', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969800f3524e9056f8f7621', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969800f3524e9056f8f7622', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969800f3524e9056f8f7623', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969800f3524e9056f8f7624', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': 1000, 'var_functions.execute_python:14': 'Total articles: 1000', 'var_functions.execute_python:16': {'total_articles': 1000, 'first_sample': {'_id': '6969800f3524e9056f8f7620', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}}, 'var_functions.execute_python:18': {'total_articles': 1000, 'samples': [{'title': 'Comets, Asteroids and Planets around a Nearby Star (SPACE.com)', 'description': 'SPACE.com - A nearby star thought to harbor comets and asteroids now appears to be home to planets, too. The presumed worlds are smaller than Jupiter and could be as tiny as Pluto, new observations suggest.'}, {'title': 'Perseid Meteor Shower Peaks Overnight (SPACE.com)', 'description': 'SPACE.com - A fine display of shooting stars is underway and peaks overnight Wednesday into early Thursday morning. Astronomers expect the 2004 Perseid meteor shower to be one of the best versions of the annual event in several years.'}, {'title': 'Redesigning Rockets: NASA Space Propulsion Finds a New Home (SPACE.com)', 'description': 'SPACE.com - While the exploration of the Moon and other planets in our solar system is nbsp;exciting, the first task for astronauts and robots alike is to actually nbsp;get to those destinations.'}, {'title': 'Studies Find Rats Can Get Hooked on Drugs (AP)', 'description': "AP - Rats can become drug addicts. That's important to know, scientists say, and has taken a long time to prove. Now two studies by French and British researchers show the animals exhibit the same compulsive drive for cocaine as people do once they're truly hooked."}, {'title': "NASA Chief: 'Let's Go Save the Hubble' (SPACE.com)", 'description': "SPACE.com - Amid uncertainty over the fate of the Hubble Space Telescope and with a key instrument not working, NASA Administrator Sean O'Keefe gave the go-ahead Monday for planning a robotic servicing mission."}, {'title': 'Armadillo Aerospaces X Prize Prototype Crashes (SPACE.com)', 'description': 'SPACE.com - Armadillo Aerospace of Mesquite, Texas has reported a \\crash last weekend of their prototype X Prize rocket.'}, {'title': "Prairie Dog Won't Be on Endangered List (AP)", 'description': 'AP - The black-tailed prairie dog has been dropped from a list of candidates for the federal endangered species list because scientists have concluded the rodents are no longer threatened.'}, {'title': 'Hubble Trouble: One of Four Instruments Stops Working (SPACE.com)', 'description': 'SPACE.com - One of the four astronomical instruments on the Hubble Space Telescope shut down earlier this week and engineers are trying to pin down the problem. The other three instruments continue to operate normally.'}, {'title': 'Invasive Purple Weed May Meet Its Match (AP)', 'description': 'AP - They burned it, mowed it, sprayed it and flooded it. But nothing killed the purple loosestrife weed, which has become a regional plague, until officials at the Parker River National Wildlife Refuge set a European beetle loose on it.'}, {'title': 'New NASA Supercomputer to Aid Theorists and Shuttle Engineers (SPACE.com)', 'description': "SPACE.com - NASA researchers have teamed up with a pair of Silicon Valley firms to build \\  a supercomputer that ranks alongside the world's largest Linux-based systems."}]}, 'var_functions.execute_python:20': {'total_articles': 1000, 'sports_articles_found': 216, 'sports_samples': [{'title': 'Fed minutes show dissent over inflation (USATODAY.com)', 'desc_length': 197}, {'title': "Shell 'could be target for Total'", 'desc_length': 121}, {'title': 'Chad seeks refugee aid from IMF', 'desc_length': 124}, {'title': 'Indians fill rail skills shortage', 'desc_length': 117}, {'title': 'Stoking the Steamroller', 'desc_length': 114}, {'title': 'Autodesk tackles project collaboration', 'desc_length': 402}, {'title': "'Madden,' 'ESPN' Football Score in Different Ways (Reuters)", 'desc_length': 251}, {'title': "Sun's Looking Glass Provides 3D View (PC World)", 'desc_length': 89}, {'title': 'Invasive Purple Weed May Meet Its Match (AP)', 'desc_length': 237}, {'title': 'New NASA Supercomputer to Aid Theorists and Shuttle Engineers (SPACE.com)', 'desc_length': 169}]}, 'var_functions.execute_python:22': 'file_storage/functions.execute_python:22.json'}

exec(code, env_args)
