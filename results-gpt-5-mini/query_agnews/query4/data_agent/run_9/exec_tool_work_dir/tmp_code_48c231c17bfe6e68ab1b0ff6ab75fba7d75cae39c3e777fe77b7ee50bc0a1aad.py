code = """import json
import pandas as pd

# Load data from storage file paths provided by earlier tool calls
with open(var_call_gMXk1haVK74LEry5MP21tLTh, 'r') as f:
    articles = json.load(f)
with open(var_call_DYFiHVDQnHR5pGXL9Mop9AUU, 'r') as f:
    metadata = json.load(f)

# Create DataFrames
df_articles = pd.DataFrame(articles)
df_meta = pd.DataFrame(metadata)

# Ensure article_id is string for reliable merging
df_articles['article_id'] = df_articles['article_id'].astype(str)
df_meta['article_id'] = df_meta['article_id'].astype(str)

# Merge metadata with article content
df = pd.merge(df_meta, df_articles[['article_id', 'title', 'description']], on='article_id', how='inner')

# Filter for year 2015
df_2015 = df[df['publication_date'].str.startswith('2015')].copy()

# Keyword-based classifier
sports_kw = ['match','goal','goals','scored','score','season','team','player','league','tournament','championship','cup','olympic','won','defeat','defeated','coach','innings','penalty','race','final']
business_kw = ['stock','stocks','market','markets','share','shares','ipo','profit','profits','earnings','company','companies','firm','investment','investor','bank','banks','dollar','economy','trade deficit','oil prices','oil','crude','merger','acquisition','debt','revenue','billion','million']
science_kw = ['scientist','research','study','nasa','space','technology','technolog','computer','software','scientific','experiment','researchers','spacecraft','satellite','lab','physics','chemistry','biology','robot','ai','artificial intelligence']
world_kw = ['president','government','election','minister','military','army','attack','attacks','killed','kidnap','rebels','border','diplomat','peace','protests','protest','refugee','sanctions','court','police','terror','terrorist','bomb','conflict','crisis','summit','foreign','immigration','visa']

import re

def count_keywords(text, keywords):
    if not isinstance(text, str):
        return 0
    t = text.lower()
    cnt = 0
    for kw in keywords:
        if ' ' in kw:
            cnt += t.count(kw)
        else:
            cnt += len(re.findall(r"\b" + re.escape(kw) + r"\b", t))
    return cnt

def classify_row(row):
    text = (str(row.get('title','')) + ' ' + str(row.get('description',''))).lower()
    s = count_keywords(text, sports_kw)
    b = count_keywords(text, business_kw)
    sc = count_keywords(text, science_kw)
    w = count_keywords(text, world_kw)
    counts = {'Sports': s, 'Business': b, 'Science/Technology': sc, 'World': w}
    if max(counts.values()) == 0:
        return 'World'
    max_count = max(counts.values())
    candidates = [k for k,v in counts.items() if v == max_count]
    if 'World' in candidates:
        return 'World'
    priority = ['Sports','Business','Science/Technology','World']
    for p in priority:
        if p in candidates:
            return p
    return 'World'

# Apply classifier
if not df_2015.empty:
    df_2015['category'] = df_2015.apply(classify_row, axis=1)
else:
    df_2015['category'] = pd.Series([], dtype=str)

# Count World articles by region
world_df = df_2015[df_2015['category'] == 'World']
counts_series = world_df.groupby('region').size()
counts = {k: int(v) for k,v in counts_series.to_dict().items()}

if counts:
    max_count = max(counts.values())
    top_regions = [r for r,c in counts.items() if c == max_count]
else:
    max_count = 0
    top_regions = []

result = {
    'top_regions': [{'region': r, 'count': counts[r]} for r in top_regions],
    'all_counts': counts,
    'total_world_articles_2015': int(sum(counts.values()))
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_gMXk1haVK74LEry5MP21tLTh': 'file_storage/call_gMXk1haVK74LEry5MP21tLTh.json', 'var_call_DYFiHVDQnHR5pGXL9Mop9AUU': 'file_storage/call_DYFiHVDQnHR5pGXL9Mop9AUU.json'}

exec(code, env_args)
