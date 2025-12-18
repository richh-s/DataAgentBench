code = """import json
import re

def clean_id(id_string):
    if isinstance(id_string, str):
        return re.sub(r'[^a-zA-Z0-9]', '', id_string).strip()
    return id_string

case_id_raw = '500Wt00000DDyznIAD'
cleaned_case_id = clean_id(case_id_raw)

print("__RESULT__:")
print(json.dumps(cleaned_case_id))"""

env_args = {'var_function-call-18214309435432692573': [{'id': 'a04Wt00000535bOIAQ', 'caseid__c': '500Wt00000DDyznIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-09-22T19:28:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000537V8IAI', 'caseid__c': '500Wt00000DDyznIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHsrIAG', 'createddate': '2022-09-22T19:28:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-7475233764344279768': [], 'var_function-call-860935569949030968': '500Wt00000DDyznIAD', 'var_function-call-5069269706846381137': []}

exec(code, env_args)
