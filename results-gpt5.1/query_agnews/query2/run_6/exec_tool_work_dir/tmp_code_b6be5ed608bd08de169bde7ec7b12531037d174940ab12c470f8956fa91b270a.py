code = """import json, pandas as pd

auth_articles = pd.DataFrame(var_call_ElQxFsadLP3WtFBdydxfQITH)

# Load full articles data
path = var_call_dS1e23eaTqGC7LBwtShuIPXZ
with open(path, 'r') as f:
    articles = json.load(f)
articles_df = pd.DataFrame(articles)

# Ensure article_id types match
auth_articles['article_id'] = auth_articles['article_id'].astype(int)
articles_df['article_id'] = articles_df['article_id'].astype(int)

# Join to get only Amy Jones's articles with text
merged = auth_articles.merge(articles_df, on='article_id', how='inner')

# Simple rule-based classifier into 4 categories based on title+description keywords
import re

def classify(row):
    text = f"{row['title']} {row['description']}".lower()
    # Science/Technology keywords
    sci_tech_kw = ['technology', 'technologies', 'tech ', 'tech-', 'computer', 'computers', 'software', 'hardware', 'internet', 'web ', 'online', 'digital', 'science', 'scientist', 'scientists', 'research', 'researchers', 'nuclear', 'space', 'nasa', 'astronaut', 'biotech', 'biotechnology', 'genetic', 'genome', 'physics', 'chemistry', 'biology', 'medical research', 'drug trial', 'clinical trial', 'robot', 'ai ', 'artificial intelligence', 'phone', 'mobile', 'cellphone', 'smartphone', 'gadget', 'patent', 'engineering']
    sports_kw = ['sport', 'sports', 'game', 'match', 'tournament', 'league', 'cup', 'olympic', 'olympics', 'nfl', 'nba', 'mlb', 'nhl', 'soccer', 'goal', 'coach', 'player', 'team', 'season', 'final', 'quarterback']
    business_kw = ['stock', 'stocks', 'market', 'shares', 'wall st', 'economy', 'economic', 'business', 'profit', 'losses', 'merger', 'acquisition', 'ipo', 'bond', 'currency', 'trade', 'trading', 'bank', 'banks', 'loan', 'budget', 'deficit', 'investment', 'investor', 'fund', 'company', 'companies', 'corporate']
    # Simple scoring
    s_sci = sum(1 for kw in sci_tech_kw if kw in text)
    s_sport = sum(1 for kw in sports_kw if kw in text)
    s_bus = sum(1 for kw in business_kw if kw in text)
    if s_sci >= s_sport and s_sci >= s_bus:
        return 'Science/Technology'
    if s_sport >= s_sci and s_sport >= s_bus:
        return 'Sports'
    if s_bus >= s_sci and s_bus >= s_sport:
        return 'Business'
    return 'World'

merged['category'] = merged.apply(classify, axis=1)

# Compute fraction of Amy Jones's articles that are Science/Technology
total = len(merged)
if total == 0:
    frac = None
else:
    sci_count = (merged['category'] == 'Science/Technology').sum()
    frac = sci_count / total

result = json.dumps({'total_articles': int(total), 'science_tech_articles': int((merged['category'] == 'Science/Technology').sum()), 'fraction_science_tech': frac})

print("__RESULT__:")
print(result)"""

env_args = {'var_call_ElQxFsadLP3WtFBdydxfQITH': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_call_dS1e23eaTqGC7LBwtShuIPXZ': 'file_storage/call_dS1e23eaTqGC7LBwtShuIPXZ.json'}

exec(code, env_args)
