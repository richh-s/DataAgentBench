code = """import re, json, pandas as pd
from datetime import datetime

# Load civic docs full result
import pathlib, os, textwrap
civic_path = var_call_lrkzei5JaTgrIzj1A9nPU2g1
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

texts = [d['text'] for d in civic_docs]

projects = []
for text in texts:
    # crude heuristic: project names are lines that look like title case and followed by 'Project' or similar, but we mostly need dates
    # We'll search for patterns like 'Begin Construction: Spring 2022' or 'Start: 2022-Spring'
    # Capture project name by looking at up to 3 preceding non-empty lines.
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if re.search(r"(Begin Construction|Start|Project Start|Construction Start)[:\s]+(Spring\s*2022|2022[- ]Spring|March 2022|April 2022|May 2022)", line, re.IGNORECASE):
            # backtrack to find project name: previous non-empty line that is not a bullet
            pname = None
            for j in range(i-1, max(-1, i-6), -1):
                pline = lines[j].strip()
                if not pline:
                    continue
                # skip lines that look like headings
                if any(x in pline for x in ["Updates", "Project Schedule", "Estimated Schedule", "Project Description"]):
                    continue
                pname = pline
                break
            if pname:
                projects.append({"Project_Name": pname})

# deduplicate
uniq_projects = sorted({p['Project_Name'] for p in projects})

# Load funding table
funding = pd.DataFrame(var_call_llOxhaF5U6vLFkaqbaQphmk5)

# Match by exact name
matched = funding[funding['Project_Name'].isin(uniq_projects)].copy()
matched['Amount'] = matched['Amount'].astype(int)

result = {
    'spring_2022_project_count': int(matched.shape[0]),
    'spring_2022_total_funding': int(matched['Amount'].sum())
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_lrkzei5JaTgrIzj1A9nPU2g1': 'file_storage/call_lrkzei5JaTgrIzj1A9nPU2g1.json', 'var_call_llOxhaF5U6vLFkaqbaQphmk5': 'file_storage/call_llOxhaF5U6vLFkaqbaQphmk5.json', 'var_call_XkxICJZ2A5vVEUAMdPoHRThh': ['civic_docs'], 'var_call_6Cg8HdNUXAbFawLhxvhON3bO': ['Funding']}

exec(code, env_args)
