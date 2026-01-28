code = """import json

# Load UC publication numbers from previous analysis
result_var = locals()['var_functions.query_db:12']

if isinstance(result_var, str) and result_var.endswith('.json'):
    with open(result_var, 'r') as f:
        uc_patents = json.load(f)
else:
    uc_patents = result_var

# Extract UC publication numbers
uc_pub_numbers = set()
for patent in uc_patents:
    patents_info = patent.get('Patents_info', '')
    match = re.search(r'pub\. number\s+([A-Z0-9\-]+)', patents_info, re.IGNORECASE)
    if not match:
        match = re.search(r'publication number\s+([A-Z0-9\-]+)', patents_info, re.IGNORECASE)
    if match:
        pub_num = match.group(1)
        uc_pub_numbers.add(pub_num)

print('__RESULT__:')
print(json.dumps({
    'uc_pub_numbers': list(uc_pub_numbers)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['publicationinfo'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [{'total_records': '277813'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'uc_patents_count': 169, 'uc_pub_numbers': ['US-2022074631-A1', 'TW-201925402-A', 'US-11421276-B2', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1', 'AU-2003247814-A1', 'AU-2017356943-A1', 'US-6237292-B1', 'US-7745569-B2'], 'total_uc_pub_numbers': 114}, 'var_functions.execute_python:18': 'file_storage/functions.execute_python:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'message': 'Found 114 UNIV CALIFORNIA publication numbers', 'count': 114, 'sample_pub_numbers': ['US-2009031436-A1', 'WO-2024112568-A1', 'AU-2015364602-B2', 'WO-2023239670-A1', 'US-11667770-B2', 'KR-20110004413-A', 'WO-2010045542-A3', 'CN-103687626-A', 'US-11072681-B2', 'AU-2008349842-A1']}, 'var_functions.execute_python:24': {'total_uc_publication_numbers': 114, 'total_cited_by_uc_patents': 1112, 'uc_pub_numbers': ['CA-2298540-A1', 'WO-2023239670-A1', 'CN-101584047-A', 'US-2010025717-A1', 'WO-2012158833-A3', 'US-10359432-B2', 'US-2023155090-A1', 'AU-2409401-A', 'US-11421276-B2', 'US-2019169580-A1', 'CA-2718348-C', 'US-11546022-B2', 'US-2019328740-A1', 'US-2021282642-A1', 'US-2020025859-A1', 'EP-1212462-A1', 'US-7052856-B2', 'WO-2023225482-A3', 'WO-2020055916-A9', 'RO-70061-A', 'US-2017281687-A1', 'EP-0826155-A4', 'US-2022018060-A1', 'US-6750960-B2', 'KR-20110004413-A', 'CN-102584712-A', 'US-2022074631-A1', 'US-2017087258-A1', 'WO-2012162563-A2', 'US-11014955-B2', 'US-2023171142-A1', 'US-11376346-B2', 'AU-2003297741-A1', 'US-2009031436-A1', 'CA-3161617-A1', 'US-2021101879-A1', 'CN-103687626-A', 'AU-6535890-A', 'US-5304932-A', 'PT-2970346-T', 'US-6237292-B1', 'TW-201925402-A', 'US-9061071-B2', 'HK-1250569-A1', 'JP-2014224156-A', 'IL-274176-A', 'WO-2024112568-A1', 'WO-2017136335-A1', 'CA-2283629-C', 'US-2020283856-A1', 'WO-2024044766-A3', 'US-2021181673-A1', 'AU-2008349842-A1', 'CA-2550552-A1', 'US-2021000566-A1', 'CN-102067370-B', 'CA-2562038-C', 'US-6980295-B2', 'HK-1052178-A1', 'WO-2014152660-A1', 'US-10744347-B2', 'EP-3668487-A4', 'WO-2021102420-A1', 'KR-20200041324-A', 'AU-2019275518-B2', 'US-6767662-B2', 'HR-P20201231-T1', 'US-2018243924-A1', 'AU-2003247814-A1', 'KR-20050085437-A', 'WO-2019173834-A1', 'EP-4284234-A1', 'US-11072681-B2', 'KR-20160119166-A', 'US-12025581-B2', 'US-2019209590-A1', 'WO-2019067860-A1', 'IL-244029-A0', 'WO-2017214343-A1', 'CN-100339724-C', 'WO-2010045542-A3', 'US-2023321419-A1', 'US-2003112494-A1', 'US-2017145219-A1', 'US-2021002329-A1', 'MX-2013002850-A', 'AU-3353000-A', 'US-2006051790-A1', 'PE-20130764-A1', 'AU-2005269556-A1', 'CN-103189548-A', 'US-5547866-A', 'AU-2007297661-A1', 'WO-2018067976-A1', 'JP-2009260386-A', 'US-2021039104-A1', 'US-11667770-B2', 'AU-2010214112-B2', 'AU-5938296-A', 'US-2004115131-A1', 'JP-S6163700-A', 'US-2006292670-A1', 'US-2023279470-A1', 'WO-2018026404-A3', 'US-2005234013-A1', 'JP-2005104983-A', 'ID-23426-A', 'EP-2210307-A4', 'AU-2898989-A', 'AU-2015364602-B2', 'WO-2023212447-A2', 'US-7745569-B2', 'AU-2004253879-A1', 'AU-2017356943-A1']}}

exec(code, env_args)
