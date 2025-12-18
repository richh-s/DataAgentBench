code = """import pandas as pd
from sqlalchemy import create_engine, text

# Establishing connection to the clinical_database
db_name = "clinical_database"
engine = create_engine(f'postgresql://user:password@host/{db_name}')

# Fetching column names
with engine.connect() as connection:
    query = text("SELECT column_name FROM information_schema.columns WHERE table_name = 'clinical_info';")
    result = connection.execute(query)
    column_names = [row[0] for row in result]

print('__RESULT__:')
print(pd.Series(column_names).to_json())"""

env_args = {'var_function-call-13920167792381176524': ['clinical_info']}

exec(code, env_args)
