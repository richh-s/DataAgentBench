code = """import json
from datetime import datetime
import pandas as pd
import numpy as np

print("Starting analysis...")

# Read the cases data from file
cases_file_path = dict(locals())['var_functions.query_db:14']
with open(cases_file_path, 'r') as f:
    cases_data = json.load(f)

# Read the accounts data from the new query
accounts_data = dict(locals())['var_functions.query_db:32']

print(f"Cases: {len(cases_data)}, Accounts: {len(accounts_data)}")

# Convert to DataFrames for analysis
cases_df = pd.DataFrame(cases_data)
accounts_df = pd.DataFrame(accounts_data)

# Debug: check data types and sample values
print(f"Cases columns: {cases_df.columns.tolist()}")
print(f"Sample createddate: {cases_df['createddate'].iloc[0] if len(cases_df) > 0 else 'None'}")
print(f"Sample closeddate: {cases_df['closeddate'].iloc[0] if len(cases_df) > 0 else 'None'}")
print(f"Sample accountid: {cases_df['accountid'].iloc[0] if len(cases_df) > 0 else 'None'}")

# Clean up data - handle missing/null values
cases_df['closeddate'] = cases_df['closeddate'].replace('None', pd.NA)

# Convert to datetime and remove timezone
cases_df['createddate'] = pd.to_datetime(cases_df['createddate'], errors='coerce').dt.tz_localize(None)
cases_df['closeddate'] = pd.to_datetime(cases_df['closeddate'], errors='coerce').dt.tz_localize(None)

# Remove leading # from IDs and trim whitespace
cases_df['accountid'] = cases_df['accountid'].astype(str).str.replace('^#', '', regex=True).str.strip()
accounts_df['Id'] = accounts_df['Id'].astype(str).str.replace('^#', '', regex=True).str.strip()
accounts_df['ShippingState'] = accounts_df['ShippingState'].astype(str).str.strip()

print(f"After cleaning - Cases with valid dates: {cases_df['createddate'].notna().sum()}")
print(f"Cases with valid closed dates: {cases_df['closeddate'].notna().sum()}")

# Define date range: 6 quarters = 18 months before 2022-10-26
cutoff_date = datetime(2021, 4, 26)  # 18 months before 2022-10-26
end_date = datetime(2022, 10, 26)

print(f"Date range: {cutoff_date} to {end_date}")

# Filter cases within the date range and only closed cases
valid_cases = cases_df[
    (cases_df['createddate'].notna()) &
    (cases_df['closeddate'].notna())
].copy()

print(f"Valid closed cases: {len(valid_cases)}")

if len(valid_cases) > 0:
    print(f"Date range of valid cases: {valid_cases['createddate'].min()} to {valid_cases['createddate'].max()}")

# Filter by date range
cases_filtered = valid_cases[
    (valid_cases['createddate'] >= cutoff_date) & 
    (valid_cases['createddate'] <= end_date)
].copy()

print(f"Cases in date range: {len(cases_filtered)}")

# Calculate closure time in hours
cases_filtered['closure_hours'] = (cases_filtered['closeddate'] - cases_filtered['createddate']).dt.total_seconds() / 3600

# Join with accounts to get states
cases_with_states = cases_filtered.merge(
    accounts_df[['Id', 'ShippingState']], 
    left_on='accountid', 
    right_on='Id', 
    how='inner'
)

print(f"Cases with state info: {len(cases_with_states)}")

# Group by state and calculate average closure time
if len(cases_with_states) > 0:
    state_stats = cases_with_states.groupby('ShippingState').agg({
        'closure_hours': ['mean', 'count']
    }).round(2)
    
    state_stats.columns = ['avg_closure_hours', 'case_count']
    state_stats = state_stats.reset_index()
    
    # Filter states with at least 3 cases to ensure meaningful averages
    state_stats_filtered = state_stats[state_stats['case_count'] >= 3]
    
    # Sort by average closure time (quickest first)
    state_stats_sorted = state_stats_filtered.sort_values('avg_closure_hours')
    
    print(f"States with >=3 cases: {len(state_stats_sorted)}")
    
    if len(state_stats_sorted) > 0:
        top_state = state_stats_sorted.iloc[0]['ShippingState']
        print(f"Top state: {top_state}")
    else:
        top_state = None
        print("No states with >=3 cases found")
else:
    top_state = None
    print("No cases with state information")

print('__RESULT__:')
print(json.dumps(top_state))"""

