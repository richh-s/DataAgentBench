code = """import json
import pandas as pd

file_path = locals()['var_function-call-12685685015457983339']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

search_terms = ['scaling difficulties', 'scalability problems', 'scaling challenge', 'scaling issue']

def check_relevance(row):
    for term in search_terms:
        if term in row['title'].lower() or term in row['faq_answer__c'].lower():
            return True
    return False

relevant_articles = df[df.apply(check_relevance, axis=1)]

if not relevant_articles.empty:
    # Assuming the first match is the most relevant, or we can add more sophisticated ranking
    result = relevant_articles.iloc[0][['id', 'title', 'faq_answer__c']].to_json(orient='records')
else:
    result = json.dumps(None)

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-1928789070847852941': [], 'var_function-call-12436842912767578103': [{'id': '#500Wt00000DDyznIAD', 'priority': 'High', 'subject': 'Scalability Problems ', 'description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.', 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqoiZIAR', 'createddate': '2022-09-22T19:28:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt000007928FIAQ', 'issueid__c': 'a03Wt00000JqxtvIAB', 'accountid': '001Wt00000PGaZCIA1', 'ownerid': '005Wt000003NHsrIAG'}], 'var_function-call-7341267426994831286': [], 'var_function-call-2629957437164010637': [{'description__c': 'Some enterprises report difficulties in scaling TechPulse solutions to meet increasing demands, impacting their expansion efforts.'}], 'var_function-call-4212715702665089855': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-1094773854009040808': [], 'var_function-call-11076342450927315059': [], 'var_function-call-9582924360432193238': [], 'var_function-call-12685685015457983339': 'file_storage/function-call-12685685015457983339.json'}

exec(code, env_args)
