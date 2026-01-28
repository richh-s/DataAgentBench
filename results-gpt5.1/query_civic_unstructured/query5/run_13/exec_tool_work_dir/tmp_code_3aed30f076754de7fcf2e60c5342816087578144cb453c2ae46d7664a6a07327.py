code = """import re, json
from pathlib import Path

# Load full civic docs
path_civic = Path(var_call_yNtVSmduS3ElgyoR68hOJd3Y)
with open(path_civic, 'r') as f:
    civic_docs = json.load(f)

texts = [d['text'] for d in civic_docs]

# Heuristic: disaster projects have FEMA/CalOES/CalJPIA or 'Disaster Recovery Projects' context
project_names = set()
for text in texts:
    for line in text.split('\n'):
        if any(tag in line for tag in ['(FEMA', '(CalOES', '(CalJPIA', 'Disaster Recovery']):
            m = re.search(r'([A-Z0-9].+?)\s*(\(|$)', line.strip())
            if m:
                name = m.group(1).strip()
                if len(name.split())>1:
                    project_names.add(name)

# Also use hint that disaster projects often have suffixes like (FEMA Project) etc.,
# So we can treat any funding record with those suffixes as disaster-type.

# Load funding table
path_funding = Path(var_call_RmmqeZSUIviHqbSnwcZ6H1mz)
with open(path_funding, 'r') as f:
    funding = json.load(f)

# Identify disaster-related projects in funding: names containing FEMA, CalOES, CalJPIA, or 'Disaster'
disaster_funding = []
for row in funding:
    name = row['Project_Name']
    if any(tag in name for tag in ['FEMA', 'CalOES', 'CalJPIA', 'Disaster']):
        disaster_funding.append(row)

# For start year 2022: need projects that started in 2022 per civic docs.
# Very rough heuristic: look in texts for lines containing project name and a 2022 date-like string.

def started_in_2022(name, texts):
    pattern = re.escape(name[:40])  # partial to allow small mismatches
    for text in texts:
        if name.split()[0] not in text:
            continue
        if '2022' in text:
            # assume if project appears in a doc discussing FY 2022-2023 or has 2022 in schedule it started then
            return True
    return False

eligible_ids = []
for row in disaster_funding:
    name = row['Project_Name']
    if started_in_2022(name, texts):
        eligible_ids.append(row['Funding_ID'])

# Sum funding amounts for eligible records
total = 0
for row in disaster_funding:
    if row['Funding_ID'] in eligible_ids:
        try:
            total += int(row['Amount'])
        except:
            pass

result = total

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_yNtVSmduS3ElgyoR68hOJd3Y': 'file_storage/call_yNtVSmduS3ElgyoR68hOJd3Y.json', 'var_call_RmmqeZSUIviHqbSnwcZ6H1mz': 'file_storage/call_RmmqeZSUIviHqbSnwcZ6H1mz.json'}

exec(code, env_args)
