code = """import re, json, pandas as pd

# Load full funding table
with open(var_call_yyKlExYan4LHoMPoAMYdUI4b, 'r') as f:
    funding = pd.DataFrame(json.load(f))

# Disaster-related projects: names containing FEMA, CalOES, CalJPIA, or explicitly 'Disaster'
pattern = re.compile(r'(FEMA|CalOES|CalJPIA|Disaster)', re.IGNORECASE)
disaster_mask = funding['Project_Name'].str.contains(pattern)

# For this question we also need projects that STARTED in 2022, but start year info is only in civic docs.
# Heuristic: many 2022-start projects have '2022' in their project names (e.g., '2022 Morning View ...').
start2022_mask = funding['Project_Name'].str.contains('2022')

# Disaster-related AND 2022-start (by name heuristic)
mask = disaster_mask & start2022_mask

selected = funding[mask]

# Sum Amount as int
selected['Amount'] = selected['Amount'].astype(int)

result_val = int(selected['Amount'].sum())

print('__RESULT__:')
print(json.dumps(result_val))"""

env_args = {'var_call_9BaVIvzP2mcuUnZpXEKXbdan': 'file_storage/call_9BaVIvzP2mcuUnZpXEKXbdan.json', 'var_call_yyKlExYan4LHoMPoAMYdUI4b': 'file_storage/call_yyKlExYan4LHoMPoAMYdUI4b.json'}

exec(code, env_args)
