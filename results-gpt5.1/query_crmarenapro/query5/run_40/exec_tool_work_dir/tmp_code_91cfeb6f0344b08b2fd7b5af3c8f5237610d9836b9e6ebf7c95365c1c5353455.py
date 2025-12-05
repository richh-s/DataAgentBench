code = """import pandas as pd, json

df = pd.DataFrame(var_call_YmGVd0zSSzDARnv17Sg6cmEt)
most_common = df['issueid__c'].value_counts().idxmax()

result = json.dumps(most_common)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_3OUHjcZwD7R4tZb23L0Lr50w': [], 'var_call_So6amIwSYKRegZCDjaENgHfc': [], 'var_call_YmGVd0zSSzDARnv17Sg6cmEt': [{'issueid__c': 'a03Wt00000JqmX6IAJ'}, {'issueid__c': 'a03Wt00000JqzR3IAJ'}, {'issueid__c': 'a03Wt00000JqxVjIAJ'}, {'issueid__c': 'a03Wt00000JqzUHIAZ'}, {'issueid__c': 'a03Wt00000JqnHwIAJ'}, {'issueid__c': 'a03Wt00000JqzR3IAJ'}, {'issueid__c': 'a03Wt00000JqzSfIAJ'}, {'issueid__c': 'a03Wt00000JqzR3IAJ'}, {'issueid__c': 'a03Wt00000JqnHwIAJ'}, {'issueid__c': 'a03Wt00000JqzUHIAZ'}, {'issueid__c': 'a03Wt00000JqzUHIAZ'}, {'issueid__c': 'a03Wt00000JqzUHIAZ'}, {'issueid__c': 'a03Wt00000JqnHwIAJ'}, {'issueid__c': 'a03Wt00000JqzSfIAJ'}, {'issueid__c': 'a03Wt00000JqnHwIAJ'}, {'issueid__c': 'a03Wt00000JqmX6IAJ'}, {'issueid__c': 'a03Wt00000JqxVjIAJ'}, {'issueid__c': 'a03Wt00000JqzR3IAJ'}, {'issueid__c': 'a03Wt00000JqmX6IAJ'}, {'issueid__c': 'a03Wt00000JqzR3IAJ'}, {'issueid__c': 'a03Wt00000JqzUHIAZ'}, {'issueid__c': 'a03Wt00000JqmX6IAJ'}]}

exec(code, env_args)
