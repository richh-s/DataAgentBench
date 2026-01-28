code = """import json
import sqlite3
from datetime import datetime

# Load closed cases from file
closed_cases_file = var_functions.query_db:10
with open(closed_cases_file, 'r') as f:
    closed_cases = json.load(f)

# Load accounts from core_crm
try:
    conn = sqlite3.connect('core_crm.db')
    cursor = conn.cursor()
    cursor.execute("SELECT Id, ShippingState FROM Account")
    accounts = cursor.fetchall()
    conn.close()
except Exception as e:
    print('__RESULT__:')
    print(json.dumps({'error': str(e)}))
    exit()

# Create account to state mapping
account_states = {row[0]: row[1] for row in accounts}

# Define cutoff date for past 6 quarters (18 months)
# Today's date: 2022-10-26
cutoff_date = datetime(2021, 4, 26)  # 18 months back

state_closure_times = {}
valid_cases = 0

for case in closed_cases:
    try:
        # Parse dates
        created_str = case['createddate'].replace('Z', '+00:00')
        closed_str = case['closeddate'].replace('Z', '+00:00')
        created = datetime.fromisoformat(created_str)
        closed = datetime.fromisoformat(closed_str)
        
        # Check if within date range
        if created < cutoff_date:
            continue
        
        # Get account ID (strip leading # if present)
        account_id = case['accountid']
        if account_id.startswith('#'):
            account_id = account_id[1:]
        
        # Get state
        state = account_states.get(account_id)
        if not state:
            continue
        
        # Calculate closure time in hours
        closure_hours = (closed - created).total_seconds() / 3600
        
        # Add to state data
        if state not in state_closure_times:
            state_closure_times[state] = []
        state_closure_times[state].append(closure_hours)
        valid_cases += 1
        
    except Exception as e:
        continue

# Calculate averages
state_averages = {}
for state, times in state_closure_times.items():
    state_averages[state] = sum(times) / len(times)

# Sort by average (ascending)
sorted_states = sorted(state_averages.items(), key=lambda x: x[1])

# Get top state
top_state = sorted_states[0][0] if sorted_states else None

print('__RESULT__:')
print(json.dumps({
    'top_state': top_state,
    'total_cases': valid_cases,
    'total_states': len(sorted_states)
}))"""

