code = """# Read the file path from the variable
import json

# The variable contains the file path, not the content
file_path = var_functions.query_db_8

print('File path:', file_path)

# Read the knowledge articles from the file
with open(file_path, 'r') as f:
    knowledge_articles = json.load(f)

print('Number of articles:', len(knowledge_articles))

# Look for articles that contain policy information about scalability issues
policy_articles = []
for article in knowledge_articles:
    article_id = article.get('id', '')
    title = article.get('title', '').lower()
    summary = article.get('summary', '').lower()
    faq = article.get('faq_answer__c', '').lower()
    
    # Check if this is a policy article about scalability
    # The case is about QuantumPCB Modeler and TechPulse Solutions
    if 'quantumpcb' in title or 'techpulse' in title:
        policy_articles.append(article)
    elif 'scalability' in title or 'scalability' in summary or 'scalability' in faq:
        if 'policy' in title or 'guideline' in title or 'standard' in title:
            policy_articles.append(article)

print('Policy articles found:', len(policy_articles))
print('__RESULT__:')
print(json.dumps(policy_articles))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': [{'id': '#500Wt00000DDyznIAD', 'priority': 'High', 'subject': 'Scalability Problems ', 'description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.', 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqoiZIAR', 'createddate': '2022-09-22T19:28:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt000007928FIAQ', 'issueid__c': 'a03Wt00000JqxtvIAB', 'accountid': '001Wt00000PGaZCIA1', 'ownerid': '005Wt000003NHsrIAG'}], 'var_functions.query_db:5': [], 'var_functions.query_db:6': [{'id': '#a03Wt00000JqxtvIAB', 'name': 'Scalability Issue', 'description__c': 'Some enterprises report difficulties in scaling TechPulse solutions to meet increasing demands, impacting their expansion efforts.'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [{'id': 'a04Wt00000535bOIAQ', 'caseid__c': '500Wt00000DDyznIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-09-22T19:28:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000537V8IAI', 'caseid__c': '500Wt00000DDyznIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHsrIAG', 'createddate': '2022-09-22T19:28:00.000+0000', 'field__c': 'Owner Assignment'}]}

exec(code, env_args)
