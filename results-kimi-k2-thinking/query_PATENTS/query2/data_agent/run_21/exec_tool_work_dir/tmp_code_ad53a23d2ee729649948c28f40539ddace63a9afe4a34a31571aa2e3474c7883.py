code = """import json
import pandas as pd
import re

# Load the data from the previous query
data_file = var_functions.query_db:0
with open(data_file, 'r') as f:
    all_patents = json.load(f)

print(f"Total patents in raw data: {len(all_patents)}")

# Create a systematic filter for German patents and second half 2019
print("\nAnalyzing German patents granted in second half 2019...")

german_patents = []
for patent in all_patents:
    patents_info = patent['Patents_info']
    grant_date = patent['grant_date']
    
    # Check for German country markers
    is_german = False
    german_markers = ['from DE', 'DE-', 'Germany', 'German', 'Deutsch']
    
    for marker in german_markers:
        if marker in patents_info or marker in patents_info.upper():
            is_german = True
            break
    
    # Check if grant_date is in second half of 2019 (July-Dec 2019)
    in_second_half_2019 = False
    if '2019' in grant_date:
        # Simple check for second half
        second_half_markers = ['July', 'August', 'September', 'October', 'November', 'December', 
                              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        for marker in second_half_markers:
            if marker in grant_date:
                in_second_half_2019 = True
                break
    
    if is_german and in_second_half_2019:
        german_patents.append(patent)

print(f"Found {len(german_patents)} German patents granted in second half of 2019")

if german_patents:
    print("\nSample German patents:")
    for i, patent in enumerate(german_patents[:3]):
        print(f"\n{i+1}. {patent['Patents_info']}")
        print(f"   Grant: {patent['grant_date']}")
        print(f"   CPC: {patent['cpc'][:100]}...")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
