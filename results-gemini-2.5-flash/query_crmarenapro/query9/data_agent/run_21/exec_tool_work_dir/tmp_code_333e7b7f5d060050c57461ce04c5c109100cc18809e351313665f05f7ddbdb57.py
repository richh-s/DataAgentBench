code = """import pandas as pd
import json

case_data = json.load(open(locals()['var_function-call-4909428130866280425'], 'r'))
cases_df = pd.DataFrame(case_data)

cases_df['id'] = cases_df['id'].astype(str).str.replace('#', '', regex=False).str.strip()
cases_df['accountid'] = cases_df['accountid'].astype(str).str.replace('#', '', regex=False).str.strip()
cases_df['createddate'] = pd.to_datetime(cases_df['createddate'], errors='coerce')
cases_df['closeddate'] = pd.to_datetime(cases_df['closeddate'], errors='coerce')

cases_df_closed = cases_df.dropna(subset=['closeddate'])
cases_df_closed['closure_time'] = (cases_df_closed['closeddate'] - cases_df_closed['createddate']).dt.total_seconds() / 3600
result = cases_df_closed[['accountid', 'closure_time']].to_json(orient='records')
print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-4909428130866280425': 'file_storage/function-call-4909428130866280425.json'}

exec(code, env_args)
