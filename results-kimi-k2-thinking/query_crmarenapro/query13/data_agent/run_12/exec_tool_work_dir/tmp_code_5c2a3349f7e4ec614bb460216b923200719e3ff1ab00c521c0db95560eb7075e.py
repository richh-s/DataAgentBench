code = """import json
import re

# Get the order data
order_data = var_functions.query_db:6

# Clean function to handle ID corruption
def clean_id(id_val):
    if id_val is None:
        return None
    # Remove leading # if present
    id_str = str(id_val)
    if id_str.startswith('#'):
        id_str = id_str[1:]
    # Remove trailing whitespace
    id_str = id_str.strip()
    return id_str

# Process the data to calculate sales per agent
agent_sales = {}

for record in order_data:
    # Clean the OwnerId
    owner_id = clean_id(record['OwnerId'])
    
    # Get quantity and unit price
    try:
        quantity = float(record['Quantity'])
        unit_price = float(record['UnitPrice'])
        
        # Calculate sales amount for this order item
        sales_amount = quantity * unit_price
        
        # Add to agent's total
        if owner_id not in agent_sales:
            agent_sales[owner_id] = 0
        agent_sales[owner_id] += sales_amount
        
    except (ValueError, TypeError) as e:
        # Skip records with invalid numeric data
        continue

# Find the agent with the highest sales
if agent_sales:
    top_agent = max(agent_sales, key=agent_sales.get)
    top_sales = agent_sales[top_agent]
    
    result = {
        'top_agent_id': top_agent,
        'total_sales': top_sales,
        'num_agents': len(agent_sales)
    }
else:
    result = {'error': 'No valid sales data found'}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Id': '801Wt00000PFsjPIAT', 'AccountId': '001Wt00000PFttwIAD', 'Status': 'Activated', 'EffectiveDate': '2023-06-25', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NJ0EIAW'}, {'Id': '801Wt00000PFsjQIAT', 'AccountId': '#001Wt00000PHVqdIAH', 'Status': 'Activated', 'EffectiveDate': '2021-09-30', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NGjwIAG'}, {'Id': '#801Wt00000PFt7UIAT', 'AccountId': '001Wt00000PGzSaIAL', 'Status': 'Activated', 'EffectiveDate': '2022-09-15', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NIiUIAW'}, {'Id': '801Wt00000PFtAmIAL', 'AccountId': '001Wt00000PHVdhIAH', 'Status': 'Activated  ', 'EffectiveDate': '2020-09-01', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NIljIAG'}, {'Id': '801Wt00000PFtAnIAL', 'AccountId': '#001Wt00000PGaNjIAL', 'Status': 'Activated', 'EffectiveDate': '2023-06-01', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NEdJIAW'}], 'var_functions.query_db:2': [{'Id': '802Wt0000078wz3IAA', 'OrderId': '801Wt00000PGSYIIA5', 'Product2Id': '#01tWt000006hVTJIA2', 'Quantity': '15.0', 'UnitPrice': '476.991', 'PriceBookEntryId': '01uWt0000027Pa1IAE'}, {'Id': '802Wt0000078wz4IAA', 'OrderId': '801Wt00000PHVkDIAX', 'Product2Id': '01tWt000006hVDBIA2', 'Quantity': '3.0', 'UnitPrice': '549.99', 'PriceBookEntryId': '01uWt0000027PF3IAM'}, {'Id': '802Wt0000078wz5IAA', 'OrderId': '801Wt00000PHQuFIAX', 'Product2Id': '01tWt000006hV8LIAU', 'Quantity': '9.0', 'UnitPrice': '503.4905', 'PriceBookEntryId': '01uWt0000027P8cIAE'}, {'Id': '802Wt0000078xAAIAY', 'OrderId': '801Wt00000PGHg7IAH', 'Product2Id': '01tWt000006hV8LIAU', 'Quantity': '10.0', 'UnitPrice': '476.991', 'PriceBookEntryId': '01uWt0000027P8cIAE'}, {'Id': '#802Wt0000078xABIAY', 'OrderId': '801Wt00000PHVicIAH', 'Product2Id': '01tWt000006hVMrIAM', 'Quantity': '1.0', 'UnitPrice': '299.99', 'PriceBookEntryId': '01uWt0000027POjIAM'}], 'var_functions.query_db:4': [{'Id': '006Wt000007AvVeIAK', 'ContractID__c': 'None', 'AccountId': '001Wt00000PGeJIIA1', 'ContactId': '003Wt00000JqvQiIAJ', 'OwnerId': '005Wt000003NIqXIAW', 'Probability': '75.0', 'Amount': '182448.4965', 'StageName': 'Qualification', 'Name': 'InnoSphere Labs - EDA Innovation Expansion', 'Description': 'InnoSphere Labs is exploring advanced EDA solutions to enhance their R&D capabilities. They are particularly interested in the AI Cirku-Tech for rapid circuit prototyping, and the EcoPCB Creator for environmentally-friendly design processes. Additionally, CloudLink Designer could improve their team collaboration across global projects.', 'CreatedDate': '2023-09-05T11:32:46.000+0000', 'CloseDate': '2024-02-15'}, {'Id': '006Wt000007Aw3WIAS', 'ContractID__c': 'None', 'AccountId': '001Wt00000PGzsMIAT', 'ContactId': '#003Wt00000JqyQEIAZ', 'OwnerId': '005Wt000003NIc1IAG', 'Probability': '75.0', 'Amount': '22238.547', 'StageName': 'Quote', 'Name': 'TechPulse-PrimeEdge Strategic Collaboration ', 'Description': "TechPulse Solutions is poised to empower PrimeEdge Technology with its suite of cutting-edge EDA tools, including AI Cirku-Tech and SecureAnalytics Pro. By integrating solutions like DesignWave Automation and CloudLink Designer, TechPulse aims to enhance workflow automation and secure data optimization within PrimeEdge's operations. This opportunity also leverages OptiPower Manager to pursue sustainable electronics development, ensuring PrimeEdge stays at the forefront of IT innovation.", 'CreatedDate': '2024-04-05T12:15:30.000+0000', 'CloseDate': '2024-06-15'}, {'Id': '006Wt000007Aw3XIAS', 'ContractID__c': 'None', 'AccountId': '#001Wt00000PGYx5IAH', 'ContactId': '003Wt00000JquRPIAZ', 'OwnerId': '#005Wt000003NJZhIAO', 'Probability': '75.0', 'Amount': '10019.8045', 'StageName': 'Quote', 'Name': 'Quantum Designs Partnership Initiative', 'Description': 'TechPulse Solutions presents Quantum Designs with an integrated EDA suite, combining the robust capabilities of PulseSim Pro and AI Cirku-Tech for advanced semiconductor solutions. Emphasizing security, SecureFlow Suite ensures compliance and safeguarding critical data. The partnership focuses on streamlining PCB development with EcoPCB Creator, enhancing both innovation and sustainability.', 'CreatedDate': '2021-02-10T14:23:45.000+0000', 'CloseDate': '2021-05-30'}, {'Id': '006Wt000007Aya9IAC', 'ContractID__c': 'None', 'AccountId': '001Wt00000PHViXIAX', 'ContactId': '003Wt00000Jqvk1IAB', 'OwnerId': '005Wt000003NDJ0IAO', 'Probability': '75.0', 'Amount': '19002.1475', 'StageName': 'Discovery', 'Name': 'Nova Healthcare Tech Strategic Enhancement', 'Description': "Leveraging TechPulse Solutions' AI Cirku-Tech for rapid prototype advancements and SecureFlow Suite for enhanced security compliance, Nova Healthcare Tech can revolutionize their service offerings. By integrating CollabCircuit Hub, interdepartmental communication will improve significantly, facilitating more efficient project management. The adoption of QuantumPCB Modeler could provide Nova Healthcare Tech with cutting-edge tech solutions, further enhancing patient care and service quality.", 'CreatedDate': '2023-08-11T09:30:00.000+0000', 'CloseDate': '2023-11-30'}, {'Id': '006Wt000007AyaAIAS', 'ContractID__c': 'None', 'AccountId': '001Wt00000PHVk9IAH', 'ContactId': '003Wt00000Jqv0wIAB', 'OwnerId': '005Wt000003NJxtIAG', 'Probability': '85.0', 'Amount': '22249.0175', 'StageName': 'Negotiation   ', 'Name': 'LiftTech Smart Integration Project', 'Description': "LiftTech Elevations aims to enhance its building automation systems using AI-driven EDA tools like CircuitAI Innovator and EcoPCB Creator. By integrating advanced security features with SecureAnalytics Pro, they can bolster data protection and compliance. The collaboration with TechPulse Solutions promises to streamline LiftTech's workflows with DesignWave Automation, ensuring seamless system operations.", 'CreatedDate': '2022-07-20T14:13:45.000+0000', 'CloseDate': '2023-11-15'}], 'var_functions.query_db:6': [{'OrderId': '#801Wt00000PFt7UIAT', 'OwnerId': '005Wt000003NIiUIAW', 'OrderItemId': '802Wt0000078xq6IAA', 'Quantity': '8.0', 'UnitPrice': '569.9905'}, {'OrderId': '#801Wt00000PFt7UIAT', 'OwnerId': '005Wt000003NIiUIAW', 'OrderItemId': '802Wt0000079A5lIAE', 'Quantity': '10.0', 'UnitPrice': '359.991'}, {'OrderId': '801Wt00000PFyITIA1', 'OwnerId': '005Wt000003NDJ0IAO', 'OrderItemId': '802Wt00000797r3IAA', 'Quantity': '15.0', 'UnitPrice': '359.991'}, {'OrderId': '801Wt00000PFyITIA1', 'OwnerId': '005Wt000003NDJ0IAO', 'OrderItemId': '802Wt00000797sfIAA', 'Quantity': '8.0', 'UnitPrice': '503.4905'}, {'OrderId': '801Wt00000PGGhBIAX', 'OwnerId': '005Wt000003NIaRIAW', 'OrderItemId': '#802Wt000007953bIAA', 'Quantity': '14.0', 'UnitPrice': '476.991'}, {'OrderId': '801Wt00000PGGhBIAX', 'OwnerId': '005Wt000003NIaRIAW', 'OrderItemId': '#802Wt0000079AP7IAM', 'Quantity': '10.0', 'UnitPrice': '359.991'}, {'OrderId': '801Wt00000PGGhBIAX', 'OwnerId': '005Wt000003NIaRIAW', 'OrderItemId': '802Wt0000079ANVIA2', 'Quantity': '8.0', 'UnitPrice': '569.9905'}, {'OrderId': '#801Wt00000PGbdMIAT', 'OwnerId': '#005Wt000003NGtcIAG', 'OrderItemId': '802Wt00000791h9IAA', 'Quantity': '30.0', 'UnitPrice': '390.9915'}, {'OrderId': '#801Wt00000PGbdMIAT', 'OwnerId': '#005Wt000003NGtcIAG', 'OrderItemId': '802Wt00000794F3IAI', 'Quantity': '20.0', 'UnitPrice': '450.4915'}, {'OrderId': '801Wt00000PH4FMIA1', 'OwnerId': '#005Wt000003NJmbIAG', 'OrderItemId': '802Wt00000796S1IAI', 'Quantity': '10.0', 'UnitPrice': '476.991'}, {'OrderId': '801Wt00000PH8yvIAD', 'OwnerId': '005Wt000003NIXCIA4', 'OrderItemId': '802Wt00000794YHIAY', 'Quantity': '20.0', 'UnitPrice': '390.9915'}, {'OrderId': '801Wt00000PH8yvIAD', 'OwnerId': '005Wt000003NIXCIA4', 'OrderItemId': '802Wt000007968gIAA', 'Quantity': '50.0', 'UnitPrice': '450.4915'}, {'OrderId': '801Wt00000PH8yvIAD', 'OwnerId': '005Wt000003NIXCIA4', 'OrderItemId': '802Wt00000798YdIAI', 'Quantity': '30.0', 'UnitPrice': '552.4915'}, {'OrderId': '801Wt00000PHHMFIA5', 'OwnerId': '005Wt000003NJ9uIAG', 'OrderItemId': '802Wt00000795XyIAI', 'Quantity': '3.0', 'UnitPrice': '499.99'}, {'OrderId': '801Wt00000PHHMFIA5', 'OwnerId': '005Wt000003NJ9uIAG', 'OrderItemId': '802Wt00000796dJIAQ', 'Quantity': '1.0', 'UnitPrice': '399.99'}, {'OrderId': '801Wt00000PHHMFIA5', 'OwnerId': '005Wt000003NJ9uIAG', 'OrderItemId': '802Wt00000799CwIAI', 'Quantity': '7.0', 'UnitPrice': '455.9905'}, {'OrderId': '801Wt00000PHHMFIA5', 'OwnerId': '005Wt000003NJ9uIAG', 'OrderItemId': '802Wt00000799xhIAA', 'Quantity': '5.0', 'UnitPrice': '427.4905'}, {'OrderId': '801Wt00000PHHhDIAX', 'OwnerId': '#005Wt000003NITxIAO', 'OrderItemId': '#802Wt00000798olIAA', 'Quantity': '12.0', 'UnitPrice': '314.991'}, {'OrderId': '801Wt00000PHLzNIAX', 'OwnerId': '005Wt000003NEoYIAW', 'OrderItemId': '#802Wt00000790WEIAY', 'Quantity': '12.0', 'UnitPrice': '476.991'}, {'OrderId': '801Wt00000PHLzNIAX', 'OwnerId': '005Wt000003NEoYIAW', 'OrderItemId': '802Wt00000797PdIAI', 'Quantity': '10.0', 'UnitPrice': '449.991'}, {'OrderId': '801Wt00000PHLzNIAX', 'OwnerId': '005Wt000003NEoYIAW', 'OrderItemId': '802Wt00000797RFIAY', 'Quantity': '8.0', 'UnitPrice': '569.9905'}, {'OrderId': '801Wt00000PHRFAIA5', 'OwnerId': '#005Wt000003NIx1IAG', 'OrderItemId': '#802Wt0000078z8mIAA', 'Quantity': '7.0', 'UnitPrice': '379.9905'}, {'OrderId': '801Wt00000PHRFAIA5', 'OwnerId': '#005Wt000003NIx1IAG', 'OrderItemId': '#802Wt00000797RIIAY', 'Quantity': '5.0', 'UnitPrice': '569.9905'}, {'OrderId': '801Wt00000PHRFAIA5', 'OwnerId': '#005Wt000003NIx1IAG', 'OrderItemId': '802Wt00000796AJIAY', 'Quantity': '8.0', 'UnitPrice': '569.9905'}, {'OrderId': '801Wt00000PHRFAIA5', 'OwnerId': '#005Wt000003NIx1IAG', 'OrderItemId': '802Wt00000796LWIAY', 'Quantity': '16.0', 'UnitPrice': '440.991'}, {'OrderId': '#801Wt00000PHVkDIAX', 'OwnerId': '005Wt000003NJt3IAG', 'OrderItemId': '802Wt0000079Ak6IAE', 'Quantity': '3.0', 'UnitPrice': '599.99'}, {'OrderId': '801Wt00000PHVqfIAH', 'OwnerId': '005Wt000003NDEBIA4', 'OrderItemId': '802Wt000007937eIAA', 'Quantity': '10.0', 'UnitPrice': '539.991'}, {'OrderId': '#801Wt00000PHWptIAH', 'OwnerId': '005Wt000003NJ0EIAW', 'OrderItemId': '802Wt00000795xPIAQ', 'Quantity': '2.0', 'UnitPrice': '339.99'}, {'OrderId': '#801Wt00000PHWptIAH', 'OwnerId': '005Wt000003NJ0EIAW', 'OrderItemId': '802Wt0000079987IAA', 'Quantity': '3.0', 'UnitPrice': '529.99'}]}

exec(code, env_args)
