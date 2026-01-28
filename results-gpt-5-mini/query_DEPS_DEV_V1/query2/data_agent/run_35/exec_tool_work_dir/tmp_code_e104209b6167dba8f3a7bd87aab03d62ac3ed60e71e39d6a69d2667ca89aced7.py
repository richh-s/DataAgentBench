code = """import json
# var_call_TOJGtn3efNkjpfVpWIwV1fnz contains the JSON result directly in storage variable, not a file path
data = var_call_TOJGtn3efNkjpfVpWIwV1fnz
# Build final output
final = [{'ProjectName': r['ProjectName'], 'Forks': r['Forks']} for r in data]
print('__RESULT__:')
print(json.dumps(final))"""

env_args = {'var_call_yLsAhTA5bdHMTrzlstkcUKhF': 'file_storage/call_yLsAhTA5bdHMTrzlstkcUKhF.json', 'var_call_ZAWEUlm0qlUdHYqISvwFHbVI': 'file_storage/call_ZAWEUlm0qlUdHYqISvwFHbVI.json', 'var_call_hW65jdsv3GmpdCSlUQsl6fxo': 'file_storage/call_hW65jdsv3GmpdCSlUQsl6fxo.json', 'var_call_ca4KRB3OW4oXuOi0zdpapENt': 'file_storage/call_ca4KRB3OW4oXuOi0zdpapENt.json', 'var_call_xsej0CgJXF5DxxGblASF1tv3': 'file_storage/call_xsej0CgJXF5DxxGblASF1tv3.json', 'var_call_D1crF1iMb1rYajTXGSwUo2mg': 'file_storage/call_D1crF1iMb1rYajTXGSwUo2mg.json', 'var_call_K88euMPheNbF1b3s6HbfkiHw': 'file_storage/call_K88euMPheNbF1b3s6HbfkiHw.json', 'var_call_mEuCUar5vYWMBnLzZvOOb5Xw': 'file_storage/call_mEuCUar5vYWMBnLzZvOOb5Xw.json', 'var_call_TBlV8rB0asYjcC8kFLanPki8': 'file_storage/call_TBlV8rB0asYjcC8kFLanPki8.json', 'var_call_TOJGtn3efNkjpfVpWIwV1fnz': [{'ProjectName': 'mui-org/material-ui', 'Name': '@docly/web', 'Version': '0.1.371', 'Forks': 30522}, {'ProjectName': 'moment/moment', 'Name': '@dollarshaveclub/cli>1.12.0>moment', 'Version': '2.22.2', 'Forks': 7201}, {'ProjectName': 'lodash/lodash', 'Name': '@dwarvesf/react-scripts>0.7.0>lodash._baseclone', 'Version': '3.3.0', 'Forks': 7109}, {'ProjectName': 'react-native-elements/react-native-elements', 'Name': '@dplus/themed', 'Version': '0.0.2', 'Forks': 4623}, {'ProjectName': 'sveltejs/svelte', 'Name': '@dylanvann/svelte', 'Version': '3.25.3', 'Forks': 4091}]}

exec(code, env_args)
