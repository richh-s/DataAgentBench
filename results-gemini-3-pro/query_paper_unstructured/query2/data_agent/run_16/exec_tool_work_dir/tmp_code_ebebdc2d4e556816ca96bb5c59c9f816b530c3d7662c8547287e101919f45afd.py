code = """import json
import pandas as pd

# Load citations
# variable name for citations result
citations_path = locals()['var_function-call-15068442808757462000']
with open(citations_path, 'r') as f:
    citations_data = json.load(f)

df_citations = pd.DataFrame(citations_data)

# Load papers
# variable name for papers result
papers_path = locals()['var_function-call-15068442808757464883']
with open(papers_path, 'r') as f:
    papers_data = json.load(f)

# Process papers to a dictionary: title -> text
# filename "Title.txt" -> title "Title"
paper_texts = {}
for p in papers_data:
    if 'filename' in p and 'text' in p:
        title = p['filename'].replace('.txt', '')
        paper_texts[title] = p['text']

# Filter citations for 2018 (should be all, but good to be sure if I query changed)
# The SQL query was "WHERE citation_year = 2018", so df_citations only has 2018 data.

acm_citations = []

for index, row in df_citations.iterrows():
    title = row['title']
    count = row['citation_count']
    
    if title in paper_texts:
        text = paper_texts[title]
        # Heuristic for ACM publication:
        # Check first 5000 chars for "ACM"
        # This avoids finding "ACM" in references at the end
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
