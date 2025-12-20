code = """import json
import pandas as pd

# Load Amy Jones article IDs
a_ids = [int(r['article_id']) for r in var_call_qUcrnaNRZgzphsIYZsRD7rmY]

# Load full articles file
with open(var_call_LVRs7aczj7j0vRDfqrnWWKhm, 'r') as f:
    articles = json.load(f)

# Filter articles authored by Amy Jones
amy_articles = [a for a in articles if int(a['article_id']) in a_ids]

# Very simple keyword-based categorization
science_keywords = ['science', 'scientist', 'research', 'study', 'studies', 'technology', 'tech ', 'computer', 'software', 'hardware', 'internet', 'online', 'web', 'physics', 'chemistry', 'biology', 'medical', 'medicine', 'space', 'nasa', 'genetic', 'gene', 'climate', 'environment', 'engineering']
world_keywords = ['iraq', 'election', 'president', 'minister', 'government', 'united nations', 'un ', 'war', 'conflict', 'attack', 'bomb', 'politics']
sports_keywords = ['game', 'games', 'season', 'team', 'teams', 'score', 'scored', 'coach', 'player', 'league', 'cup', 'tournament', 'olympics', 'nfl', 'nba', 'mlb', 'soccer', 'tennis', 'golf']


def categorize(text):
    t = text.lower()
    # Simple scores
    s_sci = sum(1 for k in science_keywords if k in t)
    s_world = sum(1 for k in world_keywords if k in t)
    s_sport = sum(1 for k in sports_keywords if k in t)
    # Business is default catch-all
    scores = {'Science/Technology': s_sci, 'World': s_world, 'Sports': s_sport, 'Business': 0}
    # If all scores zero, treat as Business
    if all(v == 0 for v in [s_sci, s_world, s_sport]):
        return 'Business'
    return max(scores.items(), key=lambda x: x[1])[0]

for a in amy_articles:
    text = (a.get('title','') or '') + ' ' + (a.get('description','') or '')
    a['category'] = categorize(text)

# Compute fraction Science/Technology
if len(amy_articles) == 0:
    frac = 0
else:
    sci_count = sum(1 for a in amy_articles if a['category'] == 'Science/Technology')
    frac = sci_count / len(amy_articles)

result = json.dumps({'total_articles': len(amy_articles), 'science_technology_articles': sci_count if len(amy_articles)>0 else 0, 'fraction_science_technology': frac})

print("__RESULT__:")
print(result)"""

env_args = {'var_call_qUcrnaNRZgzphsIYZsRD7rmY': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_call_LVRs7aczj7j0vRDfqrnWWKhm': 'file_storage/call_LVRs7aczj7j0vRDfqrnWWKhm.json'}

exec(code, env_args)
