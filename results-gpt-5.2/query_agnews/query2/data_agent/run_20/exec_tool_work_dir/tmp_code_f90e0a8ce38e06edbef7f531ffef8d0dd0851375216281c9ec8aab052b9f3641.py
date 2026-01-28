code = """import json, re
import pandas as pd

def load_records(obj):
    if isinstance(obj, str) and obj.endswith('.json'):
        with open(obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return obj

records = load_records(var_call_CGmvunBiZLrF64Qs841wYumU)

def classify(title, desc):
    t = (title or '').lower()
    d = (desc or '').lower()
    text = t + ' ' + d
    # sports
    sports_kw = ['vs', 'defeat', 'match', 'season', 'olympic', 'champions league', 'world cup', 'open', 'quarter-final', 'semifinal', 'semi-final', 'goal', 'races', 'broncos', 'giants', 'dodgers', 'liverpool', 'cricket', 'tennis', 'cycling', 'baseball', 'soccer', 'football', 'nba', 'nfl', 'mlb']
    # business
    business_kw = ['stocks', 'shares', 'profit', 'earnings', 'revenue', 'wto', 'trade', 'oil prices', 'company', 'corp', 'acquisition', 'market', 'economic', 'inflation', 'producer prices', 'debt', 'forecasts', 'mining', 'billiton', 'microsoft settles', 'intel']
    # world
    world_kw = ['iraq', 'israeli', 'gaza', 'west bank', 'sharon', 'somalia', 'kathmandu', 'nepal', 'ira', 'british', 'curfew', 'parliament', 'missiles', 'militants']
    # sci/tech
    sci_kw = ['nasa', 'space', 'shuttle', 'probe', 'genesis mission', 'science', 'technology', 'gameboy', 'intel', 'microsoft', 'e-mail', 'server', 'mobile phone', 'laboratory', 'physics', 'nuclear', 'electricity', 'waves', 'competition in math']

    def score(kws):
        return sum(1 for kw in kws if kw in text)

    scores = {
        'Sports': score(sports_kw),
        'Business': score(business_kw),
        'World': score(world_kw),
        'Science/Technology': score(sci_kw)
    }
    # tie-breaker preference: if explicit science/tech terms exist
    if scores['Science/Technology']>0 and scores['Science/Technology']>=max(scores.values()):
        return 'Science/Technology'
    # else max
    mx = max(scores.values())
    # if all zero, default based on some cues
    if mx==0:
        # default to World if mentions countries/conflict else Business if money else Sports if teams else Sci/Tech if tech words
        if any(w in text for w in ['government','minister','election','war','killed']):
            return 'World'
        if any(w in text for w in ['inc','corp','co.','$','billion','million']):
            return 'Business'
        if any(w in text for w in ['game','team','win','coach']):
            return 'Sports'
        return 'Business'
    # if tie among categories, decide with some priority order based on stronger signals
    tied = [k for k,v in scores.items() if v==mx]
    if len(tied)==1:
        return tied[0]
    # prioritize Sports if sports-specific words present
    if 'Sports' in tied and any(w in text for w in ['olympic','open','goal','match','league','races']):
        return 'Sports'
    if 'World' in tied and any(w in text for w in ['iraq','israel','gaza','west bank','somalia','nepal','ira']):
        return 'World'
    if 'Business' in tied and any(w in text for w in ['stocks','shares','profit','earnings','revenue','wto','trade','oil']):
        return 'Business'
    if 'Science/Technology' in tied:
        return 'Science/Technology'
    return tied[0]

cats = [classify(r.get('title'), r.get('description')) for r in records]
science_count = sum(1 for c in cats if c=='Science/Technology')
total = len(cats)
frac = science_count/total if total else None
out = {'science_tech': science_count, 'total': total, 'fraction': frac}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_idKyl0iP6oytZdhWuaLzA3Jd': [{'author_id': '218'}], 'var_call_Is96oL2aL5CEaBky8jRupweK': [{'total': '111'}], 'var_call_IcB8AZ2r3CzixSXvKW7QAUyb': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_call_CGmvunBiZLrF64Qs841wYumU': 'file_storage/call_CGmvunBiZLrF64Qs841wYumU.json'}

exec(code, env_args)
