code = """import json
import re

# Read the UNIV CALIFORNIA patents data
uc_patents = locals()['var_functions.query_db:28']

# Initialize data structures
uc_pub_numbers = []  # List of UNIV CALIFORNIA publication numbers
uc_cpc_map = {}      # Map publication number -> CPC codes

# Process each UC patent record
for record in uc_patents:
    patents_info = record.get('Patents_info', '')
    cpc_data = record.get('cpc', '')
    
    # Extract publication number from Patents_info
    # Look for patterns like "pub. number X" or "publication number X"
    pub_match = re.search(r'(?:pub\.|publication)\s+number\s+([A-Z]{2}-[^,\s-]+-[A-Z][0-9])', patents_info, re.IGNORECASE)
    if pub_match:
        pub_number = pub_match.group(1)
        uc_pub_numbers.append(pub_number)
        
        # Parse CPC codes
        cpc_codes = []
        if cpc_data:
            try:
                cpc_list = json.loads(cpc_data)
                # Get primary CPCs (inventive=true or first=true)
                for cpc_item in cpc_list:
                    if cpc_item.get('inventive') or cpc_item.get('first'):
                        cpc_codes.append(cpc_item.get('code'))
            except:
                pass
        uc_cpc_map[pub_number] = list(set(cpc_codes))  # Remove duplicates

result_summary = {
    'total_uc_patents': len(uc_pub_numbers),
    'sample_uc_patents': uc_pub_numbers[:5],
    'sample_cpc_mapping': {k: uc_cpc_map[k] for k in list(uc_cpc_map.keys())[:3]}
}

print('__RESULT__:')
print(json.dumps(result_summary))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:12': {'status': 'no_valid_data', 'summary': {}}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:18': [{'symbol': 'A01K2227/108', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'titleFull': 'Bovine'}, {'symbol': 'A01K2227/107', 'titleFull': 'Rabbit'}, {'symbol': 'A01K2227/103', 'titleFull': 'Ovine'}], 'var_functions.query_db:24': [{'cid': '0', 'name': 'Patents_info', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '1', 'name': 'kind_code', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'application_kind', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'pct_number', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '4', 'name': 'family_id', 'type': 'INTEGER', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '5', 'name': 'title_localized', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '6', 'name': 'abstract_localized', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '7', 'name': 'claims_localized_html', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '8', 'name': 'description_localized_html', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '9', 'name': 'publication_date', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '10', 'name': 'filing_date', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '11', 'name': 'grant_date', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '12', 'name': 'priority_date', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '13', 'name': 'priority_claim', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '14', 'name': 'inventor_harmonized', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '15', 'name': 'examiner', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '16', 'name': 'uspc', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '17', 'name': 'ipc', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '18', 'name': 'cpc', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '19', 'name': 'citation', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '20', 'name': 'parent', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '21', 'name': 'child', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '22', 'name': 'entity_status', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '23', 'name': 'art_unit', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
