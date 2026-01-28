code = """# First, let's explore the languages table to understand its structure
rl_languages = var_functions.list_db:0

# Let's query the languages table to see how language_description looks
# We'll use query_db to get sample data"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses']}

exec(code, env_args)
