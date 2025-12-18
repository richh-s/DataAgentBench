code = """import json
import pandas as pd

# The result from query_db is a list containing a string that includes the JSON array.
# We need to extract the actual JSON string from this.
raw_query_db_output = locals()['var_function-call-320778320624203021']['results'][0]

# Find the index of the first '[' and the last ']' to extract the JSON array string
json_start_index = raw_query_db_output.find('[')
json_end_index = raw_query_db_output.rfind(']')

case_description = ""
if json_start_index != -1 and json_end_index != -1 and json_end_index > json_start_index:
    json_array_str = raw_query_db_output[json_start_index : json_end_index + 1]
    try:
        parsed_case_data = json.loads(json_array_str)
        if isinstance(parsed_case_data, list) and len(parsed_case_data) > 0:
            case_description = parsed_case_data[0].get('description', '')
    except json.JSONDecodeError:
        # If parsing fails, case_description remains empty
        pass

# Load knowledge articles from the file
with open(locals()['var_function-call-8042687875836338952'], 'r') as f:
    knowledge_articles = json.load(f)

breached_article_id = None
for article in knowledge_articles:
    # Check for keywords in case description and knowledge article details
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
