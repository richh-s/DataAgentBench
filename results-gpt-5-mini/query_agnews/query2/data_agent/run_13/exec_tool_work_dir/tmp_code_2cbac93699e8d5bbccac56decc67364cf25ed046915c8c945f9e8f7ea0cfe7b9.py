code = """import json, re
# Load the Mongo query result from the provided storage file path
path = var_call_3jwq2WtnjjB4c2cqwUWjVr1s
with open(path, 'r', encoding='utf-8') as f:
    articles = json.load(f)

# Prepare keyword patterns for categories
sports_kw = [r'\bwin\b', r'\bwins\b', r'\bdefeat\b', r'\bdefeated\b', r'\blose\b', r'\bloses\b', r'\boleague\b', r'\bchampions league\b', r'\bolympic\b', r'\bsemi-final\b', r'\bquarter-final\b', r'\bmatch\b', r'\bcoach\b', r'\bgoal\b', r'\btennis\b', r'\bbaseball\b', r'\bsoccer\b', r'\bfootball\b', r'\bcaptain\b', r'\bcycl(e|ing)\b', r'\bumpire\b', r'\bpro bowl\b', r'\bchampionship\b']
business_kw = [r'\bprofit\b', r'\bprofits\b', r'\brevenue\b', r'\bearnings\b', r'\bstocks\b', r'\bshares\b', r'\bmarket\b', r'\beconomy\b', r'\btrades?\b', r'\btrade\b', r'\bcompany\b', r'\bcorp\b', r'\breuters\b', r'\bsettle(s|d)\b', r'\bprice(s)?\b', r'\bproducer prices\b', r'\bbank\b', r'\bfinancial\b', r'\bWTO\b', r'\bcost\b']
science_kw = [r'\bscience\b', r'\bscientist\b', r'\bresearch\b', r'\blaborator(y|ies)\b', r'\blab\b', r'\bnuclear\b', r'\bspace\b', r'\bNASA\b', r'\bprobe\b', r'\bshuttle\b', r'\bexperiment\b', r'\btechnology\b', r'\btech\b', r'\bcomputer\b', r'\bsoftware\b', r'\belectricit(y|ies)\b', r'\bphysics\b', r'\bchemical\b', r'\bbiology\b', r'\bEMC\b', r'\bIntel\b', r'\bMicrosoft\b', r'\bSiemens\b', r'\bWestinghouse\b', r'\bgenesis\b', r'\bGyro-Gen\b', r'\bnuclear physicist\b']
world_kw = [r'\bGaza\b', r'\bIsrael\b', r'\bPalestin\b', r'\bSomali\b', r'\bNepal\b', r'\bGeneva\b', r'\bPrime Minister\b', r'\bmilitant\b', r'\bNairobi\b', r'\bIraq\b', r'\bBush\b', r'\bKerry\b', r'\bWorld\b', r'\bdiplomat\b', r'\bAfghan\b', r'\bGaza\b']

# Compile regex patterns (case-insensitive)
def compile_patterns(lst):
    return [re.compile(p, flags=re.IGNORECASE) for p in lst]

sports_p = compile_patterns(sports_kw)
business_p = compile_patterns(business_kw)
science_p = compile_patterns(science_kw)
world_p = compile_patterns(world_kw)

def score_text(text, patterns):
    s = 0
    for p in patterns:
        if p.search(text):
            s += 1
    return s

classified = []
science_count = 0
for art in articles:
    aid = art.get('article_id')
    title = art.get('title','') or ''
    desc = art.get('description','') or ''
    text = (title + ' ' + desc).strip()
    # Score each category
    scores = {
        'Sports': score_text(text, sports_p),
        'Business': score_text(text, business_p),
        'Science/Technology': score_text(text, science_p),
        'World': score_text(text, world_p)
    }
    # Determine highest score; tie-breaker priority: Sports, Business, Science/Technology, World
    max_score = max(scores.values())
    if max_score == 0:
        # fallback: classify as World if no keywords found
        category = 'World'
    else:
        # collect categories with max score
        winners = [k for k,v in scores.items() if v == max_score]
        for pref in ['Sports','Business','Science/Technology','World']:
            if pref in winners:
                category = pref
                break
    if category == 'Science/Technology':
        science_count += 1
    classified.append({'article_id': aid, 'title': title, 'category': category, 'scores': scores})

total = len(articles)
from fractions import Fraction
fract = Fraction(science_count, total)
decimal = round(science_count / total, 4) if total>0 else None
percentage = round(decimal * 100, 2) if decimal is not None else None

result = {
    'science_count': science_count,
    'total_count': total,
    'fraction': f"{fract.numerator}/{fract.denominator}",
    'decimal': decimal,
    'percentage': percentage,
    # include list of article_ids classified as Science/Technology for transparency
    'science_article_ids': [c['article_id'] for c in classified if c['category']=='Science/Technology']
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_1jGsG8w2mi53zhIZkPl7WzVk': [{'author_id': '218'}], 'var_call_p1iDO2e873kj4BC5L74T1GJ8': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_call_3jwq2WtnjjB4c2cqwUWjVr1s': 'file_storage/call_3jwq2WtnjjB4c2cqwUWjVr1s.json'}

exec(code, env_args)
