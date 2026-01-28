code = """import json

# Read the query results
adj_close_data = var_functions.query_db:5

# Extract the adjusted closing prices and find the maximum
prices = [float(record["Adj Close"]) for record in adj_close_data]
max_price = max(prices)

# Prepare result
result_str = str(max_price)

# Print in required format
print('__RESULT__:')
print(result_str)"""

env_args = {'var_functions.query_db:0': [{'Symbol': 'REAL'}], 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.query_db:5': [{'Adj Close': '17.8700008392334'}, {'Adj Close': '18.440000534057617'}, {'Adj Close': '17.860000610351562'}, {'Adj Close': '18.104999542236328'}, {'Adj Close': '17.360000610351562'}, {'Adj Close': '18.170000076293945'}, {'Adj Close': '17.790000915527344'}, {'Adj Close': '18.15999984741211'}, {'Adj Close': '18.11000061035156'}, {'Adj Close': '17.739999771118164'}, {'Adj Close': '18.13999938964844'}, {'Adj Close': '17.440000534057617'}, {'Adj Close': '17.799999237060547'}, {'Adj Close': '16.579999923706055'}, {'Adj Close': '16.0'}, {'Adj Close': '15.5'}, {'Adj Close': '15.260000228881836'}, {'Adj Close': '15.399999618530272'}, {'Adj Close': '15.09000015258789'}, {'Adj Close': '14.789999961853027'}, {'Adj Close': '14.470000267028809'}, {'Adj Close': '14.029999732971191'}, {'Adj Close': '14.510000228881836'}, {'Adj Close': '14.420000076293944'}, {'Adj Close': '14.5'}, {'Adj Close': '14.295000076293944'}, {'Adj Close': '14.5'}, {'Adj Close': '14.954999923706056'}, {'Adj Close': '15.65999984741211'}, {'Adj Close': '15.43000030517578'}, {'Adj Close': '15.18000030517578'}, {'Adj Close': '15.239999771118164'}, {'Adj Close': '15.529999732971191'}, {'Adj Close': '15.600000381469728'}, {'Adj Close': '15.899999618530272'}, {'Adj Close': '14.949999809265137'}, {'Adj Close': '14.970000267028809'}, {'Adj Close': '14.949999809265137'}, {'Adj Close': '13.859999656677246'}, {'Adj Close': '13.989999771118164'}, {'Adj Close': '14.210000038146973'}, {'Adj Close': '13.59000015258789'}, {'Adj Close': '13.43000030517578'}, {'Adj Close': '13.0'}, {'Adj Close': '13.010000228881836'}, {'Adj Close': '12.140000343322754'}, {'Adj Close': '12.550000190734863'}, {'Adj Close': '11.390000343322754'}, {'Adj Close': '8.8100004196167'}, {'Adj Close': '8.699999809265137'}, {'Adj Close': '6.46999979019165'}, {'Adj Close': '7.579999923706055'}, {'Adj Close': '8.020000457763672'}, {'Adj Close': '8.079999923706055'}, {'Adj Close': '7.559999942779541'}, {'Adj Close': '5.460000038146973'}, {'Adj Close': '5.75'}, {'Adj Close': '6.949999809265137'}, {'Adj Close': '7.659999847412109'}, {'Adj Close': '7.309999942779541'}, {'Adj Close': '7.360000133514404'}, {'Adj Close': '7.010000228881836'}, {'Adj Close': '6.559999942779541'}]}

exec(code, env_args)
