code = """import json
import re

civic_docs_path = locals()['var_function-call-9021704853761821384']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

extracted_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        
        # Look ahead for marker
        is_project = False
        j = i + 1
        while j < len(lines):
            peek = lines[j].strip()
            if peek:
                if "(cid:190)" in peek or peek.startswith("Updates:") or peek.startswith("Project Description:"):
                    is_project = True
                break
            j += 1
        
        if is_project:
            p_name = line
            block_lines = []
            k = i + 1
            while k < len(lines):
                nav_line = lines[k].strip()
                if "Capital Improvement Projects" in nav_line and ("(Design)" in nav_line or "(Construction)" in nav_line):
                    break
                
                # Check for next project
                m = k + 1
                is_next = False
                while m < len(lines):
                    peek_next = lines[m].strip()
                    if peek_next:
                        if "(cid:190)" in peek_next and not "(cid:190)" in nav_line:
                            is_next = True
                        break
                    m += 1
                
                if is_next:
                    break
                
                block_lines.append(lines[k])
                k += 1
            
            block_text = "\n".join(block_lines)
            
            start_date = None
            date_match = re.search(r"Begin [Cc]onstruction[:\s]+(.*?)(?:\n|$)", block_text)
            if not date_match:
                 date_match = re.search(r"Start [Dd]ate[:\s]+(.*?)(?:\n|$)", block_text)
            
            if date_match:
                start_date = date_match.group(1).strip()
            
            is_disaster = False
            keywords = ["FEMA", "CalOES", "Woolsey", "Disaster", "Emergency"]
            if any(kw in block_text for kw in keywords) or any(kw in p_name for kw in keywords):
                is_disaster = True
                
            extracted_projects.append({
                "name": p_name,
                "start_date": start_date,
                "is_disaster": is_disaster,
                "text_snippet": block_text[:100]
            })
            
            i = k
        else:
            i += 1

print("__RESULT__:")
print(json.dumps(extracted_projects))"""

env_args = {'var_function-call-4835809069730370506': ['Funding'], 'var_function-call-4835809069730370969': ['civic_docs'], 'var_function-call-17294341897624108968': 'file_storage/function-call-17294341897624108968.json', 'var_function-call-17294341897624106339': 'file_storage/function-call-17294341897624106339.json', 'var_function-call-9021704853761821384': 'file_storage/function-call-9021704853761821384.json'}

exec(code, env_args)
