code = """import json
import re

# Load the large results from storage file paths
with open(var_call_Qb7M0iG2c2t74ZvhjQoKvofN, 'r') as f:
    citations = json.load(f)
with open(var_call_7X5uYqE7cc2hZSfEZ5XdD8Wu, 'r') as f:
    papers = json.load(f)

# Build mapping from filename without .txt to text
file_text_map = {}
for doc in papers:
    filename = doc.get('filename', '')
    key = filename[:-4] if filename.lower().endswith('.txt') else filename
    file_text_map[key] = doc.get('text', '')

matched = []
total = 0
for rec in citations:
    title = rec.get('title')
    if title is None:
        continue
    # match title to filename key
    if title in file_text_map:
        text = file_text_map[title]
        # detect CHI venue mentions in text (case-insensitive)
        if re.search(r'\bCHI\b', text, flags=re.IGNORECASE) or re.search(r'proceedings of the (?:sigchi|chi)', text, flags=re.IGNORECASE) or re.search(r'SIGCHI', text, flags=re.IGNORECASE):
            # get citation count as int
            try:
                c = int(rec.get('citation_count', 0))
            except:
                try:
                    c = int(float(rec.get('citation_count', 0)))
                except:
                    c = 0
            total += c
            matched.append({'title': title, 'citation_count': c})

# Prepare result JSON-serializable string
result_obj = {'total_citations_2020_for_CHI_papers': total, 'matched_papers_count': len(matched), 'matched_papers': matched}
result_str = json.dumps(result_obj)
print("__RESULT__:")
print(result_str)"""

env_args = {'var_call_Qb7M0iG2c2t74ZvhjQoKvofN': 'file_storage/call_Qb7M0iG2c2t74ZvhjQoKvofN.json', 'var_call_7X5uYqE7cc2hZSfEZ5XdD8Wu': 'file_storage/call_7X5uYqE7cc2hZSfEZ5XdD8Wu.json'}

exec(code, env_args)
