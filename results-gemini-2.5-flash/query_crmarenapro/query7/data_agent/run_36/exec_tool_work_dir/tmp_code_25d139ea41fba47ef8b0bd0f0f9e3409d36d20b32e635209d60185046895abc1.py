code = """import json
import pandas as pd
import re

# Get the raw string output from the previous query_db call
raw_query_db_output = locals()['var_function-call-320778320624203021']['results'][0]

# Extract the JSON array string using regex
json_str_match = re.search(r'\[\{.*\}\]', raw_query_db_output, re.DOTALL)

case_description = ""
if json_str_match:
    case_data_json_str = json_str_match.group(0)
    parsed_case_data = json.loads(case_data_json_str)
    if parsed_case_data:
        case_description = parsed_case_data[0].get('description', '')

# Load knowledge articles from the file
with open(locals()['var_function-call-8042687875836338952'], 'r') as f:
    knowledge_articles = json.load(f)

breached_article_id = None
for article in knowledge_articles:
    if ('QuantumPCB Modeler' in case_description) and \
       (('Quantum Circuits Inc' in article.get('title', '')) or \
        ('Quantum Circuits Inc' in article.get('faq_answer__c', '')) or \
        ('Quantum Circuits Inc' in article.get('summary', ''))) and \
       (('limited customizability and flexibility' in article.get('faq_answer__c', '')) or \
        ('limited customizability and flexibility' in article.get('summary', ''))):
        breached_article_id = article['id']
        break

print('__RESULT__:')
print(json.dumps(breached_article_id))"""

env_args = {'var_function-call-10061720471241958043': [], 'var_function-call-320778320624203021': [{'id': '#500Wt00000DDyznIAD', 'description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.'}], 'var_function-call-8042687875836338952': 'file_storage/function-call-8042687875836338952.json'}

exec(code, env_args)
