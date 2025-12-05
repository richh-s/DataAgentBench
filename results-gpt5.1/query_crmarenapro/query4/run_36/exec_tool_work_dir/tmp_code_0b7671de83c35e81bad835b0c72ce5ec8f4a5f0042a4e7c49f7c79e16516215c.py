code = """import pandas as pd, json

data = var_call_K57sHsf6NLsNs4tJySqoMYHQ

df = pd.DataFrame(data)
df['CreatedDate'] = pd.to_datetime(df['CreatedDate'])
# Last 10 months from 2021-04-10 => from 2020-06-10 inclusive
mask = (df['CreatedDate'] >= '2020-06-10') & (df['CreatedDate'] < '2021-04-11')
df = df[mask]
monthly_counts = df.groupby(df['CreatedDate'].dt.to_period('M')).size().sort_index()

# Determine if a month "significantly" exceeds others using a simple z-score threshold
counts = monthly_counts.values
if len(counts) == 0:
    result = None
else:
    mean = counts.mean()
    std = counts.std(ddof=0)
    if std == 0:
        result = None
    else:
        z_scores = (counts - mean) / std
        max_idx = z_scores.argmax()
        if z_scores[max_idx] >= 2:  # at least 2 standard deviations above mean
            top_period = monthly_counts.index[max_idx]
            month_name = top_period.to_timestamp().strftime('%B')
            result = month_name
        else:
            result = None

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_K57sHsf6NLsNs4tJySqoMYHQ': [{'Id': '00kWt000002HFA1IAO', 'OpportunityId': '006Wt000007B630IAC', 'Product2Id': '01tWt000006hVJdIAM', 'CreatedDate': '2020-08-15T10:35:45.000+0000'}, {'Id': '00kWt000002HGVYIA4', 'OpportunityId': '006Wt000007BD7aIAG', 'Product2Id': '01tWt000006hVJdIAM', 'CreatedDate': '2021-01-15T10:45:30.000+0000'}, {'Id': '00kWt000002HJA4IAO', 'OpportunityId': '006Wt000007BCZlIAO', 'Product2Id': '01tWt000006hVJdIAM', 'CreatedDate': '2020-06-15T10:53:21.000+0000'}, {'Id': '#00kWt000002HKR5IAO', 'OpportunityId': '006Wt000007BA9jIAG', 'Product2Id': '01tWt000006hVJdIAM', 'CreatedDate': '2020-06-15T09:14:27.000+0000'}, {'Id': '00kWt000002HKUFIA4', 'OpportunityId': '006Wt000007BFnhIAG', 'Product2Id': '01tWt000006hVJdIAM', 'CreatedDate': '2021-01-15T09:30:00.000+0000'}, {'Id': '00kWt000002HLf6IAG', 'OpportunityId': '006Wt000007BISDIA4', 'Product2Id': '01tWt000006hVJdIAM', 'CreatedDate': '2020-10-01T10:15:30.000+0000'}, {'Id': '00kWt000002HNQWIA4', 'OpportunityId': '006Wt000007BBQkIAO', 'Product2Id': '01tWt000006hVJdIAM', 'CreatedDate': '2021-02-01T15:22:30.000+0000'}, {'Id': '00kWt000002HNgcIAG', 'OpportunityId': '006Wt000007B6xKIAS', 'Product2Id': '01tWt000006hVJdIAM', 'CreatedDate': '2020-12-01T14:37:45.000+0000'}, {'Id': '00kWt000002HP2WIAW', 'OpportunityId': '006Wt000007BD4MIAW', 'Product2Id': '01tWt000006hVJdIAM', 'CreatedDate': '2020-07-15T10:45:00.000+0000'}, {'Id': '00kWt000002HUdGIAW', 'OpportunityId': '006Wt000007B7yGIAS', 'Product2Id': '01tWt000006hVJdIAM', 'CreatedDate': '2021-01-20T10:45:00.000+0000'}, {'Id': '00kWt000002HUtPIAW', 'OpportunityId': '006Wt000007BBP9IAO', 'Product2Id': '#01tWt000006hVJdIAM', 'CreatedDate': '2021-01-10T10:45:23.000+0000'}, {'Id': '00kWt000002HVHmIAO', 'OpportunityId': '006Wt000007BINNIA4', 'Product2Id': '01tWt000006hVJdIAM', 'CreatedDate': '2020-10-05T14:30:45.000+0000'}, {'Id': '#00kWt000002HWaDIAW', 'OpportunityId': '006Wt000007BDIsIAO', 'Product2Id': '01tWt000006hVJdIAM', 'CreatedDate': '2020-11-12T10:45:38.000+0000'}, {'Id': '#00kWt000002HXbBIAW', 'OpportunityId': '006Wt000007BFXaIAO', 'Product2Id': '01tWt000006hVJdIAM', 'CreatedDate': '2020-11-15T15:50:45.000+0000'}, {'Id': '00kWt000002HZ8KIAW', 'OpportunityId': '006Wt000007BAMjIAO', 'Product2Id': '01tWt000006hVJdIAM', 'CreatedDate': '2020-09-15T15:45:32.000+0000'}, {'Id': '00kWt000002HZ9zIAG', 'OpportunityId': '006Wt000007BHuMIAW', 'Product2Id': '01tWt000006hVJdIAM', 'CreatedDate': '2020-07-20T10:34:21.000+0000'}, {'Id': '00kWt000002HZJcIAO', 'OpportunityId': '006Wt000007BIX4IAO', 'Product2Id': '01tWt000006hVJdIAM', 'CreatedDate': '2020-07-10T14:35:47.000+0000'}, {'Id': '00kWt000002HZMoIAO', 'OpportunityId': '006Wt000007BGi9IAG', 'Product2Id': '01tWt000006hVJdIAM', 'CreatedDate': '2021-03-12T09:23:30.000+0000'}, {'Id': '00kWt000002HaFeIAK', 'OpportunityId': '006Wt000007B9X2IAK', 'Product2Id': '01tWt000006hVJdIAM', 'CreatedDate': '2020-10-05T09:45:00.000+0000'}, {'Id': '#00kWt000002HaNhIAK', 'OpportunityId': '006Wt000007BGtRIAW', 'Product2Id': '01tWt000006hVJdIAM', 'CreatedDate': '2020-07-10T14:58:10.000+0000'}]}

exec(code, env_args)
