import pandas as pd
import os


# Read the dataset from the parquet file
PARQUET_PATH = "/home/ruiying/DataAgentBench/query_agnews/agnews_gt.parquet"
df = pd.read_parquet(PARQUET_PATH)


# Function to create queries based on the dataframe

def create_query_1():
    # Query 1: What is the title of the sports article whose description has the greatest number of characters?
    sports_articles = df[df['label'] == 2].copy()  # label 2 corresponds to 'Sports'
    sports_articles['desc_length'] = sports_articles['description'].apply(len)
    max_desc_article = sports_articles.loc[sports_articles['desc_length'].idxmax()]
    # ensure that the max_desc_article is unique
    assert (sports_articles['desc_length'] == max_desc_article['desc_length']).sum() == 1, "There is a tie for the longest description."
    query_1 = f"What is the title of the sports article whose description has the greatest number of characters?"
    answer_1 = max_desc_article['title']

    query_folder = "query1"
    return query_folder, query_1, str(answer_1)


def create_query_2():
    # Query 2: What fraction of all articles authored by Amy Jones belong to the Science/Technology category?
    amy_jones_articles = df[df['author_name'] == 'Amy Jones']
    sci_tech_articles = amy_jones_articles[amy_jones_articles['label'] == 4]  # label 4 corresponds to 'Sci/Tech'
    fraction_sci_tech = len(sci_tech_articles) / len(amy_jones_articles) if len(amy_jones_articles) > 0 else 0
    query_2 = f"What fraction of all articles authored by Amy Jones belong to the Science/Technology category?"
    answer_2 = f"{fraction_sci_tech}"
    query_folder = "query2"
    return query_folder, query_2, answer_2


def create_query_3():
    # Query 3: What is the average number of business articles published per year in Europe from 2010 to 2020, inclusive?
    business_articles = df[(df['label'] == 3) & (df['region'] == 'Europe')]
    # the datetime is a string in 'YYYY-MM-DD' format
    business_articles['publication_year'] = pd.to_datetime(business_articles['publication_date']).dt.year
    articles_2010_2020 = business_articles[(business_articles['publication_year'] >= 2010) & (business_articles['publication_year'] <= 2020)]
    print(articles_2010_2020)
    total_articles = len(articles_2010_2020)
    num_years = 2020 - 2010 + 1
    average_per_year = total_articles / num_years
    query_3 = f"What is the average number of business articles published per year in Europe from 2010 to 2020, inclusive?"
    answer_3 = f"{average_per_year}"
    query_folder = "query3"
    return query_folder, query_3, answer_3

def create_query_4():
    # Query 4: In 2015, which region published the largest number of articles in the World category?
    world_articles_2015 = df[(df['label'] == 1) & (pd.to_datetime(df['publication_date']).dt.year == 2015)]
    region_counts = world_articles_2015['region'].value_counts()
    top_region = region_counts.idxmax()
    # ensure that the top_region is unique
    assert (region_counts == region_counts.max()).sum() == 1, "There is a tie for the top region."
    query_4 = f"In 2015, which region published the largest number of articles in the World category?"
    answer_4 = f"{top_region}"
    query_folder = "query4"
    return query_folder, query_4, answer_4






def write_query(query_folder, query, answer):
    os.makedirs(query_folder, exist_ok=True)
    with open(os.path.join(query_folder, "query.json"), "w") as f:
        f.write(f'"{query}"')
    with open(os.path.join(query_folder, "ground_truth.csv"), "w") as f:
        f.write(answer)


# # Create and write Query 1
# query_folder, query_1, answer_1 = create_query_1()
# write_query(query_folder, query_1, answer_1)

# # print all articles written by Amy Jones
# amy_jones_articles = df[df['author_name'] == 'Amy Jones']
# print(amy_jones_articles)

# # Create and write Query 2
# query_folder, query_2, answer_2 = create_query_2()
# write_query(query_folder, query_2, answer_2)

# # Create and write Query 3
# query_folder, query_3, answer_3 = create_query_3()
# write_query(query_folder, query_3, answer_3)

# # Create and write Query 4
# query_folder, query_4, answer_4 = create_query_4()
# write_query(query_folder, query_4, answer_4)


# Number of records in the dataset
print("Total number of articles in the dataset:", len(df))