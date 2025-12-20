code = """import json, pandas as pd
from datetime import datetime

# Load full metadata
with open(var_call_UjgvUvyZmAXMdLwXNw1aqLnF, 'r') as f:
    metadata = json.load(f)

# Load full articles
with open(var_call_E0jAyyT7zRzbevnRPcF6FEeC, 'r') as f:
    articles = json.load(f)

md = pd.DataFrame(metadata)
arts = pd.DataFrame(articles)

# Ensure types
md['article_id'] = md['article_id'].astype(int)
arts['article_id'] = arts['article_id'].astype(int)

# Filter metadata for 2015
md['year'] = md['publication_date'].str.slice(0,4).astype(int)
md2015 = md[md['year'] == 2015]

# Merge with articles
df = md2015.merge(arts, on='article_id', how='inner')

# Simple keyword-based classifier for categories
def classify(row):
    text = (str(row.get('title','')) + ' ' + str(row.get('description',''))).lower()
    sports_kw = ['sport','football','soccer','nba','nfl','mlb','olympic','tennis','cricket','golf','hockey','athletic']
    business_kw = ['stock','stocks','market','business','economy','economic','company','shares','bank','trade','trading','oil','ipo','fund','profit','losses','earnings']
    sci_kw = ['science','scientist','research','study','studies','technology','tech ','space','nasa','launch','experiment','physics','biology','chemistry','internet','software']
    # Heuristic ordering: sports, sci/tech, business, else world
    if any(k in text for k in sports_kw):
        return 'Sports'
    if any(k in text for k in sci_kw):
        return 'Science/Technology'
    if any(k in text for k in business_kw):
        return 'Business'
    return 'World'

df['category'] = df.apply(classify, axis=1)
world = df[df['category'] == 'World']

counts = world.groupby('region').size().sort_values(ascending=False)

result = {
    'region_with_most_world_articles_2015': counts.index[0] if len(counts)>0 else None,
    'counts_by_region': counts.to_dict()
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_UjgvUvyZmAXMdLwXNw1aqLnF': 'file_storage/call_UjgvUvyZmAXMdLwXNw1aqLnF.json', 'var_call_E0jAyyT7zRzbevnRPcF6FEeC': 'file_storage/call_E0jAyyT7zRzbevnRPcF6FEeC.json'}

exec(code, env_args)
