code = """import json
# Load the full result from the provided JSON file path
with open(var_call_Po3Gwg2EMo5m99hQkrE9xfBd, 'r', encoding='utf-8') as f:
    articles = json.load(f)

# Define sports-related keywords for classification
sports_keywords = [
    'sport','football','soccer','basketball','baseball','cricket','tennis','golf','rugby',
    'match','season','coach','team','scored','goal','inning','innings','mlb','nba','nfl','nhl',
    'cup','world cup','olympic','olympics','tournament','league','derby','goalkeeper','striker',
    'midfielder','pitch','stadium','fifa','uefa','manager','racing','race','motorsport','formula',
    'f1','boxing','wrestling','mma','ufc','athlete','athletics','track','field','homerun','home run',
    'batting','pitching','bat','run scored','try','tries'
]

sports_articles = []
for a in articles:
    title = a.get('title','') or ''
    description = a.get('description','') or ''
    combined = (title + ' ' + description).lower()
    is_sport = any(kw in combined for kw in sports_keywords)
    if is_sport:
        desc_len = len(description)
        sports_articles.append({'article_id': a.get('article_id'), 'title': title, 'description': description, 'desc_len': desc_len})

# If no sports articles found, return a message
if not sports_articles:
    result = {'error': 'No sports articles found'}
else:
    # Find the article(s) with the max description length
    max_len = max(a['desc_len'] for a in sports_articles)
    max_articles = [a for a in sports_articles if a['desc_len'] == max_len]
    # If multiple, list all titles
    titles = [a['title'] for a in max_articles]
    # Prepare result
    if len(titles) == 1:
        result = {'title': titles[0], 'description_length': max_len}
    else:
        result = {'titles': titles, 'description_length': max_len}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Po3Gwg2EMo5m99hQkrE9xfBd': 'file_storage/call_Po3Gwg2EMo5m99hQkrE9xfBd.json'}

exec(code, env_args)
