code = """import re, json, pandas as pd

civic_path = var_call_lrkzei5JaTgrIzj1A9nPU2g1
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

texts = [d['text'] for d in civic_docs]

projects = []
for text in texts:
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if re.search(r"(Begin Construction|Start|Project Start|Construction Start)[:\s]+(Spring\s*2022|2022[- ]Spring|March 2022|April 2022|May 2022)", line, re.IGNORECASE):
            pname = None
            for j in range(i-1, max(-1, i-6), -1):
                pline = lines[j].strip()
                if not pline:
                    continue
                if ("Updates" in pline) or ("Project Schedule" in pline) or ("Estimated Schedule" in pline) or ("Project Description" in pline):
                    continue
                pname = pline
                break
            if pname:
                projects.append({"Project_Name": pname})

uniq_projects = sorted({p['Project_Name'] for p in projects})

funding = pd.DataFrame(var_call_llOxhaF5U6vLFkaqbaQphmk5)
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
