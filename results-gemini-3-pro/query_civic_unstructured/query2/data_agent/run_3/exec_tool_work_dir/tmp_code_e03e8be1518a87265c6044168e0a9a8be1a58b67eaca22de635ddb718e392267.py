code = """import json
import re

with open(locals()['var_function-call-16179877025922844511'], 'r') as f:
    civic_docs = json.load(f)

# Just searching for "Park" in text is too broad, so use the project names logic again to isolate chunks.
with open(locals()['var_function-call-13030964589425590204'], 'r') as f:
    funding_data = json.load(f)
funding_map = {item['Project_Name']: int(item['Amount']) for item in funding_data}
project_names = list(funding_map.keys())
project_names.sort(key=len, reverse=True)

debug_info = []

for doc in civic_docs:
    text = doc['text']
    occurrences = []
    for name in project_names:
        escaped_name = re.escape(name)
        for m in re.finditer(escaped_name, text, re.IGNORECASE):
            occurrences.append((m.start(), name))
    occurrences.sort(key=lambda x: x[0])
    
    clean_occurrences = []
    if occurrences:
        curr_start, curr_name = occurrences[0]
        curr_end = curr_start + len(curr_name)
        clean_occurrences.append((curr_start, curr_name))
        for i in range(1, len(occurrences)):
            start, name = occurrences[i]
            end = start + len(name)
            if start >= curr_end:
                clean_occurrences.append((start, name))
                curr_start, curr_name = start, name
                curr_end = end

    for i in range(len(clean_occurrences)):
        start_idx, name = clean_occurrences[i]
        end_idx = clean_occurrences[i+1][0] if i < len(clean_occurrences) - 1 else len(text)
        chunk = text[start_idx:end_idx]
        
        if "park" in name.lower():
            # Check for completion info
            lines = chunk.splitlines()
            for line in lines:
                l = line.lower()
                if "complete" in l or "status" in l:
                    debug_info.append(f"Project: {name}, Doc: {doc['filename']}, Line: {line.strip()}")

print("__RESULT__:")
print(json.dumps(debug_info[:20])) # Print first 20 lines to avoid huge output"""

env_args = {'var_function-call-13030964589425589265': 'file_storage/function-call-13030964589425589265.json', 'var_function-call-13030964589425590204': 'file_storage/function-call-13030964589425590204.json', 'var_function-call-16179877025922844511': 'file_storage/function-call-16179877025922844511.json', 'var_function-call-15826040215521897163': {'total': 118000, 'projects': [{'name': 'Bluffs Park Shade Structure', 'amount': 21000}, {'name': 'Permanent Skate Park', 'amount': 97000}]}, 'var_function-call-7715372612916809138': ['Doc: malibucity_agenda__01262022-1835.txt, Line: draft plans are expected to be completed in early 2022. The Planning', 'Doc: malibucity_agenda__01262022-1835.txt, Line: draft plans are expected to be completed in early 2022. The Planning', 'Doc: malibucity_agenda__03232022-1869.txt, Line: draft plans are expected to be completed in early 2022. The Planning', 'Doc: malibucity_agenda__03232022-1869.txt, Line: draft plans are expected to be completed in early 2022. The Planning'], 'var_function-call-14360294538855612841': {'total': 21000, 'projects': [{'name': 'Bluffs Park Shade Structure', 'amount': 21000}]}}

exec(code, env_args)
