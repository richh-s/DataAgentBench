code = """import json
from math import gcd

# Access variables from previous tool calls
articles = var_call_nXXJTSipgZelEtRVl1G0hmJD
metadata_articles = var_call_HvtsKt8ZprzdWkeoQF425Xfr

# Extract article_ids from metadata (ensure ints)
meta_ids = [int(r['article_id']) for r in metadata_articles]

# Build a dict of article_id -> text (title + description)
texts = {}
for doc in articles:
    try:
        aid = int(doc.get('article_id'))
    except:
        continue
    title = doc.get('title') or ''
    desc = doc.get('description') or ''
    texts[aid] = (title + ' ' + desc).lower()

# Define keywords
sports_kw = ['football','soccer','basketball','cornerback','pro bowl','pro-bowl','practice','match','goal','scored','touchdown','wide receiver','wide reciever','defeated','beat','tries','wr','quarterback','pitch','innings','nba','nfl','mlb','cup','tournament','coach','team','player','olympic','olympics','season']
business_kw = ['company','companies','profit','profits','market','shares','economy','booming','mining','billion','million','stock','stocks','revenue','sales','bhp','bank','price','prices','boosts','acquires','acquisition','merger']
science_kw = ['science','technology','research','lab','laboratory','scientist','competition','award','electricity','machine','robot','computer','software','hardware','nasa','space','physics','chemistry','biology','innovation','micro-games','gameboy','gaming','gyro-gen','gyrogen','siemens','westinghouse']

# Classify
science_count = 0
classified_counts = {'Science/Technology': 0, 'Sports': 0, 'Business': 0, 'World': 0, 'Missing': 0}
for aid in meta_ids:
    text = texts.get(aid)
    if text is None:
        classified_counts['Missing'] += 1
        # Treat missing as World by default (but do not increment science)
        continue
    # sports first
    if any(kw in text for kw in sports_kw):
        classified_counts['Sports'] += 1
        continue
    if any(kw in text for kw in business_kw):
        classified_counts['Business'] += 1
        continue
    if any(kw in text for kw in science_kw):
        classified_counts['Science/Technology'] += 1
        science_count += 1
        continue
    # default
    classified_counts['World'] += 1

total = len(meta_ids)
num = science_count
den = total
# reduce fraction
if den == 0:
    frac_str = "0/0"
    decimal = None
else:
    g = gcd(num, den)
    frac_str = f"{num//g}/{den//g}"
    decimal = round(num/den, 4)

result = {
    'total_articles': total,
    'science_count': num,
    'fraction': frac_str,
    'decimal': decimal,
    'breakdown': classified_counts
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_4sf7ahfSAkh0f0IyiON0h9SL': [{'author_id': '218'}], 'var_call_HvtsKt8ZprzdWkeoQF425Xfr': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_call_nXXJTSipgZelEtRVl1G0hmJD': [{'_id': '69598fd53ceccf96da465e16', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '69598fd53ceccf96da4665c7', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '69598fd53ceccf96da466872', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '69598fd53ceccf96da466901', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '69598fd53ceccf96da466ad1', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}]}

exec(code, env_args)
