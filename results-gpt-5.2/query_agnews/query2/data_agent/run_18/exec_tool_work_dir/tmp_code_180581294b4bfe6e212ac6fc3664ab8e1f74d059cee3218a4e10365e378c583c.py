code = """import json, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r') as f:
            return json.load(f)
    return v

meta = load_records(var_call_KP9eFqORXpcC1szzmOiWH0VO)
arts = load_records(var_call_guUAVBTNzrMM3vrNwCY66tjE)

df_meta = pd.DataFrame(meta)
df_arts = pd.DataFrame(arts)

total = df_meta['article_id'].nunique()
retrieved = df_arts['article_id'].nunique() if not df_arts.empty else 0

# simple keyword classifier
sci_kw = [
    'science','technology','tech','research','scientist','scientists','space','nasa','mars','satellite','telescope',
    'robot','ai','artificial intelligence','computer','software','internet','web','cyber','security','virus','mobile',
    'phone','smartphone','iphone','android','chip','semiconductor','quantum','genome','genetic','dna','biotech',
    'medical','medicine','health','vaccine','disease','climate','energy','electricity','battery','physics','chemistry',
    'biology','math','mathematics','engineering'
]

biz_kw = ['profit','profits','shares','stock','market','bank','banks','economy','economic','merger','acquisition','oil','mining','company','companies','dollar','revenue']

sports_kw = ['game','match','season','coach','team','league','tournament','championship','nfl','nba','mlb','soccer','football','basketball','tennis','golf','broncos','pro bowl','wide receiver']

world_kw = ['war','election','president','government','iraq','afghanistan','china','russia','ukraine','israel','palestinian','terror','bomb','minister','parliament']

def categorize(title, desc):
    text = ((title or '') + ' ' + (desc or '')).lower()
    def has_any(kws):
        return any(kw in text for kw in kws)
    # choose Science/Technology first, then Business, Sports, World
    if has_any(sci_kw):
        return 'Science/Technology'
    if has_any(biz_kw):
        return 'Business'
    if has_any(sports_kw):
        return 'Sports'
    if has_any(world_kw):
        return 'World'
    return 'World'

if df_arts.empty:
    sci_count = 0
else:
    df_arts['category'] = df_arts.apply(lambda r: categorize(r.get('title'), r.get('description')), axis=1)
    sci_count = int((df_arts['category'] == 'Science/Technology').sum())

# fraction among all Amy Jones articles; if we didn't retrieve all, we can only compute on retrieved subset
fraction = sci_count / total if total else None

out = {
    'author': 'Amy Jones',
    'total_articles': int(total),
    'retrieved_articles_for_categorization': int(retrieved),
    'science_technology_articles': int(sci_count),
    'fraction_scitech_of_total': fraction
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_KP9eFqORXpcC1szzmOiWH0VO': [{'author_id': '218', 'name': 'Amy Jones', 'article_id': '192'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '2161'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '2844'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '2987'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '3451'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '3970'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '4447'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '5354'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '6705'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '6869'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '8962'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '9677'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '9858'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '14861'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '15100'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '15473'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '17491'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '19469'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '20362'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '21238'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '22354'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '23914'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '24495'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '25960'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '26535'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '27429'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '28079'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '29164'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '29297'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '33489'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '35408'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '35882'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '36182'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '36483'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '37042'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '38608'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '39117'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '39623'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '40545'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '41616'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '46531'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '47439'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '48635'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '48833'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '49035'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '52459'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '54906'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '57510'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '57860'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '57918'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '62404'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '62754'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '64102'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '66827'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '68509'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '68958'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '69262'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '69393'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '70498'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '70608'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '72525'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '73025'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '73684'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '78200'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '80578'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '80853'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '81851'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '82526'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '82668'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '83273'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '88553'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '88911'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '89666'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '91286'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '91822'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '92992'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '93287'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '93804'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '94618'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '96641'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '96986'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '99699'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '100613'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '101514'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '103003'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '103591'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '103695'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '104123'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '104996'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '104998'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '105804'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '106908'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '107036'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '108586'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '109601'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '110096'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '111422'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '112063'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '112770'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '113058'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '116698'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '119651'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '119920'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '120129'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '120765'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '122137'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '123747'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '124509'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '126412'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '126655'}, {'author_id': '218', 'name': 'Amy Jones', 'article_id': '126966'}], 'var_call_guUAVBTNzrMM3vrNwCY66tjE': [{'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}]}

exec(code, env_args)
