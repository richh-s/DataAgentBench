code = """import json, pandas as pd

# Load metadata
path_meta = var_call_2SgDFGDzvWj7uRRvu1QNAqMP
with open(path_meta, 'r') as f:
    meta = json.load(f)

# Load articles
path_articles = var_call_kBjNOB4KFj7DUV7Hp76EPSY0
with open(path_articles, 'r') as f:
    arts = json.load(f)

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# Ensure correct dtypes
t = pd.to_numeric(arts_df['article_id'])
arts_df['article_id'] = t
meta_df['article_id'] = pd.to_numeric(meta_df['article_id'])

# Filter to 2015
meta_df['year'] = pd.to_datetime(meta_df['publication_date']).dt.year
meta_2015 = meta_df[meta_df['year'] == 2015]

# Simple heuristic classifier for categories
world_keywords = ['iraq','war','election','president','prime minister','government','policy','UN','UN ','NATO','EU','parliament','terror','attack','bomb','Middle East','Palestinian','Israel','conflict','peace talks','nuclear','diplomat','embassy','crisis','sanction','refugee']

# Lowercase text
arts_df['text'] = (arts_df['title'].fillna('') + ' ' + arts_df['description'].fillna('')).str.lower()

# Mark as world if any world keyword appears
pattern = '|'.join([k.lower().replace(' ', '\\s+') for k in world_keywords])
arts_df['is_world'] = arts_df['text'].str.contains(pattern, regex=True, na=False)

# Join
merged = meta_2015.merge(arts_df[['article_id','is_world']], on='article_id', how='left')
world_2015 = merged[merged['is_world']]

counts = world_2015.groupby('region').size().sort_values(ascending=False)

result = {
    'counts_by_region': counts.to_dict(),
    'top_region': counts.index[0] if len(counts) > 0 else None
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_2SgDFGDzvWj7uRRvu1QNAqMP': 'file_storage/call_2SgDFGDzvWj7uRRvu1QNAqMP.json', 'var_call_kBjNOB4KFj7DUV7Hp76EPSY0': 'file_storage/call_kBjNOB4KFj7DUV7Hp76EPSY0.json'}

exec(code, env_args)
