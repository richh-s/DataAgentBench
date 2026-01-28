code = """import json
import pandas as pd
from datetime import datetime, timedelta

# Load the full data from the file
data_file = var_functions.query_db_12
with open(data_file, 'r') as f:
    case_history = json.load(f)

print(f"Number of records loaded: {len(case_history)}")

# Convert to DataFrame
df = pd.DataFrame(case_history)
print(f"DataFrame shape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")
print("\nFirst 5 records:")
print(df.head())

# Let's check unique field values
print(f"\nUnique fields: {df['field__c'].unique()}")
print(f"Sample oldvalue__c: {df['oldvalue__c'].unique()[:10]}")
print(f"Sample newvalue__c: {df['newvalue__c'].unique()[:10]}")"""

env_args = {'var_functions.list_db:0': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:2': [], 'var_functions.query_db:4': [], 'var_functions.list_db:6': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:8': [{'column_name': 'id', 'data_type': 'text'}, {'column_name': 'caseid__c', 'data_type': 'text'}, {'column_name': 'oldvalue__c', 'data_type': 'text'}, {'column_name': 'newvalue__c', 'data_type': 'text'}, {'column_name': 'createddate', 'data_type': 'text'}, {'column_name': 'field__c', 'data_type': 'text'}], 'var_functions.query_db:10': [{'field__c': 'Case Closed'}, {'field__c': 'Case Creation'}, {'field__c': 'Owner Assignment'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
