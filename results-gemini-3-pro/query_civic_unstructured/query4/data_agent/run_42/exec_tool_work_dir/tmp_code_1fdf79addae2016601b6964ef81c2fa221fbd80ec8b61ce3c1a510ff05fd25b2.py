code = """import json
import pandas as pd
import re

with open(locals()['var_function-call-6790771977792377935'], 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)

with open(locals()['var_function-call-17703270697767214172'], 'r') as f:
    civic_docs = json.load(f)

found_projects = set()
start_terms = ["Begin Construction", "Start Construction", "Construction Start", "Project Start", "Construction to begin", "Scheduled to begin"]
# Using regex patterns for dates now to be more flexible
date_patterns = [
    r"Spring[\s,-]*2022",
    r"March[\s,-]*2022",
    r"April[\s,-]*2022",
    r"May[\s,-]*2022",
    r"2022[\s,-]*Spring",
    r"2022[\s,-]*March",
    r"2022[\s,-]*03",
    r"2022[\s,-]*04",
    r"2022[\s,-]*05"
]

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
            
            # Check for start date
            found = False
            for term in start_terms:
                # Find term
                # We want to find matches of term followed by date
                # Regex: term.{0,100}date
                for d_pat in date_patterns:
                    full_pattern = re.escape(term) + r".{0,100}" + d_pat
                    # Note: re.escape escapes everything, so date_patterns regex logic might be lost if I escape it.
                    # date_patterns contains regex chars like \s, so don't escape d_pat.
                    
                    # We need to construct pattern carefully.
                    # Term is literal (except maybe spaces).
                    term_pat = re.escape(term)
                    
                    # Combine
                    pat = f"{term_pat}.{{0,100}}{d_pat}"
                    
                    if re.search(pat, block_content, re.IGNORECASE):
                        found_projects.add(project_name)
                        found = True
                        break
                if found: break

clean_found = {p.strip() for p in found_projects}
matched = funding_df[funding_df['Project_Name'].isin(clean_found)]

print("__RESULT__:")
print(json.dumps({
    "found_projects": list(clean_found),
    "matched_projects": matched['Project_Name'].tolist(),
    "matched_count": len(matched),
    "total_funding": int(matched['Amount'].astype(int).sum())
}))"""

env_args = {'var_function-call-6629743294879476725': ['civic_docs'], 'var_function-call-6629743294879475928': ['Funding'], 'var_function-call-6790771977792377935': 'file_storage/function-call-6790771977792377935.json', 'var_function-call-6790771977792376994': 'file_storage/function-call-6790771977792376994.json', 'var_function-call-17703270697767214172': 'file_storage/function-call-17703270697767214172.json', 'var_function-call-8676561060322907480': {'found_projects': ['Marie Canyon Green Streets', 'Birdview Avenue Improvements (CalOES Project)'], 'matched_projects': ['Birdview Avenue Improvements (CalOES Project)', 'Marie Canyon Green Streets'], 'matched_count': 2, 'total_funding': 135000}}

exec(code, env_args)
