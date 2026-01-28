code = """import json
# Access the articles result from the previous query
records = var_call_vJEjt6DXJmXtDzOufoEamDWO

# Define simple keyword-based classifier
sports_keywords = set(['game','season','match','player','players','team','teams','score','scores','tournament','goal','goals','coach','stadium','cup','league','olympic','fifa','nba','nfl','mlb','hockey','soccer','basketball','baseball','win','won','defeat','defeated','rally'])
world_keywords = set(['iraq','election','president','government','rebel','militia','country','international','global','authority','authorities','southern','police','war','conflict','infrastructure'])
business_keywords = set(['wall st','stock','stocks','oil','economy','earnings','market','investment','firm','private','prices','price','carlyle','defense','commercial','shares','company','bank','finance'])
science_keywords = set(['technology','scientist','scientists','research','nasa','science','software','computer','tech','ai','robot'])

def classify_article(title, description):
    text = (title + ' ' + (description or '')).lower()
    # check sports
    for kw in sports_keywords:
        if kw in text:
            return 'Sports'
    for kw in world_keywords:
        if kw in text:
            return 'World'
    for kw in business_keywords:
        if kw in text:
            return 'Business'
    for kw in science_keywords:
        if kw in text:
            return 'Science/Technology'
    # default fallback
    return 'Business'

# Classify and find sports articles
sports_articles = []
for r in records:
    title = r.get('title')
    desc = r.get('description')
    cat = classify_article(title, desc)
    if cat == 'Sports':
        sports_articles.append({'title': title, 'description': desc, 'desc_len': len(desc) if desc else 0})

if not sports_articles:
    result = {'title': None, 'message': 'No sports articles found'}
else:
    # find article with max description length
    chosen = max(sports_articles, key=lambda x: x['desc_len'])
    result = {'title': chosen['title'], 'desc_len': chosen['desc_len']}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_vJEjt6DXJmXtDzOufoEamDWO': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
