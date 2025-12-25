code = """import json, pandas as pd

amy_articles = pd.DataFrame(var_call_OLsgAkvmbgGC6gP5TCoJoYVI)
amy_articles['article_id'] = amy_articles['article_id'].astype(int)

# Load full articles data
path = var_call_eoWSueqwN8qQRAadAklRnbjA
with open(path, 'r') as f:
    articles_data = json.load(f)
articles = pd.DataFrame(articles_data)
articles['article_id'] = articles['article_id'].astype(int)

# Merge to get Amy's articles with text
merged = pd.merge(amy_articles, articles, on='article_id', how='inner')

# Basic rule-based categorization using keywords
science_keywords = ['science', 'scientist', 'study', 'research', 'technology', 'tech ', 'software', 'hardware', 'computer', 'internet', 'online', 'virus', 'bacteria', 'nasa', 'space', 'galaxy', 'planet', 'robot', 'ai ', 'artificial intelligence', 'genetic', 'dna', 'biotech', 'physics', 'chemistry', 'engineering']

business_keywords = ['stock', 'market', 'shares', 'bond', 'bank', 'economy', 'economic', 'trade', 'company', 'business', 'profit', 'loss', 'oil', 'currency', 'deficit', 'investment', 'investor']

sports_keywords = ['game', 'match', 'tournament', 'league', 'score', 'goal', 'coach', 'player', 'team', 'olympics', 'nfl', 'nba', 'mlb', 'soccer', 'cricket', 'tennis', 'golf']

world_keywords = ['president', 'prime minister', 'election', 'war', 'conflict', 'u.n.', 'united nations', 'government', 'parliament', 'iraq', 'afghanistan', 'security council', 'rebel', 'troops', 'terrorist', 'bomb']


def categorize(row):
    text = (row['title'] + ' ' + row['description']).lower()
    def has_kw(keywords):
        return any(k in text for k in keywords)
    if has_kw(science_keywords):
        return 'Science/Technology'
    if has_kw(sports_keywords):
        return 'Sports'
    if has_kw(business_keywords):
        return 'Business'
    if has_kw(world_keywords):
        return 'World'
    # fallback: default to World
    return 'World'

merged['category'] = merged.apply(categorize, axis=1)

total = len(merged)
science_count = (merged['category'] == 'Science/Technology').sum()
frac = science_count / total if total > 0 else None

result = json.dumps({"total_articles": int(total), "science_technology_articles": int(science_count), "fraction_science_technology": frac})

print("__RESULT__:")
print(result)"""

env_args = {'var_call_OLsgAkvmbgGC6gP5TCoJoYVI': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_call_eoWSueqwN8qQRAadAklRnbjA': 'file_storage/call_eoWSueqwN8qQRAadAklRnbjA.json'}

exec(code, env_args)
