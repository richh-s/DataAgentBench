code = """import json
import pandas as pd

# Access the raw string result from the previous query_db call.
raw_case_data_string = locals()['var_function-call-2901270610269859347']['query_db_response']['results'][0]

# Extract the JSON part from the string by finding the known prefix.
json_prefix = "The result is:\n"
json_start_index = raw_case_data_string.find(json_prefix)

case_details = {}
if json_start_index != -1:
    # Slice the string to get only the potential JSON part, then strip any leading/trailing whitespace.
    json_string_potential = raw_case_data_string[json_start_index + len(json_prefix):].strip()
    try:
        case_details_list = json.loads(json_string_potential)
        if case_details_list:
            case_details = case_details_list[0]
    except json.JSONDecodeError:
        case_details = {} # Fallback if JSON parsing fails

case_description = case_details.get('description', '').lower()
case_subject = case_details.get('subject', '').lower()

# Load knowledge articles from the stored file
knowledge_articles = []
file_path = locals()['var_function-call-10763788185040264350']
with open(file_path, 'r') as f:
    knowledge_articles = json.load(f)

breached_article_id = None

for article in knowledge_articles:
    title = article.get('title', '').lower()
    faq_answer = article.get('faq_answer__c', '').lower()
    summary = article.get('summary', '').lower()

    # Policy breach condition: Case involves 'QuantumPCB Modeler' and 'scalability',
    # and a knowledge article also mentions these terms.
    if ('quantumpcb modeler' in case_description or 'scalability' in case_description or 'scalability' in case_subject):
        if ('quantumpcb modeler' in title or 'quantumpcb modeler' in faq_answer or 'quantumpcb modeler' in summary or 
            'scalability' in title or 'scalability' in faq_answer or 'scalability' in summary):
            # Clean the ID from any leading '#' or trailing whitespace
            breached_article_id = article.get('id', '').replace("#", "").strip()
            break

print('__RESULT__:')
print(json.dumps(breached_article_id))"""

