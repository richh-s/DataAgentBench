code = """# Let's analyze the knowledge articles we found
import json

# Read the knowledge articles from the file
with open('var_functions.query_db:8', 'r') as f:
    knowledge_articles = json.load(f)

# Filter articles that mention scalability issues with TechPulse or QuantumPCB
relevant_articles = []
for article in knowledge_articles:
    title = article.get('title', '').lower()
    summary = article.get('summary', '').lower()
    faq = article.get('faq_answer__c', '').lower()
    
    # Check for TechPulse, QuantumPCB, or direct scalability policy content
    if 'techpulse' in title or 'techpulse' in summary or 'techpulse' in faq:
        relevant_articles.append(article)
    elif 'quantumpcb' in title or 'quantumpcb' in summary or 'quantumpcb' in faq:
        relevant_articles.append(article)
    elif 'scalability' in title and ('policy' in title or 'guideline' in title):
        relevant_articles.append(article)

print('__RESULT__:')
print(json.dumps(relevant_articles, indent=2))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': [{'id': '#500Wt00000DDyznIAD', 'priority': 'High', 'subject': 'Scalability Problems ', 'description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.', 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqoiZIAR', 'createddate': '2022-09-22T19:28:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt000007928FIAQ', 'issueid__c': 'a03Wt00000JqxtvIAB', 'accountid': '001Wt00000PGaZCIA1', 'ownerid': '005Wt000003NHsrIAG'}], 'var_functions.query_db:5': [], 'var_functions.query_db:6': [{'id': '#a03Wt00000JqxtvIAB', 'name': 'Scalability Issue', 'description__c': 'Some enterprises report difficulties in scaling TechPulse solutions to meet increasing demands, impacting their expansion efforts.'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [{'id': 'a04Wt00000535bOIAQ', 'caseid__c': '500Wt00000DDyznIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-09-22T19:28:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000537V8IAI', 'caseid__c': '500Wt00000DDyznIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHsrIAG', 'createddate': '2022-09-22T19:28:00.000+0000', 'field__c': 'Owner Assignment'}]}

exec(code, env_args)
