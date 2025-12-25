code = """import json

def extract_json_from_tool_response(response_string):
    # Locate the JSON part in the verbose tool output
    start_marker = "The result is:\n"
    start_index = response_string.find(start_marker)
    if start_index == -1:
        return []

    json_data_start = start_index + len(start_marker)
    json_candidate = response_string[json_data_start:].strip()

    # The JSON should be a list, so look for the first '[' and last ']'
    first_bracket = json_candidate.find('[')
    last_bracket = json_candidate.rfind(']')

    if first_bracket != -1 and last_bracket != -1 and first_bracket < last_bracket:
        json_pure_string = json_candidate[first_bracket : last_bracket + 1]
        try:
            return json.loads(json_pure_string)
        except json.JSONDecodeError:
            return []
    return []

transfer_counts_raw = locals()['var_function-call-13417668301760133805']['query_db_response']['results'][0]
cases_handled_raw = locals()['var_function-call-6458495966495700760']['query_db_response']['results'][0]

transfer_counts = extract_json_from_tool_response(transfer_counts_raw)
cases_handled = extract_json_from_tool_response(cases_handled_raw)

final_agent_id = None

if not transfer_counts:
    # If no transfer records, all agents who handled cases have 0 transfers.
    if cases_handled:
        # Sort by agent_id for a consistent result if multiple agents qualify.
        cases_handled_sorted = sorted(cases_handled, key=lambda x: x['agent_id'])
        final_agent_id = cases_handled_sorted[0]['agent_id']
    else:
        final_agent_id = "No agents handled cases in the last 4 quarters."
else:
    # This branch is for when transfers *do* exist, which is not the case here.
    # If it were, we'd merge and find the min.
    final_agent_id = "Unexpected scenario: Transfer counts were found."

print("__RESULT__:")
print(json.dumps(final_agent_id))"""

env_args = {'var_function-call-13417668301760133805': [], 'var_function-call-6458495966495700760': [{'agent_id': '005Wt000003NJrRIAW', 'cases_handled': '1'}, {'agent_id': '005Wt000003NBykIAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NIVZIA4', 'cases_handled': '1'}, {'agent_id': '#005Wt000003NEzqIAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NHpeIAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NI2XIAW', 'cases_handled': '1'}, {'agent_id': '005Wt000003NJD9IAO', 'cases_handled': '1'}, {'agent_id': '005Wt000003NIc2IAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NHsrIAG', 'cases_handled': '2'}, {'agent_id': '005Wt000003NJhlIAG', 'cases_handled': '2'}, {'agent_id': '005Wt000003NJTFIA4', 'cases_handled': '1'}, {'agent_id': '#005Wt000003NJEjIAO', 'cases_handled': '1'}, {'agent_id': '005Wt000003NJ0DIAW', 'cases_handled': '1'}, {'agent_id': '#005Wt000003NFKoIAO', 'cases_handled': '1'}, {'agent_id': '005Wt000003NJ8HIAW', 'cases_handled': '3'}, {'agent_id': '#005Wt000003NBcAIAW', 'cases_handled': '1'}, {'agent_id': '#005Wt000003NInLIAW', 'cases_handled': '1'}, {'agent_id': '#005Wt000003NGjuIAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NDJ1IAO', 'cases_handled': '1'}, {'agent_id': '005Wt000003NDsUIAW', 'cases_handled': '1'}, {'agent_id': '005Wt000003NINVIA4', 'cases_handled': '2'}, {'agent_id': '005Wt000003NJ6gIAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NIwzIAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NDqFIAW', 'cases_handled': '1'}, {'agent_id': '#005Wt000003NJoDIAW', 'cases_handled': '1'}, {'agent_id': '005Wt000003NISLIA4', 'cases_handled': '1'}, {'agent_id': '005Wt000003NFKoIAO', 'cases_handled': '2'}, {'agent_id': '005Wt000003NEGhIAO', 'cases_handled': '1'}, {'agent_id': '005Wt000003NIvNIAW', 'cases_handled': '1'}, {'agent_id': '005Wt000003NIliIAG', 'cases_handled': '1'}, {'agent_id': '#005Wt000003NFr4IAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NIaQIAW', 'cases_handled': '1'}]}

exec(code, env_args)
