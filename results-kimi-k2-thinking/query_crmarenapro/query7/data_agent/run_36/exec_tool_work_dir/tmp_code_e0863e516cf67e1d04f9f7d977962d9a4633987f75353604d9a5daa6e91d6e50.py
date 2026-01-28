code = """import json

# Case data from query_db:2
case_data = [{"id": "#500Wt00000DDyznIAD", "priority": "High", "subject": "Scalability Problems ", "description": "I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.", "status": "Waiting on Customer", "contactid": "003Wt00000JqoiZIAR", "createddate": "2022-09-22T19:28:00.000+0000", "closeddate": "None", "orderitemid__c": "802Wt000007928FIAQ", "issueid__c": "a03Wt00000JqxtvIAB", "accountid": "001Wt00000PGaZCIA1", "ownerid": "005Wt000003NHsrIAG"}]

# Issue data from query_db:10
issue_data = [{"id": "#a03Wt00000JqxtvIAB", "name": "Scalability Issue", "description__c": "Some enterprises report difficulties in scaling TechPulse solutions to meet increasing demands, impacting their expansion efforts."}]

# Case history from query_db:5
casehistory_data = [{"id": "a04Wt00000535bOIAQ", "caseid__c": "500Wt00000DDyznIAD", "oldvalue__c": "None", "newvalue__c": "None", "createddate": "2022-09-22T19:28:00.000+0000", "field__c": "Case Creation"}, {"id": "a04Wt00000537V8IAI", "caseid__c": "500Wt00000DDyznIAD", "oldvalue__c": "None", "newvalue__c": "005Wt000003NHsrIAG", "createddate": "2022-09-22T19:28:00.000+0000", "field__c": "Owner Assignment"}]

print("Case ID:", case_data[0]['id'])
print("Case Subject:", case_data[0]['subject'].strip())
print("Issue:", issue_data[0]['name'])
print("Issue Description:", issue_data[0]['description__c'])
print("\nCase history shows:")
for entry in casehistory_data:
    print(f"- {entry['field__c']}: {entry['createddate']}")

# The question asks: "Did the agent breach the policy, and if so, which knowledge article was breached?"
# Based on the available data:
# 1. The case is about scalability problems with QuantumPCB Modeler
# 2. The issue is "Scalability Issue" affecting TechPulse solutions
# 3. The case history shows it was created and assigned
# 4. There's no evidence of an agent action that would be a policy violation

# Looking at the knowledge articles found:
# - Scalability articles talk about competitors' scalability limitations
# - Quantum articles talk positively about QuantumPCB Modeler
# - Policy articles talk about SLA and support policies

# There's no indication that the agent breached any policy.
# The agent appears to have simply created and assigned the case normally.

result = None  # No policy violation found

# Print result in required format
print('\n__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': [{'id': '#500Wt00000DDyznIAD', 'priority': 'High', 'subject': 'Scalability Problems ', 'description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.', 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqoiZIAR', 'createddate': '2022-09-22T19:28:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt000007928FIAQ', 'issueid__c': 'a03Wt00000JqxtvIAB', 'accountid': '001Wt00000PGaZCIA1', 'ownerid': '005Wt000003NHsrIAG'}], 'var_functions.query_db:5': [{'id': 'a04Wt00000535bOIAQ', 'caseid__c': '500Wt00000DDyznIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-09-22T19:28:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000537V8IAI', 'caseid__c': '500Wt00000DDyznIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHsrIAG', 'createddate': '2022-09-22T19:28:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_functions.query_db:6': [], 'var_functions.query_db:10': [{'id': '#a03Wt00000JqxtvIAB', 'name': 'Scalability Issue', 'description__c': 'Some enterprises report difficulties in scaling TechPulse solutions to meet increasing demands, impacting their expansion efforts.'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
