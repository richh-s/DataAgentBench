code = """import re, json, pandas as pd, os, textwrap

# Load full civic docs
with open(var_call_m2LLoEH16g84QXjTOGBj4QDc, 'r') as f:
    civic_docs = json.load(f)

# Heuristic extraction: assume lines with 'Disaster Recovery Projects' section then list projects, but for year filter we just look for '2022' in implied start dates.
# For this synthetic dataset, disaster projects are typically those whose names include '(FEMA', '(CalOES', '(CalJPIA', or 'Disaster'.

# Build a set of disaster project names that have st including 2022. We approximate by searching for project names found in funding table that are disaster-typed, and then looking for '2022' near their first mention in text.

with open(var_call_npnDnK093QGTuFX57b7O0woa, 'r') as f:
    funding = json.load(f)

fund_df = pd.DataFrame(funding)

# Identify potential disaster project names from funding table
pattern = re.compile(r'\((FEMA|CalOES|CalJPIA)[^)]*\)', re.IGNORECASE)
fund_df['is_disaster_name'] = fund_df['Project_Name'].str.contains(pattern)

# Collect candidate names
disaster_names = set(fund_df[fund_df['is_disaster_name']]['Project_Name'].unique())

# For each candidate name, search in civic text for a nearby year mention. If '2022' appears within 200 characters after first occurrence, mark st_year=2022.
name_started_2022 = set()
full_text = '\n'.join(doc['text'] for doc in civic_docs)

for name in disaster_names:
    # escape for regex
    esc = re.escape(name)
    m = re.search(esc, full_text)
    if not m:
        continue
    window = full_text[m.end():m.end()+300]
    if '2022' in window:
        name_started_2022.add(name)

# Filter funding for those disaster projects started in 2022
mask = fund_df['Project_Name'].isin(name_started_2022)
sel = fund_df[mask].copy()

# Amount is string; convert to int
sel['Amount'] = sel['Amount'].astype(int)

total = int(sel['Amount'].sum())

result = {"total_disaster_funding_started_2022": total, "projects": sel[['Project_Name','Amount']].to_dict(orient='records')}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_m2LLoEH16g84QXjTOGBj4QDc': 'file_storage/call_m2LLoEH16g84QXjTOGBj4QDc.json', 'var_call_npnDnK093QGTuFX57b7O0woa': 'file_storage/call_npnDnK093QGTuFX57b7O0woa.json'}

exec(code, env_args)
