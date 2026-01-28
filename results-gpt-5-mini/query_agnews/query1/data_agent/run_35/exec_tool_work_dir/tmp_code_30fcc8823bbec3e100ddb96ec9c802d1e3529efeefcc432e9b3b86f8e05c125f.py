code = """import json, re

# Load articles from storage file
path = var_call_ha7GXPF8GohPjmGTvj63zEVh
with open(path, 'r', encoding='utf-8') as f:
    articles = json.load(f)

# Define sports keywords and multi-word phrases
sports_keywords = ['world cup','worldcup','football','soccer','match','tournament','league','cup','goal','goals','score','scored','won','win','beats','beat','defeat','defeated','draw','playoff','season','coach','manager','player','players','team','teams','innings','quarterback','touchdown','pitcher','batting','racing','race','olympic','olympics','fifa','nba','mlb','nfl','nhl','boxing','golf','tennis','cricket','rugby','hockey','stadium','fixture','athlete','athletes','coach','transfer','penalty','goalkeeper','striker']

def is_sports(text):
    t = text.lower()
    # check multi-word first
    for kw in sports_keywords:
        if ' ' in kw:
            if kw in t:
                return True
    # then whole-word match for single words
    for kw in sports_keywords:
        if ' ' not in kw:
            if re.search(r'\b' + re.escape(kw) + r'\b', t):
                return True
    return False

sports_articles = []
for art in articles:
    title = art.get('title','') or ''
    desc = art.get('description','') or ''
    combined = title + ' ' + desc
    if is_sports(combined):
        sports_articles.append({'article_id': art.get('article_id'), 'title': title, 'description': desc, 'desc_len': len(desc)})

# If no sports articles, set result None
if not sports_articles:
    res = None
else:
    best = max(sports_articles, key=lambda x: x['desc_len'])
    res = best['title']

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_eb7YuFVIxmhI47oFcD8JxeFQ': ['articles'], 'var_call_ha7GXPF8GohPjmGTvj63zEVh': 'file_storage/call_ha7GXPF8GohPjmGTvj63zEVh.json', 'var_call_ZWlnWBnwPo3c5ByoVOs0ucvt': 'Pronger opts out of World Cup', 'var_call_CKTzpzl78QGZF7zAzOror2gE': ['authors', 'article_metadata'], 'var_call_gOgN5NU5iKcUh6s3a8RAcXZc': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'author_id': '992', 'region': 'North America', 'publication_date': '2004-03-20'}, {'article_id': '2', 'author_id': '820', 'region': 'South America', 'publication_date': '2021-02-04'}, {'article_id': '3', 'author_id': '478', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '4', 'author_id': '39', 'region': 'Africa', 'publication_date': '2012-02-01'}], 'var_call_lsPlC55D5gnF3d6iGZ4CCwAB': 'Technology as Fashion'}

exec(code, env_args)
