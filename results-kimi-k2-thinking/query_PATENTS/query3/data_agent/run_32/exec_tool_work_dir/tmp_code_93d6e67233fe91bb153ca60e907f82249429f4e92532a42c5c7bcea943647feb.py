code = """import json

# Read the sample data from the file
sample_data = locals()['var_functions.query_db:0'] if isinstance(locals()['var_functions.query_db:0'], list) else None

if sample_data and len(sample_data) > 0:
    print('Total records in sample:', len(sample_data))
    
    # Let's examine one record more closely
    record = sample_data[0]
    print('Keys in record:', list(record.keys()))
    
    # Check Patents_info format
    patents_info = record.get('Patents_info', '')
    print('Sample Patents_info:', patents_info[:200])
    
    # Check citation format
    citation = record.get('citation', '')
    if citation:
        try:
            citations_list = json.loads(citation)
            print('Number of citations:', len(citations_list))
            print('First citation:', citations_list[0])
        except:
            print('Citation is not valid JSON string, content:', citation[:200])
    
    # Check cpc format
    cpc = record.get('cpc', '')
    if cpc:
        print('Sample CPC (first 200 chars):', cpc[:200])
else:
    print('No valid sample data found')

# Need to check if we can find UNIV CALIFORNIA patents
print('Looking for UNIV CALIFORNIA patterns in the data...')"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
