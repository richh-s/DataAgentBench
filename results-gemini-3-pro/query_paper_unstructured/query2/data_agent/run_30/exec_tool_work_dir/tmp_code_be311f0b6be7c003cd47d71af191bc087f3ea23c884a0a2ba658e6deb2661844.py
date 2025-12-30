code = """import json
import re

file_path_citations = locals()['var_function-call-3647625760159840601']
with open(file_path_citations, 'r') as f:
    citations_data = json.load(f)

file_path_papers = locals()['var_function-call-7977022267260973965']
with open(file_path_papers, 'r') as f:
    paper_docs = json.load(f)

paper_map = {doc['filename']: doc['text'] for doc in paper_docs}

count_simple = 0
count_strict = 0

for item in citations_data:
    filename = item['title'] + ".txt"
    if filename in paper_map:
        text = paper_map[filename]
        if "ACM" in text:
            count_simple += 1
        
        # Strict check: Look for ACM in the first 1000 chars or lines containing "Copyright"
        head = text[:3000]
        if "ACM" in head:
            # Check if it's likely the publisher
            # e.g. "Copyright * ACM"
            if "copyright" in head.lower() and "acm" in head.lower():
                count_strict += 1
            elif "© ACM" in head or "© 20" in head and "ACM" in head: # Rough check
                count_strict += 1
            elif "Association for Computing Machinery" in head:
                count_strict += 1
            else:
                 # If "ACM" is just in the text (like "ACM Classification"), it's likely an ACM paper
                 # because usually only ACM papers have ACM Classification keywords in the header.
                 if "ACM Classification Keywords" in head:
                     count_strict += 1

print(f"Simple count: {count_simple}")
print(f"Strict count: {count_strict}")
print("__RESULT__:")
print(json.dumps("Done"))"""

env_args = {'var_function-call-5264272901715907644': ['Citations', 'sqlite_sequence'], 'var_function-call-5264272901715907989': ['paper_docs'], 'var_function-call-3647625760159840601': 'file_storage/function-call-3647625760159840601.json', 'var_function-call-16517880119813488158': 158, 'var_function-call-6596666326870079897': 'file_storage/function-call-6596666326870079897.json', 'var_function-call-7977022267260973965': 'file_storage/function-call-7977022267260973965.json', 'var_function-call-4446662547743021233': 68.5}

exec(code, env_args)
