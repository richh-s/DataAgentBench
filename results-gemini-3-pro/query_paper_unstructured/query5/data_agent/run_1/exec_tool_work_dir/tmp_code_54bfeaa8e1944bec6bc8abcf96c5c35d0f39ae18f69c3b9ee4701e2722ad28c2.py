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

# Load paper docs
with open(locals()['var_function-call-17247428670658995703'], 'r') as f:
    paper_docs = json.load(f)

total_citations = 0
chi_papers_count = 0
matched_papers = []

for doc in paper_docs:
    filename = doc['filename']
    title = filename.rsplit('.', 1)[0] # remove .txt
    text = doc['text']
    
    # Check if paper is in the 2020 citations list
    if title in citations_2020:
        header = text[:2000]
        
        is_chi = False
        # Check for full conference name
        if "Human Factors in Computing Systems" in header:
            is_chi = True
        # Check for CHI 'YY or CHI YYYY
        elif re.search(r'CHI\s*[\'\u2019]?\d{2,4}', header): 
            is_chi = True
        # Check for CHI appearing as a distinct word in the first 500 characters
        elif re.search(r'\bCHI\b', text[:500]):
            is_chi = True

        if is_chi:
            count = citations_2020[title]
            total_citations += count
            chi_papers_count += 1
            matched_papers.append(title)

print(f"Matched {chi_papers_count} CHI papers cited in 2020.")
print("__RESULT__:")
print(json.dumps(total_citations))"""

env_args = {'var_function-call-12437250052302532993': 'file_storage/function-call-12437250052302532993.json', 'var_function-call-17247428670658995703': 'file_storage/function-call-17247428670658995703.json'}

exec(code, env_args)
