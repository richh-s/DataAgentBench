code = """import json
import pandas as pd
import re
from datetime import datetime

# Load the data from the previous query
result_file = var_functions.query_db:11
with open(result_file, 'r') as f:
    patents_data = json.load(f)

# Filter for Germany patents granted in 2019 second half
de_patents_2019 = []

# Parse grant dates to check if they're in second half of 2019
months_2nd_half = ['July', 'August', 'September', 'October', 'November', 'December']

for patent in patents_data:
    grant_date = patent.get('grant_date', '')
    patents_info = patent.get('Patents_info', '')
    
    # Check if it's a Germany patent
    if 'DE-' in patents_info:
        # Check if grant_date indicates 2019 second half
        if ('2019' in grant_date and 
            any(month in grant_date for month in months_2nd_half)):
            
            # Extract CPC codes
            cpc_data = patent.get('cpc', '[]')
            if isinstance(cpc_data, str):
                try:
                    cpc_codes = json.loads(cpc_data)
                except:
                    cpc_codes = []
            else:
                cpc_codes = cpc_data
                
            de_patents_2019.append({
                'patent_info': patents_info,
                'grant_date': grant_date,
                'cpc_codes': cpc_codes,
                'title_localized': patent.get('title_localized', '')
            })

print(f"Found {len(de_patents_2019)} Germany patents granted in 2nd half of 2019")

# Show first few entries for verification
print("\nFirst few entries:")
for i, p in enumerate(de_patents_2019[:3]):
    print(f"\n{i+1}. {p['patent_info']}")
    print(f"   Grant: {p['grant_date']}")
    print(f"   CPC codes: {[c.get('code', '') for c in p['cpc_codes'][:3]]}")

# Save the filtered data
with open('de_patents_2019.json', 'w') as f:
    json.dump(de_patents_2019, f)

print('__RESULT__:')
print('{"status": "success", "count": ' + str(len(de_patents_2019)) + '}')"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'Patents_info': 'Patent application (number DE-10317286-A) from DE, belonging to NICOLAY VERWALTUNGS GMBH, with publication no. DE-10317286-B3.', 'grant_date': 'dated 7th October 2004'}, {'Patents_info': 'MIELE & CIE holds the DE patent filing (app. number DE-102005018015-A), with publication number DE-102005018015-B3.', 'grant_date': '2006 on Apr 27th'}, {'Patents_info': 'UHLMANN PAC SYSTEME GMBH & CO holds the DE patent filing (app. number DE-102006022262-A), with publication number DE-102006022262-B3.', 'grant_date': 'Nov 29th, 2007'}, {'Patents_info': 'The DE patent filing (application no. DE-102007030491-A) is belonging to HEINRICH GEORG GMBH MASCHINENF and has pub. number DE-102007030491-B3.', 'grant_date': '2009, January 29th'}, {'Patents_info': 'In DE, the patent filing (application no. DE-102009032362-A) is owned by MARTOR KG and has pub. number DE-102009032362-B3.', 'grant_date': '17th Jun 2010'}, {'Patents_info': 'Patent application (no. DE-102015114819-A) from DE, held by ROCKWELL COLLINS DEUTSCHLAND GMBH, with pub. number DE-102015114819-B3.', 'grant_date': 'on December 22nd, 2016'}, {'Patents_info': 'MITUTOYO CORP holds the DE patent filing (app. number DE-10037981-A), with pub. number DE-10037981-B4.', 'grant_date': '19th of October, 2017'}, {'Patents_info': 'The DE patent application (no. DE-10052167-A) is held by YAMATO SEWING MACHINE MFG and has pub. number DE-10052167-B4.', 'grant_date': '23rd Jun 2005'}, {'Patents_info': 'Application (no. DE-10127786-A) from DE, belonging to KRAHFORST JUERGEN, with pub. number DE-10127786-B4.', 'grant_date': 'November 10th, 2005'}, {'Patents_info': 'In DE, the patent application (no. DE-10130631-A) is owned by SCHNEIDER SIEGHARD and has publication number DE-10130631-B4.', 'grant_date': '28th of October, 2010'}], 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
