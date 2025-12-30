code = """import json
import re

# Load filenames and citation counts
with open(locals()['var_function-call-13985119328028857859'], 'r') as f:
    data = json.load(f)
    title_citations = data['title_citations']
    # filenames are title + .txt. title_citations keys are titles.

# Load docs
with open(locals()['var_function-call-5489290469044726866'], 'r') as f:
    docs = json.load(f)

# Map filename -> text
docs_map = {d['filename']: d['text'] for d in docs}

missing_files = []
chi_citations = 0
chi_papers_count = 0

for title, citations in title_citations.items():
    filename = title + ".txt"
    if filename not in docs_map:
        missing_files.append(filename)
        continue
    
    text = docs_map[filename]
    # Check for CHI
    # Heuristics:
    # 1. "CHI 'YY" or "CHI 20YY"
    # 2. "Conference on Human Factors in Computing Systems"
    # 3. "CHI Conference"
    # Check first 1000 chars
    head = text[:1000]
    is_chi = False
    
    if re.search(r"\bCHI\s+'?\d{2,4}\b", head):
        is_chi = True
    elif "Conference on Human Factors in Computing Systems" in head:
        is_chi = True
    elif "CHI Conference" in head:
        is_chi = True
    
    # Also sometimes venue is just "CHI" in a header line
    # e.g. "CHI 2015, ..."
    
    if is_chi:
        chi_citations += int(citations)
        chi_papers_count += 1

print(f"Missing files: {len(missing_files)}")
print(f"CHI papers found: {chi_papers_count}")
print(f"Total citations: {chi_citations}")

print("__RESULT__:")
print(json.dumps({"total_citations": chi_citations, "missing_files": missing_files}))"""

env_args = {'var_function-call-2890407691846929350': ['Citations', 'sqlite_sequence'], 'var_function-call-2890407691846929759': 'file_storage/function-call-2890407691846929759.json', 'var_function-call-1018587870991830331': 'file_storage/function-call-1018587870991830331.json', 'var_function-call-13985119328028857859': 'file_storage/function-call-13985119328028857859.json', 'var_function-call-6633830581226945890': 'file_storage/function-call-6633830581226945890.json', 'var_function-call-5489290469044726866': 'file_storage/function-call-5489290469044726866.json', 'var_function-call-15377808340814584921': {'count_filenames': 188}}

exec(code, env_args)
