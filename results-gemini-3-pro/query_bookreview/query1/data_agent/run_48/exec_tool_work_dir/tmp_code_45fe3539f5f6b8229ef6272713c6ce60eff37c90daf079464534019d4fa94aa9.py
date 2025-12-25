code = """# Re-using previous variables
# Calculate average rating per book first
book_stats = df_merged.groupby(['decade', 'book_id'])['rating'].mean().reset_index()
book_stats.rename(columns={'rating': 'avg_book_rating'}, inplace=True)

# Group by decade and average the book ratings
decade_book_avg = book_stats.groupby('decade').agg(
    avg_of_book_avgs=('avg_book_rating', 'mean'),
    distinct_books=('book_id', 'count')
).reset_index()

filtered_book_avg = decade_book_avg[(decade_book_avg['distinct_books'] >= 10) & (decade_book_avg['decade'] != '-1s')]
best_book_avg = filtered_book_avg.sort_values(by='avg_of_book_avgs', ascending=False)

print("__RESULT__:")
print(json.dumps({
    "avg_of_reviews_winner": result['decade'], # From previous run
    "avg_of_book_avgs_winner": best_book_avg.iloc[0]['decade'],
    "avg_of_book_avgs_stats": best_book_avg.to_dict(orient='records')
}))"""

env_args = {'var_function-call-11980478109906576321': ['books_info'], 'var_function-call-9741073344249609642': 'file_storage/function-call-9741073344249609642.json', 'var_function-call-15691835330281128782': ['review'], 'var_function-call-10425051511888995697': [{'COUNT(*)': '1833'}], 'var_function-call-2377527336151131583': [{'count': '200'}], 'var_function-call-8048486413748627374': 'file_storage/function-call-8048486413748627374.json', 'var_function-call-10305899063336439880': 'file_storage/function-call-10305899063336439880.json', 'var_function-call-5379179217560364536': 'No decade meets the criteria.', 'var_function-call-9562459679862445883': {'decade': '2020s', 'average_rating': 4.663636363636364, 'distinct_books': 21, 'all_stats': [{'decade': '-1s', 'avg_rating': 4.208333333333333, 'distinct_books': 10}, {'decade': '1880s', 'avg_rating': 4.25, 'distinct_books': 1}, {'decade': '1930s', 'avg_rating': 5.0, 'distinct_books': 2}, {'decade': '1940s', 'avg_rating': 5.0, 'distinct_books': 1}, {'decade': '1970s', 'avg_rating': 4.285714285714286, 'distinct_books': 2}, {'decade': '1980s', 'avg_rating': 4.208333333333333, 'distinct_books': 11}, {'decade': '1990s', 'avg_rating': 3.8405797101449277, 'distinct_books': 18}, {'decade': '2000s', 'avg_rating': 4.273684210526316, 'distinct_books': 46}, {'decade': '2010s', 'avg_rating': 4.608591885441528, 'distinct_books': 88}, {'decade': '2020s', 'avg_rating': 4.663636363636364, 'distinct_books': 21}]}}

exec(code, env_args)
