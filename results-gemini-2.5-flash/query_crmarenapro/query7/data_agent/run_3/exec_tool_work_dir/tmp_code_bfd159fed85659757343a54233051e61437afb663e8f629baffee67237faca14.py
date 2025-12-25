code = """import json
with open(locals()['var_function-call-7637593657589422599'], 'r') as f:
    knowledge_articles = json.load(f)

case_description = "I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics."
breached_article_id = None

for article in knowledge_articles:
    if "scaling" in article['faq_answer__c'].lower() or "scalability" in article['faq_answer__c'].lower():
        breached_article_id = article['id']
        break

print('__RESULT__:')
print(json.dumps(breached_article_id))"""

env_args = {'var_function-call-2073270059983084263': [], 'var_function-call-11202807121430441742': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-7244823728580665106': [], 'var_function-call-18025898237761527515': '500Wt00000DDyznIAD', 'var_function-call-9033883074268865945': [{'description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.', 'subject': 'Scalability Problems '}], 'var_function-call-7637593657589422599': 'file_storage/function-call-7637593657589422599.json'}

exec(code, env_args)
