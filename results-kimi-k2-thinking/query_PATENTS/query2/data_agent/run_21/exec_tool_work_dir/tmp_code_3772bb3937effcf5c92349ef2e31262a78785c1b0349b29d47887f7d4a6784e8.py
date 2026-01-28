code = """import json
import pandas as pd
import re

# Load the data from the previous query
data_file = var_functions.query_db:0
with open(data_file, 'r') as f:
    all_patents = json.load(f)

print(f"Total patents in raw data: {len(all_patents)}")

# Let's look at the actual structure and patterns
print("\nFirst few entries:")
for i, patent in enumerate(all_patents[:5]):
    print(f"\n{i+1}. Patents_info: {patent['Patents_info']}")
    print(f"   Grant_date: {patent['grant_date']}")

# Identify German patents more accurately
print("\n" + "="*50)
print("Identifying German patents...")

# Create a systematic filter for German patents
german_patents = []
month_map = {
    'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
    'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
}

for patent in all_patents:
    patents_info = patent['Patents_info']
    grant_date = patent['grant_date']
    
    # Check for German country codes (from DE, DE patent, Germany, etc.)
    is_german = False
    german_markers = ['from DE', 'DE patent', 'Germany', 'DE-']
    
    for marker in german_markers:
        if marker in patents_info:
            is_german = True
            break
    
    # For patents without explicit markers, check if it has DE- prefix
    if not is_german and 'DE-' in patents_info:
        is_german = True
    
    # Check if grant_date is in second half of 2019 (July-Dec 2019)
    in_second_half_2019 = False
    if '2019' in grant_date:
        # Extract month
        for month_abbr, month_num in month_map.items():
            if month_abbr in grant_date:
                if month_num >= 7:  # July onwards
                    in_second_half_2019 = True
                break
    
    if is_german and in_second_half_2019:
        german_patents.append(patent)

print(f"Found {len(german_patents)} German patents granted in second half of 2019")

# Show a sample
print("\nSample German patents:")
for i, patent in enumerate(german_patents[:5]):
    print(f"{i+1}. {patent['Patents_info']}")
    print(f"   Grant: {patent['grant_date']}")
    print()"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
