code = """import pandas as pd
import json

project_packageversion_raw_1 = json.loads(open(locals()['var_function-call-4038209737457408224'], 'r').read())
project_packageversion_raw_2 = json.loads(open(locals()['var_function-call-9329097413793392157'], 'r').read())

project_packageversion_df_1 = pd.DataFrame(project_packageversion_raw_1)
project_packageversion_df_2 = pd.DataFrame(project_packageversion_raw_2)

combined_project_df = pd.concat([project_packageversion_df_1, project_packageversion_df_2])
unique_project_names = combined_project_df['ProjectName'].dropna().unique()

def get_project_info_queries(project_names, batch_size=100):
    queries = []
    # Limiting to a reasonable number of batches to avoid excessive tool calls during development
    max_batches = 10
    for i in range(0, min(len(project_names), batch_size * max_batches), batch_size):
        batch = project_names[i:i + batch_size]
        project_name_list = [f"'{\'%s\' % name.replace("'", "''")}'" for name in batch]
        values_str = ', '.join(project_name_list)
        query = f"SELECT Project_Information FROM project_info WHERE ProjectName IN ({values_str});"
        queries.append(query)
    return queries

queries_list = get_project_info_queries(unique_project_names)
print("__RESULT__:")
print(json.dumps(queries_list))"""

env_args = {'var_function-call-12876232258111078056': 'file_storage/function-call-12876232258111078056.json', 'var_function-call-18250586688109469417': 'file_storage/function-call-18250586688109469417.json', 'var_function-call-4038209737457408224': 'file_storage/function-call-4038209737457408224.json', 'var_function-call-12481450381314217098': 'file_storage/function-call-12481450381314217098.json', 'var_function-call-9329097413793392157': 'file_storage/function-call-9329097413793392157.json'}

exec(code, env_args)
