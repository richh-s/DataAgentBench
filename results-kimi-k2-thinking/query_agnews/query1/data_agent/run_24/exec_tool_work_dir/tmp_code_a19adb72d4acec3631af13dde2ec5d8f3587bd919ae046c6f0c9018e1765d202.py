code = """import json

# Load all articles
file_path = locals()['var_functions.query_db:2']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Let's look at some articles containing clear sports terms but not too broad
# Start with articles containing team sport terms
clear_sports_keywords = [
    'football', 'soccer', 'basketball', 'baseball', 'hockey',
    'tennis', 'golf', 'cricket', 'rugby', 'volleyball',
    'nba', 'nfl', 'mlb', 'nhl', 'premier league', 'fifa',
    'olympic', 'olympics', 'world cup', 'championship',
    'tournament', 'coach', 'player', 'team', 'game', 'match',
    'quarterback', 'goalkeeper', 'pitcher', 'quarter final', 'semi final'
]

# Find articles containing these keywords
potential_sports = []
for article in articles:
    title_lower = article['title'].lower()
    desc_lower = article['description'].lower()
    
    if any(keyword in title_lower or keyword in desc_lower for keyword in clear_sports_keywords):
        potential_sports.append(article)

# Let's sample some of these to see what we're catching
sample = potential_sports[:20]
result = {
    'total_potential_sports': len(potential_sports),
    'sample_articles': []
}

for article in sample:
    result['sample_articles'].append({
        'article_id': article['article_id'],
        'title': article['title'],
        'description': article['description']
    })

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:7': {'article_count': 1000, 'sample_articles': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}, 'var_functions.execute_python:12': {'sports_article_count': 210, 'longest_sports_article': {'title': "Why Windows isn't Unix", 'description': '\\\\"I first heard about this from one of the developers of the hit game SimCity, who\\told me that there was a critical bug in his application: it used memory right\\after freeing it, a major no-no that happened to work OK on DOS but would not\\work under Windows where memory that is freed is likely to be snatched up by\\another running application right away. The testers on the Windows team were\\going through various popular applications, testing them to make sure they\\worked OK, but SimCity kept crashing. They reported this to the Windows\\developers, who disassembled SimCity, stepped through it in a debugger, found\\the bug, and added special code that checked if SimCity was running, and if it\\did ...\\\\', 'description_length': 708, 'article_id': '183'}}, 'var_functions.execute_python:10': {'sports_article_count': 147, 'longest_sports_article': {'title': 'China Begins Countdown for Next Manned Space Flight', 'description_length': 580, 'article_id': '279'}, 'top_5_longest': [{'rank': 1, 'title': 'China Begins Countdown for Next Manned Space Flight', 'description_length': 580, 'article_id': '279'}, {'rank': 2, 'title': 'DiMarco, Riley Play Way Into Ryder Cup (AP)', 'description_length': 483, 'article_id': '661'}, {'rank': 3, 'title': "Last Year's Flu Shot Imperfect But Effective", 'description_length': 440, 'article_id': '290'}, {'rank': 4, 'title': 'Mozilla Exceptions (mexception)', 'description_length': 421, 'article_id': '174'}, {'rank': 5, 'title': 'They flocked from Games', 'description_length': 406, 'article_id': '763'}]}}

exec(code, env_args)
