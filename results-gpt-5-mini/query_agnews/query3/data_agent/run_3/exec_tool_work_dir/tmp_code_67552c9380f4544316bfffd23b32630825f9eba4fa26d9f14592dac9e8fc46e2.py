code = """import json
import pandas as pd

# Load metadata results from file and articles list from storage variables
with open(var_call_lMKPedsYoi6XU7702hFzRgG6, 'r') as f:
    metadata = json.load(f)
articles = var_call_ykaHOiCj1TUDrzxMLvXVv8NF

# DataFrames
df_meta = pd.DataFrame(metadata)
df_articles = pd.DataFrame(articles)

# Ensure article_id as string
df_meta['article_id'] = df_meta['article_id'].astype(str)
df_articles['article_id'] = df_articles['article_id'].astype(str)

# Merge on article_id (left join keeping only metadata rows)
df = pd.merge(df_meta, df_articles, on='article_id', how='left')

# Prepare text for classification
df['title'] = df.get('title', pd.Series(['']*len(df))).fillna('')
df['description'] = df.get('description', pd.Series(['']*len(df))).fillna('')
df['text'] = (df['title'] + ' ' + df['description']).str.lower()

# Define keyword sets for simple rule-based classification
business_kw = ['economy','economic','business','market','markets','stock','stocks','carlyle','investment','investor','investors','wall st','wall street','earnings','revenue','profit','profits','company','companies','commercial','financial','bank','banks','merger','acquisition','ipo','oil prices','oil','prices','short-sellers','short sellers','private investment']
world_kw = ['president','election','military','war','peace','country','countries','government','governments','minister','iraq','syria','diplomatic','foreign','officials']
sports_kw = ['match','football','soccer','tennis','nba','mlb','olympics','season','coach','goal','win','wins','player','players','tournament']
science_kw = ['technology','tech','scientist','scientists','research','study','nasa','space','software','smartphone','science']

def score_text(text, keywords):
    s = 0
    for kw in keywords:
        if kw in text:
            s += 1
    return s

def classify(text):
    b = score_text(text, business_kw)
    w = score_text(text, world_kw)
    s = score_text(text, sports_kw)
    c = score_text(text, science_kw)
    scores = {'Business': b, 'World': w, 'Sports': s, 'Science/Technology': c}
    max_score = max(scores.values())
    if max_score == 0:
        return 'World'
    top = [k for k,v in scores.items() if v == max_score]
    priority = ['Business','World','Sports','Science/Technology']
    for p in priority:
        if p in top:
            return p

# Classify
if 'text' not in df.columns:
    df['text'] = ''

df['category'] = df['text'].apply(classify)

# Extract year
df['year'] = df['publication_date'].str.slice(0,4)

# Count business articles per year for 2010-2020 inclusive
years = [str(y) for y in range(2010, 2021)]
counts_by_year = {y: int(df[(df['year'] == y) & (df['category'] == 'Business')].shape[0]) for y in years}

# Compute average
total = sum(counts_by_year.values())
avg = total / len(years) if len(years) > 0 else 0.0

result = {
    'counts_by_year': counts_by_year,
    'total_business_articles_2010_2020': total,
    'average_business_articles_per_year_2010_2020': avg
}

# Print result following required format
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_lMKPedsYoi6XU7702hFzRgG6': 'file_storage/call_lMKPedsYoi6XU7702hFzRgG6.json', 'var_call_ykaHOiCj1TUDrzxMLvXVv8NF': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
