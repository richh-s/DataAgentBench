code = """import json
import re

with open(locals()['var_function-call-17703270697767214172'], 'r') as f:
    civic_docs = json.load(f)

mentions = []
date_patterns = [r"Spring[\s,-]*2022", r"March[\s,-]*2022", r"April[\s,-]*2022", r"May[\s,-]*2022"]

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.splitlines()
    for i in range(len(lines) - 1):
        line = lines[i].strip()
        next_line = lines[i+1].strip()
        if ("Updates:" in next_line or "Project Description:" in next_line) and line:
            project_name = line
            block_content = ""
            for j in range(i+1, min(len(lines), i+100)):
                if j < len(lines)-1:
                    nxt = lines[j+1]
                    if ("Updates:" in nxt or "Project Description:" in nxt) and lines[j].strip():
                        break
                block_content += lines[j] + " "
            
            for dp in date_patterns:
                if re.search(dp, block_content, re.IGNORECASE):
                    mentions.append((project_name, block_content[:200])) # Capture snippet
                    break

print("__RESULT__:")
print(json.dumps(mentions))"""

env_args = {'var_function-call-6629743294879476725': ['civic_docs'], 'var_function-call-6629743294879475928': ['Funding'], 'var_function-call-6790771977792377935': 'file_storage/function-call-6790771977792377935.json', 'var_function-call-6790771977792376994': 'file_storage/function-call-6790771977792376994.json', 'var_function-call-17703270697767214172': 'file_storage/function-call-17703270697767214172.json', 'var_function-call-8676561060322907480': {'found_projects': ['Marie Canyon Green Streets', 'Birdview Avenue Improvements (CalOES Project)'], 'matched_projects': ['Birdview Avenue Improvements (CalOES Project)', 'Marie Canyon Green Streets'], 'matched_count': 2, 'total_funding': 135000}, 'var_function-call-1965114893715931460': {'found_projects': ['Marie Canyon Green Streets', 'Birdview Avenue Improvements (CalOES Project)'], 'matched_projects': ['Birdview Avenue Improvements (CalOES Project)', 'Marie Canyon Green Streets'], 'matched_count': 2, 'total_funding': 135000}}

exec(code, env_args)
