code = """import json
import pandas as pd

raw_query_db_output = locals()['var_function-call-320778320624203021']['results'][0]

# Define the marker string to split by. Using a triple-double-quoted string for multi-line literal.
marker = """
The result is:
"""

# Split the raw output by the marker
parts = raw_query_db_output.split(marker)

case_description = None # Initialize as None
if len(parts) > 1:
    # The second part of the split result should be the JSON string
    json_str_raw = parts[1]
    json_str = json_str_raw.strip() # Remove any leading/trailing whitespace, including newlines
    try:
        parsed_case_data = json.loads(json_str)
        if isinstance(parsed_case_data, list) and len(parsed_case_data) > 0 and isinstance(parsed_case_data[0], dict):
            case_description = parsed_case_data[0].get('description', None)
    except json.JSONDecodeError:
        # If JSON parsing fails, case_description remains None
        case_description = None

if case_description is None:
    # If case_description could not be extracted, return None
    print('__RESULT__:')
    print(json.dumps(None))
else:
    # Load knowledge articles from the file
    with open(locals()['var_function-call-8042687875836338952'], 'r') as f:
        knowledge_articles = json.load(f)

    breached_article_id = None
    for article in knowledge_articles:
        # Check for keywords in case description and knowledge article details
        # Looking for 'QuantumPCB Modeler' in case description.
        # Looking for 'Quantum Circuits Inc' in article title, faq_answer__c, or summary.
        # Looking for 'limited customizability and flexibility' in article faq_answer__c or summary.
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
