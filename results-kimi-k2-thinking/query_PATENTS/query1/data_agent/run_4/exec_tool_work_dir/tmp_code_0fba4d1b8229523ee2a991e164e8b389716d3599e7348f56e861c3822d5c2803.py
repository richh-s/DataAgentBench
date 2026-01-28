code = """import json
import re
from datetime import datetime

# Load data from the variable
publications = var_functions.query_db_6

print(f"Total publications loaded: {len(publications)}")

# Extract CPC codes and years
patent_counts = {}

for pub in publications:
    # Parse publication date
    pub_date_str = pub['publication_date']
    if pub_date_str:
        # Extract year using regex
        year_match = re.search(r'\d{4}', pub_date_str)
        if year_match:
            year = int(year_match.group())
            
            # Parse CPC codes (JSON string)
            cpc_str = pub['cpc']
            if cpc_str:
                try:
                    # Clean up the string - it might be a Python representation
                    cpc_list = json.loads(cpc_str)
                    for cpc_item in cpc_list:
                        code = cpc_item.get('code')
                        if code:
                            # Extract main group (first part before / or space)
                            main_code = code.split('/')[0].split()[0]
                            
                            # Initialize if needed
                            if main_code not in patent_counts:
                                patent_counts[main_code] = {}
                            
                            # Count patents per year
                            if year not in patent_counts[main_code]:
                                patent_counts[main_code][year] = 0
                            patent_counts[main_code][year] += 1
                            
                except (json.JSONDecodeError, TypeError):
                    # Skip malformed entries
                    continue

# Show sample of the data
sample_cpc = list(patent_counts.keys())[:5]
print(f"Sample CPC codes: {sample_cpc}")
for cpc in sample_cpc:
    print(f"  {cpc}: {dict(list(patent_counts[cpc].items())[:3])}")

# Save intermediate result
result = {
    'patent_counts': patent_counts,
    'total_cpc_codes': len(patent_counts)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
