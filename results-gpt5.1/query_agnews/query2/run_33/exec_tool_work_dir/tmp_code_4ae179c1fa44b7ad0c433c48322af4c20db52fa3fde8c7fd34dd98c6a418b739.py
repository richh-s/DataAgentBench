code = """import json, pandas as pd

# Load Amy Jones article_ids
author_articles = pd.DataFrame(var_call_vifLn8oa3U8dcm8hkzWrlMdn)
author_articles['article_id'] = author_articles['article_id'].astype(int)

# Load all articles from JSON file path
with open(var_call_pYmBEzwjiT2YDI1xqITU2nBc, 'r') as f:
    all_articles = json.load(f)
articles_df = pd.DataFrame(all_articles)
articles_df['article_id'] = articles_df['article_id'].astype(int)

# Merge to get Amy Jones articles with title & description
merged = author_articles.merge(articles_df, on='article_id', how='inner')

# Simple rule-based categorization into 4 categories
# Keywords based very roughly on typical news topic vocab
science_tech_keywords = [
    'science','scientist','research','study','studies','technology','tech','software','computer','computing',
    'internet','online','web','digital','device','gadget','phone','smartphone','satellite','space','nasa',
    'biotech','biotechnology','genetic','genome','dna','physics','chemistry','robot','robotics','ai','artificial intelligence',
    'virus','bacteria','climate','environment','engineering','engineer','astronomy','telescope','quantum','data'
]

sports_keywords = [
    'game','games','match','matches','tournament','league','cup','olympic','olympics','nfl','nba','mlb','soccer',
    'football','baseball','basketball','tennis','golf','cricket','hockey','coach','player','players','team','score',
    'scored','season','championship','victory','defeat','win ','wins ','beat ','beats ','vs.','vs '
]

business_keywords = [
    'market','markets','stocks','shares','stock','bond','bonds','investor','investors','investment','bank','banks',
    'profit','profits','loss','losses','revenue','sales','merger','acquisition','ipo','economy','economic',
    'trade','trading','oil','currency','currencies','dollar','euro','yen','company','companies','corporate',
    'business','commerce','retail','industry','industries','financial','finance','fund','funds','loan','loans'
]

world_keywords = [
    'election','elections','government','parliament','president','prime minister','war','conflict','peace',
    'united nations','u.n.','un ','eu ','european union','minister','ministry','policy','policies','diplomat',
    'diplomats','iraq','iran','israel','palestinian','palestinians','afghanistan','britain','france','germany',
    'china','japan','russia','security','bomb','bombing','attack','attacks','terror','terrorism','protest','protests'
]


def categorize(row):
    text = (str(row.get('title','')) + ' ' + str(row.get('description',''))).lower()
    def has_kw(kws):
        return any(kw in text for kw in kws)
    # Priority Science/Tech, Sports, Business, then World
    if has_kw(science_tech_keywords):
        return 'Science/Technology'
    if has_kw(sports_keywords):
        return 'Sports'
    if has_kw(business_keywords):
        return 'Business'
    return 'World'

merged['category'] = merged.apply(categorize, axis=1)

# Compute fraction of Amy Jones articles that are Science/Technology
total = len(merged)
if total == 0:
    fraction = None
else:
    sci_tech = (merged['category'] == 'Science/Technology').sum()
    fraction = sci_tech / total

result = json.dumps({
    'total_articles_amy_jones': int(total),
    'science_technology_count': int((merged['category'] == 'Science/Technology').sum()),
    'fraction_science_technology': fraction
})

print("__RESULT__:")
print(result)"""

env_args = {'var_call_vifLn8oa3U8dcm8hkzWrlMdn': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_call_pYmBEzwjiT2YDI1xqITU2nBc': 'file_storage/call_pYmBEzwjiT2YDI1xqITU2nBc.json'}

exec(code, env_args)
