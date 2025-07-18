# 📄 UCB Query Benchmark Study

This project is a **benchmark study of data agents (LLM-based agents) in querying distributed databases**, evaluating the capabilities of LLM-driven agents in accessing and reasoning over diverse data sources.

It supports **MySQL**, **SQLite**, **DuckDB**, and **MongoDB** as backends.  
The agent automatically reads database connection parameters from the `.env` file, detects and loads database files, and establishes connections as needed.

---
## Installation
### Clone the repository
```bash
git clone https://github.com/Ruiqi-Chen-0216/UCB_Query.git
cd UCB_Query

```
### Create a virtual environment
It is recommended to use a dedicated virtual environment named `ucb_query`:
Using conda:
```bash
conda create -n ucb_query python=3.9
conda activate ucb_query
```

### Install dependencies
Install Python dependencies from `requirements.txt`:
```bash
pip install -r requirements.txt
```
---
## Database Setup
This project interacts with distributed databases, combining both server-based and file-based databases.
You need to ensure the required services are running and files are available.

#### ✅ MySQL
- Requires a **local MySQL server** to be installed and running.  
- Install [MySQL](https://www.mysql.com/) on your machine according to your operating system.
- After installation, start the MySQL server. Verify that you can connect using:
  ```bash
  mysql -u root -p
  ```
- The agent reads MySQL host, port, username, password, and database name from the .env file.

#### ✅ MongoDB
- Requires a **local MongoDB server** to be installed and running.  
- Install [MongoDB Community Edition](https://www.mongodb.com/) on your machine according to your operating system.
- After installation, start the MongoDB server. Verify that you can connect.
- The agent reads the MongoDB connection string (`MONGO_URI`) from the `.env` file.

#### 📄 SQLite & DuckDB 
- Does **not** require a separate service.
- The agent automatically detects and loads the `.db` files directly from the filesystem.

Only **MySQL** and **MongoDB** require you to have their respective servers running locally (or accessible on a specified host). Please make sure both database services are properly installed and configured **before running the project**. 
**SQLite** and **DuckDB** work as standalone files — no separate server installation is needed for them.


## 🔧 Configure .env 
Create a `.env` file in the project root directory with your actual credentials.
Here is an example:

```env
# MySQL configuration
MYSQL_CLIENT=your_local_mysql.exe_path
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DB=test

# MongoDB configuration
MONGO_URI=mongodb://localhost:27017/
# If your MongoDB requires authentication, use a URI like:
MONGO_URI=mongodb://username:password@localhost:27017/?authSource=admin

# OpenAI
OPENAI_API_KEY=your_openai_api_key_here

# Azure
AZURE_API_BASE=https://your-resource-name.openai.azure.com/
AZURE_API_KEY=your_azure_api_key_here
AZURE_API_VERSION=2023-05-15

```
You only need to provide the API key for either OpenAI, Azure OpenAI, or another provider, depending on the service you’re using.

## 🚀 Run the Benchmark
This benchmark can be run in two ways:  
✅ Run on the provided datasets  
✅ Run on your own custom dataset

### 📂 Run on our datasets
We have prepared **five datasets** for this benchmark study: `GoogleLocal`, `BookReview`, `Yelp`, `StockIndex`, `StockMarket`.

Each dataset corresponds to a folder in the project directory.  
To run the benchmark on a specific dataset, simply execute the `run_experiments.py` script located in that folder.  

Example:
```bash
cd query_yelp
python run_experiments.py
```

### 📂 Run on your own datasets

You can also run our benchmark on your own dataset by following these steps:

1️⃣ Prepare your dataset folder

Create a new folder under the project root, e.g., `MyDataset`, with the following structure:
```
MyDataset/
    ├── query_dataset/               <- Your data, stored in a supported format (MySQL, MongoDB, SQLite, or DuckDB)
    ├── db_description.txt           <- A plain text description of the database
    ├── db_config.yaml               <- Basic database configuration (used for agent initialization and connection)
    ├── query_folder/
    │       ├── query.json           <- Benchmark queries
    │       ├── ground_truth.csv     <- Ground truth answers
    │       └── validation.py        <- Script to validate agent results against ground truth
    └──run_experiments.py            <- Copy an existing run_experiments.py here and adjust if needed
```
2️⃣ Notes

- Make sure your datasets in `query_dataset/` is in the supported database formats: **MySQL**, **MongoDB**, **SQLite**, or **DuckDB**. 
- You can use the existing datasets (`GoogleLocal`, `BookReview`, etc.) as templates for all these files.
- The `run_experiments.py` script and related modules in `common_scaffold/agent_tools` and `common_scaffold/db_utils` already implement the core logic — you just need to prepare your data and config.

---
3️⃣ Run the benchmark
Once everything is ready, run:
```bash
cd MyDataset
python run_experiments.py
```
