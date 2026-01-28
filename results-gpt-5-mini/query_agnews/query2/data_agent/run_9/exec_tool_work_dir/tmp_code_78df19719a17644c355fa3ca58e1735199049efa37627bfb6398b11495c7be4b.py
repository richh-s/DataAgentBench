code = """import json
from collections import Counter
# Load previous tool results
metadata_records = var_call_SamoHvx2z0viysEV6aRVdoEp
articles_docs = var_call_xZWfnuxyc1HPFiT9IQVkBriw

# Extract article_ids from metadata (strings in records)
metadata_ids = [int(r['article_id']) for r in metadata_records]
total_authored = len(metadata_ids)

# Build mapping from article_id to text
article_map = {}
for d in articles_docs:
    try:
        aid = int(d.get('article_id'))
    except:
        continue
    title = d.get('title') or ''
    desc = d.get('description') or ''
    article_map[aid] = (title, desc)

# Define keyword-based classification
sports_kw = ['game', 'season', 'team', 'coach', 'player', 'pro bowl', 'pro-bowl', 'probowl', 'pro bowl', 'broncos', 'cornerback', 'wide receiver', 'wr', 'quarterback', 'goal', 'match', 'tournament', 'nba', 'nfl', 'mlb', 'soccer', 'basketball', 'football', 'baseball', 'score', "pro bowl", 'practice', 'defense', 'offense']
science_kw = ['science', 'technology', 'research', 'laboratory', 'lab', 'innovative', 'machine', 'electricity', 'siemens', 'westinghouse', 'competition', 'experiment', 'robot', 'tech', 'gameboy', 'micro-games', 'microgames', 'micro game']
business_kw = ['profit', 'profits', 'company', 'market', 'shares', 'stock', 'economy', 'revenue', 'commodit', 'bhp', 'billiton', 'merger', 'acquire', 'acquisition', 'prices', 'boosts']
world_kw = ['country', 'government', 'president', 'election', 'minister', 'attack', 'war', 'china', 'russia', 'uk', 'united states', 'india', 'san', 'scotland', 'region', 'city', 'national']

def classify(title, desc):
    text = (title + ' ' + desc).lower()
    # Exact phrase matches for some tokens
    score = Counter()
    for kw in sports_kw:
        if kw in text:
            score['Sports'] += 1
    for kw in science_kw:
        if kw in text:
            score['Science/Technology'] += 1
    for kw in business_kw:
        if kw in text:
            score['Business'] += 1
    for kw in world_kw:
        if kw in text:
            score['World'] += 1
    if not score:
        # fallback: classify as World
        return 'World'
    # choose highest score; tie-breaker: Science/Technology > Sports > Business > World
    best = score.most_common()
    top_score = best[0][1]
    candidates = [cat for cat, sc in score.items() if sc == top_score]
    order = ['Science/Technology','Sports','Business','World']
    for o in order:
        if o in candidates:
            return o
    return candidates[0]

# Classify each article in metadata list if present, else mark as 'Missing'
classified = {}
counts = Counter()
missing_count = 0
for aid in metadata_ids:
    if aid in article_map:
        title, desc = article_map[aid]
        cat = classify(title, desc)
        classified[aid] = cat
        counts[cat] += 1
    else:
        classified[aid] = 'Missing'
        missing_count += 1
        counts['Missing'] += 1

science_count = counts.get('Science/Technology', 0)
# Prepare result
result = {
    'total_authored': total_authored,
    'found_in_articles_collection': total_authored - missing_count,
    'missing_in_articles_collection': missing_count,
    'science_technology_count': science_count,
    'fraction': f"{science_count}/{total_authored}",
    'percentage': round((science_count/total_authored*100) if total_authored>0 else 0, 2)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_mY8Cu74NqMtmMWbS1H4Ta4VK': [{'author_id': '218'}], 'var_call_SamoHvx2z0viysEV6aRVdoEp': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_call_xZWfnuxyc1HPFiT9IQVkBriw': [{'_id': '69598bf470007f829c105b2d', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '69598bf470007f829c1062de', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '69598bf470007f829c106589', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '69598bf470007f829c106618', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '69598bf470007f829c1067e8', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}]}

exec(code, env_args)
