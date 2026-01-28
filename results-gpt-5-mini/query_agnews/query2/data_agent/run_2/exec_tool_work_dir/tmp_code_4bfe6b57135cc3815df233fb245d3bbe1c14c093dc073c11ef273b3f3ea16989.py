code = """import json
import pandas as pd

# Load the large MongoDB query result from the storage file path
file_path = var_call_LYMgqRRczxLnFPjTV2HY612U
with open(file_path, 'r', encoding='utf-8') as f:
    articles = json.load(f)

# Build dataframe
df = pd.DataFrame(articles)
# Ensure title and description present
df['title'] = df.get('title', '').fillna('').astype(str)
df['description'] = df.get('description', '').fillna('').astype(str)

# Classification keyword lists
science_kw = [
    'science','scientist','research','laboratory','lab','technology','tech','space','shuttle','nasa',
    'probe','intel','microsoft','e-mail','email','nuclear','physics','electr','generator','energy',
    'researcher','siemens','westinghouse','gyro-gen','gameboy','micro-games','genesis','storage','emc', 'e-mail'
]
sports_kw = [
    'coach','olympic','gold','win','defeat','quarter-final','u.s. open','tennis','football','soccer',
    'champions league','goal','scored','match','nba','mlb','red sox','dodgers','broncos','cornerback',
    'wide receiver','practice','semifinal','sprint','cycling','champs','championship','u.s. open'
]
business_kw = [
    'profit','revenue','earnings','company','corp','stock','stocks','market','trade','wto','settles',
    'settled','settlement','debt','kroger','revenue','quarter','earnings','llc','inc','company','prices','producer prices'
]
# Note: world is fallback

def contains_any(text, keywords):
    t = text.lower()
    for kw in keywords:
        if kw.lower() in t:
            return True
    return False

categories = []
for _, row in df.iterrows():
    title = row['title']
    desc = row['description']
    combined = title + ' ' + desc
    cat = None
    # Check science/tech first
    if contains_any(combined, science_kw):
        cat = 'Science/Technology'
    elif contains_any(combined, sports_kw):
        cat = 'Sports'
    elif contains_any(combined, business_kw):
        cat = 'Business'
    else:
        cat = 'World'
    categories.append(cat)

df['category'] = categories

# Now compute fraction for Amy Jones: the articles in this result are Amy's articles
total = len(df)
scitech_count = int((df['category'] == 'Science/Technology').sum())

# Prepare result string
fraction_str = f"{scitech_count}/{total}"
percentage = (scitech_count/total*100) if total>0 else 0
result_string = f"{fraction_str} ({percentage:.2f}%)"

# Build JSON-serializable output
output = {
    'science_technology_count': scitech_count,
    'total_articles': total,
    'fraction': fraction_str,
    'percentage': round(percentage, 2),
    'result_string': result_string,
    'per-article-categories': df[['article_id','title','category']].to_dict(orient='records')
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_7d18M0JuoP0ij30z47gaKyAg': [{'author_id': '218'}], 'var_call_2XUPOXCMNh5rYWVyHO9S2ahW': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_call_LYMgqRRczxLnFPjTV2HY612U': 'file_storage/call_LYMgqRRczxLnFPjTV2HY612U.json'}

exec(code, env_args)
