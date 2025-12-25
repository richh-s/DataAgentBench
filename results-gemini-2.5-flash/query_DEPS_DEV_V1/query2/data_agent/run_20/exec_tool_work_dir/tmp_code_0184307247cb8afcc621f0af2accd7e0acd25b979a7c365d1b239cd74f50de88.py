code = """import pandas as pd
import json

package_info_raw = json.loads(open(locals()['var_function-call-12876232258111078056'], 'r').read())
package_info_df = pd.DataFrame(package_info_raw)
package_info_df = package_info_df.drop_duplicates(subset=['Name', 'Version'])

def get_project_names_in_batches(df, batch_size=1000, max_batches=10):
    queries = []
    for i in range(0, min(len(df), batch_size * max_batches), batch_size):
        batch = df.iloc[i:i + batch_size]
        name_version_pairs = []
        for index, row in batch.iterrows():
            name = row['Name'].replace("'", "''")
            version = row['Version'].replace("'", "''")
            name_version_pairs.append(f"('{name}', '{version}')")
        values_str = ', '.join(name_version_pairs)
        query = f"SELECT Name, Version, ProjectName FROM project_packageversion WHERE (Name, Version) IN ({values_str}) AND System = 'NPM';"
        queries.append(query)
    return queries

queries_list = get_project_names_in_batches(package_info_df)
print("__RESULT__:")
print(json.dumps(queries_list))"""

env_args = {'var_function-call-12876232258111078056': 'file_storage/function-call-12876232258111078056.json'}

exec(code, env_args)
