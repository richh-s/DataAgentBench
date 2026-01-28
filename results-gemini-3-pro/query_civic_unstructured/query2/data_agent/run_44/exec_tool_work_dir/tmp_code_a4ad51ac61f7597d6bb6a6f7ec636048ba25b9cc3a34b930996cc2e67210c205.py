code = """import json
import pandas as pd

with open(locals()['var_function-call-2604806260123295524'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-2604806260123292981'], 'r') as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Extract specific project texts
target_names = ["Point Dume Walkway Repairs", "Broad Beach Road Water Quality Repair", "Bluffs Park Shade Structure"]
texts = {}

NEWLINE = chr(10)

# Simplistic extraction again to find these names
# We know they exist as headers
for doc in civic_docs:
    lines = doc['text'].splitlines()
    for i, line in enumerate(lines):
        for name in target_names:
            if name in line:
                # Capture next 20 lines
                snippet = NEWLINE.join(lines[i:i+20])
                texts[name] = snippet

print('__RESULT__:')
print(json.dumps({
    "texts": texts,
    "funding": funding_df[funding_df['Project_Name'].isin(target_names)][['Project_Name', 'Amount']].to_dict(orient='records')
}))"""

env_args = {'var_function-call-2604806260123295524': 'file_storage/function-call-2604806260123295524.json', 'var_function-call-2604806260123292981': 'file_storage/function-call-2604806260123292981.json', 'var_function-call-11287208145778595060': {'total_funding': 21000, 'projects': ['Bluffs Park Shade Structure']}, 'var_function-call-595158838709480876': ['Bluffs Park Shade Structure', 'Broad Beach Road Water Quality Repair', 'Point Dume Walkway Repairs', 'amenities such as trash cans, benches, tables, and restrooms.', 'at 24712 Malibu Road has been eroded and caused damage to Malibu Road.', 'amenities such as trash cans, benches, tables, and restrooms.', 'facilities and roadway embankments that were damaged by the Woolsey Fire.']}

exec(code, env_args)
