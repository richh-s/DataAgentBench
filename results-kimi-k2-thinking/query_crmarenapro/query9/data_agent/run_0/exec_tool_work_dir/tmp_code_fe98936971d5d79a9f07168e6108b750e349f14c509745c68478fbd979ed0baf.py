code = """import json
import pandas as pd
from datetime import datetime

# Read the case data from file
cases_file_path = var_functions.query_db:8
cases_df = pd.read_json(cases_file_path)

# Read account data
account_data = var_functions.query_db:10
account_df = pd.DataFrame(account_data)

# Define cleaning functions for ID fields
def clean_id(id_value):
    """Clean ID fields by removing leading # and trailing whitespace"""
    if pd.isna(id_value) or id_value is None:
        return None
    return str(id_value).strip().lstrip('#')

# Clean account IDs in both dataframes
cases_df['accountid_clean'] = cases_df['accountid'].apply(clean_id)
account_df['Id_clean'] = account_df['Id'].apply(clean_id)
account_df['ShippingState_clean'] = account_df['ShippingState'].str.strip()

# Parse dates and calculate closure time
cases_df['createddate_parsed'] = pd.to_datetime(cases_df['createddate'])
cases_df['closeddate_parsed'] = pd.to_datetime(cases_df['closeddate'])
cases_df['closure_hours'] = (cases_df['closeddate_parsed'] - cases_df['createddate_parsed']).dt.total_seconds() / 3600

# Filter for past 6 quarters from 2022-10-26 (going back to approximately 2021-07-01)
# 6 quarters = 18 months
end_date = datetime(2022, 10, 26)
start_date = datetime(2021, 7, 1)

filtered_cases = cases_df[
    (cases_df['createddate_parsed'] >= start_date) & 
    (cases_df['createddate_parsed'] <= end_date)
]

print(f"Total closed cases: {len(cases_df)}")
print(f"Cases in past 6 quarters: {len(filtered_cases)}")

# Join with account data to get states
merged_df = filtered_cases.merge(
    account_df[['Id_clean', 'ShippingState_clean']], 
    left_on='accountid_clean', 
    right_on='Id_clean', 
    how='left'
)

# Group by state and calculate average closure time
state_stats = merged_df.groupby('ShippingState_clean').agg({
    'closure_hours': ['mean', 'count']
}).round(2)

state_stats.columns = ['avg_closure_hours', 'case_count']
state_stats = state_stats.reset_index()

# Filter out states with very few cases (less than 3) to ensure statistical significance
significant_states = state_stats[state_stats['case_count'] >= 3]

# Sort by average closure time (quickest first)
quickest_states = significant_states.sort_values('avg_closure_hours')

print("Top 10 states with quickest case closure:")
print(quickest_states.head(10).to_string(index=False))

# Get the state with quickest closure time
if not quickest_states.empty:
    quickest_state = quickest_states.iloc[0]
    result_state = quickest_state['ShippingState_clean']
    result_hours = quickest_state['avg_closure_hours']
    result_count = quickest_state['case_count']
    
    print(f"\nQuickest state: {result_state}")
    print(f"Average closure time: {result_hours:.2f} hours")
    print(f"Number of cases: {result_count}")
