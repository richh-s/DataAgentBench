code = """import json, pandas as pd

# Load full metadata and articles from files
with open(var_call_TG9cN48Kx91yauq2uLVaCGOJ, 'r') as f:
    metadata = json.load(f)
with open(var_call_1jIKHG5XzJS3bJGxi1KOluFO, 'r') as f:
    articles = json.load(f)

md_df = pd.DataFrame(metadata)
art_df = pd.DataFrame(articles)

# Ensure correct dtypes
md_df['article_id'] = md_df['article_id'].astype(int)
art_df['article_id'] = art_df['article_id'].astype(int)

# Filter metadata for 2015
md_df['year'] = md_df['publication_date'].str.slice(0,4).astype(int)
md_2015 = md_df[md_df['year'] == 2015]

# Merge with articles
df = md_2015.merge(art_df, on='article_id', how='inner')

# Simple keyword-based classifier for categories
world_keywords = ['iraq','war','election','elections','minister','president','government','united nations','u.n.','u.n','taliban','israel','palestinian','palestine','gaza','afghanistan','attack','bomb','explosion','military','conflict','terror','terrorist','al-qaeda','al qaeda','european union','eu ','parliament','border','refugee','diplomat','embassy','nato','summit']

sports_keywords = ['football','soccer','nba','nfl','mlb','nhl','tennis','golf','olympic','olympics','olympian','coach','player','team','league','tournament','cup','grand slam','finals','playoffs','world cup','fifa','championship','medal']

business_keywords = ['stock','stocks','market','shares','bond','bonds','investor','investors','nasdaq','nyse','dow','profit','profits','loss','losses','earnings','ipo','merger','acquisition','bank','banking','loan','loans','finance','financial','fund','funds','currency','currencies','trade deficit','trade surplus','economy','economic','company','corporate','business','revenue','sales','quarter','q1','q2','q3','q4']

sci_tech_keywords = ['researchers','scientists','research','study','studies','laboratory','experiment','physics','chemistry','biology','space','nasa','telescope','planet','galaxy','universe','quantum','technology','technological','computer','software','hardware','internet','online','web','ai ','artificial intelligence','robot','robots','robotics','gadget','smartphone','mobile phone','cellphone','data','genetic','genome','climate','environment','global warming']


def classify(text):
    if not isinstance(text, str):
        text = ''
    t = text.lower()
    score = {'World':0,'Sports':0,'Business':0,'Science/Technology':0}
    for kw in world_keywords:
        if kw in t:
            score['World'] += 1
    for kw in sports_keywords:
        if kw in t:
            score['Sports'] += 1
    for kw in business_keywords:
        if kw in t:
            score['Business'] += 1
    for kw in sci_tech_keywords:
        if kw in t:
            score['Science/Technology'] += 1
    # choose category with max score, default Business if all zero? but we just pick max which will be 0 ties -> first key
    return max(score, key=score.get)


# Apply classifier on combined title + description
texts = (df['title'].fillna('') + ' ' + df['description'].fillna(''))
df['category'] = texts.apply(classify)

world_df = df[df['category'] == 'World']

# Count by region
counts = world_df.groupby('region').size().sort_values(ascending=False)

if counts.empty:
    result = None
else:
    top_region = counts.idxmax()
    result = top_region

import json as _json
out = _json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_TG9cN48Kx91yauq2uLVaCGOJ': 'file_storage/call_TG9cN48Kx91yauq2uLVaCGOJ.json', 'var_call_1jIKHG5XzJS3bJGxi1KOluFO': 'file_storage/call_1jIKHG5XzJS3bJGxi1KOluFO.json'}

exec(code, env_args)
