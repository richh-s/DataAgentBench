code = """import json
articles = var_call_0wNuShmhHeKt8pBz18izImGn
# list of article ids for Amy Jones
amy_ids = var_call_aOTUwQPjWHFhvZPV8LaKyye0
# Ensure articles list are dicts, convert article_id to int
for a in articles:
    try:
        a['article_id'] = int(a.get('article_id'))
    except:
        pass
# Build text and classify
science_kw = ['science','scientist','research','laboratory','university','competition','technology','tech','robot','robotics','electricity','wave','waves','nasa','software','computer','algorithm','device','micro-games','gameboy','video game','gyrogen','gyro-gen','engineering','biology','chemistry','physics','lab','study','studies','siemens','westinghouse']
# sports
sports_kw = ['cornerback','pro bowl','wide receiver','wide receiver','bronco','score','goal','match','player','team','season','coach','touchdown','wr','nba','mlb','nfl','soccer','basketball','rugby','tennis','win','wins','defeat','defeats','defeated','beat','beats']
# business
business_kw = ['profit','profits','company','companies','market','shares','stock','bank','investment','economic','economy','mining','commodity','bhp','billiton','revenue','merger','acquisition']

def contains_any(text, keywords):
    for kw in keywords:
        if kw in text:
            return True
    return False

classified = []
for a in articles:
    title = (a.get('title') or '')
    desc = (a.get('description') or '')
    text = (title + ' ' + desc).lower()
    cat = 'World'
    if contains_any(text, science_kw):
        cat = 'Science/Technology'
    elif contains_any(text, sports_kw):
        cat = 'Sports'
    elif contains_any(text, business_kw):
        cat = 'Business'
    classified.append({'article_id': a.get('article_id'), 'title': title, 'category': cat})

# Count
total = len(classified)
science_count = sum(1 for c in classified if c['category']=='Science/Technology')

# Prepare result
from fractions import Fraction
if total>0:
    frac = Fraction(science_count, total)
    frac_str = f"{science_count}/{total}"
    decimal = round(science_count/total, 4)
    percent = round(decimal*100,2)
else:
    frac_str = "0/0"
    decimal = None
    percent = None

result = {'science_count': science_count, 'total': total, 'fraction': frac_str, 'decimal': decimal, 'percentage': percent, 'classified_sample': classified[:10]}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_tXahDRctxmEOP97nShef4R9k': ['authors', 'article_metadata'], 'var_call_zvKqKs2UuoKuM7MS6uPMuq33': 'file_storage/call_zvKqKs2UuoKuM7MS6uPMuq33.json', 'var_call_aOTUwQPjWHFhvZPV8LaKyye0': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966], 'var_call_0wNuShmhHeKt8pBz18izImGn': [{'_id': '69598e247e5ce247758e8c32', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '69598e247e5ce247758e93e3', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '69598e247e5ce247758e968e', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '69598e247e5ce247758e971d', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '69598e247e5ce247758e98ed', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}]}

exec(code, env_args)
