code = """import re, json, pandas as pd

# Load full civic docs from file
with open(var_call_regjihqD0YcOz2LaOk1w5e8Z, 'r') as f:
    civic_docs = json.load(f)

texts = ' '.join(doc['text'] for doc in civic_docs)

# Heuristic: extract project lines under "Disaster Recovery Projects" or with FEMA/CalOES in name
projects = set()
for line in texts.split('\n'):
    line_stripped = line.strip()
    if not line_stripped:
        continue
    if 'FEMA' in line_stripped or 'CalOES' in line_stripped or 'CalJPIA' in line_stripped:
        projects.add(line_stripped)

# Normalize project names by stripping bullets and extra annotations
norm_projects = set()
for p in projects:
    # Remove leading bullets or characters
    p_clean = re.sub(r'^[-•\d\.\)\s]+', '', p)
    norm_projects.add(p_clean)

# Get funding table preview from storage variable
funding_records = var_call_sNebHVFA58PyIoie8pT1LswA

# If it's a filepath (string), load full; else it's already a list
if isinstance(funding_records, str):
    with open(funding_records, 'r') as f:
        funding_records = json.load(f)

fund_df = pd.DataFrame(funding_records)

# Ensure Amount is numeric
fund_df['Amount'] = pd.to_numeric(fund_df['Amount'])

# Disaster-type projects: those that have FEMA/CalOES/CalJPIA in the project name
disaster_mask = fund_df['Project_Name'].str.contains('FEMA|CalOES|CalJPIA', case=False, regex=True)

disaster_funding = fund_df[disaster_mask].copy()

# Now we need only those that started in 2022. We approximate start year 2022 by matching
# project names that appear near "2022" in civic texts.

projects_2022 = set()
for match in re.finditer(r'(2022[^\n]+)', texts):
    segment = match.group(1)
    # crudely extract capitalized project-like phrases around this
    # Here, just take the full line containing 2022
    line = segment
    # Also check previous 60 chars for project name
    start = max(0, match.start() - 60)
    end = min(len(texts), match.end() + 60)
    context = texts[start:end]
    # Collect capitalized phrases (words starting uppercase, >=2 words)
    words = context.split()
    # no robust NLP; skip

# Given lack of structured start dates, we'll answer based on funding names that clearly
# include "2022" and are disaster-related.

mask_2022_name = disaster_funding['Project_Name'].str.contains('2022', regex=False)

fund_2022_disaster = disaster_funding[mask_2022_name]

total_2022_disaster = float(fund_2022_disaster['Amount'].sum())

result = {
    'total_2022_disaster_funding': total_2022_disaster,
    'assumption': 'Only disaster projects (FEMA/CalOES/CalJPIA) whose names include 2022 were treated as starting in 2022 due to lack of explicit start dates.'
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_regjihqD0YcOz2LaOk1w5e8Z': 'file_storage/call_regjihqD0YcOz2LaOk1w5e8Z.json', 'var_call_sNebHVFA58PyIoie8pT1LswA': 'file_storage/call_sNebHVFA58PyIoie8pT1LswA.json'}

exec(code, env_args)
