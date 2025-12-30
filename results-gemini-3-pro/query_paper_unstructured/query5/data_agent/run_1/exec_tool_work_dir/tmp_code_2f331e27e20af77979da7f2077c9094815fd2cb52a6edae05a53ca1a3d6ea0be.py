code = """import json
import re

# Load citations
with open(locals()['var_function-call-12437250052302532993'], 'r') as f:
    citations_data = json.load(f)

# Filter citations for 2020
citations_2020 = {}
for item in citations_data:
    if int(item['citation_count']) > 0: 
        citations_2020[item['title']] = int(item['citation_count'])

print(f"Total papers with citations in 2020: {len(citations_2020)}")

# Load paper docs
with open(locals()['var_function-call-17247428670658995703'], 'r') as f:
    paper_docs = json.load(f)

print(f"Total paper docs: {len(paper_docs)}")

matched_papers = []
total_citations = 0

for doc in paper_docs:
    filename = doc['filename']
    title = filename.rsplit('.', 1)[0]
    text = doc['text']
    
    if title in citations_2020:
        header = text[:2000]
        is_chi = False
        if "Human Factors in Computing Systems" in header:
            is_chi = True
        elif re.search(r"CHI\s*[']?\d{2,4}", header): 
            is_chi = True
        elif re.search(r"\bCHI\b", text[:500]):
            is_chi = True
            
        if is_chi:
            count = citations_2020[title]
            total_citations += count
            matched_papers.append((title, count))

print(f"Matched {len(matched_papers)} CHI papers.")
print(f"Sample matched: {matched_papers[:5]}")
print(f"Total citations: {total_citations}")

print("__RESULT__:")
print(json.dumps(total_citations))"""

env_args = {'var_function-call-12437250052302532993': 'file_storage/function-call-12437250052302532993.json', 'var_function-call-17247428670658995703': 'file_storage/function-call-17247428670658995703.json', 'var_function-call-767057999987748063': 16}

exec(code, env_args)
