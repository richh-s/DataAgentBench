code = """import re, json, pandas as pd
path_docs = var_call_aXakWvKpPU3E8iFsR0AHMy6I
with open(path_docs, 'r') as f:
    civic_docs = json.load(f)
funding_records = var_call_ESdBbS9Ejz9h1lmdCEuwfFe8
funding_df = pd.DataFrame(funding_records)
funding_df['Amount'] = funding_df['Amount'].astype(int)
pattern = re.compile(r"\b(Begin Construction|Start of Construction|Project Start)\s*[:-]?\s*Spring\s*2022", re.IGNORECASE)
projects_spring_2022 = set()
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    last_title = None
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if (not re.match(r"^[•*\-]", stripped)) and stripped == stripped.title() and len(stripped.split()) <= 12:
            last_title = stripped
        if pattern.search(stripped):
            if last_title:
                projects_spring_2022.add(last_title)
funding_spring = funding_df[funding_df['Project_Name'].isin(projects_spring_2022)]
result = {
    'projects_started_spring_2022_count': int(funding_spring['Project_Name'].nunique()),
    'total_funding_spring_2022': int(funding_spring['Amount'].sum()),
    'matched_project_names': sorted(funding_spring['Project_Name'].unique().tolist()),
}
out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_aXakWvKpPU3E8iFsR0AHMy6I': 'file_storage/call_aXakWvKpPU3E8iFsR0AHMy6I.json', 'var_call_ESdBbS9Ejz9h1lmdCEuwfFe8': 'file_storage/call_ESdBbS9Ejz9h1lmdCEuwfFe8.json'}

exec(code, env_args)
