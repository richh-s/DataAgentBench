code = """import json
import re

file_path = locals()['var_function-call-7323233515042588768']
with open(file_path, 'r') as f:
    articles = json.load(f)

safe_single_keywords = {
    'olympics', 'olympic', 'paralympics', 
    'football', 'basketball', 'baseball', 'soccer', 'tennis', 'golf', 'hockey', 
    'volleyball', 'cricket', 'rugby', 'boxing', 'wrestling', 'swimming', 'gymnastics', 
    'marathon', 'triathlon', 'badminton', 'nfl', 'nba', 'mlb', 'nhl', 'fifa', 'uefa', 
    'nascar', 'f1', 'wimbledon', 'pga', 'lpga',
    'tournament', 'championship', 'stadium', 'athlete', 'athletics', 'medal', 'medals'
}

safe_phrases = [
    'super bowl', 'world series', 'stanley cup', 'world cup', 'euro 2004', 'athens 2004', 
    'gold medal', 'red sox', 'yankees', 'formula one', 'grand slam', 'us open', 'french open', 'australian open',
    'white sox', 'premier league', 'champions league', 'grand prix', 'ryder cup', 'davis cup',
    'tour de france', 'british open'
]

max_len = -1
best_title = None
best_desc = ""
count = 0

for art in articles:
    title = art.get('title', '')
    desc = art.get('description', '')
    full_text = title + " " + desc
    
    # Check phrases first
    lower_text = full_text.lower()
    is_sport = False
    for p in safe_phrases:
        if p in lower_text:
            is_sport = True
            break
    
    if not is_sport:
        clean_text = re.sub(r'[^a-zA-Z0-9]', ' ', lower_text)
        words = set(clean_text.split())
        if not words.isdisjoint(safe_single_keywords):
            is_sport = True
            
    if is_sport:
        count += 1
        if len(desc) > max_len:
            max_len = len(desc)
            best_title = title
            best_desc = desc

print("__RESULT__:")
print(json.dumps({"count": count, "best_title": best_title, "max_len": max_len, "desc_preview": best_desc[:200]}))"""

env_args = {'var_function-call-2682744700755730866': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}], 'var_function-call-2682744700755734105': [{'_id': '69447bad1ca91dff0c5cc85b', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-15609243146355962304': ['authors', 'article_metadata'], 'var_function-call-10373301645421909439': [{'_id': '69447bad1ca91dff0c5cc85b', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447bad1ca91dff0c5cc85c', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447bad1ca91dff0c5cc85d', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447bad1ca91dff0c5cc85e', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447bad1ca91dff0c5cc85f', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}, {'_id': '69447bad1ca91dff0c5cc860', 'article_id': '5', 'title': 'Stocks End Up, But Near Year Lows (Reuters)', 'description': 'Reuters - Stocks ended slightly higher on Friday\\but stayed near lows for the year as oil prices surged past  #36;46\\a barrel, offsetting a positive outlook from computer maker\\Dell Inc. (DELL.O)'}, {'_id': '69447bad1ca91dff0c5cc861', 'article_id': '6', 'title': 'Money Funds Fell in Latest Week (AP)', 'description': "AP - Assets of the nation's retail money market mutual funds fell by  #36;1.17 billion in the latest week to  #36;849.98 trillion, the Investment Company Institute said Thursday."}, {'_id': '69447bad1ca91dff0c5cc862', 'article_id': '7', 'title': 'Fed minutes show dissent over inflation (USATODAY.com)', 'description': 'USATODAY.com - Retail sales bounced back a bit in July, and new claims for jobless benefits fell last week, the government said Thursday, indicating the economy is improving from a midsummer slump.'}, {'_id': '69447bad1ca91dff0c5cc863', 'article_id': '8', 'title': 'Safety Net (Forbes.com)', 'description': 'Forbes.com - After earning a PH.D. in Sociology, Danny Bazil Riley started to work as the general manager at a commercial real estate firm at an annual base salary of  #36;70,000. Soon after, a financial planner stopped by his desk to drop off brochures about insurance benefits available through his employer. But, at 32, "buying insurance was the furthest thing from my mind," says Riley.'}, {'_id': '69447bad1ca91dff0c5cc864', 'article_id': '9', 'title': 'Wall St. Bears Claw Back Into the Black', 'description': " NEW YORK (Reuters) - Short-sellers, Wall Street's dwindling  band of ultra-cynics, are seeing green again."}], 'var_function-call-3668121026551465757': [{'_id': '69447bad1ca91dff0c5cc85b', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447bad1ca91dff0c5cc85c', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447bad1ca91dff0c5cc85d', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447bad1ca91dff0c5cc85e', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447bad1ca91dff0c5cc85f', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-7323233515042588768': 'file_storage/function-call-7323233515042588768.json', 'var_function-call-14661292092377225536': {'count_sports': 31088, 'best_title': 'Nokia earmarks millions to build new plant in India', 'max_len': 957, 'best_desc_preview': "Nokia, the world's largest handset maker, is investing up to \\$150 million over the next four years "}, 'var_function-call-3930677297530208569': {'count_sports': 0, 'best_title': None, 'max_len': -1, 'best_desc_preview': ''}, 'var_function-call-16485497495526994072': ["'Madden,' 'ESPN' Football Score in Different Ways (Reuters)", "'Invisible' technology for Olympics", 'Satellite boosts Olympic security', "'Madden,' 'ESPN' Football Score in Different Ways", 'Ancient Olympics Mixed Naked Sports, Pagan Partying', 'Olympics Could Call Out the Couch Potatoes'], 'var_function-call-4217819610303164359': {'count': 0, 'best_title': None, 'max_len': -1, 'desc_preview': ''}, 'var_function-call-1753447067190488821': {'match': False, 'pattern': '\x08(?:football|olympics)\x08'}, 'var_function-call-13478211147769960342': {'count': 13986, 'best_title': 'Area College Football Capsules', 'max_len': 761, 'desc_preview': "Navy at Tulsa &lt;br&gt;   Where:  Skelly Stadium    When:  7 p.m. &lt;br&gt;   Shooting for 3-0:  Navy is off to its first 2-0 start since 1996. The Midshipmen haven't started 3-0 since 1979, when th"}, 'var_function-call-6499578749605881191': {'count': 16411, 'best_title': 'Cavaliers, Hokies Play Host', 'max_len': 773, 'desc_preview': "Akron at No. 12 Virginia &lt;br&gt;   Where:  Scott Stadium, Charlottesville&lt;br&gt;   When:  3 p.m.    Radio:  WTNT-570    Tickets:  Sold out &lt;br&gt;   Another Top QB:  Like North Carolina's Dar"}}

exec(code, env_args)
