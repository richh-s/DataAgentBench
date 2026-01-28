code = """import json
import pandas as pd
# Load the large query_db result from file path stored in var_call_izL5DNG1nbq2O4DXYfZm51xD
with open(var_call_izL5DNG1nbq2O4DXYfZm51xD, 'r') as f:
    citations = json.load(f)
# citations is a list of dicts with keys 'title' and 'citation_count'
df = pd.DataFrame(citations)
# Ensure citation_count is integer
if not df.empty:
    df['citation_count'] = df['citation_count'].astype(int)
# Extract filenames from paper_docs query result var_call_K9UAnGyZQOwYIxsLv33vbQPz
filenames = [d.get('filename') for d in var_call_K9UAnGyZQOwYIxsLv33vbQPz]
# Convert filenames to titles by stripping .txt
titles = set()
for fn in filenames:
    if fn and fn.lower().endswith('.txt'):
        titles.add(fn[:-4])
    else:
        titles.add(fn)
# Filter citations for these titles
df_acm = df[df['title'].isin(titles)]
# Compute average citation count
if len(df_acm) > 0:
    avg = float(df_acm['citation_count'].mean())
    avg_rounded = round(avg, 2)
else:
    avg_rounded = None
# Prepare result
result = {
    'average_citation_count': avg_rounded,
    'num_matched_papers': int(len(df_acm)),
    'matched_titles': sorted(list(titles))
}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_YUcGNl960GufrxTl2QJDanJa': ['paper_docs'], 'var_call_y23YPplNaZEoXV1zKzG2XtGI': ['Citations', 'sqlite_sequence'], 'var_call_izL5DNG1nbq2O4DXYfZm51xD': 'file_storage/call_izL5DNG1nbq2O4DXYfZm51xD.json', 'var_call_K9UAnGyZQOwYIxsLv33vbQPz': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}]}

exec(code, env_args)