env_args = {'var_functions.list_db:0': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:2': [{'id': '#500Wt00000DDDfwIAH', 'priority': 'Medium', 'subject': 'Feature Update Notifications Lack', 'description': "Without regular update notifications, we are unable to fully utilize CollabCircuit Hub's latest features.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000797r4IAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDDtTIAX', 'priority': 'Medium', 'subject': 'Missing Feature Update Alerts', 'description': 'I have noticed that I am not consistently receiving notifications about new feature updates for the SecureFlow Suite, which affects my ability to use the software to its full potential.', 'status': 'Waiting on Customer   ', 'contactid': '003Wt00000Jqp3WIAR', 'createddate': '2020-12-29T08:36:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798aDIAQ', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PHVkAIAX', 'ownerid': '#005Wt000003NJWTIA4'}, {'id': '500Wt00000DDNYoIAP', 'priority': 'Medium', 'subject': 'Delayed Support Response ', 'description': 'I am experiencing delays in getting timely responses from TechPulse support during busy periods, which is affecting our project timelines.', 'status': 'Closed', 'contactid': '#003Wt00000JqqVtIAJ', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000', 'orderitemid__c': '802Wt00000792tiIAA', 'issueid__c': 'a03Wt00000JqtOtIAJ', 'accountid': '001Wt00000PGZZoIAP', 'ownerid': '005Wt000003NIc3IAG'}, {'id': '500Wt00000DDPIsIAP', 'priority': 'Medium', 'subject': 'AI Feature Malfunction', 'description': 'Some of the AI-powered features in CloudLink Designer are intermittently failing to operate, leading to reduced efficiency and user frustration.', 'status': 'Closed ', 'contactid': '003Wt00000JqlkjIAB', 'createddate': '2022-08-05T14:30:00.000+0000', 'closeddate': '2022-08-05T14:39:32.000+0000', 'orderitemid__c': '802Wt00000797r3IAA', 'issueid__c': 'a03Wt00000JqxVjIAJ', 'accountid': '#001Wt00000PGRnYIAX', 'ownerid': '#005Wt000003NEzqIAG'}, {'id': '500Wt00000DDPM6IAP', 'priority': 'High', 'subject': 'Access Issues with Training Module', 'description': "I am experiencing difficulty accessing the online training modules which are crucial for my team's smooth adoption of the SecureFlow Suite.", 'status': 'Closed', 'contactid': '#003Wt00000Jqv14IAB', 'createddate': '2020-09-01T10:30:00.000+0000', 'closeddate': '2020-09-01T14:08:55.000+0000', 'orderitemid__c': '802Wt00000797r5IAA', 'issueid__c': 'a03Wt00000JqvNUIAZ', 'accountid': '001Wt00000PGzSaIAL', 'ownerid': '005Wt000003NISLIA4'}], 'var_functions.query_db:5': [{'id': '#500Wt00000DE03tIAD', 'accountid': '001Wt00000PGcpMIAT', 'createddate': '2023-12-02T11:30:00.000+0000', 'closeddate': '2023-12-02T16:45:51.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DE0BxIAL', 'accountid': '001Wt00000PH90cIAD', 'createddate': '2023-11-02T10:00:00.000+0000', 'closeddate': '2023-11-02T14:10:33.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDnt6IAD', 'accountid': '001Wt00000PFt7TIAT', 'createddate': '2023-10-16T09:00:00.000+0000', 'closeddate': '2023-10-16T15:22:17.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDU5iIAH', 'accountid': '#001Wt00000PHVvRIAX', 'createddate': '2023-10-15T09:15:47.000+0000', 'closeddate': '2023-10-15T14:23:52.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzW2IAL', 'accountid': '001Wt00000PGZZoIAP', 'createddate': '2023-10-05T09:45:00.000+0000', 'closeddate': '2023-10-05T16:02:30.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDPSZIA5', 'accountid': '#001Wt00000PGZZoIAP', 'createddate': '2023-10-02T14:15:00.000+0000', 'closeddate': '2023-10-02T14:45:22.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDYUGIA5', 'accountid': '001Wt00000PHVqdIAH', 'createddate': '2023-10-02T09:15:00.000+0000', 'closeddate': '2023-10-02T09:32:45.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDNYoIAP', 'accountid': '001Wt00000PGZZoIAP', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DE0NGIA1', 'accountid': '001Wt00000PGYx5IAH', 'createddate': '2023-09-25T10:30:00.000+0000', 'closeddate': '2023-09-26T12:20:45.000+0000', 'status': 'Closed'}, {'id': '#500Wt00000DDfFcIAL', 'accountid': '001Wt00000PGYx5IAH', 'createddate': '2023-09-22T08:28:00.000+0000', 'closeddate': '2023-09-22T08:43:27.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DE0GnIAL', 'accountid': '001Wt00000PFttwIAD', 'createddate': '2023-09-18T09:45:00.000+0000', 'closeddate': '2023-09-18T09:53:18.000+0000', 'status': 'Closed  '}, {'id': '500Wt00000DE078IAD', 'accountid': '001Wt00000PFttwIAD', 'createddate': '2023-09-16T15:30:00.000+0000', 'closeddate': '2023-09-16T21:27:33.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDz6FIAT', 'accountid': '#001Wt00000PGb5MIAT', 'createddate': '2023-09-03T10:15:00.000+0000', 'closeddate': '2023-09-08T16:25:49.000+0000', 'status': 'Closed '}, {'id': '#500Wt00000DDzpNIAT', 'accountid': '001Wt00000PGb5MIAT', 'createddate': '2023-09-07T16:30:00.000+0000', 'closeddate': '2023-09-07T16:45:30.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDyzpIAD', 'accountid': '001Wt00000PHViZIAX', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDepmIAD', 'accountid': '001Wt00000PFttwIAD', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzsbIAD', 'accountid': '#001Wt00000PGovMIAT', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'status': 'Closed'}, {'id': '#500Wt00000DE02HIAT', 'accountid': '001Wt00000PGcpMIAT', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzuEIAT', 'accountid': '001Wt00000PGcpMIAT', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzUPIA1', 'accountid': '001Wt00000PHVfJIAX', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'status': 'Closed'}], 'var_functions.execute_python:8': 'Date range: 2021-05-04 to 2022-10-26', 'var_functions.list_db:10': ['User', 'Account', 'Contact'], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:24': "['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5', 'var_functions.execute_python:8', 'var_functions.list_db:10', 'var_functions.query_db:14']", 'var_functions.execute_python:30': {'total_cases': 153, 'sample_record': {'id': '#500Wt00000DDDfwIAH', 'accountid': '001Wt00000PFttwIAD', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'status': 'Waiting on Customer'}}, 'var_functions.query_db:32': [{'Id': '001Wt00000PFj4zIAD', 'Name': 'NaviCorp Tech ', 'ShippingState': 'FL'}, {'Id': '001Wt00000PFj50IAD', 'Name': 'FusionTech Systems', 'ShippingState': 'TX'}, {'Id': '#001Wt00000PFluoIAD', 'Name': 'BlueSky Aerospace', 'ShippingState': 'AZ'}, {'Id': '#001Wt00000PFlupIAD', 'Name': 'NeuralWave Technologies', 'ShippingState': 'CA'}, {'Id': '001Wt00000PFrk1IAD', 'Name': 'SkyNet Technologies', 'ShippingState': 'MO'}, {'Id': '001Wt00000PFsjMIAT', 'Name': 'EvoTrend Systems', 'ShippingState': 'OH'}, {'Id': '001Wt00000PFsjOIAT', 'Name': 'QuantumLeap Computing', 'ShippingState': 'NY'}, {'Id': '001Wt00000PFsmZIAT', 'Name': 'EcoVision Engineering', 'ShippingState': 'CO'}, {'Id': '001Wt00000PFsmaIAD', 'Name': 'EcoLite Innovations   ', 'ShippingState': 'MI'}, {'Id': '001Wt00000PFsmbIAD', 'Name': 'Innovative Robotics', 'ShippingState': 'NV'}, {'Id': '#001Wt00000PFsmcIAD', 'Name': 'Nordic HealthTech', 'ShippingState': 'MN'}, {'Id': '001Wt00000PFsmdIAD', 'Name': 'NexGen Biotech', 'ShippingState': 'MA'}, {'Id': '001Wt00000PFt7TIAT', 'Name': 'TerraForm Engineering  ', 'ShippingState': 'CO'}, {'Id': '#001Wt00000PFttwIAD', 'Name': 'Digital Horizon Media', 'ShippingState': 'CA'}, {'Id': '001Wt00000PGGTtIAP', 'Name': 'SecureWise Solutions', 'ShippingState': 'CA'}, {'Id': '#001Wt00000PGGTuIAP', 'Name': 'Horizon Tech Integrations  ', 'ShippingState': 'CA'}, {'Id': '#001Wt00000PGHsyIAH', 'Name': 'Circuit Dynamics Inc.', 'ShippingState': 'FL'}, {'Id': '001Wt00000PGQzcIAH', 'Name': 'UrbanEDGE Innovation', 'ShippingState': 'WA'}, {'Id': '001Wt00000PGR63IAH', 'Name': 'Pioneer Envisions', 'ShippingState': 'WA'}, {'Id': '001Wt00000PGRnYIAX', 'Name': 'AgroSmart Innovations', 'ShippingState': 'IA'}, {'Id': '001Wt00000PGRqjIAH', 'Name': 'DataWave Analytics', 'ShippingState': 'CA'}, {'Id': '001Wt00000PGSwYIAX', 'Name': 'GreenLeaf Engineering  ', 'ShippingState': 'IA'}, {'Id': '001Wt00000PGSwZIAX', 'Name': 'Insight Analytics Group', 'ShippingState': 'FL'}, {'Id': '#001Wt00000PGXrKIAX', 'Name': 'InnovateX Solutions', 'ShippingState': 'WA'}, {'Id': '#001Wt00000PGXrLIAX', 'Name': 'DataGuard Insights', 'ShippingState': 'NY'}, {'Id': '001Wt00000PGXrMIAX', 'Name': 'Innovatech Group', 'ShippingState': 'NY'}, {'Id': '001Wt00000PGXrNIAX', 'Name': 'FutureTech Innovations', 'ShippingState': 'WA'}, {'Id': '#001Wt00000PGYgxIAH', 'Name': 'EcoShield Technologies', 'ShippingState': 'OR'}, {'Id': '001Wt00000PGYx4IAH', 'Name': 'UrbanSmart Inc.', 'ShippingState': 'NY'}, {'Id': '#001Wt00000PGYx5IAH', 'Name': 'Quantum Designs', 'ShippingState': 'MA'}, {'Id': '001Wt00000PGZZnIAP', 'Name': 'SolarWind Innovations', 'ShippingState': 'TX'}, {'Id': '001Wt00000PGZZoIAP', 'Name': 'EnviroTech Solutions', 'ShippingState': 'OR'}, {'Id': '001Wt00000PGZgHIAX', 'Name': 'TechGrove Systems', 'ShippingState': 'UT'}, {'Id': '#001Wt00000PGZmeIAH', 'Name': 'AlphaWave Networks', 'ShippingState': 'TX'}, {'Id': '001Wt00000PGZmfIAH', 'Name': 'Quantum Dynamics LLC', 'ShippingState': 'MI'}, {'Id': '001Wt00000PGaHIIA1', 'Name': 'MetroGrid Networks', 'ShippingState': 'NV'}, {'Id': '001Wt00000PGaNjIAL', 'Name': 'MetaData Analytics', 'ShippingState': 'GA'}, {'Id': '001Wt00000PGaNkIAL', 'Name': 'Horizon Dynamics', 'ShippingState': 'VA'}, {'Id': '#001Wt00000PGaZCIA1', 'Name': 'GreenStar Electronics  ', 'ShippingState': 'OR'}, {'Id': '001Wt00000PGaZDIA1', 'Name': 'Oceanic Innovation Labs  ', 'ShippingState': 'CA'}, {'Id': '#001Wt00000PGb5MIAT', 'Name': 'InnoBuild Constructors', 'ShippingState': 'FL'}, {'Id': '#001Wt00000PGb5NIAT', 'Name': 'SkyLink Communications', 'ShippingState': 'GA'}, {'Id': '001Wt00000PGb5OIAT', 'Name': 'UrbanTech Developments', 'ShippingState': 'IL'}, {'Id': '#001Wt00000PGcFxIAL', 'Name': 'GreenWave Circuits   ', 'ShippingState': 'MI'}, {'Id': '001Wt00000PGccRIAT', 'Name': 'CyberWave Security', 'ShippingState': 'GA'}, {'Id': '001Wt00000PGcpMIAT', 'Name': 'TechBridge Systems', 'ShippingState': 'MO'}, {'Id': '#001Wt00000PGdBuIAL', 'Name': 'TechSavvy Innovations', 'ShippingState': 'WA'}, {'Id': '#001Wt00000PGdwiIAD', 'Name': 'EcoTech Manufacturing', 'ShippingState': 'WA'}, {'Id': '#001Wt00000PGdzxIAD', 'Name': 'AquaSys Controls', 'ShippingState': 'FL'}, {'Id': '001Wt00000PGeJIIA1', 'Name': 'InnoSphere Labs', 'ShippingState': 'MA'}, {'Id': '001Wt00000PGoAaIAL', 'Name': 'TrueNorth Technologies', 'ShippingState': 'NJ'}, {'Id': '#001Wt00000PGovMIAT', 'Name': 'ClearSky Data Solutions', 'ShippingState': 'CO'}, {'Id': '001Wt00000PGtdJIAT', 'Name': 'Quantum Innovations Inc.', 'ShippingState': 'IL'}, {'Id': '001Wt00000PGtdKIAT', 'Name': 'CyberPulse Security', 'ShippingState': 'VA'}, {'Id': '001Wt00000PGtmwIAD', 'Name': 'InfiLink Solutions', 'ShippingState': 'IL'}, {'Id': '001Wt00000PGtmxIAD', 'Name': 'Titan Robotics Group', 'ShippingState': 'TX'}, {'Id': '001Wt00000PGyTIIA1', 'Name': 'GreenTech Dynamics', 'ShippingState': 'CO'}, {'Id': '001Wt00000PGyv0IAD', 'Name': 'Future Innovations LLC   ', 'ShippingState': 'MA'}, {'Id': '001Wt00000PGz2nIAD', 'Name': 'GreenEnergy Solutions', 'ShippingState': 'CO'}, {'Id': '001Wt00000PGzM9IAL', 'Name': 'MediLux Solutions', 'ShippingState': 'GA'}, {'Id': '001Wt00000PGzSaIAL', 'Name': 'TechFusion Inc.', 'ShippingState': 'WA'}, {'Id': '001Wt00000PGzSbIAL', 'Name': 'AquaGuard Solutions   ', 'ShippingState': 'FL'}, {'Id': '001Wt00000PGzVpIAL', 'Name': 'EcoEnergy Solutions', 'ShippingState': 'TX'}, {'Id': '001Wt00000PGzsMIAT', 'Name': 'PrimeEdge Technology   ', 'ShippingState': 'CA'}, {'Id': '001Wt00000PH90cIAD', 'Name': 'InspireTech Consulting', 'ShippingState': 'MA'}, {'Id': '#001Wt00000PH9DRIA1', 'Name': 'SkyLevel Systems ', 'ShippingState': 'FL'}, {'Id': '#001Wt00000PH9ITIA1', 'Name': 'DigitalWave Solutions', 'ShippingState': 'TX'}, {'Id': '#001Wt00000PHHXXIA5', 'Name': 'Innovate Sphere', 'ShippingState': 'TX'}, {'Id': '001Wt00000PHR75IAH', 'Name': 'RenewSys Corp', 'ShippingState': 'OR'}, {'Id': '#001Wt00000PHR8gIAH', 'Name': 'SkyTech Ventures', 'ShippingState': 'AZ'}, {'Id': '001Wt00000PHRF8IAP', 'Name': 'EcoWave Solutions', 'ShippingState': 'NY'}, {'Id': '001Wt00000PHRF9IAP', 'Name': 'Green Circuitry LLC', 'ShippingState': 'WA'}, {'Id': '001Wt00000PHRTeIAP', 'Name': 'Metro Security Systems', 'ShippingState': 'FL'}, {'Id': '#001Wt00000PHRTfIAP', 'Name': 'Vertex Engineering Corp', 'ShippingState': 'FL'}, {'Id': '001Wt00000PHRVGIA5', 'Name': 'AlphaTech Productions', 'ShippingState': 'CA'}, {'Id': '001Wt00000PHRVHIA5', 'Name': 'InnovateGrid Systems', 'ShippingState': 'TX'}, {'Id': '001Wt00000PHRVIIA5', 'Name': 'SkyVista Technologies', 'ShippingState': 'NY'}, {'Id': '001Wt00000PHRbiIAH', 'Name': 'PowerGrid Innovations   ', 'ShippingState': 'GA'}, {'Id': '001Wt00000PHVaUIAX', 'Name': 'TerraSync Solutions', 'ShippingState': 'CA'}, {'Id': '001Wt00000PHVaVIAX', 'Name': 'Precision Circuit Systems', 'ShippingState': 'NY'}, {'Id': '#001Wt00000PHVdhIAH', 'Name': 'NeonTech Industries', 'ShippingState': 'TX'}, {'Id': '#001Wt00000PHVfJIAX', 'Name': 'BrightTech Systems', 'ShippingState': 'MN'}, {'Id': '001Wt00000PHVgvIAH', 'Name': 'Skyline Robotics   ', 'ShippingState': 'CA'}, {'Id': '001Wt00000PHViXIAX', 'Name': 'Nova Healthcare Tech ', 'ShippingState': 'NC'}, {'Id': '001Wt00000PHViYIAX', 'Name': 'BioPulse MedTech', 'ShippingState': 'MD'}, {'Id': '#001Wt00000PHViZIAX', 'Name': 'OmegaDesign Labs', 'ShippingState': 'PA'}, {'Id': '001Wt00000PHViaIAH', 'Name': 'InnovateVibes LLC', 'ShippingState': 'CO'}, {'Id': '001Wt00000PHVk9IAH', 'Name': 'LiftTech Elevations', 'ShippingState': 'NY'}, {'Id': '#001Wt00000PHVkAIAX', 'Name': 'SecureLink Technologies  ', 'ShippingState': 'VA'}, {'Id': '001Wt00000PHVllIAH', 'Name': 'SafetyNet Inc.', 'ShippingState': 'FL'}, {'Id': '001Wt00000PHVnNIAX', 'Name': 'BrightField Ventures', 'ShippingState': 'SC'}, {'Id': '001Wt00000PHVnOIAX', 'Name': 'CraftTech Electronics', 'ShippingState': 'CA'}, {'Id': '001Wt00000PHVozIAH', 'Name': 'TechSphere Design', 'ShippingState': 'NY'}, {'Id': '001Wt00000PHVqbIAH', 'Name': 'Onyx Security Systems', 'ShippingState': 'GA'}, {'Id': '001Wt00000PHVqdIAH', 'Name': 'TechWave Innovations', 'ShippingState': 'CA'}, {'Id': '001Wt00000PHVsDIAX', 'Name': 'NeoGreen Enterprises', 'ShippingState': 'OR'}, {'Id': '001Wt00000PHVtpIAH', 'Name': 'EnergyNova Corp', 'ShippingState': 'TX'}, {'Id': '001Wt00000PHVvRIAX', 'Name': 'AeroFusion Systems', 'ShippingState': 'TX'}, {'Id': '001Wt00000PHVx3IAH', 'Name': 'Altai Innovations', 'ShippingState': 'AZ'}, {'Id': '#001Wt00000PHVyfIAH', 'Name': 'MedTech Advances', 'ShippingState': 'NC'}, {'Id': '001Wt00000PHW0HIAX', 'Name': 'DataStream Analytics', 'ShippingState': 'NY'}]}

exec(code, env_args)
