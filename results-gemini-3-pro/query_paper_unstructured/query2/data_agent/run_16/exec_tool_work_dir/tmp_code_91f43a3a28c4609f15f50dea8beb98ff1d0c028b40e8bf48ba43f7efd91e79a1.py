code = """import json
import pandas as pd

citations_path = locals()['var_function-call-15068442808757462000']
with open(citations_path, 'r') as f:
    citations_data = json.load(f)

df_citations = pd.DataFrame(citations_data)

papers_path = locals()['var_function-call-15068442808757464883']
with open(papers_path, 'r') as f:
    papers_data = json.load(f)

paper_texts = {}
for p in papers_data:
    if 'filename' in p and 'text' in p:
        title = p['filename'].replace('.txt', '')
        paper_texts[title] = p['text']

acm_citations = []

for index, row in df_citations.iterrows():
    title = row['title']
    try:
        count = int(row['citation_count'])
    except:
        continue
    
    if title in paper_texts:
        text = paper_texts[title]
        # Check first 5000 chars for "ACM"
        if "ACM" in text[:5000]: 
            acm_citations.append(count)

if len(acm_citations) > 0:
    avg_citations = sum(acm_citations) / len(acm_citations)
    result = {"average_citation_count": avg_citations, "num_papers": len(acm_citations)}
else:
    result = {"average_citation_count": 0, "num_papers": 0}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-15068442808757462000': 'file_storage/function-call-15068442808757462000.json', 'var_function-call-15068442808757464883': 'file_storage/function-call-15068442808757464883.json'}

exec(code, env_args)
