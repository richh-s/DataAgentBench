code = """import json

# Read the sample data
sample_data = locals()['var_functions.query_db:0']

result_text = ""

if isinstance(sample_data, list) and len(sample_data) > 0:
    result_text += 'Total records in sample: ' + str(len(sample_data)) + '\n'
    
    # Let's examine one record
    record = sample_data[0]
    result_text += 'Keys in record: ' + str(list(record.keys())) + '\n'
    
    # Check Patents_info format
    patents_info = record.get('Patents_info', '')
    result_text += 'Sample Patents_info: ' + patents_info[:200] + '\n'
    
    # Check citation format
    citation = record.get('citation', '')
    if citation:
        try:
            citations_list = json.loads(citation)
            result_text += 'Number of citations: ' + str(len(citations_list)) + '\n'
            result_text += 'First citation: ' + str(citations_list[0]) + '\n'
        except:
            result_text += 'Citation is not valid JSON string, content: ' + citation[:200] + '\n'
    
    # Check cpc format
    cpc = record.get('cpc', '')
    if cpc:
        result_text += 'Sample CPC (first 200 chars): ' + cpc[:200] + '\n'
else:
    result_text += 'No valid sample data found\n'

# Search for UNIV CALIFORNIA in the data
if isinstance(sample_data, list):
    uc_count = 0
    for rec in sample_data:
        patents_info = rec.get('Patents_info', '')
        if 'UNIV CALIFORNIA' in patents_info.upper():
            uc_count += 1
            if uc_count <= 2:
                result_text += 'Found UC patent: ' + patents_info[:150] + '\n'
    
    result_text += 'Total UNIV CALIFORNIA patents found in sample: ' + str(uc_count) + '\n'

print('__RESULT__:')
print(result_text)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
