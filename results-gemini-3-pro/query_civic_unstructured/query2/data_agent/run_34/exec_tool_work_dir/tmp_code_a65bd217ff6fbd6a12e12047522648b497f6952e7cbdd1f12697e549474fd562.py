code = """import json
import re

path_civic = locals()["var_function-call-15046969363982349672"]
with open(path_civic, "r") as f:
    civic_docs = json.load(f)

path_funding = locals()["var_function-call-6734558309770551932"]
with open(path_funding, "r") as f:
    funding_data = json.load(f)

projects = []

for doc in civic_docs:
    text = doc["text"]
    lines = text.split("\n")
    idx = 0
    n_lines = len(lines)
    
    while idx < n_lines:
        line = lines[idx].strip()
        
        is_title = False
        if len(line) > 3 and not line.startswith("(cid:") and not line.startswith("Page") and "Capital Improvement" not in line and "Agenda Item" not in line and "Subject:" not in line:
            for k in range(1, 10):
                if idx + k < n_lines:
                    nl = lines[idx+k].strip()
                    if nl.startswith("(cid:190)"):
                        is_title = True
                        break
        
        if is_title:
            p_name = line
            p_text_list = []
            current_idx = idx + 1
            
            while current_idx < n_lines:
                c_line = lines[current_idx].strip()
                
                is_next_title = False
                if len(c_line) > 3 and not c_line.startswith("(cid:") and not c_line.startswith("Page") and "Capital Improvement" not in c_line and "Agenda Item" not in c_line:
                    for m in range(1, 10):
                        if current_idx + m < n_lines:
                            nnl = lines[current_idx+m].strip()
                            if nnl.startswith("(cid:190)"):
                                is_next_title = True
                                break
                
                if is_next_title:
                    break
                
                p_text_list.append(c_line)
                current_idx += 1
            
            p_text = " ".join(p_text_list)
            projects.append({"name": p_name, "text": p_text})
            idx = current_idx
        else:
            idx += 1

matched_names = []
for p in projects:
    name = p["name"]
    text = p["text"].lower()
    name_lower = name.lower()
    
    if "park" in name_lower or "playground" in name_lower or "park" in text or "playground" in text:
        if "completed" in text and "2022" in text:
            if re.search(r"completed.{0,50}2022", text) or re.search(r"completion.{0,50}2022", text):
                matched_names.append(name)

total_funding = 0
funding_map = {item["Project_Name"]: int(item["Amount"]) for item in funding_data}

matched_clean = []
for m in matched_names:
    m_clean = m.strip()
    if m_clean in funding_map:
        total_funding += funding_map[m_clean]
        matched_clean.append(m_clean)

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "projects": matched_clean}))"""

env_args = {'var_function-call-6734558309770552995': 'file_storage/function-call-6734558309770552995.json', 'var_function-call-6734558309770551932': 'file_storage/function-call-6734558309770551932.json', 'var_function-call-15046969363982349672': 'file_storage/function-call-15046969363982349672.json', 'var_function-call-11152109866840209153': {'count': 5}}

exec(code, env_args)
