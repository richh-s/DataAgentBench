code = """import json
import re

# Load the query results from storage file paths
funding_path = var_call_VzgihgZ7OwHfelcmF5z1sI2X
docs_path = var_call_zyKqzSQAopIHC3ukf8gNzESM

with open(funding_path, 'r', encoding='utf-8') as f:
    funding = json.load(f)

with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Build combined design sections from all documents
design_sections = []
header_pattern = re.compile(r'Capital Improvement Projects\s*\(([^)]*)\)', re.IGNORECASE)
for doc in docs:
    text = doc.get('text', '')
    matches = list(header_pattern.finditer(text))
    if not matches:
        continue
    for i, m in enumerate(matches):
        section_type = m.group(1).strip().lower()
        start = m.end()
        end = len(text)
        if i + 1 < len(matches):
            end = matches[i+1].start()
        if 'design' in section_type:
            design_sections.append(text[start:end])

combined_design_text = "\n".join(design_sections).lower()

# Prepare funding project names (already filtered to Amount > 50000 by earlier query)
proj_names = [r.get('Project_Name', '') for r in funding]

matched = set()
for name in proj_names:
    name_low = name.lower()
    # variant: remove trailing parenthesis content
    name_strip = re.sub(r"\s*\(.*\)\s*$", "", name_low).strip()
    variants = [name_low, name_strip]
    found = False
    for v in variants:
        if v and v in combined_design_text:
            matched.add(name)
            found = True
            break
    # also try more flexible: check if most words (>=3) of the name appear in order
    if not found:
        words = re.findall(r"[a-z0-9]+", name_strip)
        if len(words) >= 3:
            # create a simple in-order fuzzy check
            idx = 0
            pos = 0
            for w in words:
                pos = combined_design_text.find(w, pos)
                if pos == -1:
                    idx = -1
                    break
                pos += len(w)
                idx += 1
            if idx == len(words):
                matched.add(name)

matched_list = sorted(list(matched))
result = {"count": len(matched_list), "projects": matched_list}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_w6mzZJWh1Qf1WequniXaReqc': ['civic_docs'], 'var_call_8FNlL82nAuBCB7zgbjsxnppT': ['Funding'], 'var_call_VzgihgZ7OwHfelcmF5z1sI2X': 'file_storage/call_VzgihgZ7OwHfelcmF5z1sI2X.json', 'var_call_zyKqzSQAopIHC3ukf8gNzESM': 'file_storage/call_zyKqzSQAopIHC3ukf8gNzESM.json'}

exec(code, env_args)
