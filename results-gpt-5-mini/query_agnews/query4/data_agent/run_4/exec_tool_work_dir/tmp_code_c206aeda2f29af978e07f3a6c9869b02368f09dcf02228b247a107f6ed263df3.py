code = """import json
# Load metadata 2015 records from file stored in var_call_Daa8lM9TAamUdd11DC7tAQtu
with open(var_call_Daa8lM9TAamUdd11DC7tAQtu, 'r') as f:
    meta2015 = json.load(f)
# Articles list is stored in var_call_pm8bUbFTfliwACrNwuneM9uD
articles = var_call_pm8bUbFTfliwACrNwuneM9uD

# Build maps
meta_map = {int(item['article_id']): item['region'] for item in meta2015}
articles_map = {int(a['article_id']): (a.get('title','') + ' ' + a.get('description','')) for a in articles}

# Keywords for classification
sports_kw = ['match','goal','tournament','season','football','soccer','basketball','baseball','tennis','cricket','score','coach','team','league','olympic','olympics','fifa','nba','mlb','nfl','player','match','cup']
business_kw = ['market','markets','stocks','stock','economy','economics','shares','bonds','invest','investment','company','companies','firm','bank','banks','ipo','revenue','earnings','profit','business','financial']
science_kw = ['technology','technolog','scientists','research','nasa','space','computer','software','hardware','iphone','android','ai','artificial intelligence','scientific','study','tech','robot','physics','biology','chemistry','satellite','spacecraft','scientist','engineer']
world_kw = ['president','government','election','elections','war','conflict','country','countries','minister','diplomat','diplomacy','united nations','un ','attack','attacked','killed','military','terror','refugee','border','parliament','police','protest','protests']

# Helper to check presence
def contains_any(text, keywords):
    t = text.lower()
    for kw in keywords:
        if kw in t:
            return True
    return False

# Classify function
def classify(text):
    if contains_any(text, sports_kw):
        return 'Sports'
    if contains_any(text, business_kw):
        return 'Business'
    if contains_any(text, science_kw):
        return 'Science/Technology'
    if contains_any(text, world_kw):
        return 'World'
    # fallback: if contains Reuters/AFP etc and finance words, Business
    if 'reuters' in text.lower() or 'bloomberg' in text.lower() or 'afp' in text.lower():
        # check for markets or economy
        if contains_any(text, business_kw):
            return 'Business'
    # default to World
    return 'World'

# Count World category per region for 2015
from collections import Counter
region_counter = Counter()
missing = 0
for aid, region in meta_map.items():
    text = articles_map.get(aid)
    if text is None:
        missing += 1
        continue
    cat = classify(text)
    if cat == 'World':
        region_counter[region] += 1

# Determine top region
if region_counter:
    top_region, top_count = region_counter.most_common(1)[0]
    result_str = f"{top_region} ({top_count} articles)"
else:
    result_str = "No World articles found in 2015"

print("__RESULT__:")
print(json.dumps(result_str))"""

env_args = {'var_call_Daa8lM9TAamUdd11DC7tAQtu': 'file_storage/call_Daa8lM9TAamUdd11DC7tAQtu.json', 'var_call_r2RqtKEsSm0kqgwsQxyqUVCE': 'file_storage/call_r2RqtKEsSm0kqgwsQxyqUVCE.json', 'var_call_pm8bUbFTfliwACrNwuneM9uD': [{'_id': '6959a3027d138fbd7120e8d1', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6959a3027d138fbd7120e8d2', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6959a3027d138fbd7120e8d3', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6959a3027d138fbd7120e8d4', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6959a3027d138fbd7120e8d5', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
