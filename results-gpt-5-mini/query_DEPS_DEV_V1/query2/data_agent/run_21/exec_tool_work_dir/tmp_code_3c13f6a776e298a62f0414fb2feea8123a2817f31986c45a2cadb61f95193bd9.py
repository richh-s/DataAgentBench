code = """import json
# var_call_mK5Yt9LL1mUeV4BqC0c5wFUy is a storage key containing the JSON result directly as a Python list variable
# According to instruction, storage variables are available as variables with that name. We'll try to access it.
try:
    data = var_call_mK5Yt9LL1mUeV4BqC0c5wFUy
except NameError:
    # fallback: load from file if path
    import os
    path = 'var_call_mK5Yt9LL1mUeV4BqC0c5wFUy'
    if os.path.exists(path):
        with open(path,'r',encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = []
# data should be a list
records = data
seen = {}
for rec in records:
    pname = rec.get('ProjectName')
    if not pname:
        continue
    if pname in seen:
        if rec['Forks'] > seen[pname]['Forks']:
            seen[pname] = rec
    else:
        seen[pname] = rec
final = list(seen.values())
final.sort(key=lambda x: x['Forks'], reverse=True)
final = final[:5]
print("__RESULT__:")
print(json.dumps(final))"""

env_args = {'var_call_HEzdcz70IjrP9lRgEgpSAqfY': 'file_storage/call_HEzdcz70IjrP9lRgEgpSAqfY.json', 'var_call_XyVtwkmcTawWXvXXtuY1XOGs': 'file_storage/call_XyVtwkmcTawWXvXXtuY1XOGs.json', 'var_call_4C61MtgpdwSLhWSyl0zVwwny': 'file_storage/call_4C61MtgpdwSLhWSyl0zVwwny.json', 'var_call_NHugqj7ugVKcE6M5w7ByHebC': 'file_storage/call_NHugqj7ugVKcE6M5w7ByHebC.json', 'var_call_0Yio9djOf8WN2eIIwHwi7GWg': 'file_storage/call_0Yio9djOf8WN2eIIwHwi7GWg.json', 'var_call_jMQP6mA54MC2pwJLxqYCD0zQ': 'file_storage/call_jMQP6mA54MC2pwJLxqYCD0zQ.json', 'var_call_mK5Yt9LL1mUeV4BqC0c5wFUy': [{'ProjectName': 'rails/rails', 'Forks': 55319, 'Project_Information': 'The project is hosted on GitHub under the name rails/rails, which currently has an open issues count of 1199, a stars count of 55319, and a forks count of 21423.'}, {'ProjectName': 'moment/moment', 'Forks': 47549, 'Project_Information': 'The project moment/moment on GitHub has an open issues count of 305, a stars count of 47549, and a forks count of 7201, making it a popular choice among developers for handling date and time in JavaScript.'}, {'ProjectName': 'tj/co', 'Forks': 25437, 'Project_Information': 'The project tj/commander.js is hosted on GitHub and currently has an open issues count of 20, along with a notable stars count of 25437 and a forks count of 1739.'}, {'ProjectName': 'tj/commander.js', 'Forks': 25437, 'Project_Information': 'The project tj/commander.js is hosted on GitHub and currently has an open issues count of 20, along with a notable stars count of 25437 and a forks count of 1739.'}, {'ProjectName': 'medusajs/medusa', 'Forks': 20285, 'Project_Information': 'The project medusajs/medusa on GitHub has an open issues count of 384, a stars count of 20285, and a forks count of 1699, making it a popular choice among developers for building e-commerce applications.'}]}

exec(code, env_args)
