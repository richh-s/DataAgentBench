code = """import json, pandas as pd

df = pd.DataFrame(var_call_m0hG4ENcGiZGgKH0Hn7PSIaB)
# all transfer counts are zero (no owner history in window)
df['transfer_count'] = 0
# choose min transfer_count then smallest agent_id
agent_id = df.sort_values(['transfer_count','agent_id']).iloc[0]['agent_id']
print('__RESULT__:')
print(json.dumps({'Id': agent_id}))"""

env_args = {'var_call_3osUd2YrOkFfiHKg79TcTdbw': [], 'var_call_m4nONanir2LaB3WzyNZyrmwr': [{'cnt': '0'}], 'var_call_m0hG4ENcGiZGgKH0Hn7PSIaB': [{'agent_id': '005Wt000003NBcAIAW', 'cases_handled': '1'}, {'agent_id': '005Wt000003NBykIAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NDJ1IAO', 'cases_handled': '1'}, {'agent_id': '005Wt000003NDqFIAW', 'cases_handled': '1'}, {'agent_id': '005Wt000003NDsUIAW', 'cases_handled': '1'}, {'agent_id': '005Wt000003NEGhIAO', 'cases_handled': '1'}, {'agent_id': '005Wt000003NEzqIAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NFKoIAO', 'cases_handled': '3'}, {'agent_id': '005Wt000003NFr4IAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NGjuIAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NHpeIAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NHsrIAG', 'cases_handled': '2'}, {'agent_id': '005Wt000003NI2XIAW', 'cases_handled': '1'}, {'agent_id': '005Wt000003NINVIA4', 'cases_handled': '2'}, {'agent_id': '005Wt000003NISLIA4', 'cases_handled': '1'}, {'agent_id': '005Wt000003NIVZIA4', 'cases_handled': '1'}, {'agent_id': '005Wt000003NIaQIAW', 'cases_handled': '1'}, {'agent_id': '005Wt000003NIc2IAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NIddIAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NIliIAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NInLIAW', 'cases_handled': '1'}, {'agent_id': '005Wt000003NIvNIAW', 'cases_handled': '1'}, {'agent_id': '005Wt000003NIwzIAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NJ0DIAW', 'cases_handled': '1'}, {'agent_id': '005Wt000003NJ6gIAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NJ8HIAW', 'cases_handled': '3'}, {'agent_id': '005Wt000003NJD9IAO', 'cases_handled': '1'}, {'agent_id': '005Wt000003NJEjIAO', 'cases_handled': '1'}, {'agent_id': '005Wt000003NJTFIA4', 'cases_handled': '1'}, {'agent_id': '005Wt000003NJhlIAG', 'cases_handled': '2'}, {'agent_id': '005Wt000003NJoDIAW', 'cases_handled': '1'}, {'agent_id': '005Wt000003NJrRIAW', 'cases_handled': '1'}], 'var_call_ZdHJKnNjHTN5jfS3dgJLeKaZ': []}

exec(code, env_args)
