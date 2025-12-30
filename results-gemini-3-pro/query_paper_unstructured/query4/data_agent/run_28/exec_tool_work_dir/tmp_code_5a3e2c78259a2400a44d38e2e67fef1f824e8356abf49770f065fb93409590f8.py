code = """import json
import pandas as pd

# Load citations
with open(locals()['var_function-call-14596373756638571722'], 'r') as f:
    citations_data = json.load(f)

df_citations = pd.DataFrame(citations_data)
df_citations['citation_count'] = df_citations['citation_count'].astype(int)
citation_totals = df_citations.groupby('title')['citation_count'].sum().to_dict()

# Load paper docs
with open(locals()['var_function-call-12508593236145811836'], 'r') as f:
    paper_docs = json.load(f)

results = []
debug_info = {}
debug_info["total_docs"] = len(paper_docs)
debug_info["pa_docs"] = 0
debug_info["y2016_docs"] = 0

for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']
    
    # Check domain
    if 'physical activity' in text.lower():
        debug_info["pa_docs"] += 1
        # Check year
        header = text[:1000]
        if '2016' in header:
            debug_info["y2016_docs"] += 1
            # Get total citations
            total_citations = citation_totals.get(title, 0)
            
            results.append({
                "title": title,
                "total_citation_count": total_citations
            })

results.sort(key=lambda x: x['title'])

final_output = {
    "results": results,
    "debug_info": debug_info
}

print("__RESULT__:")
print(json.dumps(final_output))"""

env_args = {'var_function-call-5420876219690003843': 'file_storage/function-call-5420876219690003843.json', 'var_function-call-14495357574425764744': 'file_storage/function-call-14495357574425764744.json', 'var_function-call-7398565704940874410': 'file_storage/function-call-7398565704940874410.json', 'var_function-call-14596373756638571722': 'file_storage/function-call-14596373756638571722.json', 'var_function-call-10948899133377792843': [], 'var_function-call-10604739559875805637': {'total_docs': 5, 'total_citations': 1405, 'pa_count': 4, 'y2016_count': 0, 'match_count': 0, 'sample_title': 'A Lived Informatics Model of Personal Informatics', 'sample_in_citations': True, 'matching_samples': []}, 'var_function-call-12508593236145811836': 'file_storage/function-call-12508593236145811836.json'}

exec(code, env_args)
