code = """import json
# Load metadata (2015 entries) and articles
with open(var_call_dQoiCxChR4oghhJO7R8ycSOr, 'r') as f:
    metadata = json.load(f)
with open(var_call_L1SbYLZ9WJOrJKAMWhw0fr30, 'r') as f:
    articles = json.load(f)

# Build dict of articles by article_id (int -> text)
arts = {}
for a in articles:
    try:
        aid = int(a.get('article_id'))
    except:
        continue
    title = a.get('title') or ''
    desc = a.get('description') or ''
    text = (title + ' ' + desc).lower()
    arts[aid] = text

# classifier keywords
sports = ['match','score','goal','team','league','season','tournament','coach','player','olymp','world cup','fifa','nba','mlb','soccer','tennis','golf','cup','defeat','victory','win','scoreboard']
science = ['research','scientist','study','nasa','space','technology','tech','software','computer','internet','scientists','researchers','device','gadget','ai','robot','scientific','physics','chemistry','biology','study finds','study shows']
business = ['stock','stocks','market','economy','company','companies','share','shares','profit','loss','investment','bank','ipo','merger','acquisition','oil prices','oil','dollar','trade deficit','business','earnings','reuters -','billion','million']
world = ['president','government','minister','attack','war','soldier','rebel','united nations','un','diplomat','election','refugee','border','country','crisis','sanction','terror','terrorist','health','disease','earthquake','flood','hurricane','foreign','embassy','iraq','syria','afghanistan','china','russia','europe','asia','africa','korea','iran','israel','palestine','protest','authorities','police']

# helper
def score_text(text, keywords):
    s = 0
    for kw in keywords:
        if kw in text:
            s += text.count(kw)
    return s

# Process metadata entries, classify joined articles, count world by region
from collections import Counter
world_counts = Counter()
classified_counts = Counter()
for m in metadata:
    try:
        aid = int(m.get('article_id'))
    except:
        continue
    region = m.get('region')
    # get article text
    text = arts.get(aid, '')
    if not text:
        # if no text, skip classification
        continue
    sc_w = score_text(text, world)
    sc_b = score_text(text, business)
    sc_s = score_text(text, sports)
    sc_sc = score_text(text, science)
    scores = {'World': sc_w, 'Business': sc_b, 'Sports': sc_s, 'Science': sc_sc}
    # choose max score, tie-breaker priority
    max_score = max(scores.values())
    if max_score == 0:
        # fallback: if title contains common business words like 'reuters' or '$' assume Business, else World
        if 'reuters' in text or '$' in text or 'company' in text or 'stock' in text or 'market' in text or 'ipo' in text:
            cat = 'Business'
        else:
            cat = 'World'
    else:
        # get all categories with max
        winners = [k for k,v in scores.items() if v==max_score]
        priority = ['World','Business','Sports','Science']
        for p in priority:
            if p in winners:
                cat = p
                break
    classified_counts[cat] += 1
    if cat == 'World':
        world_counts[region] += 1

# find top region
if world_counts:
    top_region, top_count = world_counts.most_common(1)[0]
else:
    top_region, top_count = None, 0

out = {'top_region': top_region, 'top_count': top_count, 'world_counts': dict(world_counts), 'classified_counts': dict(classified_counts)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_8B3NDebFVOdGEGWGO8nU1Ntj': ['articles'], 'var_call_dQoiCxChR4oghhJO7R8ycSOr': 'file_storage/call_dQoiCxChR4oghhJO7R8ycSOr.json', 'var_call_L3fdcl2zcAp1sgnLI4npoWeX': 'file_storage/call_L3fdcl2zcAp1sgnLI4npoWeX.json', 'var_call_L1SbYLZ9WJOrJKAMWhw0fr30': 'file_storage/call_L1SbYLZ9WJOrJKAMWhw0fr30.json'}

exec(code, env_args)
