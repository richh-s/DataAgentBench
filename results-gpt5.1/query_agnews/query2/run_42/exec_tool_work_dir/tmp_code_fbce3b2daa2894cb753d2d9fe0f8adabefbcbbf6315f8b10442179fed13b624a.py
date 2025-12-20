code = """import json
import pandas as pd

# Load Amy Jones's article IDs
auth_ids = [int(r['article_id']) for r in var_call_IsDUxlY6Y6y4wQmaDgTZUkiJ]

data_path = var_call_uLVGw5tcMJK0N3uUecXxXWUp
with open(data_path, 'r') as f:
    articles = json.load(f)

articles_df = pd.DataFrame(articles)
articles_df['article_id'] = articles_df['article_id'].astype(int)

amy_articles = articles_df[articles_df['article_id'].isin(auth_ids)].copy()

# Simple keyword-based categorization
def categorize(row):
    text = (row['title'] + ' ' + row['description']).lower()
    sci_tech_keywords = ['science', 'scientist', 'research', 'physics', 'biology', 'space', 'nasa', 'technology', 'software', 'computer', 'internet', 'online', 'web', 'virus', 'nuclear', 'laboratory', 'lab ', 'engineer', 'engineering', 'medical', 'medicine', 'clinical', 'trial', 'genetic', 'genome']
    sports_keywords = ['sport', 'game', 'match', 'tournament', 'league', 'cup', 'olympic', 'goal', 'score', 'coach', 'player', 'team']
    business_keywords = ['stock', 'market', 'share', 'company', 'business', 'profit', 'loss', 'trade', 'economy', 'economic', 'bank', 'loan', 'investment', 'investor']

    sci_tech = any(k in text for k in sci_tech_keywords)
    sports = any(k in text for k in sports_keywords)
    business = any(k in text for k in business_keywords)

    if sci_tech and not (sports or business):
        return 'Science/Technology'
    if sports and not (sci_tech or business):
        return 'Sports'
    if business and not (sci_tech or sports):
        return 'Business'
    # Fallbacks
    if sci_tech:
        return 'Science/Technology'
    if sports:
        return 'Sports'
    if business:
        return 'Business'
    return 'World'

if not amy_articles.empty:
    amy_articles['category'] = amy_articles.apply(categorize, axis=1)
    total = len(amy_articles)
    sci_tech_count = (amy_articles['category'] == 'Science/Technology').sum()
    fraction = sci_tech_count / total if total > 0 else None
else:
    total = 0
    sci_tech_count = 0
    fraction = None

result = {
    'total_articles_by_amy_jones': int(total),
    'science_technology_articles_by_amy_jones': int(sci_tech_count),
    'fraction_science_technology': fraction
}

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_IsDUxlY6Y6y4wQmaDgTZUkiJ': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_call_uLVGw5tcMJK0N3uUecXxXWUp': 'file_storage/call_uLVGw5tcMJK0N3uUecXxXWUp.json'}

exec(code, env_args)
