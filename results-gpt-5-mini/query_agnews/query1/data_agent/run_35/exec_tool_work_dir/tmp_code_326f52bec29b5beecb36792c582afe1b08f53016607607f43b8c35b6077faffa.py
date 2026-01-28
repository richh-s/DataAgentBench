code = """import json

# Access the earlier classified articles (from var_call_ha7GXPF8GohPjmGTvj63zEVh)
path = var_call_ha7GXPF8GohPjmGTvj63zEVh
with open(path, 'r', encoding='utf-8') as f:
    articles = json.load(f)

# Build mapping by article_id
id_map = {a['article_id']: a for a in articles}

# From previous classification result we used var_call_ZWln... which holds the final title string
# But to be robust, let's re-run a direct search: find articles whose title or description indicate sports
sports_keywords = ['football','soccer','match','tournament','league','cup','goal','goals','score','scored','won','win','beats','beat','defeat','defeated','draw','playoff','season','coach','manager','player','players','team','teams','innings','quarterback','touchdown','pitcher','batting','racing','race','olympic','olympics','fifa','nba','mlb','nfl','nhl','world cup','boxing','golf','tennis','cricket','rugby','hockey','stadium','fixture']

sports_articles = []
for art in articles:
    txt = (art.get('title','') + ' ' + art.get('description','')).lower()
    if any(kw in txt for kw in sports_keywords):
        sports_articles.append({'article_id': art['article_id'], 'title': art.get('title',''), 'description': art.get('description',''), 'desc_len': len(art.get('description','') or '')})

# find sports article with max description length
if not sports_articles:
    res_title = None
else:
    best = max(sports_articles, key=lambda x: x['desc_len'])
    res_title = best['title']

import json
print('__RESULT__:')
print(json.dumps(res_title))"""

env_args = {'var_call_eb7YuFVIxmhI47oFcD8JxeFQ': ['articles'], 'var_call_ha7GXPF8GohPjmGTvj63zEVh': 'file_storage/call_ha7GXPF8GohPjmGTvj63zEVh.json', 'var_call_ZWlnWBnwPo3c5ByoVOs0ucvt': 'Pronger opts out of World Cup', 'var_call_CKTzpzl78QGZF7zAzOror2gE': ['authors', 'article_metadata'], 'var_call_gOgN5NU5iKcUh6s3a8RAcXZc': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'author_id': '992', 'region': 'North America', 'publication_date': '2004-03-20'}, {'article_id': '2', 'author_id': '820', 'region': 'South America', 'publication_date': '2021-02-04'}, {'article_id': '3', 'author_id': '478', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '4', 'author_id': '39', 'region': 'Africa', 'publication_date': '2012-02-01'}]}

exec(code, env_args)
