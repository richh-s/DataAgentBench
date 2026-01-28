code = """import json
import re
import sqlite3
import os

# Load UC patents data
result_file = locals()['var_functions.query_db:6']
if isinstance(result_file, str) and result_file.endswith('.json'):
    with open(result_file, 'r') as f:
        uc_patents = json.load(f)
else:
    uc_patents = result_file

# Extract all UC publication numbers
uc_pub_numbers = set()
for patent in uc_patents:
    patents_info = patent.get('Patents_info', '')
    matches = re.findall(r'[A-Z]{2}-[A-Z0-9-]+', patents_info)
    for match in matches:
        uc_pub_numbers.add(match)

# Load the full database
full_db_file = locals()['var_functions.query_db:18']
if isinstance(full_db_file, str) and full_db_file.endswith('.json'):
    with open(full_db_file, 'r') as f:
        all_patents = json.load(f)
else:
    all_patents = full_db_file

# Process patents in chunks to find citations to UC patents
citing_patents = []
chunk_size = 1000

for i in range(0, len(all_patents), chunk_size):
    chunk = all_patents[i:i + chunk_size]
    
    for patent in chunk:
        citation_str = patent.get('citation', '[]')
        if not citation_str or citation_str == '[]':
            continue
            
        try:
            citations = json.loads(citation_str)
            for cit in citations:
                pub_num = cit.get('publication_number', '')
                if pub_num and pub_num in uc_pub_numbers:
                    citing_patents.append({
                        'patent_info': patent.get('Patents_info', ''),
                        'citation': pub_num,
                        'cpc': patent.get('cpc', '[]')
                    })
                    break
        except:
            # Try regex extraction
            pub_nums = re.findall(r'"publication_number"\s*:\s*"([A-Z]{2}-[A-Z0-9-]+)"', citation_str)
            for pub_num in pub_nums:
                if pub_num in uc_pub_numbers:
                    citing_patents.append({
                        'patent_info': patent.get('Patents_info', ''),
                        'citation': pub_num,
                        'cpc': patent.get('cpc', '[]')
                    })
                    break

print('__RESULT__:')
print(json.dumps(f"Found {len(citing_patents)} patents that cite UNIV CALIFORNIA patents"))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'Found 5 patents from UNIV CALIFORNIA', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:8': 'Found 169 patents assigned to UNIV CALIFORNIA', 'var_functions.execute_python:10': 'Found 1112 unique cited publication numbers', 'var_functions.query_db:12': [], 'var_functions.execute_python:14': 'Found 114 UNIV CALIFORNIA publication numbers', 'var_functions.execute_python:16': ['US-70199003-A', 'AU-2007297661-A', 'WO-2012158833-A3', 'US-2018053351-W', 'AU-2004253879-A1', 'KR-20107024636-A', 'WO-2023239670-A1', 'US-2017145219-A1', 'EP-07753965-A', 'RO-7944874-A'], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': 'Total patents in database: 277813', 'var_functions.execute_python:22': 'UC publication numbers sample: "CA-2718348-C", "HK-18104296-A", "AU-2019275518-B2", "CA-3027364-A", "US-2018053351-W", "IL-24402916-A", "AU-2007297661-A1", "US-2022016812-W", "CN-201280035828-A", "US-2017281687-A1"...', 'var_functions.execute_python:24': 'Total UC publication numbers: 329, divided into 7 chunks', 'var_functions.execute_python:26': "Sample UC publication numbers to check: ['AU-2019275518-A', 'US-202117472182-A', 'US-201916454755-A']", 'var_functions.query_db:28': [], 'var_functions.execute_python:30': 'Loaded 277813 patents. Searching for citations to 329 UC patents...'}

exec(code, env_args)
