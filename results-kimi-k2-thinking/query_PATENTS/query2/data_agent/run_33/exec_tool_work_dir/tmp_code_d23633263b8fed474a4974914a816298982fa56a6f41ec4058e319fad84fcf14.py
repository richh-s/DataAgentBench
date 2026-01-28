code = """import json
import re

# Load data from query result
result_file = var_functions.query_db:20
print('Loading data from:', result_file)

with open(result_file, 'r') as f:
    patents_data = json.load(f)

print('Total records:', len(patents_data))

# Filter for German patents granted in 2nd half of 2019
months_2nd_half = ['July', 'August', 'September', 'October', 'November', 'December']
de_patents_2019 = []

for patent in patents_data:
    patents_info = patent.get('Patents_info', '')
    grant_date = patent.get('grant_date', '')
    
    # Check if grant date contains second half months
    in_second_half = any(month in grant_date for month in months_2nd_half)
    
    if in_second_half:
        # Process CPC codes
        cpc_data = patent.get('cpc', '[]')
        try:
            if isinstance(cpc_data, str):
                cpc_codes = json.loads(cpc_data)
            else:
                cpc_codes = cpc_data
        except:
            cpc_codes = []
        
        # Process titles
        title_data = patent.get('title_localized', '[]')
        try:
            if isinstance(title_data, str):
                titles = json.loads(title_data)
            else:
                titles = title_data
            
            primary_title = ''
            if titles and isinstance(titles, list):
                for t in titles:
                    if isinstance(t, dict) and t.get('language') == 'de':
                        primary_title = t.get('text', '')
                        break
                if not primary_title and titles and isinstance(titles[0], dict):
                    primary_title = titles[0].get('text', '')
        except:
            primary_title = ''
        
        de_patents_2019.append({
            'patent_info': patents_info,
            'grant_date': grant_date,
            'cpc_codes': cpc_codes,
            'title': primary_title
        })

print('German patents in 2nd half 2019:', len(de_patents_2019))

# Show first few entries
for i in range(min(3, len(de_patents_2019))):
    p = de_patents_2019[i]
    print('Entry', i+1)
    print('Title:', p['title'][:60])
    print('Grant:', p['grant_date'])
    cpc_list = [c.get('code', '') for c in p['cpc_codes'][:2]] if p['cpc_codes'] else []
    print('CPC codes:', cpc_list)
    print()

# Save filtered data
with open('german_patents_2019.json', 'w') as f:
    json.dump(de_patents_2019, f)

result = {'status': 'success', 'count': len(de_patents_2019)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'Patents_info': 'Patent application (number DE-10317286-A) from DE, belonging to NICOLAY VERWALTUNGS GMBH, with publication no. DE-10317286-B3.', 'grant_date': 'dated 7th October 2004'}, {'Patents_info': 'MIELE & CIE holds the DE patent filing (app. number DE-102005018015-A), with publication number DE-102005018015-B3.', 'grant_date': '2006 on Apr 27th'}, {'Patents_info': 'UHLMANN PAC SYSTEME GMBH & CO holds the DE patent filing (app. number DE-102006022262-A), with publication number DE-102006022262-B3.', 'grant_date': 'Nov 29th, 2007'}, {'Patents_info': 'The DE patent filing (application no. DE-102007030491-A) is belonging to HEINRICH GEORG GMBH MASCHINENF and has pub. number DE-102007030491-B3.', 'grant_date': '2009, January 29th'}, {'Patents_info': 'In DE, the patent filing (application no. DE-102009032362-A) is owned by MARTOR KG and has pub. number DE-102009032362-B3.', 'grant_date': '17th Jun 2010'}, {'Patents_info': 'Patent application (no. DE-102015114819-A) from DE, held by ROCKWELL COLLINS DEUTSCHLAND GMBH, with pub. number DE-102015114819-B3.', 'grant_date': 'on December 22nd, 2016'}, {'Patents_info': 'MITUTOYO CORP holds the DE patent filing (app. number DE-10037981-A), with pub. number DE-10037981-B4.', 'grant_date': '19th of October, 2017'}, {'Patents_info': 'The DE patent application (no. DE-10052167-A) is held by YAMATO SEWING MACHINE MFG and has pub. number DE-10052167-B4.', 'grant_date': '23rd Jun 2005'}, {'Patents_info': 'Application (no. DE-10127786-A) from DE, belonging to KRAHFORST JUERGEN, with pub. number DE-10127786-B4.', 'grant_date': 'November 10th, 2005'}, {'Patents_info': 'In DE, the patent application (no. DE-10130631-A) is owned by SCHNEIDER SIEGHARD and has publication number DE-10130631-B4.', 'grant_date': '28th of October, 2010'}], 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.execute_python:18': {'status': 'check_complete'}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.list_db:22': ['cpc_definition']}

exec(code, env_args)
