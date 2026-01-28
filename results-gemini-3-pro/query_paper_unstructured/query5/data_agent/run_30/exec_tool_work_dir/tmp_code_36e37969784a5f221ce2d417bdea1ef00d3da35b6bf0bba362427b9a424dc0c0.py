code = """import json
import re

with open(locals()['var_function-call-7711183651007727056'], 'r') as f:
    citations_data = json.load(f)

with open(locals()['var_function-call-4121090962908109712'], 'r') as f:
    paper_docs_data = json.load(f)

print("Total citation records:", len(citations_data))
print("Total paper docs:", len(paper_docs_data))

paper_map = {d['filename'].replace('.txt', ''): d['text'] for d in paper_docs_data if 'filename' in d}

matches = 0
chi_matches = 0
non_chi_headers = []

for record in citations_data:
    title = record['title']
    if title in paper_map:
        matches += 1
        text = paper_map[title]
        # Check CHI
        is_chi = False
        if re.search(r'\bCHI\b', text[:2000]):
            is_chi = True
        
        if is_chi:
            chi_matches += 1
        else:
            if len(non_chi_headers) < 3:
                # Capture first 200 chars to see what venue looks like
                non_chi_headers.append(text[:200].replace('\n', ' '))

print("Matches:", matches)
print("CHI Matches:", chi_matches)
print("Sample Non-CHI Headers:", non_chi_headers)

print("__RESULT__:")
print(json.dumps("debug"))"""

env_args = {'var_function-call-7711183651007727056': 'file_storage/function-call-7711183651007727056.json', 'var_function-call-4121090962908109712': 'file_storage/function-call-4121090962908109712.json', 'var_function-call-5326245820750148638': 16}

exec(code, env_args)
