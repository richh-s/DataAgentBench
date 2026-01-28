code = """import json

# Read the sample data
sample_data = locals()['var_functions.query_db:0']

result_dict = {"status": "completed", "summary": {}}

if isinstance(sample_data, list) and len(sample_data) > 0:
    result_dict["summary"]["total_records"] = len(sample_data)
    
    # Let's examine one record
    record = sample_data[0]
    result_dict["sample_record_keys"] = list(record.keys())
    
    # Extract Patents_info
    patents_info = record.get('Patents_info', '')
    result_dict["sample_patents_info"] = patents_info[:200]
    
    # Process citation
    citation = record.get('citation', '')
    if citation:
        try:
            citations_list = json.loads(citation)
            result_dict["sample_citation_count"] = len(citations_list)
            result_dict["sample_first_citation"] = citations_list[0]
        except:
            result_dict["citation_parse_error"] = citation[:200]
    
    # Process cpc
    cpc = record.get('cpc', '')
    if cpc:
        result_dict["sample_cpc_preview"] = cpc[:200]
        
    # Search for UNIV CALIFORNIA in the sample
    uc_count = 0
    for rec in sample_data:
        patents_info = rec.get('Patents_info', '')
        if 'UNIV CALIFORNIA' in patents_info.upper():
            uc_count += 1
    
    result_dict["summary"]["uc_patents_in_sample"] = uc_count
else:
    result_dict["status"] = "no_valid_data"

print('__RESULT__:')
print(json.dumps(result_dict))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
