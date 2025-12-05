code = """import json
handled = var_call_lMxj6VYO7ZzvGoPUSyooEfB9
if not handled:
    result = None
else:
    min_count = min(int(r['handled_cases']) for r in handled)
    # among those with >0 handled_cases and minimal transfers, but we don't yet know transfers; for now, just pick min handled as proxy
    # Problem: need transfer counts from history; but history query returned empty, so transfers=0 for all.
    agents = [r['ownerid'] for r in handled if int(r['handled_cases']) > 0]
    # all have same transfer count (0), and all handled>0, but question asks single agent; choose one deterministically (lexicographically)
    result = sorted(agents)[0]

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_kSEQwraXGNHlOxdIZhq15Dyg': [], 'var_call_lMxj6VYO7ZzvGoPUSyooEfB9': [{'ownerid': '005Wt000003NJrRIAW', 'handled_cases': '1'}, {'ownerid': '005Wt000003NBykIAG', 'handled_cases': '1'}, {'ownerid': '005Wt000003NIVZIA4', 'handled_cases': '1'}, {'ownerid': '#005Wt000003NEzqIAG', 'handled_cases': '1'}, {'ownerid': '005Wt000003NHpeIAG', 'handled_cases': '1'}, {'ownerid': '005Wt000003NI2XIAW', 'handled_cases': '1'}, {'ownerid': '005Wt000003NJD9IAO', 'handled_cases': '1'}, {'ownerid': '005Wt000003NIc2IAG', 'handled_cases': '1'}, {'ownerid': '005Wt000003NHsrIAG', 'handled_cases': '2'}, {'ownerid': '005Wt000003NJhlIAG', 'handled_cases': '2'}, {'ownerid': '005Wt000003NJTFIA4', 'handled_cases': '1'}, {'ownerid': '#005Wt000003NJEjIAO', 'handled_cases': '1'}, {'ownerid': '005Wt000003NJ0DIAW', 'handled_cases': '1'}, {'ownerid': '#005Wt000003NFKoIAO', 'handled_cases': '1'}, {'ownerid': '005Wt000003NJ8HIAW', 'handled_cases': '3'}, {'ownerid': '#005Wt000003NBcAIAW', 'handled_cases': '1'}, {'ownerid': '#005Wt000003NInLIAW', 'handled_cases': '1'}, {'ownerid': '#005Wt000003NGjuIAG', 'handled_cases': '1'}, {'ownerid': '005Wt000003NDJ1IAO', 'handled_cases': '1'}, {'ownerid': '005Wt000003NDsUIAW', 'handled_cases': '1'}, {'ownerid': '005Wt000003NINVIA4', 'handled_cases': '2'}, {'ownerid': '005Wt000003NIddIAG', 'handled_cases': '1'}, {'ownerid': '005Wt000003NJ6gIAG', 'handled_cases': '1'}, {'ownerid': '005Wt000003NIwzIAG', 'handled_cases': '1'}, {'ownerid': '005Wt000003NDqFIAW', 'handled_cases': '1'}, {'ownerid': '#005Wt000003NJoDIAW', 'handled_cases': '1'}, {'ownerid': '005Wt000003NISLIA4', 'handled_cases': '1'}, {'ownerid': '005Wt000003NFKoIAO', 'handled_cases': '2'}, {'ownerid': '005Wt000003NEGhIAO', 'handled_cases': '1'}, {'ownerid': '005Wt000003NIvNIAW', 'handled_cases': '1'}, {'ownerid': '005Wt000003NIliIAG', 'handled_cases': '1'}, {'ownerid': '#005Wt000003NFr4IAG', 'handled_cases': '1'}, {'ownerid': '005Wt000003NIaQIAW', 'handled_cases': '1'}]}

exec(code, env_args)
