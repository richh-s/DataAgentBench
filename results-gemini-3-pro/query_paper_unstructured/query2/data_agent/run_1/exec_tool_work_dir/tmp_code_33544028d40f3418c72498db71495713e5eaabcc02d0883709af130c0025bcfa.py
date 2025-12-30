code = """import json

with open(locals()['var_function-call-3176844419962824888'], 'r') as f:
    paper_docs = json.load(f)

doc_titles = [d['filename'].replace('.txt', '') for d in paper_docs]

print("__RESULT__:")
print(json.dumps(doc_titles))"""

env_args = {'var_function-call-1269001259179698706': 'file_storage/function-call-1269001259179698706.json', 'var_function-call-1269001259179697405': 'file_storage/function-call-1269001259179697405.json', 'var_function-call-10709454489142440522': 68.5, 'var_function-call-910537287014842228': {'total_matched_papers_2018': 2, 'acm_count': 2, 'ieee_count': 1, 'pubmed_count': 0, 'acm_and_ieee_overlap': 1}, 'var_function-call-3176844419962824888': 'file_storage/function-call-3176844419962824888.json', 'var_function-call-12679360961776693881': [{'title': 'A Lived Informatics Model of Personal Informatics', 'citations': '50', 'is_acm': True, 'is_ieee': False}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'citations': '87', 'is_acm': True, 'is_ieee': True}], 'var_function-call-4888063600565384953': {'acm_context': '; \nstroke rehabilitation; occupational therapy  \n\nACM Classification Keywords \nH.5.m. Information in', 'ieee_context': 'Monitoring Arm \nActivity in Daily Life. Conf Proc IEEE Eng Med Biol Soc \n2011 (2011), 5219-5223. \nht'}}

exec(code, env_args)
