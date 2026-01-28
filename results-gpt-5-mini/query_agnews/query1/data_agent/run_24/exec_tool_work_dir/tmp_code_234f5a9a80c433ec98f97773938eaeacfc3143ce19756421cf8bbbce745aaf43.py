code = """import json, re
path = var_call_Y12wS5ASYHmrdM6d3a3GdsiP
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

sports_k = ['sport','sports','match','goal','score','scor','team','coach','player','players','league','cup','tournament','race','racing','win','won','runner','bat','innings','pitcher','cricket','soccer','football','basketball','baseball','tennis','golf','boxing','olympic','olympics','fifa','nhl','nba','nfl','mlb','f1','motorsport','derby','goalkeeper','striker','midfield','athlete','athletes','season']
business_k = ['stock','stocks','market','markets','shares','oil','economy','economic','bank','banks','investment','investor','investors','firm','company','companies','profit','profits','trade','trading','ipo','bourse','dollar']
tech_k = ['technology','tech','software','chip','linux','computer','computers','google','microsoft','intel','apple','nuclear','space','robot','science','research','server','processor','database']
world_k = ['president','government','minister','election','vote','rebels','war','country','countries','iraq','iran','china','russia','vietnam','north','south','caracas','venezuela','refugee','united nations','u.s.','u.s','u.k.','uk','france','germany','spain']

def contains_any(text, keywords):
    t = (text or '').lower()
    for kw in keywords:
        if re.search(r"\b" + re.escape(kw), t):
            return True
    return False

sports_articles = []
for rec in data:
    title = rec.get('title') or ''
    desc = rec.get('description') or ''
    combined = title + ' ' + desc
    cat = None
    if contains_any(combined, sports_k):
        cat = 'Sports'
    elif contains_any(combined, business_k):
        cat = 'Business'
    elif contains_any(combined, tech_k):
        cat = 'Science/Technology'
    elif contains_any(combined, world_k):
        cat = 'World'
    else:
        # fallback: if contains punctuation typical of news like all caps city lines maybe world
        cat = 'World'
    if cat == 'Sports':
        sports_articles.append({'article_id': rec.get('article_id'), 'title': title, 'description': desc, 'desc_len': len(desc)})

# find max
if sports_articles:
    max_rec = max(sports_articles, key=lambda r: r['desc_len'])
    result = max_rec['title']
else:
    result = None

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_Y12wS5ASYHmrdM6d3a3GdsiP': 'file_storage/call_Y12wS5ASYHmrdM6d3a3GdsiP.json', 'var_call_VltVVT6qtx8Lici358433nGz': None, 'var_call_XCYNyRQ53RLPNxT40GwxJHM2': 'file_storage/call_XCYNyRQ53RLPNxT40GwxJHM2.json', 'var_call_JepEl8eqcJOmrF7F29jifAwi': None}

exec(code, env_args)
