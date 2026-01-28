code = """import json

# Manually list the park-related projects that were completed in 2022
# From analyzing the civic documents

projects_completed_2022 = [
    {
        "name": "Bluffs Park Shade Structure",
        "amount": 21000,
        "funding_name": "Bluffs Park Shade Structure"
    },
    {
        "name": "Point Dume Walkway Repairs", 
        "amount": 0,  # Will look up
        "funding_name": "Point Dume Walkway Repairs"
    }
]

print('__RESULT__:')
print(json.dumps(projects_completed_2022))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.list_db:4', 'var_functions.query_db:6', '__builtins__', 'json'], 'var_functions.execute_python:14': {'civic_docs_count': 5, 'funding_records_count': 500, 'civic_sample_keys': ['_id', 'filename', 'text'], 'funding_sample': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}, 'var_functions.execute_python:36': {'civic_type': "<class 'str'>", 'funding_type': "<class 'str'>", 'civic_is_file': True, 'funding_is_file': True}, 'var_functions.execute_python:44': {'civic_docs_count': 5, 'funding_records_count': 500, 'sample_text': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current and\nupcoming Capital Improvement Projects and Disaster Recovery Projects.\n\nDISCUSSION: Staff will provide a status update on the following active projects in the\nFiscal Year 2022-2023 Capital Improvement Program:\n\nCapital Improvement Projects (Design)\n\n2022 Morning View Resurfacing & Storm Drain Improvements\n\n(cid:190) Updates:\n\n(cid:131) Staff is working with the consultant to finalize the design plans for this\n\nproject and will submit to the County for review.\n\n(cid:190) Project Schedule:\n\n(cid:'}, 'var_functions.query_db:72': 'file_storage/functions.query_db:72.json', 'var_functions.query_db:76': 'file_storage/functions.query_db:76.json'}

exec(code, env_args)
