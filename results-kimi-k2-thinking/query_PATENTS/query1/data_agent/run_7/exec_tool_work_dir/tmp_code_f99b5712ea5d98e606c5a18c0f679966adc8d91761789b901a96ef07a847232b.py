code = """import json
import ast
from datetime import datetime

# Read the full result file
file_path = var_functions.query_db:10
with open(file_path, 'r') as f:
    records = json.load(f)

print(f'Loaded {len(records)} patent records')
print(f'First record date: {records[0].get("publication_date")}')
print(f'First record CPC (first 100 chars): {str(records[0].get("cpc"))[:100]}')

# Let's parse CPC codes and extract years
patent_data = []
for record in records:
    pub_date = record.get('publication_date', '')
    cpc_data = record.get('cpc', '[]')
    
    # Parse publication year
    year = None
    if pub_date:
        try:
            # Handle format like "Aug 3rd, 2021" or "Oct 6th, 2020"
            parts = pub_date.split(', ')
            if len(parts) >= 2:
                year_str = parts[1]
                year = int(year_str)
        except:
            pass
    
    # Parse CPC codes
    try:
        # Try json.loads first
        cpc_list = json.loads(cpc_data)
    except:
        try:
            # Fallback to ast.literal_eval
            cpc_list = ast.literal_eval(cpc_data)
        except:
            cpc_list = []
    
    # Extract CPC codes at level 5 (format like X00X00/00)
    for cpc_entry in cpc_list:
        code = cpc_entry.get('code', '')
        if code and year:
            # Count dots in symbol to determine level
            # CPC format: C01B33/00 - this is level 5 (group)
            # Level 5 has the pattern: Section (1) + Class (2) + Subclass (1) + Group (2-3+ digits) + / + Subgroup
            # For level 5, we want the group level (before the /)
            if '/' in code:
                main_group = code.split('/')[0]
                # Count total characters to validate it's a group (not main group)
                if len(main_group) >= 4:  # e.g., C01B33
                    # This appears to be at group level
                    patent_data.append({
                        'cpc_code': code,
                        'year': year
                    })

print(f'\nExtracted {len(patent_data)} CPC-year entries')
if patent_data:
    print(f'Sample entries: {patent_data[:3]}')
    print(f'Years range: {min([p["year"] for p in patent_data])} to {max([p["year"] for p in patent_data])}')

# Save processed data
with open('/tmp/patent_cpc_data.json', 'w') as f:
    json.dump(patent_data, f)

print("Saved processed data to /tmp/patent_cpc_data.json")"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
