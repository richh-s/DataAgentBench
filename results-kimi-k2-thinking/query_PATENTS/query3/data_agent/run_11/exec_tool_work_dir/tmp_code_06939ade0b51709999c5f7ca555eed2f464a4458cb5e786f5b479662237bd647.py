code = """import json
import re

# Load all UC patents and extract their publication numbers and CPC codes
result_file = locals()['var_functions.query_db:20']
with open(result_file, 'r') as f:
    ucs_patents = json.load(f)

# Create mappings
uc_pub_to_cpc = {}  # publication_number -> list of CPC codes
uc_pub_numbers = []

for patent in ucs_patents:
    patents_info = patent.get('Patents_info', '')
    
    if 'UNIV CALIFORNIA' in patents_info.upper():
        # Extract publication number
        pub_match = re.search(r'(?:pub\. number|publication number|number)\s+([A-Z]{2}-[A-Z0-9-]+)', patents_info)
        if pub_match:
            pub_num = pub_match.group(1)
            uc_pub_numbers.append(pub_num)
            
            # Extract CPC codes
            cpc_codes = []
            cpc_data = patent.get('cpc', '[]')
            if cpc_data:
                try:
                    cpc_list = json.loads(cpc_data)
                    for cpc_item in cpc_list:
                        if 'code' in cpc_item:
                            code = cpc_item['code']
                            # Extract just the main class, not the whole hierarchy
                            cpc_codes.append(code)
                except:
                    pass
            
            uc_pub_to_cpc[pub_num] = list(set(cpc_codes))  # Remove duplicates

result_summary = {
    'uc_patent_count': len(uc_pub_numbers),
    'sample_pubs': list(uc_pub_to_cpc.keys())[:5],
    'sample_cpcs': uc_pub_to_cpc.get(list(uc_pub_to_cpc.keys())[0], [])[:5] if uc_pub_to_cpc else []
}

print('__RESULT__:')
print(json.dumps(result_summary))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'total_uc_patents': 8, 'sample_pub_numbers': ['US-202117472182-A', 'TW-107142982-A', 'US-11421276-B2', 'AU-2019275518-B2', 'JP-S6163700-A'], 'patents_with_citations': 5}, 'var_functions.execute_python:16': {'/tmp': [], '/tmp/patent_dbs': 'access error', '/': ['root', 'tmp', 'lib', 'run', 'srv', 'lib64', 'usr', 'sys', 'sbin', 'opt']}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'total_uc_patents': 137, 'uc_pub_numbers': ['US-202117472182-A', 'TW-107142982-A', 'US-11421276-B2', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-201715625819-A', 'AU-2003247814-A', 'AU-2017356943-A1', 'US-39548599-A', 'US-55161904-A', 'US-11072681-B2', 'US-9061071-B2', 'KR-20050085437-A', 'KR-20167024476-A', 'EP-0826155-A4', 'US-2019169580-A1', 'US-2020283856-A1', 'AU-2898989-A', 'RO-70061-A', 'US-2017015812-W', 'WO-2021102420-A1', 'US-2012039471-W', 'US-11376346-B2', 'US-201715646074-A', 'KR-20187008669-A', 'CN-100339724-C', 'US-2009031436-A1', 'AU-2005269556-A', 'WO-2019173834-A1', 'US-201715422925-A', 'US-2021002329-A1', 'KR-20207004898-A', 'CN-103189548-A', 'CA-2298540-A1', 'AU-2001296493-A', 'JP-2005104983-A', 'US-202017021925-A', 'US-2006051790-A1', 'KR-20207010098-A', 'PT-14764430-T', 'AU-7724398-A', 'US-202117926000-A', 'WO-2018026404-A3', 'US-54455304-A', 'US-2021101879-A1', 'US-202117791452-A', 'AU-2003297741-A1', 'WO-2017214343-A1', 'US-201715614287-A', 'US-202117197897-A', 'US-2019209590-A1', 'KR-20087016723-A', 'FR-7327711-A', 'US-10359432-B2', 'US-11667770-B2', 'CA-3161617-A1', 'JP-2009181101-A', 'CA-2562038-A', 'US-41229799-A', 'US-39137803-A', 'EP-08826523-A', 'US-201716335976-A', 'US-2021039104-A1', 'EP-00959970-A', 'US-2014027588-W', 'US-2023073050-W', 'US-27746394-A', 'KR-19940700442-A', 'US-202318169681-A', 'AU-2008349842-A1', 'EP-22746465-A', 'WO-2018067976-A1', 'WO-2020055916-A9', 'US-6767662-B2', 'US-2021181673-A1', 'WO-2023212447-A2', 'US-6980295-B2', 'AU-2015364602-B2', 'US-30426202-A', 'CN-96195210-A', 'IL-27417620-A', 'JP-2014180140-A', 'IL-24402916-A', 'US-70199003-A', 'US-4541105-A', 'US-58729205-A', 'US-91189497-A', 'CN-101584047-A', 'AU-2010214112-A', 'MX-2013002850-A', 'US-201916396723-A', 'US-2022018060-A1', 'US-2023067015-W', 'WO-2024044766-A3', 'CA-3055214-A', 'AU-2007297661-A1', 'EP-19908337-A', 'WO-2019067860-A1', 'US-202017422807-A', 'US-2023080114-W', 'CA-2550552-A', 'PE-20130764-A1', 'US-201515514092-A', 'US-202016843567-A', 'KR-20110004413-A', 'CN-102584712-A', 'CN-103687626-A', 'ZA-200802422-A', 'CN-200880129911-A', 'CA-2718348-C', 'US-201816201848-A', 'US-11546022-B2', 'HK-1052178-A1', 'US-12025581-B2', 'US-2023155090-A1', 'WO-2010045542-A3', 'EP-18847365-A', 'AP-2011005954-A', 'CA-2283629-A', 'US-202218054917-A', 'HK-18104296-A', 'AU-2004253879-A', 'WO-2023239670-A1', 'WO-2012158833-A3', 'US-10744347-B2', 'HR-P20201231-T', 'BR-9610580-A', 'AU-2409401-A', 'AU-5366398-A', 'ID-990914-A', 'US-5304932-A', 'AU-3353000-A', 'AU-5938296-A', 'US-2010025717-A1', 'US-201615265158-A', 'US-201615758551-A', 'AU-6535890-A'], 'sample_cpc_map': {'US-202117472182-A': ['Y02B30/00', 'F25B2321/001', 'F25B21/00', 'F28D15/00', 'F25B21/00', 'F25B2321/001', 'F25B2321/001', 'F28D15/00', 'F25B21/00'], 'TW-107142982-A': ['C09J11/04', 'C08K3/08', 'C08K2201/001', 'C09J9/02', 'C09D11/52', 'C08K7/00', 'C09D11/322', 'C09J9/02', 'C08K2201/011', 'C09D11/037', 'C08K2003/0806', 'B82Y30/00', 'B82Y30/00', 'C08K2201/011', 'C09J11/04', 'C08K2003/0806', 'C09J2463/00', 'C08K3/042', 'C09D11/52', 'B82Y40/00', 'B82Y40/00', 'C08K3/042', 'C09D11/322', 'C08K7/00', 'C09D11/037', 'C08K2201/001', 'C08K3/08', 'C09J9/02', 'C09D11/037', 'C08K3/042', 'C08K2003/0806', 'C09J11/04', 'C08K2201/011', 'C09D11/322', 'C09D11/52', 'C08K2201/001', 'B82Y40/00'], 'US-11421276-B2': ['Y02A50/30', 'C12Q1/6883', 'C12Q1/6883', 'C12Q2600/136', 'C12Q2600/158', 'C12Q2600/112', 'C12Q2600/158', 'C12Q2600/112', 'C12Q2600/118', 'C12Q2600/136', 'C12Q1/6883', 'C12Q2600/136', 'C12Q2600/112', 'C12Q2600/158', 'C12Q2600/118']}}, 'var_functions.execute_python:24': {'uc_pub_count': 137, 'sample_uc_pubs': ['US-202117472182-A', 'TW-107142982-A', 'US-11421276-B2', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-201715625819-A', 'AU-2003247814-A', 'AU-2017356943-A1', 'US-39548599-A', 'US-55161904-A']}, 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
