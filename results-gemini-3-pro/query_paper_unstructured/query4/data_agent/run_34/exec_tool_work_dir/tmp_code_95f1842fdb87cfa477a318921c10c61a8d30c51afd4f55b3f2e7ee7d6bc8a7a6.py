code = """import json
import pandas as pd

with open(locals()['var_function-call-799378154932565658'], 'r') as f:
    papers = json.load(f)

debug_info = {}
debug_info["total_papers"] = len(papers)

# Check for 'physical activity'
pa_papers = [p for p in papers if 'physical activity' in p['text'].lower()]
debug_info["pa_papers_count"] = len(pa_papers)

# Check for '2016' in header
y2016_papers = [p for p in papers if '2016' in p['text'][:1000]]
debug_info["y2016_papers_count"] = len(y2016_papers)

# Overlap
overlap = [p for p in papers if 'physical activity' in p['text'].lower() and '2016' in p['text'][:1000]]
debug_info["overlap_count"] = len(overlap)

# Sample headers
debug_info["sample_headers"] = [p['text'][:300] for p in papers[:3]]

# Sample titles
debug_info["paper_titles"] = [p['filename'].replace('.txt', '') for p in papers[:5]]

with open(locals()['var_function-call-799378154932566157'], 'r') as f:
    citations = json.load(f)
df_citations = pd.DataFrame(citations)
debug_info["citation_titles"] = df_citations['title'].unique()[:5].tolist()

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-18105369077024110272': 'file_storage/function-call-18105369077024110272.json', 'var_function-call-18105369077024110379': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}], 'var_function-call-799378154932565658': 'file_storage/function-call-799378154932565658.json', 'var_function-call-799378154932566157': 'file_storage/function-call-799378154932566157.json', 'var_function-call-16897121803853272035': []}

exec(code, env_args)