env_args = {'var_function-call-4528939135170288868': [], 'var_function-call-8457985838288064179': '500Wt00000DDyznIAD', 'var_function-call-12283488889908289824': [], 'var_function-call-7804752545967688268': [], 'var_function-call-10669657275739780826': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-14138365754065778393': [{'id': '#500Wt00000DDDfwIAH'}, {'id': '500Wt00000DDDtTIAX'}, {'id': '500Wt00000DDNYoIAP'}, {'id': '500Wt00000DDPIsIAP'}, {'id': '500Wt00000DDPM6IAP'}, {'id': '500Wt00000DDPSZIA5'}, {'id': '500Wt00000DDPZ0IAP'}, {'id': '500Wt00000DDPsOIAX'}, {'id': '500Wt00000DDPsPIAX'}, {'id': '500Wt00000DDQRsIAP'}, {'id': '500Wt00000DDQoUIAX'}, {'id': '500Wt00000DDRB2IAP'}, {'id': '500Wt00000DDRVzIAP'}, {'id': '500Wt00000DDRW0IAP'}, {'id': '#500Wt00000DDTEQIA5'}, {'id': '#500Wt00000DDTERIA5'}, {'id': '500Wt00000DDTHfIAP'}, {'id': '500Wt00000DDTxbIAH'}, {'id': '500Wt00000DDU5iIAH'}, {'id': '500Wt00000DDYUGIA5'}, {'id': '#500Wt00000DDYdwIAH'}, {'id': '500Wt00000DDzRCIA1'}, {'id': '500Wt00000DDYipIAH'}, {'id': '500Wt00000DDYpGIAX'}, {'id': '#500Wt00000DDYpHIAX'}, {'id': '500Wt00000DDZ0VIAX'}, {'id': '#500Wt00000DDZ27IAH'}, {'id': '500Wt00000DDZ5LIAX'}, {'id': '500Wt00000DDZJuIAP'}, {'id': '#500Wt00000DDZmsIAH'}, {'id': '#500Wt00000DDZtKIAX'}, {'id': '500Wt00000DDZtLIAX'}, {'id': '500Wt00000DDeoCIAT'}, {'id': '500Wt00000DDepmIAD'}, {'id': '#500Wt00000DDet1IAD'}, {'id': '#500Wt00000DDfFcIAL'}, {'id': '500Wt00000DDfHCIA1'}, {'id': '#500Wt00000DDfYwIAL'}, {'id': '500Wt00000DDfYxIAL'}, {'id': '500Wt00000DDflsIAD'}, {'id': '#500Wt00000DDfvXIAT'}, {'id': '500Wt00000DDfx8IAD'}, {'id': '500Wt00000DDg1yIAD'}, {'id': '500Wt00000DDg1zIAD'}, {'id': '500Wt00000DDg20IAD'}, {'id': '#500Wt00000DDg8QIAT'}, {'id': '500Wt00000DDg8RIAT'}, {'id': '500Wt00000DDgLKIA1'}, {'id': '500Wt00000DDgLLIA1'}, {'id': '500Wt00000DDnt6IAD'}, {'id': '500Wt00000DDnt7IAD'}, {'id': '#500Wt00000DDsG2IAL'}, {'id': '#500Wt00000DDsG3IAL'}, {'id': '500Wt00000DDsG4IAL'}, {'id': '#500Wt00000DDsKtIAL'}, {'id': '500Wt00000DDsKuIAL'}, {'id': '500Wt00000DDt7GIAT'}, {'id': '500Wt00000DDt7HIAT'}, {'id': '500Wt00000DDxScIAL'}, {'id': '500Wt00000DDxSdIAL'}, {'id': '500Wt00000DDxVqIAL'}, {'id': '500Wt00000DDxZ4IAL'}, {'id': '500Wt00000DDxduIAD'}, {'id': '#500Wt00000DDxkMIAT'}, {'id': '#500Wt00000DDxnbIAD'}, {'id': '500Wt00000DDy8aIAD'}, {'id': '500Wt00000DDy8bIAD'}, {'id': '500Wt00000DDyRvIAL'}, {'id': '500Wt00000DDydCIAT'}, {'id': '500Wt00000DDymuIAD'}, {'id': '#500Wt00000DDyuwIAD'}, {'id': '#500Wt00000DDyznIAD'}, {'id': '#500Wt00000DDyzoIAD'}, {'id': '500Wt00000DDyzpIAD'}, {'id': '500Wt00000DDz6FIAT'}, {'id': '500Wt00000DDz6GIAT'}, {'id': '500Wt00000DDzB4IAL'}, {'id': '500Wt00000DDzEIIA1'}, {'id': '#500Wt00000DDzJ8IAL'}, {'id': '#500Wt00000DDzKjIAL'}, {'id': '#500Wt00000DDzMLIA1'}, {'id': '500Wt00000DDzMMIA1'}, {'id': '500Wt00000DDzNxIAL'}, {'id': '500Wt00000DDzPZIA1'}, {'id': '500Wt00000DDzRBIA1'}, {'id': '500Wt00000DDzSnIAL'}, {'id': '#500Wt00000DDzSoIAL'}, {'id': '500Wt00000DDzUPIA1'}, {'id': '#500Wt00000DDzUQIA1'}, {'id': '500Wt00000DDzW2IAL'}, {'id': '500Wt00000DDzW3IAL'}, {'id': '500Wt00000DDzXdIAL'}, {'id': '#500Wt00000DDzXeIAL'}, {'id': '#500Wt00000DDzZFIA1'}, {'id': '#500Wt00000DDzZGIA1'}, {'id': '500Wt00000DDzZHIA1'}, {'id': '500Wt00000DDzarIAD'}, {'id': '500Wt00000DDzcTIAT'}, {'id': '#500Wt00000DDze5IAD'}, {'id': '500Wt00000DDze6IAD'}, {'id': '500Wt00000DDzfhIAD'}, {'id': '500Wt00000DDzhJIAT'}, {'id': '#500Wt00000DDzivIAD'}, {'id': '500Wt00000DDzkXIAT'}, {'id': '500Wt00000DDzm9IAD'}, {'id': '500Wt00000DDzmAIAT'}, {'id': '#500Wt00000DDzmBIAT'}, {'id': '500Wt00000DDzmCIAT'}, {'id': '500Wt00000DDznlIAD'}, {'id': '#500Wt00000DDzpNIAT'}, {'id': '500Wt00000DDzqzIAD'}, {'id': '500Wt00000DDzr0IAD'}, {'id': '500Wt00000DDzr2IAD'}, {'id': '500Wt00000DDzsbIAD'}, {'id': '#500Wt00000DDzscIAD'}, {'id': '#500Wt00000DDzuDIAT'}, {'id': '500Wt00000DDzuEIAT'}, {'id': '#500Wt00000DDzvpIAD'}, {'id': '#500Wt00000DDzvqIAD'}, {'id': '500Wt00000DDzxRIAT'}, {'id': '500Wt00000DDzz3IAD'}, {'id': '500Wt00000DE00fIAD'}, {'id': '500Wt00000DE00gIAD'}, {'id': '#500Wt00000DE00hIAD'}, {'id': '#500Wt00000DE02HIAT'}, {'id': '#500Wt00000DE03tIAD'}, {'id': '500Wt00000DE05VIAT'}, {'id': '#500Wt00000DE077IAD'}, {'id': '500Wt00000DE078IAD'}, {'id': '500Wt00000DE079IAD'}, {'id': '500Wt00000DE07AIAT'}, {'id': '500Wt00000DE08jIAD'}, {'id': '500Wt00000DE0ALIA1'}, {'id': '500Wt00000DE0AMIA1'}, {'id': '500Wt00000DE0BxIAL'}, {'id': '500Wt00000DE0ByIAL'}, {'id': '500Wt00000DE0DZIA1'}, {'id': '#500Wt00000DE0FCIA1'}, {'id': '500Wt00000DE0FDIA1'}, {'id': '500Wt00000DE0GnIAL'}, {'id': '500Wt00000DE0IPIA1'}, {'id': '500Wt00000DE0K1IAL'}, {'id': '500Wt00000DE0LdIAL'}, {'id': '500Wt00000DE0NFIA1'}, {'id': '500Wt00000DE0NGIA1'}, {'id': '500Wt00000DE0QTIA1'}, {'id': '500Wt00000DE0S5IAL'}, {'id': '#500Wt00000DE0ThIAL'}, {'id': '#500Wt00000DE0VJIA1'}, {'id': '500Wt00000DE0WvIAL'}, {'id': '500Wt00000DE0WwIAL'}, {'id': '500Wt00000DE0YXIA1'}, {'id': '500Wt00000DE0a9IAD'}], 'var_function-call-16336322330613192733': [], 'var_function-call-2901270610269859347': [{'description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.', 'status': 'Waiting on Customer', 'subject': 'Scalability Problems '}], 'var_function-call-10763788185040264350': 'file_storage/function-call-10763788185040264350.json'}

exec(code, env_args)
