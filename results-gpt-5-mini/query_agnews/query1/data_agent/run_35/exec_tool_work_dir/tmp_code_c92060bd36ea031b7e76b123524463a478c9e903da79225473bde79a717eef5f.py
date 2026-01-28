code = """import json, re

# Load data from the storage file path variable
path = var_call_ha7GXPF8GohPjmGTvj63zEVh
with open(path, 'r', encoding='utf-8') as f:
    articles = json.load(f)

# Define keyword lists for rough classification
sports_kw = ['football','soccer','match','tournament','league','cup','goal','goals','score','scored','won','win','beats','beat','defeat','defeated','draw','playoff','season','coach','manager','player','players','team','teams','innings','quarterback','touchdown','pitcher','batting','racing','race','olympic','olympics','fifa','nba','mlb','nfl','nhl','world cup','boxer','boxing','golf','tennis','cricket','rugby','hockey','stadium','fixture']
business_kw = ['stock','stocks','market','oil','dollar','trade','shares','ipo','company','firm','investment','profits','profit','earnings','bank','economy','economic','merger','acquisition','deal','revenue']
world_kw = ['government','president','minister','election','rebels','militia','police','attack','war','killed','protest','country','nations','border','arrested','official','diplomatic','ceasefire','peace','sanction','soldier']
science_kw = ['scientist','research','researchers','laboratory','study','drug','nuclear','technology','computer','software','internet','scientific','experiment','medical','dna','lab','biology','chemistry','tech','device','iphone','ibm','microsoft']

# helper to score
def score_text(text, keywords):
    s = 0
    for kw in keywords:
        # count occurrences as whole words where reasonable
        # For multi-word keywords, use simple substring
        if ' ' in kw:
            s += text.count(kw)
        else:
            # word boundary match
            s += len(re.findall(r'\b' + re.escape(kw) + r'\b', text))
    return s

# classify articles
classified = []
for art in articles:
    title = art.get('title','') or ''
    desc = art.get('description','') or ''
    combined = (title + ' ' + desc).lower()
    # score title more
    title_text = title.lower()
    desc_text = desc.lower()
    s_sports = score_text(title_text, sports_kw)*3 + score_text(desc_text, sports_kw)
    s_business = score_text(title_text, business_kw)*3 + score_text(desc_text, business_kw)
    s_world = score_text(title_text, world_kw)*3 + score_text(desc_text, world_kw)
    s_science = score_text(title_text, science_kw)*3 + score_text(desc_text, science_kw)
    scores = {'Sports': s_sports, 'Business': s_business, 'World': s_world, 'Science/Technology': s_science}
    # pick highest
    cat = max(scores.items(), key=lambda x: (x[1], x[0]))[0]
    classified.append({'article_id': art.get('article_id'), 'title': title, 'description': desc, 'category': cat, 'desc_len': len(desc)})

# filter sports
sports_articles = [a for a in classified if a['category']=='Sports']

# If none found, try another heuristic: look for sports keywords anywhere (looser)
if not sports_articles:
    for art in classified:
        t = (art['title'] + ' ' + art['description']).lower()
        if any(kw in t for kw in sports_kw):
            sports_articles.append(art)

# If still none, return null
if not sports_articles:
    result = None
else:
    # find max description length
    best = max(sports_articles, key=lambda x: x['desc_len'])
    result = best['title']

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_eb7YuFVIxmhI47oFcD8JxeFQ': ['articles'], 'var_call_ha7GXPF8GohPjmGTvj63zEVh': 'file_storage/call_ha7GXPF8GohPjmGTvj63zEVh.json'}

exec(code, env_args)
