code = """import json
import pandas as pd

# Load data from previous queries
ids = pd.DataFrame(var_call_8EQ3cb7HRnINhEMu5qJL2Tmi)
articles = pd.DataFrame(var_call_JUcsiC6O57x1UmI6vooJHdkS)

# Normalize types
ids['article_id'] = ids['article_id'].astype(int)
if 'article_id' in articles.columns:
    articles['article_id'] = articles['article_id'].astype(int)
else:
    articles['article_id'] = articles['article_id'].astype(int)

# Build lookup
articles_lookup = {row['article_id']: {'title': row.get('title','') or '', 'description': row.get('description','') or ''} for _, row in articles.iterrows()}

# Keywords for categories
sports_kw = ['pro', 'cornerback', 'wide receiver', 'wide reciever', 'broncos', 'practice', 'pro bowl', 'goal', 'season', 'tournament', 'score', 'match', 'nfl', 'basketball', 'soccer', 'football', 'baseball', 'player', 'tries wr']
business_kw = ['profit', 'profits', 'company', 'mining', 'market', 'shares', 'stocks', 'economy', 'business', 'trade', 'bank', 'earnings', 'boosts', 'bhp']
scitech_kw = ['science', 'technology', 'research', 'laboratory', 'lab', 'university', 'competition', 'siemens', 'westinghouse', 'electricity', 'energy', 'machine', 'gyro-gen', 'gameboy', 'micro-games', 'microgames', 'innovative', 'computer', 'software', 'tech', 'robot', 'nasa', 'space', 'waves', 'scientist', 'award', 'researcher', 'chemistry', 'physics', 'biology', 'medical', 'technology']
world_kw = ['scotland', 'country', 'government', 'president', 'minister', 'war', 'protests', 'election', 'china', "china's", 'global']

def categorize_text(text):
    t = (text or '').lower()
    scores = {'Sports':0, 'Business':0, 'Science/Technology':0, 'World':0}
    for kw in sports_kw:
        if kw in t:
            scores['Sports'] += 1
    for kw in business_kw:
        if kw in t:
            scores['Business'] += 1
    for kw in scitech_kw:
        if kw in t:
            scores['Science/Technology'] += 1
    for kw in world_kw:
        if kw in t:
            scores['World'] += 1
    # Choose category with highest score; if tie and all zero -> World
    max_score = max(scores.values())
    if max_score == 0:
        return 'World'
    # If tie, prefer Science/Technology over others, then Business, Sports, World
    candidates = [k for k,v in scores.items() if v==max_score]
    priority = ['Science/Technology','Business','Sports','World']
    for p in priority:
        if p in candidates:
            return p
    return candidates[0]

# Categorize all articles for the author
results = []
for aid in ids['article_id'].tolist():
    info = articles_lookup.get(aid, {'title':'', 'description':''})
    text = (info.get('title','') or '') + ' ' + (info.get('description','') or '')
    cat = categorize_text(text)
    results.append({'article_id': int(aid), 'category': cat, 'title': info.get('title',''), 'description': info.get('description','')})

df_res = pd.DataFrame(results)
total = len(df_res)
scitech_count = int((df_res['category']=='Science/Technology').sum())

# Fraction as simplified fraction and decimal
from fractions import Fraction
fract = Fraction(scitech_count, total)
fract_str = f"{fract.numerator}/{fract.denominator}"
decimal = scitech_count/total if total>0 else 0.0

output = {'scitech_count': scitech_count, 'total_articles': total, 'fraction': fract_str, 'decimal': round(decimal,4)}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_XXlbbj5yIN6HAn9EImfdEDP7': [{'author_id': '218'}], 'var_call_8EQ3cb7HRnINhEMu5qJL2Tmi': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_call_JUcsiC6O57x1UmI6vooJHdkS': [{'_id': '6959949d3c037b12064fe527', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '6959949d3c037b12064fecd8', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '6959949d3c037b12064fef83', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '6959949d3c037b12064ff012', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '6959949d3c037b12064ff1e2', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}]}

exec(code, env_args)
