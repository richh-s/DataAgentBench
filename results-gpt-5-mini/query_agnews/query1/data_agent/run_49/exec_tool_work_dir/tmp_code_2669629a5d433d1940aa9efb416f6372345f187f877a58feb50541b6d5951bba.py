code = """import json
# var_call_kjAbiJ7C2kgZ9VWNqcHynfPR is available from previous query_db call
records = var_call_kjAbiJ7C2kgZ9VWNqcHynfPR

# define sports-related keywords
sports_keywords = [
    'sport','sports','game','match','score','scored','season','coach','team','win','defeat',
    'golf','tennis','football','soccer','baseball','basketball','hockey','nhl','nfl','mlb','fifa',
    'goal','league','tournament','cup','olymp','innings','bat','run','strike','matchup','fixture'
]

sports_articles = []
for r in records:
    title = r.get('title','') or ''
    desc = r.get('description','') or ''
    text = (title + ' ' + desc).lower()
    is_sports = any(kw in text for kw in sports_keywords)
    sports_articles.append({
        'article_id': r.get('article_id'),
        'title': title,
        'description': desc,
        'description_length': len(desc),
        'is_sports': is_sports
    })

# filter sports
sports_only = [a for a in sports_articles if a['is_sports']]

if sports_only:
    # find max length
    best = max(sports_only, key=lambda x: x['description_length'])
    selected_title = best['title']
else:
    selected_title = None

result = {
    'sports_articles': sports_only,
    'selected_title': selected_title
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_kjAbiJ7C2kgZ9VWNqcHynfPR': [{'_id': '695989c27274f19dd1cbfad7', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '695989c27274f19dd1cbfad8', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '695989c27274f19dd1cbfad9', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '695989c27274f19dd1cbfada', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '695989c27274f19dd1cbfadb', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
