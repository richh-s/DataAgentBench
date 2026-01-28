code = """import json
import re
from collections import defaultdict

# Load CPC titles data
cpc_data = locals().get('var_functions.query_db:30')
cpc_titles = cpc_data if isinstance(cpc_data, list) else []

# Load assignee-CPC pairs data
assignee_cpc_data = locals().get('var_functions.execute_python:26')
assignee_cpc_pairs = assignee_cpc_data.get('assignee_cpc_pairs', []) if isinstance(assignee_cpc_data, dict) else []

# Create mapping of CPC code to title
cpc_title_map = {}
for entry in cpc_titles:
    symbol = entry.get('symbol', '')
    title = entry.get('titleFull', '')
    if symbol and title:
        cpc_title_map[symbol] = title

# Clean up assignee names and create final mapping
assignee_cpc_mapping = defaultdict(list)

for item in assignee_cpc_pairs:
    original_assignee = item.get('assignee', '')
    cpc_code = item.get('cpc_code', '')
    
    # Extract clean company name
    clean_assignee = original_assignee
    if 'held by' in original_assignee or 'owned by' in original_assignee:
        match = re.search(r'(?:held by|owned by)\s+([A-Z][A-Z\s]+?)(?:\sand|$)', original_assignee)
        if match:
            clean_assignee = match.group(1).strip()
    
    # Get CPC title
    cpc_title = cpc_title_map.get(cpc_code, 'Title not found')
    
    assignee_cpc_mapping[clean_assignee].append({
        'cpc_code': cpc_code,
        'cpc_title': cpc_title
    })

# Create final result as a list of dictionaries
final_result = []
for assignee, cpc_list in assignee_cpc_mapping.items():
    for cpc_item in cpc_list:
        final_result.append({
            'assignee': assignee,
            'cpc_code': cpc_item['cpc_code'],
            'cpc_title': cpc_item['cpc_title']
        })

print('__RESULT__:')
print(json.dumps(final_result, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': [{'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/108', 'synonyms': '[]', 'titleFull': 'Swine', 'titlePart': '[\n  "Swine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/105', 'synonyms': '[]', 'titleFull': 'Murine', 'titlePart': '[\n  "Murine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/101', 'synonyms': '[]', 'titleFull': 'Bovine', 'titlePart': '[\n  "Bovine"\n]'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:20': {'uc_patents_count': 169, 'all_patents_count': 277813}, 'var_functions.execute_python:22': {'uc_pub_numbers': ['CA-2298540-A1', 'US-2023321419-A1', 'US-2023155090-A1', 'WO-2012158833-A3', 'TW-201925402-A', 'EP-2210307-A4', 'EP-4284234-A1', 'US-6980295-B2', 'AU-3353000-A', 'WO-2024044766-A3'], 'citation_count': 2, 'uc_patents_with_cpc': 114}, 'var_functions.execute_python:24': {'citing_assignees': ['is held by BLOOM ENERGY CORP and has publication no', 'is owned by CRYSTAL IS INC and has publication no'], 'total_cpc_codes': 23, 'cpc_sample': ['H01L33/50', 'H01L33/0093', 'H01M4/8885', 'Y02E60/50', 'H01L33/00', 'H01L33/32', 'H01L33/30', 'H01L33/007', 'H01M4/9066', 'H01M8/1246', 'H01L33/54', 'H01M4/0419', 'Y02P70/50', 'H01L2224/16225', 'H01M4/9016', 'H01M4/9033', 'Y02E60/10', 'H01M8/1226', 'H01L33/06', 'H01M2008/1293']}, 'var_functions.execute_python:26': {'assignee_cpc_pairs': [{'assignee': 'is held by BLOOM ENERGY CORP and has publication no', 'cpc_code': 'Y02E60/50', 'count': 1}, {'assignee': 'is held by BLOOM ENERGY CORP and has publication no', 'cpc_code': 'H01M8/1226', 'count': 1}, {'assignee': 'is held by BLOOM ENERGY CORP and has publication no', 'cpc_code': 'H01M8/1246', 'count': 1}, {'assignee': 'is held by BLOOM ENERGY CORP and has publication no', 'cpc_code': 'H01M4/9066', 'count': 1}, {'assignee': 'is held by BLOOM ENERGY CORP and has publication no', 'cpc_code': 'H01M2008/1293', 'count': 1}, {'assignee': 'is held by BLOOM ENERGY CORP and has publication no', 'cpc_code': 'H01M4/9033', 'count': 1}, {'assignee': 'is held by BLOOM ENERGY CORP and has publication no', 'cpc_code': 'Y02P70/50', 'count': 1}, {'assignee': 'is held by BLOOM ENERGY CORP and has publication no', 'cpc_code': 'Y02E60/10', 'count': 1}, {'assignee': 'is held by BLOOM ENERGY CORP and has publication no', 'cpc_code': 'H01M4/9016', 'count': 1}, {'assignee': 'is held by BLOOM ENERGY CORP and has publication no', 'cpc_code': 'H01M8/1213', 'count': 1}, {'assignee': 'is held by BLOOM ENERGY CORP and has publication no', 'cpc_code': 'H01M4/8885', 'count': 1}, {'assignee': 'is held by BLOOM ENERGY CORP and has publication no', 'cpc_code': 'H01M4/0419', 'count': 1}, {'assignee': 'is owned by CRYSTAL IS INC and has publication no', 'cpc_code': 'H01L2224/16225', 'count': 1}, {'assignee': 'is owned by CRYSTAL IS INC and has publication no', 'cpc_code': 'H01L33/54', 'count': 1}, {'assignee': 'is owned by CRYSTAL IS INC and has publication no', 'cpc_code': 'H01L33/007', 'count': 1}, {'assignee': 'is owned by CRYSTAL IS INC and has publication no', 'cpc_code': 'H01L33/50', 'count': 1}, {'assignee': 'is owned by CRYSTAL IS INC and has publication no', 'cpc_code': 'H01L33/32', 'count': 1}, {'assignee': 'is owned by CRYSTAL IS INC and has publication no', 'cpc_code': 'H01L33/30', 'count': 1}, {'assignee': 'is owned by CRYSTAL IS INC and has publication no', 'cpc_code': 'H01L33/22', 'count': 1}, {'assignee': 'is owned by CRYSTAL IS INC and has publication no', 'cpc_code': 'H01L33/60', 'count': 1}, {'assignee': 'is owned by CRYSTAL IS INC and has publication no', 'cpc_code': 'H01L33/0093', 'count': 1}, {'assignee': 'is owned by CRYSTAL IS INC and has publication no', 'cpc_code': 'H01L33/00', 'count': 1}, {'assignee': 'is owned by CRYSTAL IS INC and has publication no', 'cpc_code': 'H01L33/06', 'count': 1}], 'all_cpc_codes': ['H01L2224/16225', 'H01L33/54', 'H01M4/9066', 'H01M4/9033', 'H01M4/9016', 'H01L33/06', 'H01L33/30', 'H01M8/1213', 'H01L33/60', 'H01M8/1226', 'Y02E60/50', 'H01M8/1246', 'H01M4/8885', 'H01L33/00', 'H01L33/007', 'H01L33/50', 'H01L33/32', 'H01M2008/1293', 'Y02P70/50', 'Y02E60/10', 'H01L33/22', 'H01L33/0093', 'H01M4/0419']}, 'var_functions.query_db:30': [{'symbol': 'H01M4/9016', 'titleFull': 'Oxides, hydroxides or oxygenated metallic salts'}, {'symbol': 'H01M8/1213', 'titleFull': 'Fuel cells with solid electrolytes operating at high temperature, e.g. with stabilised ZrO2 electrolyte characterised by the electrode/electrolyte combination or the supporting material'}, {'symbol': 'H01M2008/1293', 'titleFull': 'Fuel cells with solid oxide electrolytes'}, {'symbol': 'H01L2224/16225', 'titleFull': 'Disposition the bump connector connecting between a semiconductor or solid-state body and an item not being a semiconductor or solid-state body, e.g. chip-to-substrate, chip-to-passive the body and the item being stacked the item being non-metallic, e.g. insulating substrate with or without metallisation'}, {'symbol': 'H01L33/50', 'titleFull': 'Wavelength conversion elements'}, {'symbol': 'Y02E60/50', 'titleFull': 'Fuel cells'}, {'symbol': 'H01L33/007', 'titleFull': 'Processes for devices with an active region comprising only III-V compounds with a substrate not being a III-V compound comprising nitride compounds'}, {'symbol': 'Y02E60/10', 'titleFull': 'Energy storage using batteries'}, {'symbol': 'Y02P70/50', 'titleFull': 'Manufacturing or production processes characterised by the final manufactured product'}, {'symbol': 'H01L33/06', 'titleFull': 'Semiconductor devices having potential barriers specially adapted for light emission; Processes or apparatus specially adapted for the manufacture or treatment thereof or of parts thereof; Details thereof characterised by the semiconductor bodies with a quantum effect structure or superlattice, e.g. tunnel junction within the light emitting region, e.g. quantum confinement structure or tunnel barrier'}, {'symbol': 'H01L33/22', 'titleFull': 'Roughened surfaces, e.g. at the interface between epitaxial layers'}, {'symbol': 'H01L33/30', 'titleFull': 'Materials of the light emitting region containing only elements of Group III and Group V of the Periodic Table'}, {'symbol': 'H01L33/54', 'titleFull': 'Encapsulations having a particular shape'}, {'symbol': 'H01L33/60', 'titleFull': 'Reflective elements'}, {'symbol': 'H01L33/32', 'titleFull': 'Materials of the light emitting region containing only elements of Group III and Group V of the Periodic Table containing nitrogen'}, {'symbol': 'H01M8/1246', 'titleFull': 'Fuel cells with solid electrolytes operating at high temperature, e.g. with stabilised ZrO2 electrolyte characterised by the process of manufacturing or by the material of the electrolyte the electrolyte consisting of oxides'}, {'symbol': 'H01M4/0419', 'titleFull': 'Methods of deposition of the material involving spraying'}, {'symbol': 'H01M8/1226', 'titleFull': 'Fuel cells with solid electrolytes operating at high temperature, e.g. with stabilised ZrO2 electrolyte characterised by the electrode/electrolyte combination or the supporting material characterised by the supporting layer'}, {'symbol': 'H01M4/9066', 'titleFull': 'Metals or alloys specially used in fuel cell operating at high temperature, e.g. SOFC of metal-ceramic composites or mixtures, e.g. cermets'}, {'symbol': 'H01M4/8885', 'titleFull': 'Sintering or firing'}, {'symbol': 'H01M4/9033', 'titleFull': 'Complex oxides, optionally doped, of the type M1MeO3, M1 being an alkaline earth metal or a rare earth, Me being a metal, e.g. perovskites'}, {'symbol': 'H01L33/00', 'titleFull': 'Semiconductor devices having potential barriers specially adapted for light emission; Processes or apparatus specially adapted for the manufacture or treatment thereof or of parts thereof; Details thereof'}, {'symbol': 'H01L33/0093', 'titleFull': 'Wafer bonding; Removal of the growth substrate'}]}

exec(code, env_args)
