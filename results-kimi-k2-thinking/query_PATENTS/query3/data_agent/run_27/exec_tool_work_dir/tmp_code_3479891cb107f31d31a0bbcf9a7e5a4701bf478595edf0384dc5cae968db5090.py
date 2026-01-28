code = """import json
import re
from collections import defaultdict

# Load data
all_patents_file = locals()['var_functions.query_db:74']
with open(all_patents_file, 'r') as f:
    all_data = json.load(f)

print('Total records:', len(all_data))

# Extract UC patent publication numbers
uc_pub_numbers = set()
for record in all_data:
    patents_info = record.get('Patents_info', '')
    if 'UNIV CALIFORNIA' in patents_info:
        patterns = [r'has pub\. number\s+([A-Z]{2,3}-[A-Z0-9-]+)', r'publication number\s+([A-Z]{2,3}-[A-Z0-9-]+)']
        pub_num = None
        for pattern in patterns:
            match = re.search(pattern, patents_info)
            if match:
                pub_num = match.group(1)
                break
        if pub_num:
            uc_pub_numbers.add(pub_num)

print('UC patents found:', len(uc_pub_numbers))

# Find citations
citation_map = defaultdict(list)
assignment_counts = defaultdict(int)
assignee_cpc = defaultdict(set)

processed = 0
for record in all_data:
    patents_info = record.get('Patents_info', '')
    citation = record.get('citation', '[]')
    cpc = record.get('cpc', '[]')
    
    # Skip UC patents
    if 'UNIV CALIFORNIA' in patents_info:
        continue
    
    # Get assignee
    assignee = None
    if 'owned by' in patents_info:
        match = re.search(r'owned by\s+([^,\.]+)', patents_info)
        if match:
            assignee = match.group(1).strip()
    elif 'assigned to' in patents_info:
        match = re.search(r'assigned to\s+([^,\.]+)', patents_info)
        if match:
            assignee = match.group(1).strip()
    elif 'holds the' in patents_info:
        match = re.match(r'([A-Z][A-Z\s]+)\s+holds the', patents_info)
        if match:
            assignee = match.group(1).strip()
    
    if not assignee or 'UNIV CALIFORNIA' in assignee:
        continue
    
    # Parse citations
    try:
        citations = json.loads(citation)
    except:
        continue
    
    for cite in citations:
        pub_num = cite.get('publication_number')
        if pub_num and pub_num in uc_pub_numbers:
            # Parse CPC codes
            try:
                cpc_codes = json.loads(cpc)
                cpc_list = list(set([code.get('code') for code in cpc_codes if code.get('code')]))
            except:
                cpc_list = []
            
            # Record citation
            citation_map[pub_num].append({'assignee': assignee, 'cpc': cpc_list})
            assignment_counts[assignee] += 1
            assignee_cpc[assignee].update(cpc_list)
    
    processed += 1
    if processed % 10000 == 0:
        print('Processed', processed, 'records')

print('Citations found:', len(citation_map))
print('Total citations:', sum(len(v) for v in citation_map.values()))

# Top assignees
top_assignees = sorted(assignment_counts.items(), key=lambda x: x[1], reverse=True)[:10]
print('Top assignees:', top_assignees)

# Save results
result = {
    'uc_patents_cited': len(citation_map),
    'total_citations': sum(len(v) for v in citation_map.values()),
    'top_assignees': top_assignees,
    'assignee_cpc': {k: list(v) for k, v in assignee_cpc.items()}
}

with open('/tmp/final_citation_analysis.json', 'w') as f:
    json.dump(result, f, indent=2)

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': 'Loaded 100 records', 'var_functions.execute_python:12': {'uc_patents': ['US-202117472182-A', 'TW-107142982-A', 'US-11421276-B2', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-201715625819-A', 'AU-2003247814-A', 'AU-2017356943-A1', 'US-39548599-A', 'US-55161904-A', 'US-11072681-B2', 'US-9061071-B2', 'KR-20050085437-A', 'KR-20167024476-A', 'EP-0826155-A4', 'US-2019169580-A1', 'US-2020283856-A1', 'AU-2898989-A', 'RO-70061-A', 'US-2017015812-W', 'WO-2021102420-A1', 'US-2012039471-W', 'US-11376346-B2', 'US-201715646074-A', 'KR-20187008669-A', 'CN-100339724-C', 'US-2009031436-A1', 'AU-2005269556-A', 'WO-2019173834-A1', 'US-201715422925-A', 'US-2021002329-A1', 'KR-20207004898-A', 'CN-103189548-A', 'CA-2298540-A1', 'AU-2001296493-A', 'JP-2005104983-A', 'US-202017021925-A', 'US-2006051790-A1', 'KR-20207010098-A', 'PT-14764430-T', 'AU-7724398-A', 'US-202117926000-A', 'WO-2018026404-A3', 'US-54455304-A', 'US-2021101879-A1', 'US-202117791452-A', 'AU-2003297741-A1', 'WO-2017214343-A1', 'US-201715614287-A', 'US-202117197897-A', 'US-2019209590-A1', 'KR-20087016723-A', 'FR-7327711-A', 'US-10359432-B2', 'US-11667770-B2', 'CA-3161617-A1', 'JP-2009181101-A', 'CA-2562038-A', 'US-41229799-A', 'US-39137803-A', 'EP-08826523-A', 'US-201716335976-A', 'US-2021039104-A1', 'EP-00959970-A', 'US-2014027588-W', 'US-2023073050-W', 'US-27746394-A', 'KR-19940700442-A', 'US-202318169681-A', 'AU-2008349842-A1', 'EP-22746465-A', 'WO-2018067976-A1', 'WO-2020055916-A9', 'US-6767662-B2', 'US-2021181673-A1', 'WO-2023212447-A2', 'US-6980295-B2', 'AU-2015364602-B2', 'US-30426202-A', 'CN-96195210-A', 'IL-27417620-A'], 'citations': ['US-4599677-A', 'US-2015129765-A1', 'FR-3105380-A1', 'US-11466906-B2', 'US-2001053519-A1', 'WO-0212892-A2', 'US-2002115120-A1', 'WO-03016910-A1', 'US-2003119064-A1', 'US-2003199000-A1']}, 'var_functions.execute_python:14': ['US-2022074631-A1', 'TW-107142982-A', 'US-11421276-B2', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1', 'AU-2003247814-A1', 'AU-2017356943-A1', 'US-6237292-B1', 'US-7745569-B2', 'US-11072681-B2', 'US-9061071-B2', 'KR-20050085437-A', 'KR-20160119166-A', 'EP-0826155-A4', 'US-2019169580-A1', 'US-2020283856-A1', 'AU-2898989-A', 'RO-70061-A', 'WO-2017136335-A1'], 'var_functions.query_db:16': [], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': ['US-2022074631-A1', 'TW-201925402-A', 'US-11421276-B2', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1', 'AU-2003247814-A1', 'AU-2017356943-A1', 'US-6237292-B1', 'US-7745569-B2', 'US-11072681-B2', 'US-9061071-B2', 'KR-20050085437-A', 'KR-20160119166-A', 'EP-0826155-A4', 'US-2019169580-A1', 'US-2020283856-A1', 'AU-2898989-A', 'RO-70061-A', 'WO-2017136335-A1'], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'count': 114, 'sample': ['US-2022074631-A1', 'TW-201925402-A', 'US-11421276-B2', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1', 'AU-2003247814-A1', 'AU-2017356943-A1', 'US-6237292-B1', 'US-7745569-B2']}, 'var_functions.query_db:28': [], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:32': {'count': 114, 'sample': ['US-2022074631-A1', 'TW-201925402-A', 'US-11421276-B2', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1', 'AU-2003247814-A1', 'AU-2017356943-A1', 'US-6237292-B1', 'US-7745569-B2']}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:36': {'uc_count': 157, 'sample': {'US-2022074631-A1': 'F28D15/00', 'TW-201925402-A': 'C09D11/322', 'US-11421276-B2': 'C12Q2600/136', 'AU-2019275518-B2': 'A61P25/20', 'US-2017194630-A1': 'H01M4/386'}}, 'var_functions.query_db:38': [], 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:46': {'uc_patents_count': 114, 'sample': {'US-2022074631-A1': ['F25B2321/001', 'Y02B30/00', 'F28D15/00'], 'TW-201925402-A': ['C08K3/08', 'C08K2003/0806', 'C09J11/04'], 'US-11421276-B2': ['C12Q2600/136', 'C12Q2600/158', 'C12Q1/6883']}}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:50': [], 'var_functions.execute_python:52': {'uc_patents_count': 137, 'sample': ['US-2022074631-A1', 'TW-201925402-A', 'US-11421276-B2', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1', 'AU-2003247814-A1', 'AU-2017356943-A1', 'US-6237292-B1', 'US-7745569-B2']}, 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:56': 'file_storage/functions.query_db:56.json', 'var_functions.execute_python:58': {'count': 114, 'sample': {'US-2022074631-A1': ['F25B2321/001', 'F28D15/00', 'F25B21/00', 'Y02B30/00'], 'TW-201925402-A': ['C09D11/037', 'C09J9/02', 'C09D11/52', 'B82Y40/00', 'C08K3/08', 'C08K2201/011', 'C09J2463/00', 'C08K3/042', 'C09D11/322', 'C09J11/04', 'C08K2003/0806', 'B82Y30/00', 'C08K7/00', 'C08K2201/001'], 'US-11421276-B2': ['C12Q2600/118', 'C12Q2600/158', 'C12Q2600/112', 'Y02A50/30', 'C12Q2600/136', 'C12Q1/6883']}}, 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.execute_python:62': {'uc_count': 169, 'sample_uc_pub': ['HK-1052178-A1', 'US-2020283856-A1', 'US-2017087258-A1', 'TW-201925402-A', 'CN-101584047-A', 'US-2006292670-A1', 'RO-70061-A', 'US-202017604154-A', 'US-2022074631-A1', 'US-2023155090-A1']}, 'var_functions.execute_python:64': {'total_citing': 0, 'sample': []}, 'var_functions.query_db:66': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}], 'var_functions.execute_python:70': {'uc_patents_cited': 0, 'total_citations': 0, 'sample': {}}, 'var_functions.query_db:74': 'file_storage/functions.query_db:74.json'}

exec(code, env_args)
