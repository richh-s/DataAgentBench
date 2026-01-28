code = """import json

# Read the sample data
sample_data = locals()['var_functions.query_db:0']

result_text = []

if isinstance(sample_data, list) and len(sample_data) > 0:
    result_text.append('Total records in sample: ' + str(len(sample_data)))
    
    # Let's examine one record
    record = sample_data[0]
    result_text.append('Keys in record: ' + str(list(record.keys())))
    
    # Check Patents_info format
    patents_info = record.get('Patents_info', '')
    result_text.append('Sample Patents_info: ' + patents_info[:200])
    
    # Check citation format
    citation = record.get('citation', '')
    if citation:
        try:
            citations_list = json.loads(citation)
            result_text.append('Number of citations: ' + str(len(citations_list)))
            result_text.append('First citation: ' + str(citations_list[0]))
        except:
            result_text.append('Citation is not valid JSON string, content: ' + citation[:200])
    
    # Check cpc format
    cpc = record.get('cpc', '')
    if cpc:
        result_text.append('Sample CPC (first 200 chars): ' + cpc[:200])
else:
    result_text.append('No valid sample data found')

# Search for UNIV CALIFORNIA in the data
if isinstance(sample_data, list):
    uc_count = 0
    for rec in sample_data:
        patents_info = rec.get('Patents_info', '')
        if 'UNIV CALIFORNIA' in patents_info.upper():
            uc_count += 1
            if uc_count <= 2:
                result_text.append('Found UC patent: ' + patents_info[:150])
    
    result_text.append('Total UNIV CALIFORNIA patents found in sample: ' + str(uc_count))

final_result = '\\n'.join(result_text)
print('__RESULT__:')
print(final_result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
