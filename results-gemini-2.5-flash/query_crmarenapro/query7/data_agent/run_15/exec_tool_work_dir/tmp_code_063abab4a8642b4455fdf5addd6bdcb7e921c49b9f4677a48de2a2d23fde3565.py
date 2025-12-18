code = """import json
import pandas as pd

case_description = locals()['var_function-call-5897297069914496341'][0]['description']
knowledge_articles_path = locals()['var_function-call-9073989045128889236']

with open(knowledge_articles_path, 'r') as f:
    knowledge_articles = json.load(f)

breached_article_id = None
keywords_from_case = ["QuantumPCB Modeler", "GreenStar Electronics"]
policy_breach_keywords = ["breach", "policy", "violation"]

for article in knowledge_articles:
    content = (article.get('title', '') + ' ' +
               article.get('faq_answer__c', '') + ' ' +
               article.get('summary', '')).lower()

    # Check for direct mention of case details AND policy breach keywords
    case_detail_match = any(keyword.lower() in content for keyword in keywords_from_case)
    policy_breach_match = any(keyword.lower() in content for keyword in policy_breach_keywords)

    if case_detail_match and policy_breach_match:
        breached_article_id = article.get('id')
        break
    elif case_detail_match: # If no direct policy breach mention, but case details are in competitor article, it could be a clue.
        if "quantum circuits inc" in content and "competitor" in article.get('title', '').lower():
            # This article is about a competitor "Quantum Circuits Inc" and the case mentions "QuantumPCB Modeler".
            # The context implies a potential policy breach related to a competitor.
            breached_article_id = article.get('id')
            break

print("__RESULT__:")
print(json.dumps(breached_article_id))"""

env_args = {'var_function-call-6634253311432304931': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-9318803101170084187': [], 'var_function-call-5897297069914496341': [{'id': '#500Wt00000DDyznIAD', 'description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.'}], 'var_function-call-9073989045128889236': 'file_storage/function-call-9073989045128889236.json'}

exec(code, env_args)
