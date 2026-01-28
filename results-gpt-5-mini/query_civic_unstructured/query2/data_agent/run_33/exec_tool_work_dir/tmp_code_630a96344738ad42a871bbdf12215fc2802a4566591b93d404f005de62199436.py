code = """import json
import pandas as pd

# Load funding data
with open(var_call_B3cOZcIzwasXby51pMoWCzCG, 'r') as f:
    funding_records = json.load(f)
funding_df = pd.DataFrame(funding_records)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'], errors='coerce').fillna(0).astype(int)

# Also consider 'Malibu Bluffs Park' and other park-related names that might match funding table
possible_park_names = [
    'Bluffs Park Shade Structure',
    'Bluffs Park Workout Station',
    'Malibu Bluffs Park Roof Replacement Project',
    'Malibu Bluffs Park South Walkway',
    'Malibu Bluffs Park South Walkway Repairs',
    'Legacy Park Benches and Arbors Renovation',
    'Legacy Park Paver Repair Project',
    'Malibu Park Drainage Improvements',
    'Malibu Park Resurfacing Project',
    'Malibu Park Storm Drain Repairs',
    'Trancas Canyon Park Upper and Lower Slopes Repair',
    'Trancas Canyon Park Playground'
]

# Filter funding table for these names
matched = funding_df[funding_df['Project_Name'].isin(possible_park_names)]

# Sum amounts for those whose projects were completed in 2022 per civic docs we parsed earlier
# From earlier parse, completed-in-2022 park projects found: Bluffs Park Shade Structure

matched_records = matched.to_dict(orient='records')

result = {
    'considered_park_names': possible_park_names,
    'matched_records': matched_records,
    'sum_amount_matched': int(matched['Amount'].sum())
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_B3cOZcIzwasXby51pMoWCzCG': 'file_storage/call_B3cOZcIzwasXby51pMoWCzCG.json', 'var_call_Wx9sBVIXluqh7TjyDQANyuuO': ['civic_docs'], 'var_call_s5Sf1sLBWUAmmTXBqNBgDVPn': 'file_storage/call_s5Sf1sLBWUAmmTXBqNBgDVPn.json', 'var_call_mtn0Z1erNp1W1K6yjYr03ZNN': {'park_projects_completed_2022': ['Bluffs Park Shade Structure'], 'matched_funding_records': [{'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': 21000}], 'total_funding': 21000}}

exec(code, env_args)
