code = """import json
import re

# Load the full results from the query
result_file = var_functions.query_db:2
with open(result_file, 'r') as f:
    patents_raw = json.load(f)

print(f"Total records loaded: {len(patents_raw)}")

# Filter for German patents in second half of 2019
de_patents = []
for patent in patents_raw:
    # Check if it's a German patent
    if 'DE-' in patent['Patents_info']:
        # Parse grant date
        grant_date = patent['grant_date']
        
        # Extract month and year from grant date
        # Handle various formats like "14th Mar 2019", "on October 31st, 2019", "8th Jan 2019"
        year_match = re.search(r'2019', grant_date)
        if year_match:
            # Look for month names
            month_match = re.search(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)', grant_date, re.IGNORECASE)
            if month_match:
                month_name = month_match.group(1).lower()
                month_map = {
                    'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
                    'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
                }
                month_num = month_map.get(month_name, 0)
                
                # Second half of 2019: July (7) to December (12)
                if 7 <= month_num <= 12:
                    de_patents.append(patent)

print(f"German patents in second half of 2019: {len(de_patents)}")
print("__RESULT__:")
print(json.dumps(de_patents[:5]))  # Return first 5 as preview"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
