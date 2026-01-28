code = """import json

with open(locals()['var_function-call-3176844419962824888'], 'r') as f:
    paper_docs = json.load(f)

for doc in paper_docs:
    if "ArmSleeve" in doc['filename']:
        text = doc['text']
        # Find ACM context
        acm_index = text.find("ACM")
        acm_context = text[max(0, acm_index-50):min(len(text), acm_index+50)]
        
        # Find IEEE context
        ieee_index = text.find("IEEE")
        ieee_context = text[max(0, ieee_index-50):min(len(text), ieee_index+50)]
        
        print("__RESULT__:")
        print(json.dumps({
            "acm_context": acm_context,
            "ieee_context": ieee_context
        }))
        break"""

env_args = {'var_function-call-1269001259179698706': 'file_storage/function-call-1269001259179698706.json', 'var_function-call-1269001259179697405': 'file_storage/function-call-1269001259179697405.json', 'var_function-call-10709454489142440522': 68.5, 'var_function-call-910537287014842228': {'total_matched_papers_2018': 2, 'acm_count': 2, 'ieee_count': 1, 'pubmed_count': 0, 'acm_and_ieee_overlap': 1}, 'var_function-call-3176844419962824888': 'file_storage/function-call-3176844419962824888.json', 'var_function-call-12679360961776693881': [{'title': 'A Lived Informatics Model of Personal Informatics', 'citations': '50', 'is_acm': True, 'is_ieee': False}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'citations': '87', 'is_acm': True, 'is_ieee': True}]}

exec(code, env_args)
