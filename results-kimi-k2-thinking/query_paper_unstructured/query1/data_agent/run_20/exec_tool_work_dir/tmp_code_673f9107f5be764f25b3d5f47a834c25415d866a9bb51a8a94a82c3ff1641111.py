code = """# Debug: Check what data we have available
print('Checking available variables...')
print('Keys in locals():')
for key in sorted(locals().keys()):
    if 'var_functions' in key:
        value = locals()[key]
        print(f'  {key}: type={type(value)}, value={str(value)[:100]}...' if len(str(value)) > 100 else f'  {key}: type={type(value)}, value={value}')

# Try to access the data directly
citations_file = None
papers_file = None

citations_result = locals().get('var_functions.query_db:10')
if citations_result and isinstance(citations_result, str) and citations_result.endswith('.json'):
    citations_file = citations_result
    print(f'citations_file path: {citations_file}')

papers_result = locals().get('var_functions.query_db:16')
if papers_result and isinstance(papers_result, str) and papers_result.endswith('.json'):
    papers_file = papers_result
    print(f'papers_file path: {papers_file}')

print('__RESULT__:')
print('{"status": "debug_complete"}')"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}, {'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}, {'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt'}], 'var_functions.list_db:14': ['paper_docs'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'total_food_papers': 4, 'papers_with_citations': 4, 'total_citation_count': 1328, 'top_papers': [['ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 452], ['A Lived Informatics Model of Personal Informatics', 390], ['A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 266], ['A Stage-based Model of Personal Informatics Systems', 220]]}, 'var_functions.execute_python:22': {'total_food_domain_papers_identified': 0, 'papers_with_citation_data': 0, 'total_citation_count': 0, 'papers': []}, 'var_functions.execute_python:26': {'total_food_papers': 0, 'papers_with_data': 0, 'total_citations': 0, 'papers': []}}

exec(code, env_args)
