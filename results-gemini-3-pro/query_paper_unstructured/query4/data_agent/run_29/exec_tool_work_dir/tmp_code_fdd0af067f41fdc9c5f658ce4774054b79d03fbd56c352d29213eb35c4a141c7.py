code = """import json

with open(locals()['var_function-call-4420579621073480200'], 'r') as f:
    papers = json.load(f)

print("Number of papers passing Mongo filter:", len(papers))

debug_data = []
for i, p in enumerate(papers[:5]):
    info = {}
    info['filename'] = p['filename']
    info['header_snippet'] = p.get('text', '')[:500]
    debug_data.append(info)

print("__RESULT__:")
print(json.dumps(debug_data))"""

env_args = {'var_function-call-524279506149407119': ['paper_docs'], 'var_function-call-524279506149405588': 'file_storage/function-call-524279506149405588.json', 'var_function-call-524279506149408153': ['Citations', 'sqlite_sequence'], 'var_function-call-524279506149406622': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-9551284447428774224': [{'count(*)': '1405'}], 'var_function-call-9551284447428775563': 'file_storage/function-call-9551284447428775563.json', 'var_function-call-4736821834278124027': 'file_storage/function-call-4736821834278124027.json', 'var_function-call-1276767600603300389': [], 'var_function-call-8853061178265091948': 'debug_done', 'var_function-call-17995316611090094079': {'total_papers': 5, 'total_citations': 1405, 'pa_count': 4, 'year_2016_count': 0, 'match_count': 0, 'sample_matches': [], 'sample_citation_titles': ['Shifting Dynamics or Breaking Sacred Traditions?: The Role of Technology in Twelve-step Fellowships', 'How to Drive a London Bus: Measuring Performance in a Mobile and Remote Workplace', 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'Quantifying the Body and Caring for the Mind: Self-Tracking in Multiple Sclerosis', 'Rotating Online Behavior Change Interventions Increases Effectiveness But Also Increases Attrition'], 'test_title_in_citations': False}, 'var_function-call-4420579621073480200': 'file_storage/function-call-4420579621073480200.json', 'var_function-call-4810167469021822824': []}

exec(code, env_args)
