code = """import json

# Access the stored file path variables using locals()
file_path = locals().get('var_functions.query_db:14')

with open(file_path, 'r') as f:
    knowledge_articles = json.load(f)

# Case details from previous queries
case_description = "I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics."
case_subject = "Scalability Problems "
issue_name = "Scalability Issue"
issue_description = "Some enterprises report difficulties in scaling TechPulse solutions to meet increasing demands, impacting their expansion efforts."

# Search for relevant knowledge articles
search_terms = ['quantumpcb', 'greenstar', 'scalability', 'performance', 'limitation', 'known issue', 'support policy', 'agent policy']

relevant_articles = []

for article in knowledge_articles:
    article_id = article.get('id', '')
    title = article.get('title', '').lower()
    summary = article.get('summary', '').lower()
    faq = article.get('faq_answer__c', '').lower()
    
    content = title + ' ' + summary + ' ' + faq
    
    # Check if any search term appears in the article
    for term in search_terms:
        if term in content:
            relevant_articles.append({
                'id': article_id,
                'title': article.get('title', ''),
                'term': term
            })
            break

print('Found', len(relevant_articles), 'potentially relevant articles')
for article in relevant_articles:
    print(f"ID: {article['id']}, Title: {article['title']}, Matched term: {article['term']}")"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': [{'id': '#500Wt00000DDyznIAD', 'priority': 'High', 'subject': 'Scalability Problems ', 'description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.', 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqoiZIAR', 'createddate': '2022-09-22T19:28:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt000007928FIAQ', 'issueid__c': 'a03Wt00000JqxtvIAB', 'accountid': '001Wt00000PGaZCIA1', 'ownerid': '005Wt000003NHsrIAG'}], 'var_functions.query_db:4': [], 'var_functions.query_db:6': [{'id': '#a03Wt00000JqxtvIAB', 'name': 'Scalability Issue', 'description__c': 'Some enterprises report difficulties in scaling TechPulse solutions to meet increasing demands, impacting their expansion efforts.'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