env_args = {'var_functions.query_db:0': [{'id': '#500Wt00000DDDfwIAH', 'priority': 'Medium', 'subject': 'Feature Update Notifications Lack', 'description': "Without regular update notifications, we are unable to fully utilize CollabCircuit Hub's latest features.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000797r4IAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDDtTIAX', 'priority': 'Medium', 'subject': 'Missing Feature Update Alerts', 'description': 'I have noticed that I am not consistently receiving notifications about new feature updates for the SecureFlow Suite, which affects my ability to use the software to its full potential.', 'status': 'Waiting on Customer   ', 'contactid': '003Wt00000Jqp3WIAR', 'createddate': '2020-12-29T08:36:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798aDIAQ', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PHVkAIAX', 'ownerid': '#005Wt000003NJWTIA4'}, {'id': '500Wt00000DDNYoIAP', 'priority': 'Medium', 'subject': 'Delayed Support Response ', 'description': 'I am experiencing delays in getting timely responses from TechPulse support during busy periods, which is affecting our project timelines.', 'status': 'Closed', 'contactid': '#003Wt00000JqqVtIAJ', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000', 'orderitemid__c': '802Wt00000792tiIAA', 'issueid__c': 'a03Wt00000JqtOtIAJ', 'accountid': '001Wt00000PGZZoIAP', 'ownerid': '005Wt000003NIc3IAG'}, {'id': '500Wt00000DDPIsIAP', 'priority': 'Medium', 'subject': 'AI Feature Malfunction', 'description': 'Some of the AI-powered features in CloudLink Designer are intermittently failing to operate, leading to reduced efficiency and user frustration.', 'status': 'Closed ', 'contactid': '003Wt00000JqlkjIAB', 'createddate': '2022-08-05T14:30:00.000+0000', 'closeddate': '2022-08-05T14:39:32.000+0000', 'orderitemid__c': '802Wt00000797r3IAA', 'issueid__c': 'a03Wt00000JqxVjIAJ', 'accountid': '#001Wt00000PGRnYIAX', 'ownerid': '#005Wt000003NEzqIAG'}, {'id': '500Wt00000DDPM6IAP', 'priority': 'High', 'subject': 'Access Issues with Training Module', 'description': "I am experiencing difficulty accessing the online training modules which are crucial for my team's smooth adoption of the SecureFlow Suite.", 'status': 'Closed', 'contactid': '#003Wt00000Jqv14IAB', 'createddate': '2020-09-01T10:30:00.000+0000', 'closeddate': '2020-09-01T14:08:55.000+0000', 'orderitemid__c': '802Wt00000797r5IAA', 'issueid__c': 'a03Wt00000JqvNUIAZ', 'accountid': '001Wt00000PGzSaIAL', 'ownerid': '005Wt000003NISLIA4'}], 'var_functions.query_db:2': [{'Id': '001Wt00000PFj4zIAD', 'Name': 'NaviCorp Tech ', 'Phone': '000-111-2222', 'Industry': 'Navigation Technology', 'Description': 'NaviCorp Tech excels in developing advanced navigation technologies, with a focus on precision and power efficiency. Utilizing CircuitAI Innovator alongside OptiPower Manager, they deliver solutions that redefine navigation systems, enhancing accuracy and operational excellence.', 'NumberOfEmployees': '800.0', 'ShippingState': 'FL'}, {'Id': '001Wt00000PFj50IAD', 'Name': 'FusionTech Systems', 'Phone': '333-987-6543', 'Industry': 'Technology Manufacturing', 'Description': 'FusionTech Systems stands out in technology manufacturing by integrating AI and cloud-based solutions. With products like AI Cirku-Tech and CloudLink Designer, they commit to providing innovative manufacturing processes. Their dedication to tech-driven manufacturing ensures high-quality, reliable outputs.', 'NumberOfEmployees': '760.0', 'ShippingState': 'TX'}, {'Id': '#001Wt00000PFluoIAD', 'Name': 'BlueSky Aerospace', 'Phone': '839-393-9393', 'Industry': 'Aerospace Engineering', 'Description': "BlueSky Aerospace excels in aerospace engineering through innovative simulation and circuit design tools. With QuantumPCB Modeler and SimuFlow Xtreme, they develop precise and advanced aerospace components. Their continuous pursuit of innovation drives aerospace technology's evolution.", 'NumberOfEmployees': '980.0', 'ShippingState': 'AZ'}, {'Id': '#001Wt00000PFlupIAD', 'Name': 'NeuralWave Technologies', 'Phone': '444-333-4444', 'Industry': 'Artificial Intelligence', 'Description': 'NeuralWave Technologies leads advancements in AI-driven solutions for various applications. Using products like AI Cirku-Tech and Workflow Genius, they optimize design processes and enhance power management in AI systems. Focused on innovation, they continue to push the boundaries of artificial intelligence capabilities.', 'NumberOfEmployees': '950.0', 'ShippingState': 'CA'}, {'Id': '001Wt00000PFrk1IAD', 'Name': 'SkyNet Technologies', 'Phone': '111-222-3334', 'Industry': 'Drones & Aviation', 'Description': 'SkyNet Technologies pioneers in drone development and aviation technology, combining precision design with advanced cloud capabilities. Through QuantumPCB Modeler and CloudLink Designer, they produce innovative and efficient aviation systems. Their contributions set standards in the modernization of aerial technology.', 'NumberOfEmployees': '700.0', 'ShippingState': 'MO'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
