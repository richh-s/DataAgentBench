code = """import json
import pandas as pd
import re

# Access the full tool output dictionary
tool_output_dict = locals()['var_function-call-320778320624203021']

# Navigate to the list of results which is nested under 'query_db_response' and then 'results'
results_list = tool_output_dict['query_db_response']['results']

# Get the first (and likely only) element of this list, which is the verbose string.
raw_verbose_string = results_list[0]

# Use regex to extract the actual JSON array string from the verbose output.
# This pattern looks for a string that starts with '[' and ends with ']',
# allowing for any characters (including newlines) in between, in a non-greedy way.
json_match = re.search(r'\[.*?\]', raw_verbose_string, re.DOTALL)

case_description = None
if json_match:
    json_array_str = json_match.group(0)
    try:
        # Attempt to load the extracted string as JSON. This should yield a list of dictionaries.
        parsed_case_data = json.loads(json_array_str)
        # Verify that the parsed data is a list, not empty, and its first element is a dictionary
        if isinstance(parsed_case_data, list) and len(parsed_case_data) > 0 and isinstance(parsed_case_data[0], dict):
            case_description = parsed_case_data[0].get('description', None)
    except json.JSONDecodeError:
        # If JSON parsing fails, case_description remains None
        pass

if case_description is None:
    # If case_description could not be extracted or was not found, return None as the final answer.
    print('__RESULT__:')
    print(json.dumps(None))
else:
    # If case_description was successfully extracted, proceed to load and search knowledge articles.
    # The knowledge articles are stored in a .json file, so we open and load it.
    with open(locals()['var_function-call-8042687875836338952'], 'r') as f:
        knowledge_articles = json.load(f)

    breached_article_id = None
    for article in knowledge_articles:
        # Check for keywords in case description and knowledge article details.
        # The policy breach criteria are:
        # 1. 'QuantumPCB Modeler' must be present in the case description.
        # 2. 'Quantum Circuits Inc' must be present in the article's title, faq_answer__c, or summary.
        # 3. 'limited customizability and flexibility' must be present in the article's faq_answer__c or summary.
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
