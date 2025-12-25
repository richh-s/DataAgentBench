code = """import pandas as pd
import json

user_data = pd.read_json(locals()['var_function-call-16896666519348856818'])

def parse_yelping_since(date_str):
    if 'at' in date_str:
        return pd.to_datetime(date_str, format='%B %d, %Y at %I:%M %p', errors='coerce')
    elif ',' in date_str:
        return pd.to_datetime(date_str, format='%d %b %Y, %H:%M', errors='coerce')
    else:
        return pd.to_datetime(date_str, errors='coerce')

user_data['yelping_since_parsed'] = user_data['yelping_since'].apply(parse_yelping_since)
users_2016 = user_data[user_data['yelping_since_parsed'].dt.year == 2016]['user_id'].tolist()

print('__RESULT__:')
print(json.dumps(users_2016))"""

env_args = {'var_function-call-13108768714940623492': [{'_id': '6859a000fe8b31cd7362e2ab', 'name': 'Steps to Learning Montessori Preschool', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-8905274414612016032': [{'yelping_since': '15 Jan 2009, 16:40'}], 'var_function-call-16896666519348856818': 'file_storage/function-call-16896666519348856818.json'}

exec(code, env_args)
