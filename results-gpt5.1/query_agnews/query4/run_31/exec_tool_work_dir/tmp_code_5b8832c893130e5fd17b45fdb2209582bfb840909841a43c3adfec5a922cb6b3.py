code = """import json, pandas as pd
from datetime import datetime

# Load full results from files
with open(var_call_8Hmk5oIdkhl6eVGbhpMTren6, 'r') as f:
    meta = json.load(f)
with open(var_call_lHmzB2b5lLtZzrsfS0Wfzftv, 'r') as f:
    arts = json.load(f)

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# Ensure correct dtypes
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# Filter metadata for year 2015
meta_df['year'] = pd.to_datetime(meta_df['publication_date']).dt.year
meta_2015 = meta_df[meta_df['year'] == 2015]

# Merge to get titles and descriptions for 2015 articles
merged = meta_2015.merge(arts_df, on='article_id', how='inner')

# Simple heuristic classifier for categories based on title+description keywords
world_keywords = ['iraq','war','election','president','government','minister','parliament','united nations','u.n.','UN ','UN,','UN.','peace talks','conflict','attack','bomber','bombing','troops','terror','israel','palestinian','gaza','afghanistan','syria','russia','china','european union','eu ','eu,','eu.','diplomat','foreign policy','sanction','nato','refugee','crisis','protest','demonstrator','border','nuclear program','missile','embassy','summit']

sports_keywords = ['game','games','tournament','league','season','goal','score','scored','coach','team','teams','match','cup','olympic','olympics','nfl','nba','mlb','nhl','soccer','football','basketball','baseball','tennis','golf','cricket','rugby','hockey','playoff','finals','world cup']

business_keywords = ['stock','stocks','bond','bonds','market','shares','share','nasdaq','dow','s&p','profit','losses','earnings','ipo','merger','acquisition','bank','banks','banking','loan','loans','interest rate','interest rates','fed ','federal reserve','oil prices','gold prices','currency','currencies','dollar','yen','euro','ftse','nikkei','economy','economic','trade deficit','trade surplus','unemployment','jobs report','retail sales','investment','investor','investors','company','companies','corporate','business','growth']

sci_keywords = ['researchers','scientist','scientists','study','studies','laboratory','lab ','laboratories','nasa','space','planet','galaxy','astronomy','physics','chemistry','biology','genetics','genome','dna ','climate','environment','global warming','greenhouse','technology','software','computer','computers','internet','online','web site','website','websites','smartphone','smart phone','mobile phone','cellphone','robot','robots','ai ','artificial intelligence','quantum','particle','vaccine','disease','medical','medicine','neuron','brain','clinical trial']


def classify(text):
    t = text.lower()
    scores = {'World':0,'Sports':0,'Business':0,'Science/Technology':0}
    for w in world_keywords:
        if w in t:
            scores['World'] += 1
    for w in sports_keywords:
        if w in t:
            scores['Sports'] += 1
    for w in business_keywords:
        if w in t:
            scores['Business'] += 1
    for w in sci_keywords:
        if w in t:
            scores['Science/Technology'] += 1
    # pick max; tie-breaker by fixed order
    order = ['World','Sports','Business','Science/Technology']
    best = order[0]
    best_score = -1
    for cat in order:
        if scores[cat] > best_score:
            best_score = scores[cat]
            best = cat
    return best

merged['text'] = merged['title'].fillna('') + ' ' + merged['description'].fillna('')
merged['category'] = merged['text'].apply(classify)

world_2015 = merged[merged['category'] == 'World']

# Count per region and get region with max count
counts = world_2015.groupby('region').size().sort_values(ascending=False)

if counts.empty:
    answer = None
else:
    answer = counts.index[0]

out = json.dumps(answer)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_8Hmk5oIdkhl6eVGbhpMTren6': 'file_storage/call_8Hmk5oIdkhl6eVGbhpMTren6.json', 'var_call_lHmzB2b5lLtZzrsfS0Wfzftv': 'file_storage/call_lHmzB2b5lLtZzrsfS0Wfzftv.json'}

exec(code, env_args)
