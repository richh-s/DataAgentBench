code = """import json
# prepare a clear final answer: total funding amount
res = var_call_lqKgUi3BF62YojIhWiMUZO87
total = res['total_funding']
print('__RESULT__:')
print(json.dumps({'total_funding_for_park_projects_completed_in_2022': total}))"""

env_args = {'var_call_V4vF7nwAMnAbiopKMftn913k': ['civic_docs'], 'var_call_zhqmXNrCRCQ3GsnKQ7jhMenX': ['Funding'], 'var_call_V2Ly6OD6obg5ajtxJc9hBho4': 'file_storage/call_V2Ly6OD6obg5ajtxJc9hBho4.json', 'var_call_hpPReWfvyf7lehCWFK0cGfHh': 'file_storage/call_V2Ly6OD6obg5ajtxJc9hBho4.json', 'var_call_38i97AxeFe4LtdSqT17QEvSZ': ['Bluffs Park Shade Structure', 'Malibu Park Drainage Improvements', 'need of replacing at Malibu Bluffs Park', 'permanent skate park located on the Crummer/Case Court parcel adjacent', 'the Malibu Park Drainage', 'to Malibu Bluffs Park. The project would include parking and additional site'], 'var_call_bFWevv3m4UiSTymHbwzrNNrc': 'file_storage/call_bFWevv3m4UiSTymHbwzrNNrc.json', 'var_call_lqKgUi3BF62YojIhWiMUZO87': {'park_projects_found': ['Bluffs Park Shade Structure', 'Malibu Park Drainage Improvements', 'need of replacing at Malibu Bluffs Park', 'permanent skate park located on the Crummer/Case Court parcel adjacent', 'the Malibu Park Drainage', 'to Malibu Bluffs Park. The project would include parking and additional site'], 'matched_funding_records': [['Bluffs Park Shade Structure', 21000], ['Bluffs Park Workout Station', 39000], ['Malibu Park Drainage Improvements', 17000], ['Malibu Park Resurfacing Project', 14000], ['Malibu Park Storm Drain Repairs', 50000], ['Permanent Skate Park', 97000]], 'total_funding': 238000}}

exec(code, env_args)