else:
    result_state = None
    print("No state found with significant case volume")"""

env_args = {'var_functions.list_db:0': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:2': [{'id': '#500Wt00000DDDfwIAH', 'priority': 'Medium', 'subject': 'Feature Update Notifications Lack', 'description': "Without regular update notifications, we are unable to fully utilize CollabCircuit Hub's latest features.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000797r4IAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDDtTIAX', 'priority': 'Medium', 'subject': 'Missing Feature Update Alerts', 'description': 'I have noticed that I am not consistently receiving notifications about new feature updates for the SecureFlow Suite, which affects my ability to use the software to its full potential.', 'status': 'Waiting on Customer   ', 'contactid': '003Wt00000Jqp3WIAR', 'createddate': '2020-12-29T08:36:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798aDIAQ', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PHVkAIAX', 'ownerid': '#005Wt000003NJWTIA4'}, {'id': '500Wt00000DDNYoIAP', 'priority': 'Medium', 'subject': 'Delayed Support Response ', 'description': 'I am experiencing delays in getting timely responses from TechPulse support during busy periods, which is affecting our project timelines.', 'status': 'Closed', 'contactid': '#003Wt00000JqqVtIAJ', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000', 'orderitemid__c': '802Wt00000792tiIAA', 'issueid__c': 'a03Wt00000JqtOtIAJ', 'accountid': '001Wt00000PGZZoIAP', 'ownerid': '005Wt000003NIc3IAG'}, {'id': '500Wt00000DDPIsIAP', 'priority': 'Medium', 'subject': 'AI Feature Malfunction', 'description': 'Some of the AI-powered features in CloudLink Designer are intermittently failing to operate, leading to reduced efficiency and user frustration.', 'status': 'Closed ', 'contactid': '003Wt00000JqlkjIAB', 'createddate': '2022-08-05T14:30:00.000+0000', 'closeddate': '2022-08-05T14:39:32.000+0000', 'orderitemid__c': '802Wt00000797r3IAA', 'issueid__c': 'a03Wt00000JqxVjIAJ', 'accountid': '#001Wt00000PGRnYIAX', 'ownerid': '#005Wt000003NEzqIAG'}, {'id': '500Wt00000DDPM6IAP', 'priority': 'High', 'subject': 'Access Issues with Training Module', 'description': "I am experiencing difficulty accessing the online training modules which are crucial for my team's smooth adoption of the SecureFlow Suite.", 'status': 'Closed', 'contactid': '#003Wt00000Jqv14IAB', 'createddate': '2020-09-01T10:30:00.000+0000', 'closeddate': '2020-09-01T14:08:55.000+0000', 'orderitemid__c': '802Wt00000797r5IAA', 'issueid__c': 'a03Wt00000JqvNUIAZ', 'accountid': '001Wt00000PGzSaIAL', 'ownerid': '005Wt000003NISLIA4'}], 'var_functions.list_db:5': ['User', 'Account', 'Contact'], 'var_functions.query_db:6': [{'Id': '001Wt00000PFj4zIAD', 'Name': 'NaviCorp Tech ', 'Phone': '000-111-2222', 'Industry': 'Navigation Technology', 'Description': 'NaviCorp Tech excels in developing advanced navigation technologies, with a focus on precision and power efficiency. Utilizing CircuitAI Innovator alongside OptiPower Manager, they deliver solutions that redefine navigation systems, enhancing accuracy and operational excellence.', 'NumberOfEmployees': '800.0', 'ShippingState': 'FL'}, {'Id': '001Wt00000PFj50IAD', 'Name': 'FusionTech Systems', 'Phone': '333-987-6543', 'Industry': 'Technology Manufacturing', 'Description': 'FusionTech Systems stands out in technology manufacturing by integrating AI and cloud-based solutions. With products like AI Cirku-Tech and CloudLink Designer, they commit to providing innovative manufacturing processes. Their dedication to tech-driven manufacturing ensures high-quality, reliable outputs.', 'NumberOfEmployees': '760.0', 'ShippingState': 'TX'}, {'Id': '#001Wt00000PFluoIAD', 'Name': 'BlueSky Aerospace', 'Phone': '839-393-9393', 'Industry': 'Aerospace Engineering', 'Description': "BlueSky Aerospace excels in aerospace engineering through innovative simulation and circuit design tools. With QuantumPCB Modeler and SimuFlow Xtreme, they develop precise and advanced aerospace components. Their continuous pursuit of innovation drives aerospace technology's evolution.", 'NumberOfEmployees': '980.0', 'ShippingState': 'AZ'}, {'Id': '#001Wt00000PFlupIAD', 'Name': 'NeuralWave Technologies', 'Phone': '444-333-4444', 'Industry': 'Artificial Intelligence', 'Description': 'NeuralWave Technologies leads advancements in AI-driven solutions for various applications. Using products like AI Cirku-Tech and Workflow Genius, they optimize design processes and enhance power management in AI systems. Focused on innovation, they continue to push the boundaries of artificial intelligence capabilities.', 'NumberOfEmployees': '950.0', 'ShippingState': 'CA'}, {'Id': '001Wt00000PFrk1IAD', 'Name': 'SkyNet Technologies', 'Phone': '111-222-3334', 'Industry': 'Drones & Aviation', 'Description': 'SkyNet Technologies pioneers in drone development and aviation technology, combining precision design with advanced cloud capabilities. Through QuantumPCB Modeler and CloudLink Designer, they produce innovative and efficient aviation systems. Their contributions set standards in the modernization of aerial technology.', 'NumberOfEmployees': '700.0', 'ShippingState': 'MO'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [{'Id': '001Wt00000PFj4zIAD', 'ShippingState': 'FL'}, {'Id': '001Wt00000PFj50IAD', 'ShippingState': 'TX'}, {'Id': '#001Wt00000PFluoIAD', 'ShippingState': 'AZ'}, {'Id': '#001Wt00000PFlupIAD', 'ShippingState': 'CA'}, {'Id': '001Wt00000PFrk1IAD', 'ShippingState': 'MO'}, {'Id': '001Wt00000PFsjMIAT', 'ShippingState': 'OH'}, {'Id': '001Wt00000PFsjOIAT', 'ShippingState': 'NY'}, {'Id': '001Wt00000PFsmZIAT', 'ShippingState': 'CO'}, {'Id': '001Wt00000PFsmaIAD', 'ShippingState': 'MI'}, {'Id': '001Wt00000PFsmbIAD', 'ShippingState': 'NV'}, {'Id': '#001Wt00000PFsmcIAD', 'ShippingState': 'MN'}, {'Id': '001Wt00000PFsmdIAD', 'ShippingState': 'MA'}, {'Id': '001Wt00000PFt7TIAT', 'ShippingState': 'CO'}, {'Id': '#001Wt00000PFttwIAD', 'ShippingState': 'CA'}, {'Id': '001Wt00000PGGTtIAP', 'ShippingState': 'CA'}, {'Id': '#001Wt00000PGGTuIAP', 'ShippingState': 'CA'}, {'Id': '#001Wt00000PGHsyIAH', 'ShippingState': 'FL'}, {'Id': '001Wt00000PGQzcIAH', 'ShippingState': 'WA'}, {'Id': '001Wt00000PGR63IAH', 'ShippingState': 'WA'}, {'Id': '001Wt00000PGRnYIAX', 'ShippingState': 'IA'}, {'Id': '001Wt00000PGRqjIAH', 'ShippingState': 'CA'}, {'Id': '001Wt00000PGSwYIAX', 'ShippingState': 'IA'}, {'Id': '001Wt00000PGSwZIAX', 'ShippingState': 'FL'}, {'Id': '#001Wt00000PGXrKIAX', 'ShippingState': 'WA'}, {'Id': '#001Wt00000PGXrLIAX', 'ShippingState': 'NY'}, {'Id': '001Wt00000PGXrMIAX', 'ShippingState': 'NY'}, {'Id': '001Wt00000PGXrNIAX', 'ShippingState': 'WA'}, {'Id': '#001Wt00000PGYgxIAH', 'ShippingState': 'OR'}, {'Id': '001Wt00000PGYx4IAH', 'ShippingState': 'NY'}, {'Id': '#001Wt00000PGYx5IAH', 'ShippingState': 'MA'}, {'Id': '001Wt00000PGZZnIAP', 'ShippingState': 'TX'}, {'Id': '001Wt00000PGZZoIAP', 'ShippingState': 'OR'}, {'Id': '001Wt00000PGZgHIAX', 'ShippingState': 'UT'}, {'Id': '#001Wt00000PGZmeIAH', 'ShippingState': 'TX'}, {'Id': '001Wt00000PGZmfIAH', 'ShippingState': 'MI'}, {'Id': '001Wt00000PGaHIIA1', 'ShippingState': 'NV'}, {'Id': '001Wt00000PGaNjIAL', 'ShippingState': 'GA'}, {'Id': '001Wt00000PGaNkIAL', 'ShippingState': 'VA'}, {'Id': '#001Wt00000PGaZCIA1', 'ShippingState': 'OR'}, {'Id': '001Wt00000PGaZDIA1', 'ShippingState': 'CA'}, {'Id': '#001Wt00000PGb5MIAT', 'ShippingState': 'FL'}, {'Id': '#001Wt00000PGb5NIAT', 'ShippingState': 'GA'}, {'Id': '001Wt00000PGb5OIAT', 'ShippingState': 'IL'}, {'Id': '#001Wt00000PGcFxIAL', 'ShippingState': 'MI'}, {'Id': '001Wt00000PGccRIAT', 'ShippingState': 'GA'}, {'Id': '001Wt00000PGcpMIAT', 'ShippingState': 'MO'}, {'Id': '#001Wt00000PGdBuIAL', 'ShippingState': 'WA'}, {'Id': '#001Wt00000PGdwiIAD', 'ShippingState': 'WA'}, {'Id': '#001Wt00000PGdzxIAD', 'ShippingState': 'FL'}, {'Id': '001Wt00000PGeJIIA1', 'ShippingState': 'MA'}, {'Id': '001Wt00000PGoAaIAL', 'ShippingState': 'NJ'}, {'Id': '#001Wt00000PGovMIAT', 'ShippingState': 'CO'}, {'Id': '001Wt00000PGtdJIAT', 'ShippingState': 'IL'}, {'Id': '001Wt00000PGtdKIAT', 'ShippingState': 'VA'}, {'Id': '001Wt00000PGtmwIAD', 'ShippingState': 'IL'}, {'Id': '001Wt00000PGtmxIAD', 'ShippingState': 'TX'}, {'Id': '001Wt00000PGyTIIA1', 'ShippingState': 'CO'}, {'Id': '001Wt00000PGyv0IAD', 'ShippingState': 'MA'}, {'Id': '001Wt00000PGz2nIAD', 'ShippingState': 'CO'}, {'Id': '001Wt00000PGzM9IAL', 'ShippingState': 'GA'}, {'Id': '001Wt00000PGzSaIAL', 'ShippingState': 'WA'}, {'Id': '001Wt00000PGzSbIAL', 'ShippingState': 'FL'}, {'Id': '001Wt00000PGzVpIAL', 'ShippingState': 'TX'}, {'Id': '001Wt00000PGzsMIAT', 'ShippingState': 'CA'}, {'Id': '001Wt00000PH90cIAD', 'ShippingState': 'MA'}, {'Id': '#001Wt00000PH9DRIA1', 'ShippingState': 'FL'}, {'Id': '#001Wt00000PH9ITIA1', 'ShippingState': 'TX'}, {'Id': '#001Wt00000PHHXXIA5', 'ShippingState': 'TX'}, {'Id': '001Wt00000PHR75IAH', 'ShippingState': 'OR'}, {'Id': '#001Wt00000PHR8gIAH', 'ShippingState': 'AZ'}, {'Id': '001Wt00000PHRF8IAP', 'ShippingState': 'NY'}, {'Id': '001Wt00000PHRF9IAP', 'ShippingState': 'WA'}, {'Id': '001Wt00000PHRTeIAP', 'ShippingState': 'FL'}, {'Id': '#001Wt00000PHRTfIAP', 'ShippingState': 'FL'}, {'Id': '001Wt00000PHRVGIA5', 'ShippingState': 'CA'}, {'Id': '001Wt00000PHRVHIA5', 'ShippingState': 'TX'}, {'Id': '001Wt00000PHRVIIA5', 'ShippingState': 'NY'}, {'Id': '001Wt00000PHRbiIAH', 'ShippingState': 'GA'}, {'Id': '001Wt00000PHVaUIAX', 'ShippingState': 'CA'}, {'Id': '001Wt00000PHVaVIAX', 'ShippingState': 'NY'}, {'Id': '#001Wt00000PHVdhIAH', 'ShippingState': 'TX'}, {'Id': '#001Wt00000PHVfJIAX', 'ShippingState': 'MN'}, {'Id': '001Wt00000PHVgvIAH', 'ShippingState': 'CA'}, {'Id': '001Wt00000PHViXIAX', 'ShippingState': 'NC'}, {'Id': '001Wt00000PHViYIAX', 'ShippingState': 'MD'}, {'Id': '#001Wt00000PHViZIAX', 'ShippingState': 'PA'}, {'Id': '001Wt00000PHViaIAH', 'ShippingState': 'CO'}, {'Id': '001Wt00000PHVk9IAH', 'ShippingState': 'NY'}, {'Id': '#001Wt00000PHVkAIAX', 'ShippingState': 'VA'}, {'Id': '001Wt00000PHVllIAH', 'ShippingState': 'FL'}, {'Id': '001Wt00000PHVnNIAX', 'ShippingState': 'SC'}, {'Id': '001Wt00000PHVnOIAX', 'ShippingState': 'CA'}, {'Id': '001Wt00000PHVozIAH', 'ShippingState': 'NY'}, {'Id': '001Wt00000PHVqbIAH', 'ShippingState': 'GA'}, {'Id': '001Wt00000PHVqdIAH', 'ShippingState': 'CA'}, {'Id': '001Wt00000PHVsDIAX', 'ShippingState': 'OR'}, {'Id': '001Wt00000PHVtpIAH', 'ShippingState': 'TX'}, {'Id': '001Wt00000PHVvRIAX', 'ShippingState': 'TX'}, {'Id': '001Wt00000PHVx3IAH', 'ShippingState': 'AZ'}, {'Id': '#001Wt00000PHVyfIAH', 'ShippingState': 'NC'}, {'Id': '001Wt00000PHW0HIAX', 'ShippingState': 'NY'}]}

exec(code, env_args)
