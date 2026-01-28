code = """import json
import pandas as pd
import re

# Load the data from the previous query
data_file = var_functions.query_db:8
with open(data_file, 'r') as f:
    all_patents = json.load(f)

print(f"Total patents in raw data: {len(all_patents)}")

# Check data structure
print("\nFirst 3 entries:")
for i, patent in enumerate(all_patents[:3]):
    print(f"\n{i+1}. Patents_info: {patent['Patents_info']}")
    print(f"   Grant_date: {patent['grant_date']}")
    print(f"   CPC codes: {patent['cpc'][:200]}...")

# Now filter for German patents granted in second half 2019 (July-Dec 2019)
print("\n" + "="*60)
print("Filtering for German patents granted in second half 2019...")

# Function to extract month from grant_date
def get_grant_month(grant_date):
    month_patterns = {
        'January': 1, 'Jan': 1,'February': 2, 'Feb': 2,'March': 3, 'Mar': 3,
        'April': 4, 'Apr': 4,'May': 5,'June': 6, 'Jun': 6,
        'July': 7, 'Jul': 7,'August': 8, 'Aug': 8,
        'September': 9, 'Sep': 9,
        'October': 10, 'Oct': 10,'November': 11, 'Nov': 11,'December': 12, 'Dec': 12
    }
    
    for month_name, month_num in month_patterns.items():
        if month_name in grant_date:
            return month_num
    return None

# Filter for German patents granted in second half of 2019
german_patents_2019 = []

german_markers = ['from DE', 'DE patent', 'Germany', 'German', 'Deutsch', 'DE-']

for patent in all_patents:
    patents_info = patent['Patents_info']
    grant_date = patent['grant_date']
    
    # Check if it's a German patent
    is_german = any(marker in patents_info for marker in german_markers)
    if not is_german and 'DE-' in patents_info:
        is_german = True
    
    # Check if grant date is in 2019 and second half
    if '2019' in grant_date:
        month = get_grant_month(grant_date)
        if month is not None and month >= 7:  # July onwards
            if is_german:
                german_patents_2019.append(patent)

print(f"Found {len(german_patents_2019)} German patents granted in second half 2019")

# Show sample of filtered patents
if german_patents_2019:
    print("\nSample filtered patents:")
    for i, patent in enumerate(german_patents_2019[:5]):
        print(f"\n{i+1}. {patent['Patents_info']}")
        print(f"   Grant: {patent['grant_date']}")
        print(f"   CPC: {patent['cpc'][:150]}...")
else:
    print("No German patents found in second half 2019, checking what's available...")
    # Check all 2019 german patents
    for patent in all_patents:
        patents_info = patent['Patents_info']
        grant_date = patent['grant_date']
        
        is_german = any(marker in patents_info for marker in german_markers)
        if not is_german and 'DE-' in patents_info:
            is_german = True
        
        if '2019' in grant_date and is_german:
            print(f"Found: {patent['Patents_info'][:100]} - {grant_date}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
