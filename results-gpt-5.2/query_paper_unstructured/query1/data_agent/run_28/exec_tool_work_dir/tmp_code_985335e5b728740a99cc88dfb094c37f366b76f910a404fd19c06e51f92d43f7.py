code = """import json, re
import pandas as pd

# load mongo filenames
mongo_src = var_call_otfhnFXiC6a1DRIOBtUa6jKR
if isinstance(mongo_src, str):
    with open(mongo_src, 'r', encoding='utf-8') as f:
        mongo_recs = json.load(f)
else:
    mongo_recs = mongo_src

# load citations
cit_src = var_call_O2mU87nmqmLDFrJs2kMrnLLO
if isinstance(cit_src, str):
    with open(cit_src, 'r', encoding='utf-8') as f:
        cit_recs = json.load(f)
else:
    cit_recs = cit_src

# infer food domain from title/filename containing 'food'
food_titles = set()
for r in mongo_recs:
    fn = r.get('filename','') or ''
    title = re.sub(r'\.txt$', '', fn)
    if 'food' in title.lower():
        food_titles.add(title)

# sum citations for those titles
cits_df = pd.DataFrame(cit_recs)
if not cits_df.empty:
    cits_df['citation_count'] = pd.to_numeric(cits_df['citation_count'], errors='coerce').fillna(0).astype(int)

    total = int(cits_df[cits_df['title'].isin(food_titles)]['citation_count'].sum())
else:
    total = 0

out = {"total_citation_count_food_domain": total, "num_food_papers_matched": len(food_titles)}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_otfhnFXiC6a1DRIOBtUa6jKR': 'file_storage/call_otfhnFXiC6a1DRIOBtUa6jKR.json', 'var_call_O2mU87nmqmLDFrJs2kMrnLLO': 'file_storage/call_O2mU87nmqmLDFrJs2kMrnLLO.json'}

exec(code, env_args)
