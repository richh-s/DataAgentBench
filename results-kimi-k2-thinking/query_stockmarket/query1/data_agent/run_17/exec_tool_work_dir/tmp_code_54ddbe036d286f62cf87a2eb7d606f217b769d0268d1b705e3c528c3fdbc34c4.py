code = """import json
import pandas as pd

# Get the stock data using locals() to handle the variable name with colon
stock_data_key = 'var_functions.query_db:8'
stock_data = locals()[stock_data_key]

# Convert to DataFrame
df = pd.DataFrame(stock_data)

# Convert Adj Close to float
df['Adj Close'] = df['Adj Close'].astype(float)

# Find the maximum adjusted closing price
max_adj_close = df['Adj Close'].max()

# Find the date when this maximum occurred
max_date = df[df['Adj Close'] == max_adj_close]['Date'].iloc[0]

print("__RESULT__:")
print(json.dumps({
    "max_adj_close": float(max_adj_close),
    "max_date": max_date
}))"""

env_args = {'var_functions.query_db:0': [{'Symbol': 'REAL', 'Company Description': 'The RealReal, Inc. is a leader in the luxury consignment market, offering a platform for buying and selling authenticated pre-owned designer fashion, jewelry, and art.'}], 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:6': {'real_table_exists': True, 'total_tables': 2753}, 'var_functions.query_db:8': [{'Date': '2020-01-02', 'Adj Close': '17.8700008392334'}, {'Date': '2020-01-03', 'Adj Close': '18.440000534057617'}, {'Date': '2020-01-06', 'Adj Close': '17.860000610351562'}, {'Date': '2020-01-07', 'Adj Close': '18.104999542236328'}, {'Date': '2020-01-08', 'Adj Close': '17.360000610351562'}, {'Date': '2020-01-09', 'Adj Close': '18.170000076293945'}, {'Date': '2020-01-10', 'Adj Close': '17.790000915527344'}, {'Date': '2020-01-13', 'Adj Close': '18.15999984741211'}, {'Date': '2020-01-14', 'Adj Close': '18.11000061035156'}, {'Date': '2020-01-15', 'Adj Close': '17.739999771118164'}, {'Date': '2020-01-16', 'Adj Close': '18.13999938964844'}, {'Date': '2020-01-17', 'Adj Close': '17.440000534057617'}, {'Date': '2020-01-21', 'Adj Close': '17.799999237060547'}, {'Date': '2020-01-22', 'Adj Close': '16.579999923706055'}, {'Date': '2020-01-23', 'Adj Close': '16.0'}, {'Date': '2020-01-24', 'Adj Close': '15.5'}, {'Date': '2020-01-27', 'Adj Close': '15.260000228881836'}, {'Date': '2020-01-28', 'Adj Close': '15.399999618530272'}, {'Date': '2020-01-29', 'Adj Close': '15.09000015258789'}, {'Date': '2020-01-30', 'Adj Close': '14.789999961853027'}, {'Date': '2020-01-31', 'Adj Close': '14.470000267028809'}, {'Date': '2020-02-03', 'Adj Close': '14.029999732971191'}, {'Date': '2020-02-04', 'Adj Close': '14.510000228881836'}, {'Date': '2020-02-05', 'Adj Close': '14.420000076293944'}, {'Date': '2020-02-06', 'Adj Close': '14.5'}, {'Date': '2020-02-07', 'Adj Close': '14.295000076293944'}, {'Date': '2020-02-10', 'Adj Close': '14.5'}, {'Date': '2020-02-11', 'Adj Close': '14.954999923706056'}, {'Date': '2020-02-12', 'Adj Close': '15.65999984741211'}, {'Date': '2020-02-13', 'Adj Close': '15.43000030517578'}, {'Date': '2020-02-14', 'Adj Close': '15.18000030517578'}, {'Date': '2020-02-18', 'Adj Close': '15.239999771118164'}, {'Date': '2020-02-19', 'Adj Close': '15.529999732971191'}, {'Date': '2020-02-20', 'Adj Close': '15.600000381469728'}, {'Date': '2020-02-21', 'Adj Close': '15.899999618530272'}, {'Date': '2020-02-24', 'Adj Close': '14.949999809265137'}, {'Date': '2020-02-25', 'Adj Close': '14.970000267028809'}, {'Date': '2020-02-26', 'Adj Close': '14.949999809265137'}, {'Date': '2020-02-27', 'Adj Close': '13.859999656677246'}, {'Date': '2020-02-28', 'Adj Close': '13.989999771118164'}, {'Date': '2020-03-02', 'Adj Close': '14.210000038146973'}, {'Date': '2020-03-03', 'Adj Close': '13.59000015258789'}, {'Date': '2020-03-04', 'Adj Close': '13.43000030517578'}, {'Date': '2020-03-05', 'Adj Close': '13.0'}, {'Date': '2020-03-06', 'Adj Close': '13.010000228881836'}, {'Date': '2020-03-09', 'Adj Close': '12.140000343322754'}, {'Date': '2020-03-10', 'Adj Close': '12.550000190734863'}, {'Date': '2020-03-11', 'Adj Close': '11.390000343322754'}, {'Date': '2020-03-12', 'Adj Close': '8.8100004196167'}, {'Date': '2020-03-13', 'Adj Close': '8.699999809265137'}, {'Date': '2020-03-16', 'Adj Close': '6.46999979019165'}, {'Date': '2020-03-17', 'Adj Close': '7.579999923706055'}, {'Date': '2020-03-18', 'Adj Close': '8.020000457763672'}, {'Date': '2020-03-19', 'Adj Close': '8.079999923706055'}, {'Date': '2020-03-20', 'Adj Close': '7.559999942779541'}, {'Date': '2020-03-23', 'Adj Close': '5.460000038146973'}, {'Date': '2020-03-24', 'Adj Close': '5.75'}, {'Date': '2020-03-25', 'Adj Close': '6.949999809265137'}, {'Date': '2020-03-26', 'Adj Close': '7.659999847412109'}, {'Date': '2020-03-27', 'Adj Close': '7.309999942779541'}, {'Date': '2020-03-30', 'Adj Close': '7.360000133514404'}, {'Date': '2020-03-31', 'Adj Close': '7.010000228881836'}, {'Date': '2020-04-01', 'Adj Close': '6.559999942779541'}]}

exec(code, env_args)
