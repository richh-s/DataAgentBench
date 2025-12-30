code = """import json, pandas as pd

# Load full results from files
with open(var_call_ky4WVAMq2caVeneOqvrmqxl8, 'r') as f:
    papers = json.load(f)
with open(var_call_ZhpFLateFx2wNg25bLaUHPwR, 'r') as f:
    citations = json.load(f)

# Extract titles from filenames (remove .txt)
for p in papers:
    fn = p.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    p['title'] = title

# Filter papers whose text/domain suggests 'food' domain.
# We only know 'food' via substring matching in text; use case-insensitive contains.
food_papers = []
for p in papers:
    text = p.get('text','').lower()
    if ' food ' in text or 'food tracking' in text or 'food journal' in text or 'diet' in text or 'calorie' in text:
        food_papers.append(p)

food_titles = set(p['title'] for p in food_papers)

# Sum citation counts for those titles
cit_df = pd.DataFrame(citations)
# Ensure numeric citation_count
cit_df['citation_count'] = pd.to_numeric(cit_df['citation_count'], errors='coerce').fillna(0).astype(int)

food_cit_df = cit_df[cit_df['title'].isin(food_titles)]

total_citations = int(food_cit_df['citation_count'].sum())

result = json.dumps({"total_citations_food_domain": total_citations})

print("__RESULT__:")
print(result)"""

env_args = {'var_call_ky4WVAMq2caVeneOqvrmqxl8': 'file_storage/call_ky4WVAMq2caVeneOqvrmqxl8.json', 'var_call_ZhpFLateFx2wNg25bLaUHPwR': 'file_storage/call_ZhpFLateFx2wNg25bLaUHPwR.json'}

exec(code, env_args)
