code = """import json
import re

# Load the large JSON result from storage file path
with open(var_call_t2jfp7S0sJVqRepmKrfqk7Ug, 'r', encoding='utf-8') as f:
    articles = json.load(f)

# Define keyword sets for simple heuristic classification
sports_kw = set([k.lower() for k in ['match','game','score','goal','football','soccer','basketball','baseball','tennis','cricket','golf','tournament','season','coach','player','players','cup','league','nhl','nba','mlb','fifa','olympic','olympics','rowing','boxing','rugby','hockey','race','races','won','beat','defeat','defeated','victory','draw','innings','bat','batsman','pitcher','quarter','halftime','club','team','striker','goalkeeper']])
business_kw = set([k.lower() for k in ['stocks','stock','market','shares','ipo','oil','economy','company','companies','profits','profit','financial','investment','investors','revenue','sales','merger','acquisition','bank','banking','dollar','trade','trading','bond','price','prices']])
science_kw = set([k.lower() for k in ['scientist','research','researchers','technology','tech','scientific','nuclear','ibm','internet','e-mail','email','study','drug','drugs','medicine','medical','data','computer','software','google','hp','microsoft','experiment']])
world_kw = set([k.lower() for k in ['president','gov','government','country','countries','election','war','rebel','militia','prime minister','minister','foreign','talks','peace','terror','blast','attacks','border','united nations','un','sanctions','iraq','afghanistan','china','russia','iran','saudi','japan','europe','eurozone','authorities','officials']])

# helper to count keyword hits
def score_text(text, keywords):
    if not text:
        return 0
    text_low = text.lower()
    # simple token matching
    count = 0
    for kw in keywords:
        # count occurrences
        count += text_low.count(kw)
    return count

# classify and find sports article with max description length
sports_articles = []
for a in articles:
    title = a.get('title','') or ''
    desc = a.get('description','') or ''
    combined = title + ' ' + desc
    s_sports = score_text(combined, sports_kw)
    s_business = score_text(combined, business_kw)
    s_science = score_text(combined, science_kw)
    s_world = score_text(combined, world_kw)
    scores = {'Sports': s_sports, 'Business': s_business, 'Science/Technology': s_science, 'World': s_world}
    # choose highest score
    category = max(scores.items(), key=lambda x: (x[1], x[0]))[0]
    # if all zero, fallback to World for geopolitics-looking words else Business if business-like words present
    if sum(scores.values()) == 0:
        category = 'World'
    if category == 'Sports':
        sports_articles.append({'article_id': a.get('article_id'), 'title': title, 'description': desc, 'desc_len': len(desc)})

# If no sports found, try a looser approach: mark articles whose title contains sports keywords
if not sports_articles:
    for a in articles:
        title = a.get('title','') or ''
        desc = a.get('description','') or ''
        combined = title + ' ' + desc
        if any(kw in combined.lower() for kw in sports_kw):
            sports_articles.append({'article_id': a.get('article_id'), 'title': title, 'description': desc, 'desc_len': len(desc)})

# find max by description length
if sports_articles:
    sports_articles_sorted = sorted(sports_articles, key=lambda x: x['desc_len'], reverse=True)
    top = sports_articles_sorted[0]
    result_title = top['title']
else:
    result_title = None

# Print result in required format as JSON string
import json
out = json.dumps({'title': result_title})
print("__RESULT__:")
print(out)"""

env_args = {'var_call_t2jfp7S0sJVqRepmKrfqk7Ug': 'file_storage/call_t2jfp7S0sJVqRepmKrfqk7Ug.json'}

exec(code, env_args)
