code = """import json
# Use the query result variable
var = var_call_oZ9g100G3Sed0aSBZvfongPz
# Extract owner id
ownerid = None
if isinstance(var, list) and len(var) > 0:
    ownerid = var[0].get('ownerid')
# Prepare output as JSON string
output = json.dumps({'agent_id': ownerid})
print('__RESULT__:')
print(output)"""

env_args = {'var_call_lSJN7v8gxV10ZGwTh8gkpl8y': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_6yd5Mz6soMtcoS37JX6edGxK': [{'field__c': 'Owner Assignment'}, {'field__c': 'Case Closed'}, {'field__c': 'Case Creation'}], 'var_call_PhksEy9fOQMRBdZ7ShcifstX': 'file_storage/call_PhksEy9fOQMRBdZ7ShcifstX.json', 'var_call_oZ9g100G3Sed0aSBZvfongPz': [{'ownerid': '005Wt000003NDqDIAW'}]}

exec(code, env_args)
