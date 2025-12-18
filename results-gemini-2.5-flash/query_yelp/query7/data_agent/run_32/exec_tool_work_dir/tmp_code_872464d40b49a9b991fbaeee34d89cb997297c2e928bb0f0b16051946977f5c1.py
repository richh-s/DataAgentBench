code = """import pandas as pd
import json

user_data = json.load(open(locals()['var_function-call-12866667841927513755']))
df_user = pd.DataFrame(user_data)

# Function to extract year from various date formats
def extract_year(date_str):
    if 'Jan' in date_str or 'Feb' in date_str or 'Mar' in date_str or \
       'Apr' in date_str or 'May' in date_str or 'Jun' in date_str or \
       'Jul' in date_str or 'Aug' in date_str or 'Sep' in date_str or \
       'Oct' in date_str or 'Nov' in date_str or 'Dec' in date_str:
        return pd.to_datetime(date_str, format='%d %b %Y, %H:%M', errors='coerce').year
    elif 'at' in date_str and ',' in date_str:
        return pd.to_datetime(date_str, format='%B %d, %Y at %I:%M %p', errors='coerce').year
    elif '-' in date_str:
        return pd.to_datetime(date_str, format='%Y-%m-%d %H:%M:%S', errors='coerce').year
    return None

df_user['registration_year'] = df_user['yelping_since'].apply(extract_year)
users_2016 = df_user[df_user['registration_year'] == 2016]['user_id'].tolist()

print("__RESULT__:")
print(json.dumps(users_2016))"""

env_args = {'var_function-call-15894947515502659557': [], 'var_function-call-284802155866071807': [], 'var_function-call-10252835108612809372': [{'yelping_since': '15 Jan 2009, 16:40'}, {'yelping_since': '13 Jul 2010, 15:42'}, {'yelping_since': '2010-09-07 23:24:36'}, {'yelping_since': 'October 23, 2011 at 07:47 PM'}, {'yelping_since': '2011-08-30 13:46:26'}], 'var_function-call-12866667841927513755': 'file_storage/function-call-12866667841927513755.json'}

exec(code, env_args)
