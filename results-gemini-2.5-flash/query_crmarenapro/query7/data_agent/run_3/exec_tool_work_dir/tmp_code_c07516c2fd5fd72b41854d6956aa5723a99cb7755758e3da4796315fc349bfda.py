code = """import json
case_id = '500Wt00000DDyznIAD'.strip().lstrip('#')
print('__RESULT__:')
print(json.dumps(case_id))"""

env_args = {'var_function-call-2073270059983084263': [], 'var_function-call-11202807121430441742': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-7244823728580665106': []}

exec(code, env_args)
