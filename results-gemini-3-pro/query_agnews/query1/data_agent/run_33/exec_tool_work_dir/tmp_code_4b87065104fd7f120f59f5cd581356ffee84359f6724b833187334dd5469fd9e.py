code = """import json
import re

# Load the file
file_path = locals()['var_function-call-7323233515042588768']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Define SAFER sports keywords
# Use word boundaries for short words
safe_keywords = [
    "olympics", "olympic", "paralympics",
    "football", "basketball", "baseball", "soccer", "tennis", "golf", "hockey", "volleyball", "cricket", "rugby", "boxing", "wrestling", "swimming", "gymnastics", "marathon", "triathlon", "badminton", "table tennis",
    "nfl", "nba", "mlb", "nhl", "fifa", "uefa", "pga", "lpga", "atp", "wta", "nascar", "formula one", "formula 1", "indycar",
    "wimbledon", "super bowl", "world series", "stanley cup", "world cup", "euro 2004", "athens 2004", "gold medal", "silver medal", "bronze medal", "grand slam", "touchdown", "quarterback", "home run", "slam dunk",
    "red sox", "yankees", "lakers", "celtics", "knicks", "real madrid", "manchester united", "arsenal", "chelsea", "liverpool"
]

# Compile regex for faster and accurate matching (whole words only for short ones)
# \b word boundary
regex_list = [re.compile(r'\b' + re.escape(k) + r'\b', re.IGNORECASE) for k in safe_keywords]

def is_sports(text):
    # Check against regex
    for pattern in regex_list:
        if pattern.search(text):
            return True
    return False

# Find the sports article with the longest description
max_len = -1
best_title = None
best_desc = ""

count_sports = 0
for art in articles:
    title = art.get('title', '')
    desc = art.get('description', '')
    combined = title + " " + desc
    
    if is_sports(combined):
        count_sports += 1
        if len(desc) > max_len:
            max_len = len(desc)
            best_title = title
            best_desc = desc

print("__RESULT__:")
print(json.dumps({"count_sports": count_sports, "best_title": best_title, "max_len": max_len, "best_desc_preview": best_desc[:100]}))"""

env_args = {'var_function-call-2682744700755730866': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}], 'var_function-call-2682744700755734105': [{'_id': '69447bad1ca91dff0c5cc85b', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-15609243146355962304': ['authors', 'article_metadata'], 'var_function-call-10373301645421909439': [{'_id': '69447bad1ca91dff0c5cc85b', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447bad1ca91dff0c5cc85c', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447bad1ca91dff0c5cc85d', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447bad1ca91dff0c5cc85e', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447bad1ca91dff0c5cc85f', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}, {'_id': '69447bad1ca91dff0c5cc860', 'article_id': '5', 'title': 'Stocks End Up, But Near Year Lows (Reuters)', 'description': 'Reuters - Stocks ended slightly higher on Friday\\but stayed near lows for the year as oil prices surged past  #36;46\\a barrel, offsetting a positive outlook from computer maker\\Dell Inc. (DELL.O)'}, {'_id': '69447bad1ca91dff0c5cc861', 'article_id': '6', 'title': 'Money Funds Fell in Latest Week (AP)', 'description': "AP - Assets of the nation's retail money market mutual funds fell by  #36;1.17 billion in the latest week to  #36;849.98 trillion, the Investment Company Institute said Thursday."}, {'_id': '69447bad1ca91dff0c5cc862', 'article_id': '7', 'title': 'Fed minutes show dissent over inflation (USATODAY.com)', 'description': 'USATODAY.com - Retail sales bounced back a bit in July, and new claims for jobless benefits fell last week, the government said Thursday, indicating the economy is improving from a midsummer slump.'}, {'_id': '69447bad1ca91dff0c5cc863', 'article_id': '8', 'title': 'Safety Net (Forbes.com)', 'description': 'Forbes.com - After earning a PH.D. in Sociology, Danny Bazil Riley started to work as the general manager at a commercial real estate firm at an annual base salary of  #36;70,000. Soon after, a financial planner stopped by his desk to drop off brochures about insurance benefits available through his employer. But, at 32, "buying insurance was the furthest thing from my mind," says Riley.'}, {'_id': '69447bad1ca91dff0c5cc864', 'article_id': '9', 'title': 'Wall St. Bears Claw Back Into the Black', 'description': " NEW YORK (Reuters) - Short-sellers, Wall Street's dwindling  band of ultra-cynics, are seeing green again."}], 'var_function-call-3668121026551465757': [{'_id': '69447bad1ca91dff0c5cc85b', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447bad1ca91dff0c5cc85c', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447bad1ca91dff0c5cc85d', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447bad1ca91dff0c5cc85e', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447bad1ca91dff0c5cc85f', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-7323233515042588768': 'file_storage/function-call-7323233515042588768.json', 'var_function-call-14661292092377225536': {'count_sports': 31088, 'best_title': 'Nokia earmarks millions to build new plant in India', 'max_len': 957, 'best_desc_preview': "Nokia, the world's largest handset maker, is investing up to \\$150 million over the next four years "}}

exec(code, env_args)
