code = """# Check start dates
start_dates = df.groupby('Index')['Date'].min()
print("Start dates for top 10:")
print(start_dates[results_df.head(10)['Index']])

# Let's see which indices have data in Jan 2000
valid_indices = df[(df['Date'] >= '2000-01-01') & (df['Date'] < '2000-02-01')]['Index'].unique()
print("\nIndices with data in Jan 2000:", valid_indices)

# Re-run ranking for only valid indices
valid_results = results_df[results_df['Index'].isin(valid_indices)]
print("\nTop 5 Valid Indices:")
print(valid_results.head(5))"""

env_args = {'var_function-call-6614466468539824704': ['index_info'], 'var_function-call-6614466468539823285': ['index_trade'], 'var_function-call-4749975929176175058': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-4749975929176178023': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'Open': '2552.399902', 'High': '2552.399902', 'Low': '2552.399902', 'Close': '2552.399902', 'Adj Close': '2552.399902', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'Open': '2583.899902', 'High': '2583.899902', 'Low': '2583.899902', 'Close': '2583.899902', 'Adj Close': '2583.899902', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'Open': '2607.100098', 'High': '2607.100098', 'Low': '2607.100098', 'Close': '2607.100098', 'Adj Close': '2607.100098', 'CloseUSD': '338.92301274'}], 'var_function-call-5062678747963144670': [{'count_star()': '104224'}], 'var_function-call-782064260025852418': 'file_storage/function-call-782064260025852418.json', 'var_function-call-333989073081993697': [{'Index': 'IXIC', 'Total_Invested': 257, 'Final_Value': 1240.524390630478, 'ROI': 3.8269431542041943}, {'Index': 'NSEI', 'Total_Invested': 165, 'Final_Value': 389.1405118556778, 'ROI': 1.3584273445798654}, {'Index': '399001.SZ', 'Total_Invested': 258, 'Final_Value': 605.6456273462345, 'ROI': 1.3474636718846298}, {'Index': 'GDAXI', 'Total_Invested': 257, 'Final_Value': 603.1863799884268, 'ROI': 1.3470287159082754}, {'Index': 'TWII', 'Total_Invested': 257, 'Final_Value': 590.6374811720752, 'ROI': 1.2982003158446507}, {'Index': 'N225', 'Total_Invested': 258, 'Final_Value': 559.6187075559984, 'ROI': 1.1690647579689861}, {'Index': 'NYA', 'Total_Invested': 257, 'Final_Value': 517.8730341864626, 'ROI': 1.0150701719317612}, {'Index': 'GSPTSE', 'Total_Invested': 257, 'Final_Value': 444.6643713625033, 'ROI': 0.7302115617218027}, {'Index': '000001.SS', 'Total_Invested': 257, 'Final_Value': 422.19204703169305, 'ROI': 0.6427706110182609}, {'Index': 'N100', 'Total_Invested': 258, 'Final_Value': 416.0559801681327, 'ROI': 0.6126200781710569}]}

exec(code, env_args)
