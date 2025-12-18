code = """import json
import pandas as pd

# Load the result from the previous execute_python call
ema_results = json.loads(locals()['var_function-call-2487011880571689373'])
df_ema = pd.DataFrame(ema_results)

# Get unique CPC group codes
cpc_codes = df_ema['cpc_group_code'].unique().tolist()

# Prepare the list of codes for the SQL query (PostgreSQL requires single quotes for string literals)
cpc_codes_str = ', '.join([f"'{code}'" for code in cpc_codes])

print("__RESULT__:")
print(json.dumps(cpc_codes_str))"""

env_args = {'var_function-call-13693480272750509533': 'file_storage/function-call-13693480272750509533.json', 'var_function-call-11158641396443767350': [{'cpc_group_code': 'A43B13/2', 'best_year': 2016.0, 'highest_ema': 1.0}, {'cpc_group_code': 'A43B17/', 'best_year': 2016.0, 'highest_ema': 2.0}, {'cpc_group_code': 'A43B7/', 'best_year': 2016.0, 'highest_ema': 2.0}, {'cpc_group_code': 'A61F5/', 'best_year': 2016.0, 'highest_ema': 2.0}, {'cpc_group_code': 'A61F5/01', 'best_year': 2016.0, 'highest_ema': 4.0}, {'cpc_group_code': 'B60K6/4', 'best_year': 2013.0, 'highest_ema': 1.0}, {'cpc_group_code': 'B60W30/1', 'best_year': 2013.0, 'highest_ema': 1.0}, {'cpc_group_code': 'F02N11/', 'best_year': 2013.0, 'highest_ema': 1.0}, {'cpc_group_code': 'F02N11/0', 'best_year': 2013.0, 'highest_ema': 1.0}, {'cpc_group_code': 'F02N11/08', 'best_year': 2013.0, 'highest_ema': 1.0}, {'cpc_group_code': 'F02N2200/0', 'best_year': 2013.0, 'highest_ema': 2.0}, {'cpc_group_code': 'F02N2300/20', 'best_year': 2013.0, 'highest_ema': 2.0}, {'cpc_group_code': 'F02P15/', 'best_year': 2011.0, 'highest_ema': 2.0}, {'cpc_group_code': 'F02P3/', 'best_year': 2011.0, 'highest_ema': 2.0}, {'cpc_group_code': 'H01F27/', 'best_year': 2011.0, 'highest_ema': 2.0}, {'cpc_group_code': 'H01F38/', 'best_year': 2011.0, 'highest_ema': 2.0}, {'cpc_group_code': 'Y02T10/', 'best_year': 2013.0, 'highest_ema': 2.0}], 'var_function-call-11165716241033857098': ['cpc_definition'], 'var_function-call-16529514565601507171': "'A43B13/2', 'A43B17/', 'A43B7/', 'A61F5/', 'A61F5/01', 'B60K6/4', 'B60W30/1', 'F02N11/', 'F02N11/0', 'F02N11/08', 'F02N2200/0', 'F02N2300/20', 'F02P15/', 'F02P3/', 'H01F27/', 'H01F38/', 'Y02T10/'", 'var_function-call-15219561017373187378': [{'symbol': 'A61F5/01', 'titleFull': 'Orthopaedic devices, e.g. splints, casts or braces'}, {'symbol': 'F02N11/08', 'titleFull': 'Circuits or control means specially adapted for starting of engines'}, {'symbol': 'F02N2300/20', 'titleFull': 'Control related aspects of engine starting characterised by the control method'}], 'var_function-call-13241246895042270800': 'file_storage/function-call-13241246895042270800.json', 'var_function-call-2487011880571689373': [{'cpc_group_code': 'A43B13/22', 'best_year': 2016, 'highest_ema': 1.0}, {'cpc_group_code': 'A43B17/00', 'best_year': 2016, 'highest_ema': 2.0}, {'cpc_group_code': 'A43B7/20', 'best_year': 2016, 'highest_ema': 2.0}, {'cpc_group_code': 'A61F5/01', 'best_year': 2016, 'highest_ema': 4.0}, {'cpc_group_code': 'A61F5/14', 'best_year': 2016, 'highest_ema': 2.0}]}

exec(code, env_args)
