code = """import json
import pandas as pd

with open(locals()['var_function-call-799378154932565658'], 'r') as f:
    papers = json.load(f)

print("Total papers:", len(papers))

# Check for 'physical activity'
pa_papers = [p for p in papers if 'physical activity' in p['text'].lower()]
print("Papers with 'physical activity':", len(pa_papers))

# Check for '2016' in header
y2016_papers = [p for p in papers if '2016' in p['text'][:1000]]
print("Papers with '2016' in header:", len(y2016_papers))

# Print first 500 chars of a few papers to inspect headers
for p in papers[:3]:
    print("--- HEADER ---")
    print(p['text'][:300])
    
# Check a specific paper if known or just list some titles
titles = [p['filename'].replace('.txt', '') for p in papers[:5]]
print("Sample titles from papers:", titles)

with open(locals()['var_function-call-799378154932566157'], 'r') as f:
    citations = json.load(f)
df_citations = pd.DataFrame(citations)
print("Sample titles from citations:", df_citations['title'].unique()[:5])
print("__RESULT__:")
print("done")"""

env_args = {'var_function-call-18105369077024110272': 'file_storage/function-call-18105369077024110272.json', 'var_function-call-18105369077024110379': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}], 'var_function-call-799378154932565658': 'file_storage/function-call-799378154932565658.json', 'var_function-call-799378154932566157': 'file_storage/function-call-799378154932566157.json', 'var_function-call-16897121803853272035': []}

exec(code, env_args)
