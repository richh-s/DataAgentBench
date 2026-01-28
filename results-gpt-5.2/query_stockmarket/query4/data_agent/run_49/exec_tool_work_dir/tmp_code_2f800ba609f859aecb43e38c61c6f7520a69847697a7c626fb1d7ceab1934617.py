code = """import json

def load_json_maybe(x):
    if isinstance(x, str):
        with open(x,'r') as f:
            return json.load(f)
    return x

info = load_json_maybe(var_call_9x43jhvltlIk3SV75Wkfhm1D)
tables = set(load_json_maybe(var_call_2AhcoWPmgTbeg1mwSm0bl5Iu))
nyse_syms = sorted([r['Symbol'] for r in info if r.get('Symbol') in tables])

# pick first 5 alphabetically
picked = nyse_syms[:5]
print('__RESULT__:')
print(json.dumps({'picked': picked, 'n': len(nyse_syms)}))"""

env_args = {'var_call_2AhcoWPmgTbeg1mwSm0bl5Iu': 'file_storage/call_2AhcoWPmgTbeg1mwSm0bl5Iu.json', 'var_call_9x43jhvltlIk3SV75Wkfhm1D': 'file_storage/call_9x43jhvltlIk3SV75Wkfhm1D.json', 'var_call_PcX3URHolGNr3LCrnXyGvtYl': [{'table_name': 'AAAU'}, {'table_name': 'AADR'}, {'table_name': 'AAME'}, {'table_name': 'AAWW'}, {'table_name': 'AAXJ'}], 'var_call_gcCoUDDwmTZgAujoo3GWRYxN': {'ok': True, 'n': 5}, 'var_call_sVFDtSgXuR1uhJiGj3xemzGS': [{'cnt': '2753'}], 'var_call_SJBkav9SANFxwSXYdNgiGg5g': {'n_symbols': 234, 'n_chunks': 1, 'first_chunk': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_call_gHnttgm3rfA2U00yiYMcwMAn': [{'Symbol': 'AEFC'}, {'Symbol': 'AIN'}], 'var_call_Lo4ndOg9ZaTM9TfJcEjdOJ0G': [{'Symbol': 'AEFC'}, {'Symbol': 'AIN'}], 'var_call_30d8enOzVDh5eKqwK2q0KpXt': [{'Symbol': 'AEFC'}, {'Symbol': 'AIN'}], 'var_call_fsIBBTWaAJaId6tIbLGRLceB': {'a': 1}, 'var_call_rGHbRm95iPANQgfszImibk16': [{'Symbol': 'AEFC', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_3IXmuufx6fXKO5izD6G0Y0qe': [{'n': '110', 'mind': '2019-10-24', 'maxd': '2020-04-01'}], 'var_call_LKHFAoBPRs8WVNgIZeZ27IiG': [{'Symbol': 'CVX', 'company_name': 'Chevron Corporation is a leading global energy company involved in the exploration, production, and refining of oil and natural gas, powering industries and communities worldwide.'}, {'Symbol': 'GD', 'company_name': 'General Dynamics Corporation specializes in aerospace and defense, providing advanced technology solutions to governments and commercial customers worldwide.'}, {'Symbol': 'IBM', 'company_name': 'International Business Machines Corporation, commonly known as IBM, is a global leader in technology, specializing in cloud computing, artificial intelligence, and enterprise solutions to drive digital transformation across industries.'}], 'var_call_pidDF3pYBnelBSmGObJ1kVn1': [{'Symbol': 'IBM', 'up_days': '111.0', 'down_days': '136.0'}], 'var_call_ZYErdi38DeZetFzUpUmFjR02': [{'Symbol': 'GD', 'up_days': '134.0', 'down_days': '117.0'}], 'var_call_pZWtkQ0KqKrcXSOWPKhB832C': [{'Symbol': 'CVX', 'up_days': '118.0', 'down_days': '132.0'}], 'var_call_0M6AepY3AKBMkXG8P8UIdFJg': [{'table_name': 'ROAM'}, {'table_name': 'ROBO'}, {'table_name': 'ROBT'}, {'table_name': 'RODE'}, {'table_name': 'RODM'}, {'table_name': 'ROG'}, {'table_name': 'ROKT'}, {'table_name': 'ROL'}, {'table_name': 'ROM'}, {'table_name': 'ROMO'}, {'table_name': 'ROOF'}, {'table_name': 'RORE'}, {'table_name': 'ROSC'}, {'table_name': 'ROUS'}], 'var_call_1eA1YHm0P48Gqa42MazGKUVZ': [], 'var_call_mlk4HhekPfGr28plUfFGpV5U': []}

exec(code, env_args)
