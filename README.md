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

### ✅ MySQL
- requires a **local MySQL server** to be installed and running.  
- Install [MySQL](https://www.mysql.com/) on your machine according to your operating system.
- After installation, start the MySQL server. Verify that you can connect using:
  ```bash
  mysql -u root -p
  ```
- The agent reads MySQL host, port, username, password, and database name from the .env file.

### ✅ MongoDB
- requires a **local MongoDB server** to be installed and running.  
- Install [MongoDB Community Edition](https://www.mongodb.com/) on your machine according to your operating system.
- After installation, start the MongoDB server. Verify that you can connect.
- The agent reads MySQL host, port, username, password, and database name from the .env file.

### 📄 SQLite 
- does **not** require a separate service.
- SQLite is a file-based database. The agent automatically detects and loads the `.db` files directly from the filesystem.

### 📄 DuckDB 
- does **not** require a separate service.
- DuckDB is also a file-based, embedded database. The agent automatically detects and loads the `.db` files directly from the filesystem.

Only **MySQL** and **MongoDB** require you to have their respective servers running locally (or accessible on a specified host). Please make sure both database services are properly installed and configured **before running the project**. 
**SQLite** and **DuckDB** work as standalone files — no separate server installation is needed for them.


# 📄 .env Example

Below is an example `.env` file you can create in the project root directory.  
Fill in your actual MySQL and MongoDB credentials.

```env
# MySQL configuration
MYSQL_CLIENT=your_local_mysql.exe_path
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DB=test

# MongoDB configuration
MONGO_HOST=localhost
MONGO_PORT=27017
MONGO_USER=your_mongo_username   
MONGO_PASSWORD=your_mongo_password 
```
