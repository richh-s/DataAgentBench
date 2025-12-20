code = """import json, pandas as pd

amy_articles = pd.DataFrame(var_call_5HmkbTPI9CA0uF3YgP4SENJj)

# Load full articles data
with open(var_call_XtP7dX0gs7qWGazTkzod7BDt, 'r') as f:
    articles_data = json.load(f)
articles = pd.DataFrame(articles_data)

# Keep only Amy Jones's articles
amy_articles['article_id'] = amy_articles['article_id'].astype(str)
articles['article_id'] = articles['article_id'].astype(str)
amy_full = articles.merge(amy_articles, on='article_id', how='inner')

# Simple keyword-based classifier for 4 categories
science_keywords = ['science', 'scientist', 'nasa', 'space', 'experiment', 'technology', 'software', 'hardware', 'computer', 'internet', 'research', 'biology', 'physics', 'chemistry', 'astronomy', 'genetic', 'robot', 'ai', 'artificial intelligence', 'quantum', 'engineer', 'engineering']
sports_keywords = ['game', 'games', 'season', 'team', 'teams', 'coach', 'league', 'score', 'scored', 'match', 'tournament', 'cup', 'olympic', 'olympics', 'nfl', 'nba', 'mlb', 'nhl', 'soccer', 'football', 'baseball', 'basketball', 'tennis', 'golf']
business_keywords = ['stock', 'stocks', 'market', 'markets', 'shares', 'profit', 'profits', 'loss', 'losses', 'company', 'companies', 'business', 'economic', 'economy', 'trade', 'oil', 'bank', 'banks', 'fund', 'funds', 'ipo', 'merger', 'acquisition', 'earnings', 'revenue']


def classify(row):
    text = (str(row['title']) + ' ' + str(row['description'])).lower()
    def has_kw(kws):
        return any(k in text for k in kws)
    is_science = has_kw(science_keywords)
    is_sports = has_kw(sports_keywords)
    is_business = has_kw(business_keywords)
    # Priority: Sports, Business, Science/Tech, else World
    if is_sports and not (is_business or is_science):
        return 'Sports'
    if is_business and not is_sports and not is_science:
        return 'Business'
    if is_science and not is_sports and not is_business:
        return 'Science/Technology'
    # tie-breaking
    if is_sports:
        return 'Sports'
    if is_business:
        return 'Business'
    if is_science:
        return 'Science/Technology'
    return 'World'

amy_full['category'] = amy_full.apply(classify, axis=1)

total = len(amy_full)
science_tech = (amy_full['category'] == 'Science/Technology').sum()
frac = science_tech / total if total > 0 else None

result = json.dumps({"total_articles": int(total), "science_tech_articles": int(science_tech), "fraction_science_tech": frac})

print("__RESULT__:")
print(result)"""

env_args = {'var_call_5HmkbTPI9CA0uF3YgP4SENJj': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_call_XtP7dX0gs7qWGazTkzod7BDt': 'file_storage/call_XtP7dX0gs7qWGazTkzod7BDt.json'}

exec(code, env_args)
