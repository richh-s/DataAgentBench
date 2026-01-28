code = """import json
import re

# Load UCLA patents data
ucla_path = globals()['var_functions.query_db:24']
with open(ucla_path, 'r') as f:
    ucla_patents = json.load(f)

# Find the UCLA patent with pub number US-2010025717-A1
target_pub_num = "US-2010025717-A1"
cpc_codes_for_cited_patent = []

for patent in ucla_patents:
    patents_info = patent.get('Patents_info', '')
    
    # Check if this is the target publication
    if target_pub_num in patents_info:
        cpc_data = patent.get('cpc', '[]')
        try:
            cpc_list = json.loads(cpc_data) if isinstance(cpc_data, str) else cpc_data
            cpc_codes_for_cited_patent = [cpc['code'] for cpc in cpc_list if 'code' in cpc]
            print(f'Found {target_pub_num} with {len(cpc_codes_for_cited_patent)} CPC codes')
        except:
            pass
        break

print(f'CPC codes for cited patent: {cpc_codes_for_cited_patent}')

# Get unique CPC codes (removing duplicates)
unique_cpc_codes = list(set(cpc_codes_for_cited_patent))
print(f'Unique CPC codes: {unique_cpc_codes}')

result = {
    'target_patent': target_pub_num,
    'cpc_codes': unique_cpc_codes
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/108', 'synonyms': '[]', 'titleFull': 'Swine', 'titlePart': '[\n  "Swine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/105', 'synonyms': '[]', 'titleFull': 'Murine', 'titlePart': '[\n  "Murine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/101', 'synonyms': '[]', 'titleFull': 'Bovine', 'titlePart': '[\n  "Bovine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/107', 'synonyms': '[]', 'titleFull': 'Rabbit', 'titlePart': '[\n  "Rabbit"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/103', 'synonyms': '[]', 'titleFull': 'Ovine', 'titlePart': '[\n  "Ovine"\n]'}], 'var_functions.execute_python:12': {'ucla_patents_count': 5}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:18': {'ucla_patents_count': 169, 'ucla_pub_numbers_count': 165, 'ucla_pub_numbers': ['US-2022074631-A1', 'TW-201925402-A', 'US-11421276-B2', 'AU-2019275518-B2', 'US-2017194630-A1', 'JP-S6163700-A', 'US-2017281687-A1', 'EP-00992018-A', 'AU-2003247814-A1', 'AU-2017356943-A1', 'US-6237292-B1', 'US-7745569-B2', 'US-11072681-B2', 'AU-2002254753-A', 'US-9061071-B2', 'KR-20050085437-A', 'KR-20160119166-A', 'EP-0826155-A4', 'US-2019169580-A1', 'US-2020283856-A1', 'AU-2898989-A', 'RO-70061-A', 'WO-2017136335-A1', 'US-2019059638-W', 'WO-2021102420-A1', 'WO-2012162563-A2', 'US-10900049-B2', 'US-11376346-B2', 'US-2017369950-A1', 'CN-100339724-C', 'US-2009031436-A1', 'AU-2005269556-A1', 'US-11248107-B2', 'WO-2019173834-A1', 'US-2017145219-A1', 'US-2018304537-A1', 'US-2021002329-A1', 'KR-20200041324-A', 'CN-103189548-A', 'CA-2298540-A1', 'AU-2001296493-A', 'AU-2008329628-A', 'US-10765865-B2', 'JP-2005104983-A', 'IL-14014099-A', 'US-2021000566-A1', 'US-2006051790-A1', 'PT-2970346-T', 'US-37750473-A', 'AU-7724398-A', 'US-2023171142-A1', 'US-2022016812-W', 'WO-2018026404-A3', 'US-2006292670-A1', 'US-2017050153-A1', 'US-2021101879-A1', 'US-2023321419-A1', 'AU-2003297741-A1', 'WO-2017214343-A1', 'US-2018348310-A1', 'US-2021282642-A1', 'US-2019209590-A1', 'FR-7327711-A', 'US-10359432-B2', 'US-11667770-B2', 'CA-3161617-A1', 'CA-3225295-A', 'JP-2009260386-A', 'CA-2562038-C', 'US-7052856-B2', 'US-6750960-B2', 'EP-2210307-A4', 'US-74211203-A', 'US-2020025859-A1', 'US-2021039104-A1', 'EP-1212462-A1', 'WO-2014152660-A1', 'US-2023073050-W', 'US-5547866-A', 'KR-100228821-B1', 'US-2023279470-A1', 'AU-2008349842-A1', 'EP-4284234-A1', 'WO-2018067976-A1', 'WO-2020055916-A9', 'US-6767662-B2', 'US-2021181673-A1', 'US-2023314781-A1', 'US-2018018836-W', 'WO-2023212447-A2', 'US-6980295-B2', 'AU-2015364602-B2', 'US-2003112494-A1', 'CN-96195210-A', 'CA-2220674-A', 'IL-274176-A', 'JP-2014224156-A', 'IL-244029-A0', 'US-2004115131-A1', 'US-2005234013-A1', 'US-58729205-A', 'US-91189497-A', 'CN-101584047-A', 'AU-2010214112-B2', 'MX-2013002850-A', 'US-2019328740-A1', 'US-2022018060-A1', 'WO-2023225482-A3', 'WO-2024044766-A3', 'CA-3027364-A', 'CA-3055214-A', 'AU-2007297661-A1', 'EP-19908337-A', 'WO-2019067860-A1', 'EP-07753965-A', 'US-2018080022-A1', 'US-2022123166-A1', 'WO-2024112568-A1', 'US-2018277766-A1', 'AU-5711401-A', 'CA-2550552-A1', 'PE-20130764-A1', 'US-2017294981-A1', 'US-11445941-B2', 'US-11014955-B2', 'US-3666017-A', 'IL-23672515-A', 'KR-20110004413-A', 'CN-103237558-A', 'CN-102584712-A', 'CN-103687626-A', 'ZA-200802422-A', 'CN-102067370-B', 'CA-2718348-C', 'CA-2278751-A', 'US-10337029-B2', 'US-11546022-B2', 'HK-1052178-A1', 'US-11607427-B2', 'US-12025581-B2', 'US-11960018-B2', 'US-2023155090-A1', 'WO-2010045542-A3', 'EP-3668487-A4', 'US-56389709-A', 'AP-2011005954-A', 'CA-2283629-C', 'US-2023340506-A1', 'HK-1250569-A1', 'AU-2004253879-A1', 'WO-2023239670-A1', 'WO-2012158833-A3', 'US-10744347-B2', 'HR-P20201231-T1', 'BR-9610580-A', 'AU-2409401-A', 'AU-5366398-A', 'ID-23426-A', 'US-5304932-A', 'AU-3353000-A', 'AU-5938296-A', 'US-2010025717-A1', 'US-2017087258-A1', 'US-2018243924-A1', 'AU-6535890-A']}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:28': 'file_storage/functions.execute_python:28.json', 'var_functions.query_db:30': [{'symbol': 'H01M10/448', 'titleFull': 'End of discharge regulating measures'}, {'symbol': 'H01M10/465', 'titleFull': 'Accumulators structurally combined with charging apparatus with solar battery as charging system'}, {'symbol': 'H01M10/445', 'titleFull': 'Methods for charging or discharging in response to gas pressure'}], 'var_functions.execute_python:32': 'file_storage/functions.execute_python:32.json'}

exec(code, env_args)
