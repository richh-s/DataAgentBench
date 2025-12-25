code = """import pandas as pd
import json

package_info_raw = json.loads(open(locals()['var_function-call-12876232258111078056'], 'r').read())
package_info_df = pd.DataFrame(package_info_raw)
package_info_df = package_info_df.drop_duplicates(subset=['Name', 'Version'])

# Prepare to query project_database in batches due to potential size
def get_project_names_in_batches(df, batch_size=1000):
    queries = []
    for i in range(0, len(df), batch_size):
        batch = df.iloc[i:i + batch_size]
        name_version_pairs = [f"('{\'%s\' % row['Name'].replace("'", "''")}', '{\'%s\' % row['Version'].replace("'", "''")}')" for index, row in batch.iterrows()]
        values_str = ', '.join(name_version_pairs)
        # Using a direct SQL query with a VALUES clause for efficient querying
        query = f"""SELECT Name, Version, ProjectName FROM project_packageversion WHERE (Name, Version) IN ({values_str}) AND System = 'NPM';"""
        queries.append(query)
    return queries

queries_list = get_project_names_in_batches(package_info_df)
print("__RESULT__:")
print(json.dumps(queries_list))"""

env_args = {'var_function-call-12876232258111078056': 'file_storage/function-call-12876232258111078056.json'}

exec(code, env_args)
