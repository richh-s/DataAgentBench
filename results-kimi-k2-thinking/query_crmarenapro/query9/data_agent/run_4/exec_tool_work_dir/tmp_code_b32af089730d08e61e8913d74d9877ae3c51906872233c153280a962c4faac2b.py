code = """import json
import pandas as pd
import numpy as np

# Reload data to verify results
case_file_path = locals()['var_functions.query_db:9']
with open(case_file_path, 'r') as f:
    cases_data = json.load(f)
df_cases = pd.DataFrame(cases_data)

# Load account data
accounts_data = locals()['var_functions.query_db:10']
df_accounts = pd.DataFrame(accounts_data)

# Find all states and their case counts to ensure we have complete picture
df_cases['accountid_clean'] = df_cases['accountid'].str.replace('#', '', regex=False)
df_accounts['Id_clean'] = df_accounts['Id'].str.replace('#', '', regex=False)

df_cases['status_clean'] = df_cases['status'].str.strip()
df_cases = df_cases[df_cases['status_clean'] == 'Closed'].copy()

# Convert dates
for col in ['createddate', 'closeddate']:
    df_cases[col] = df_cases[col].str.replace(r'\.\d{3}\+\d{4}$', '', regex=True)
    df_cases[col] = pd.to_datetime(df_cases[col])

# Filter date range
end_date = pd.to_datetime('2022-10-26')
start_date = pd.to_datetime('2021-04-26')

df_cases_filtered = df_cases[
    (df_cases['closeddate'] >= start_date) & 
    (df_cases['closeddate'] <= end_date)
].copy()

# Join with accounts
df_merged = df_cases_filtered.merge(
    df_accounts[['Id_clean', 'ShippingState']],
    left_on='accountid_clean',
    right_on='Id_clean',
    how='inner'
)

df_merged['ShippingState_clean'] = df_merged['ShippingState'].str.strip()
df_merged['closure_hours'] = (df_merged['closeddate'] - df_merged['createddate']).dt.total_seconds() / 3600

# Get all state stats
all_state_stats = df_merged.groupby('ShippingState_clean').agg({
    'closure_hours': ['mean', 'count', 'std']
})
all_state_stats.columns = ['avg_closure_hours', 'case_count', 'std_closure_hours']
all_state_stats = all_state_stats.reset_index()

# Fill NaN std with 0
all_state_stats['std_closure_hours'] = all_state_stats['std_closure_hours'].fillna(0)

# Only keep states with at least 3 cases
all_state_stats_valid = all_state_stats[all_state_stats['case_count'] >= 3].copy()
all_state_stats_valid = all_state_stats_valid.sort_values('avg_closure_hours')

print('__RESULT__:')
result = {
    'top_state': all_state_stats_valid.iloc[0]['ShippingState_clean'] if len(all_state_stats_valid) > 0 else None,
    'state_stats': all_state_stats_valid.to_dict('records'),
    'total_states_analyzed': len(all_state_stats_valid)
}
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:2': [{'id': '500Wt00000DDNYoIAP', 'accountid': '001Wt00000PGZZoIAP', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDPIsIAP', 'accountid': '#001Wt00000PGRnYIAX', 'createddate': '2022-08-05T14:30:00.000+0000', 'closeddate': '2022-08-05T14:39:32.000+0000', 'status': 'Closed '}, {'id': '500Wt00000DDPSZIA5', 'accountid': '#001Wt00000PGZZoIAP', 'createddate': '2023-10-02T14:15:00.000+0000', 'closeddate': '2023-10-02T14:45:22.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDPsPIAX', 'accountid': '#001Wt00000PGHsyIAH', 'createddate': '2023-04-05T17:51:00.000+0000', 'closeddate': '2023-04-06T11:30:54.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDQRsIAP', 'accountid': '001Wt00000PGzM9IAL', 'createddate': '2023-03-08T06:49:00.000+0000', 'closeddate': '2023-03-08T07:07:30.000+0000', 'status': 'Closed'}, {'id': '#500Wt00000DDTERIA5', 'accountid': '001Wt00000PGzSaIAL', 'createddate': '2022-03-10T09:30:00.000+0000', 'closeddate': '2022-03-13T09:45:27.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDU5iIAH', 'accountid': '#001Wt00000PHVvRIAX', 'createddate': '2023-10-15T09:15:47.000+0000', 'closeddate': '2023-10-15T14:23:52.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDYUGIA5', 'accountid': '001Wt00000PHVqdIAH', 'createddate': '2023-10-02T09:15:00.000+0000', 'closeddate': '2023-10-02T09:32:45.000+0000', 'status': 'Closed'}, {'id': '#500Wt00000DDYdwIAH', 'accountid': '001Wt00000PFj4zIAD', 'createddate': '2022-02-03T14:30:00.000+0000', 'closeddate': '2022-02-03T14:46:56.000+0000', 'status': 'Closed'}, {'id': '#500Wt00000DDYpHIAX', 'accountid': '#001Wt00000PHHXXIA5', 'createddate': '2022-09-05T11:15:00.000+0000', 'closeddate': '2022-09-05T11:42:09.000+0000', 'status': 'Closed'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['User', 'Account', 'Contact'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:10': [{'Id': '001Wt00000PFj4zIAD', 'Name': 'NaviCorp Tech ', 'ShippingState': 'FL'}, {'Id': '001Wt00000PFj50IAD', 'Name': 'FusionTech Systems', 'ShippingState': 'TX'}, {'Id': '#001Wt00000PFluoIAD', 'Name': 'BlueSky Aerospace', 'ShippingState': 'AZ'}, {'Id': '#001Wt00000PFlupIAD', 'Name': 'NeuralWave Technologies', 'ShippingState': 'CA'}, {'Id': '001Wt00000PFrk1IAD', 'Name': 'SkyNet Technologies', 'ShippingState': 'MO'}, {'Id': '001Wt00000PFsjMIAT', 'Name': 'EvoTrend Systems', 'ShippingState': 'OH'}, {'Id': '001Wt00000PFsjOIAT', 'Name': 'QuantumLeap Computing', 'ShippingState': 'NY'}, {'Id': '001Wt00000PFsmZIAT', 'Name': 'EcoVision Engineering', 'ShippingState': 'CO'}, {'Id': '001Wt00000PFsmaIAD', 'Name': 'EcoLite Innovations   ', 'ShippingState': 'MI'}, {'Id': '001Wt00000PFsmbIAD', 'Name': 'Innovative Robotics', 'ShippingState': 'NV'}, {'Id': '#001Wt00000PFsmcIAD', 'Name': 'Nordic HealthTech', 'ShippingState': 'MN'}, {'Id': '001Wt00000PFsmdIAD', 'Name': 'NexGen Biotech', 'ShippingState': 'MA'}, {'Id': '001Wt00000PFt7TIAT', 'Name': 'TerraForm Engineering  ', 'ShippingState': 'CO'}, {'Id': '#001Wt00000PFttwIAD', 'Name': 'Digital Horizon Media', 'ShippingState': 'CA'}, {'Id': '001Wt00000PGGTtIAP', 'Name': 'SecureWise Solutions', 'ShippingState': 'CA'}, {'Id': '#001Wt00000PGGTuIAP', 'Name': 'Horizon Tech Integrations  ', 'ShippingState': 'CA'}, {'Id': '#001Wt00000PGHsyIAH', 'Name': 'Circuit Dynamics Inc.', 'ShippingState': 'FL'}, {'Id': '001Wt00000PGQzcIAH', 'Name': 'UrbanEDGE Innovation', 'ShippingState': 'WA'}, {'Id': '001Wt00000PGR63IAH', 'Name': 'Pioneer Envisions', 'ShippingState': 'WA'}, {'Id': '001Wt00000PGRnYIAX', 'Name': 'AgroSmart Innovations', 'ShippingState': 'IA'}, {'Id': '001Wt00000PGRqjIAH', 'Name': 'DataWave Analytics', 'ShippingState': 'CA'}, {'Id': '001Wt00000PGSwYIAX', 'Name': 'GreenLeaf Engineering  ', 'ShippingState': 'IA'}, {'Id': '001Wt00000PGSwZIAX', 'Name': 'Insight Analytics Group', 'ShippingState': 'FL'}, {'Id': '#001Wt00000PGXrKIAX', 'Name': 'InnovateX Solutions', 'ShippingState': 'WA'}, {'Id': '#001Wt00000PGXrLIAX', 'Name': 'DataGuard Insights', 'ShippingState': 'NY'}, {'Id': '001Wt00000PGXrMIAX', 'Name': 'Innovatech Group', 'ShippingState': 'NY'}, {'Id': '001Wt00000PGXrNIAX', 'Name': 'FutureTech Innovations', 'ShippingState': 'WA'}, {'Id': '#001Wt00000PGYgxIAH', 'Name': 'EcoShield Technologies', 'ShippingState': 'OR'}, {'Id': '001Wt00000PGYx4IAH', 'Name': 'UrbanSmart Inc.', 'ShippingState': 'NY'}, {'Id': '#001Wt00000PGYx5IAH', 'Name': 'Quantum Designs', 'ShippingState': 'MA'}, {'Id': '001Wt00000PGZZnIAP', 'Name': 'SolarWind Innovations', 'ShippingState': 'TX'}, {'Id': '001Wt00000PGZZoIAP', 'Name': 'EnviroTech Solutions', 'ShippingState': 'OR'}, {'Id': '001Wt00000PGZgHIAX', 'Name': 'TechGrove Systems', 'ShippingState': 'UT'}, {'Id': '#001Wt00000PGZmeIAH', 'Name': 'AlphaWave Networks', 'ShippingState': 'TX'}, {'Id': '001Wt00000PGZmfIAH', 'Name': 'Quantum Dynamics LLC', 'ShippingState': 'MI'}, {'Id': '001Wt00000PGaHIIA1', 'Name': 'MetroGrid Networks', 'ShippingState': 'NV'}, {'Id': '001Wt00000PGaNjIAL', 'Name': 'MetaData Analytics', 'ShippingState': 'GA'}, {'Id': '001Wt00000PGaNkIAL', 'Name': 'Horizon Dynamics', 'ShippingState': 'VA'}, {'Id': '#001Wt00000PGaZCIA1', 'Name': 'GreenStar Electronics  ', 'ShippingState': 'OR'}, {'Id': '001Wt00000PGaZDIA1', 'Name': 'Oceanic Innovation Labs  ', 'ShippingState': 'CA'}, {'Id': '#001Wt00000PGb5MIAT', 'Name': 'InnoBuild Constructors', 'ShippingState': 'FL'}, {'Id': '#001Wt00000PGb5NIAT', 'Name': 'SkyLink Communications', 'ShippingState': 'GA'}, {'Id': '001Wt00000PGb5OIAT', 'Name': 'UrbanTech Developments', 'ShippingState': 'IL'}, {'Id': '#001Wt00000PGcFxIAL', 'Name': 'GreenWave Circuits   ', 'ShippingState': 'MI'}, {'Id': '001Wt00000PGccRIAT', 'Name': 'CyberWave Security', 'ShippingState': 'GA'}, {'Id': '001Wt00000PGcpMIAT', 'Name': 'TechBridge Systems', 'ShippingState': 'MO'}, {'Id': '#001Wt00000PGdBuIAL', 'Name': 'TechSavvy Innovations', 'ShippingState': 'WA'}, {'Id': '#001Wt00000PGdwiIAD', 'Name': 'EcoTech Manufacturing', 'ShippingState': 'WA'}, {'Id': '#001Wt00000PGdzxIAD', 'Name': 'AquaSys Controls', 'ShippingState': 'FL'}, {'Id': '001Wt00000PGeJIIA1', 'Name': 'InnoSphere Labs', 'ShippingState': 'MA'}, {'Id': '001Wt00000PGoAaIAL', 'Name': 'TrueNorth Technologies', 'ShippingState': 'NJ'}, {'Id': '#001Wt00000PGovMIAT', 'Name': 'ClearSky Data Solutions', 'ShippingState': 'CO'}, {'Id': '001Wt00000PGtdJIAT', 'Name': 'Quantum Innovations Inc.', 'ShippingState': 'IL'}, {'Id': '001Wt00000PGtdKIAT', 'Name': 'CyberPulse Security', 'ShippingState': 'VA'}, {'Id': '001Wt00000PGtmwIAD', 'Name': 'InfiLink Solutions', 'ShippingState': 'IL'}, {'Id': '001Wt00000PGtmxIAD', 'Name': 'Titan Robotics Group', 'ShippingState': 'TX'}, {'Id': '001Wt00000PGyTIIA1', 'Name': 'GreenTech Dynamics', 'ShippingState': 'CO'}, {'Id': '001Wt00000PGyv0IAD', 'Name': 'Future Innovations LLC   ', 'ShippingState': 'MA'}, {'Id': '001Wt00000PGz2nIAD', 'Name': 'GreenEnergy Solutions', 'ShippingState': 'CO'}, {'Id': '001Wt00000PGzM9IAL', 'Name': 'MediLux Solutions', 'ShippingState': 'GA'}, {'Id': '001Wt00000PGzSaIAL', 'Name': 'TechFusion Inc.', 'ShippingState': 'WA'}, {'Id': '001Wt00000PGzSbIAL', 'Name': 'AquaGuard Solutions   ', 'ShippingState': 'FL'}, {'Id': '001Wt00000PGzVpIAL', 'Name': 'EcoEnergy Solutions', 'ShippingState': 'TX'}, {'Id': '001Wt00000PGzsMIAT', 'Name': 'PrimeEdge Technology   ', 'ShippingState': 'CA'}, {'Id': '001Wt00000PH90cIAD', 'Name': 'InspireTech Consulting', 'ShippingState': 'MA'}, {'Id': '#001Wt00000PH9DRIA1', 'Name': 'SkyLevel Systems ', 'ShippingState': 'FL'}, {'Id': '#001Wt00000PH9ITIA1', 'Name': 'DigitalWave Solutions', 'ShippingState': 'TX'}, {'Id': '#001Wt00000PHHXXIA5', 'Name': 'Innovate Sphere', 'ShippingState': 'TX'}, {'Id': '001Wt00000PHR75IAH', 'Name': 'RenewSys Corp', 'ShippingState': 'OR'}, {'Id': '#001Wt00000PHR8gIAH', 'Name': 'SkyTech Ventures', 'ShippingState': 'AZ'}, {'Id': '001Wt00000PHRF8IAP', 'Name': 'EcoWave Solutions', 'ShippingState': 'NY'}, {'Id': '001Wt00000PHRF9IAP', 'Name': 'Green Circuitry LLC', 'ShippingState': 'WA'}, {'Id': '001Wt00000PHRTeIAP', 'Name': 'Metro Security Systems', 'ShippingState': 'FL'}, {'Id': '#001Wt00000PHRTfIAP', 'Name': 'Vertex Engineering Corp', 'ShippingState': 'FL'}, {'Id': '001Wt00000PHRVGIA5', 'Name': 'AlphaTech Productions', 'ShippingState': 'CA'}, {'Id': '001Wt00000PHRVHIA5', 'Name': 'InnovateGrid Systems', 'ShippingState': 'TX'}, {'Id': '001Wt00000PHRVIIA5', 'Name': 'SkyVista Technologies', 'ShippingState': 'NY'}, {'Id': '001Wt00000PHRbiIAH', 'Name': 'PowerGrid Innovations   ', 'ShippingState': 'GA'}, {'Id': '001Wt00000PHVaUIAX', 'Name': 'TerraSync Solutions', 'ShippingState': 'CA'}, {'Id': '001Wt00000PHVaVIAX', 'Name': 'Precision Circuit Systems', 'ShippingState': 'NY'}, {'Id': '#001Wt00000PHVdhIAH', 'Name': 'NeonTech Industries', 'ShippingState': 'TX'}, {'Id': '#001Wt00000PHVfJIAX', 'Name': 'BrightTech Systems', 'ShippingState': 'MN'}, {'Id': '001Wt00000PHVgvIAH', 'Name': 'Skyline Robotics   ', 'ShippingState': 'CA'}, {'Id': '001Wt00000PHViXIAX', 'Name': 'Nova Healthcare Tech ', 'ShippingState': 'NC'}, {'Id': '001Wt00000PHViYIAX', 'Name': 'BioPulse MedTech', 'ShippingState': 'MD'}, {'Id': '#001Wt00000PHViZIAX', 'Name': 'OmegaDesign Labs', 'ShippingState': 'PA'}, {'Id': '001Wt00000PHViaIAH', 'Name': 'InnovateVibes LLC', 'ShippingState': 'CO'}, {'Id': '001Wt00000PHVk9IAH', 'Name': 'LiftTech Elevations', 'ShippingState': 'NY'}, {'Id': '#001Wt00000PHVkAIAX', 'Name': 'SecureLink Technologies  ', 'ShippingState': 'VA'}, {'Id': '001Wt00000PHVllIAH', 'Name': 'SafetyNet Inc.', 'ShippingState': 'FL'}, {'Id': '001Wt00000PHVnNIAX', 'Name': 'BrightField Ventures', 'ShippingState': 'SC'}, {'Id': '001Wt00000PHVnOIAX', 'Name': 'CraftTech Electronics', 'ShippingState': 'CA'}, {'Id': '001Wt00000PHVozIAH', 'Name': 'TechSphere Design', 'ShippingState': 'NY'}, {'Id': '001Wt00000PHVqbIAH', 'Name': 'Onyx Security Systems', 'ShippingState': 'GA'}, {'Id': '001Wt00000PHVqdIAH', 'Name': 'TechWave Innovations', 'ShippingState': 'CA'}, {'Id': '001Wt00000PHVsDIAX', 'Name': 'NeoGreen Enterprises', 'ShippingState': 'OR'}, {'Id': '001Wt00000PHVtpIAH', 'Name': 'EnergyNova Corp', 'ShippingState': 'TX'}, {'Id': '001Wt00000PHVvRIAX', 'Name': 'AeroFusion Systems', 'ShippingState': 'TX'}, {'Id': '001Wt00000PHVx3IAH', 'Name': 'Altai Innovations', 'ShippingState': 'AZ'}, {'Id': '#001Wt00000PHVyfIAH', 'Name': 'MedTech Advances', 'ShippingState': 'NC'}, {'Id': '001Wt00000PHW0HIAX', 'Name': 'DataStream Analytics', 'ShippingState': 'NY'}], 'var_functions.execute_python:16': [{'ShippingState_clean': 'TX', 'avg_closure_hours': 1.19, 'case_count': 5}, {'ShippingState_clean': 'FL', 'avg_closure_hours': 1.32, 'case_count': 3}, {'ShippingState_clean': 'IA', 'avg_closure_hours': 1.64, 'case_count': 3}, {'ShippingState_clean': 'OR', 'avg_closure_hours': 4.9, 'case_count': 3}]}

exec(code, env_args)
