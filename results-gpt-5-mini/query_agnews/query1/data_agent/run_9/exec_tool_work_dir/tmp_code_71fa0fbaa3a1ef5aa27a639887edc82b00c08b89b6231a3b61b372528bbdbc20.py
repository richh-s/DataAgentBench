code = """import json
records = var_call_j12ErLHgDBDm8ZWI8wKQfYv2

# Define keyword sets for categories
sports_keywords = {"match","game","season","goal","goals","team","teams","player","players","coach","scored","wins","loss","tournament","cup","league","athlete","athletes","nba","nfl","mlb","soccer","football","basketball","baseball","hockey","golf","tennis","olympic","olympics","score","defeat","victory"}
world_keywords = {"iraq","president","election","rebel","militia","government","minister","country","countries","world","international","border","war","attacks","conflict","police","authorities"}
business_keywords = {"stock","stocks","wall street","short-sellers","short-seller","short sellers","private investment","investment","firm","economy","earnings","market","oil prices","crude","prices","commercial","aerospace","carlyle","group","company","companies"}
sci_keywords = {"technology","tech","science","research","aerospace","space","robot","computer","software","hardware"}

def score_category(text):
    text = text.lower()
    scores = {
        'Sports': sum(text.count(k) for k in sports_keywords),
        'World': sum(text.count(k) for k in world_keywords),
        'Business': sum(text.count(k) for k in business_keywords),
        'Science/Technology': sum(text.count(k) for k in sci_keywords)
    }
    # Choose highest score; if all zero, return 'Uncategorized'
    max_cat = max(scores, key=lambda k: scores[k])
    if scores[max_cat] == 0:
        return 'Uncategorized'
    return max_cat

# Classify records and find sports articles
sports_articles = []
for r in records:
    title = r.get('title')
    description = r.get('description', '')
    text = (title or '') + ' ' + (description or '')
    category = score_category(text)
    r['category'] = category
    r['description_length'] = len(description or '')
    if category == 'Sports':
        sports_articles.append(r)

# Find sports article with max description length
if sports_articles:
    best = max(sports_articles, key=lambda x: x['description_length'])
    selected_title = best.get('title')
else:
    selected_title = None

result = {
    'sports_titles': [r.get('title') for r in sports_articles],
    'selected_title': selected_title
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_j12ErLHgDBDm8ZWI8wKQfYv2': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
