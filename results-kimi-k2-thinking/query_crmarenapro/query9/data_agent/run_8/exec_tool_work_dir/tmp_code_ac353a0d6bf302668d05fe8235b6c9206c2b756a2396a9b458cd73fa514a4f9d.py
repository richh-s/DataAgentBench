code = """import json, sqlite3, datetime

# Load closed cases
f = open(var_functions.query_db:10, 'r')
closed_cases = json.load(f)
f.close()

# Get accounts from sqlite
def get_accounts():
    conn = sqlite3.connect('core_crm.db')
    c = conn.cursor()
    c.execute("SELECT Id, ShippingState FROM Account")
    rows = c.fetchall()
    conn.close()
    return {r[0]: r[1] for r in rows}

account_states = get_accounts()

# Process cases
cutoff = datetime.datetime(2021, 4, 26)
state_times = {}
case_count = 0

for case in closed_cases:
    try:
        created = datetime.datetime.fromisoformat(case['createddate'].replace('Z', '+00:00'))
        if created < cutoff: continue
        
        acc_id = case['accountid']
        if acc_id.startswith('#'): acc_id = acc_id[1:]
        
        state = account_states.get(acc_id)
        if not state: continue
        
        closed = datetime.datetime.fromisoformat(case['closeddate'].replace('Z', '+00:00'))
        hours = (closed - created).total_seconds() / 3600
        
        if state not in state_times: state_times[state] = []
        state_times[state].append(hours)
        case_count += 1
    except:
        pass

# Calculate averages
avg_times = {s: sum(times)/len(times) for s, times in state_times.items()}
sorted_states = sorted(avg_times.items(), key=lambda x: x[1])

top_state = sorted_states[0][0] if sorted_states else None

print('__RESULT__:')
print(json.dumps({'top_state': top_state, 'cases': case_count, 'states': len(sorted_states)}))"""

env_args = {'var_functions.query_db:0': [{'id': '#500Wt00000DDDfwIAH', 'priority': 'Medium', 'subject': 'Feature Update Notifications Lack', 'description': "Without regular update notifications, we are unable to fully utilize CollabCircuit Hub's latest features.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000797r4IAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDDtTIAX', 'priority': 'Medium', 'subject': 'Missing Feature Update Alerts', 'description': 'I have noticed that I am not consistently receiving notifications about new feature updates for the SecureFlow Suite, which affects my ability to use the software to its full potential.', 'status': 'Waiting on Customer   ', 'contactid': '003Wt00000Jqp3WIAR', 'createddate': '2020-12-29T08:36:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798aDIAQ', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PHVkAIAX', 'ownerid': '#005Wt000003NJWTIA4'}, {'id': '500Wt00000DDNYoIAP', 'priority': 'Medium', 'subject': 'Delayed Support Response ', 'description': 'I am experiencing delays in getting timely responses from TechPulse support during busy periods, which is affecting our project timelines.', 'status': 'Closed', 'contactid': '#003Wt00000JqqVtIAJ', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000', 'orderitemid__c': '802Wt00000792tiIAA', 'issueid__c': 'a03Wt00000JqtOtIAJ', 'accountid': '001Wt00000PGZZoIAP', 'ownerid': '005Wt000003NIc3IAG'}, {'id': '500Wt00000DDPIsIAP', 'priority': 'Medium', 'subject': 'AI Feature Malfunction', 'description': 'Some of the AI-powered features in CloudLink Designer are intermittently failing to operate, leading to reduced efficiency and user frustration.', 'status': 'Closed ', 'contactid': '003Wt00000JqlkjIAB', 'createddate': '2022-08-05T14:30:00.000+0000', 'closeddate': '2022-08-05T14:39:32.000+0000', 'orderitemid__c': '802Wt00000797r3IAA', 'issueid__c': 'a03Wt00000JqxVjIAJ', 'accountid': '#001Wt00000PGRnYIAX', 'ownerid': '#005Wt000003NEzqIAG'}, {'id': '500Wt00000DDPM6IAP', 'priority': 'High', 'subject': 'Access Issues with Training Module', 'description': "I am experiencing difficulty accessing the online training modules which are crucial for my team's smooth adoption of the SecureFlow Suite.", 'status': 'Closed', 'contactid': '#003Wt00000Jqv14IAB', 'createddate': '2020-09-01T10:30:00.000+0000', 'closeddate': '2020-09-01T14:08:55.000+0000', 'orderitemid__c': '802Wt00000797r5IAA', 'issueid__c': 'a03Wt00000JqvNUIAZ', 'accountid': '001Wt00000PGzSaIAL', 'ownerid': '005Wt000003NISLIA4'}], 'var_functions.query_db:2': [{'Id': '001Wt00000PFj4zIAD', 'Name': 'NaviCorp Tech ', 'Phone': '000-111-2222', 'Industry': 'Navigation Technology', 'Description': 'NaviCorp Tech excels in developing advanced navigation technologies, with a focus on precision and power efficiency. Utilizing CircuitAI Innovator alongside OptiPower Manager, they deliver solutions that redefine navigation systems, enhancing accuracy and operational excellence.', 'NumberOfEmployees': '800.0', 'ShippingState': 'FL'}, {'Id': '001Wt00000PFj50IAD', 'Name': 'FusionTech Systems', 'Phone': '333-987-6543', 'Industry': 'Technology Manufacturing', 'Description': 'FusionTech Systems stands out in technology manufacturing by integrating AI and cloud-based solutions. With products like AI Cirku-Tech and CloudLink Designer, they commit to providing innovative manufacturing processes. Their dedication to tech-driven manufacturing ensures high-quality, reliable outputs.', 'NumberOfEmployees': '760.0', 'ShippingState': 'TX'}, {'Id': '#001Wt00000PFluoIAD', 'Name': 'BlueSky Aerospace', 'Phone': '839-393-9393', 'Industry': 'Aerospace Engineering', 'Description': "BlueSky Aerospace excels in aerospace engineering through innovative simulation and circuit design tools. With QuantumPCB Modeler and SimuFlow Xtreme, they develop precise and advanced aerospace components. Their continuous pursuit of innovation drives aerospace technology's evolution.", 'NumberOfEmployees': '980.0', 'ShippingState': 'AZ'}, {'Id': '#001Wt00000PFlupIAD', 'Name': 'NeuralWave Technologies', 'Phone': '444-333-4444', 'Industry': 'Artificial Intelligence', 'Description': 'NeuralWave Technologies leads advancements in AI-driven solutions for various applications. Using products like AI Cirku-Tech and Workflow Genius, they optimize design processes and enhance power management in AI systems. Focused on innovation, they continue to push the boundaries of artificial intelligence capabilities.', 'NumberOfEmployees': '950.0', 'ShippingState': 'CA'}, {'Id': '001Wt00000PFrk1IAD', 'Name': 'SkyNet Technologies', 'Phone': '111-222-3334', 'Industry': 'Drones & Aviation', 'Description': 'SkyNet Technologies pioneers in drone development and aviation technology, combining precision design with advanced cloud capabilities. Through QuantumPCB Modeler and CloudLink Designer, they produce innovative and efficient aviation systems. Their contributions set standards in the modernization of aerial technology.', 'NumberOfEmployees': '700.0', 'ShippingState': 'MO'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.list_db:16': ['User', 'Account', 'Contact']}

exec(code, env_args)
