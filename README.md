# 📄 Project Dependencies

This project depends on **MySQL**, **SQLite**, **DuckDB**, and **MongoDB** as data sources.  
The agent automatically reads database connection parameters from the `.env` file, detects and loads the database files, and establishes the connections as needed.  

You only need to make sure that the required database services are running (where applicable), and the `.env` file is properly configured.  

## 🔷 Database Requirements

- ✅ **MySQL** — requires a **local MySQL server** to be installed and running.  
  The agent will automatically read the host, port, username, and password from the `.env` file and connect to the MySQL service on your machine or specified host.

- ✅ **MongoDB** — requires a **local MongoDB server** to be installed and running.  
  Similarly, the agent will read the host, port, and username and password from the `.env` file and connect to the MongoDB service.

- 📄 **SQLite** — does **not** require a separate service.  
  SQLite is a file-based database. The agent automatically detects and loads the `.db` files directly from the filesystem.

- 📄 **DuckDB** — does **not** require a separate service.  
  DuckDB is also a file-based, embedded database. The agent automatically detects and loads the `.db` files directly from the filesystem.

Only **MySQL** and **MongoDB** require you to have their respective servers running locally (or accessible on a specified host). Please make sure both database services are properly installed and configured **before running the project**. 
**SQLite** and **DuckDB** work as standalone files — no separate server installation is needed for them.


## ⚙️ Prerequisites

### 1️⃣ Install MySQL

- Install [MySQL](https://www.mysql.com/) on your machine according to your operating system.
- After installation, start the MySQL server. Verify that you can connect using:
  ```bash
  mysql -u root -p
  ```
  
2️⃣ Install MongoDB
- Install [MongoDB Community Edition](https://www.mongodb.com/) on your machine according to your operating system.
- After installation, start the MongoDB server. Verify that you can connect.

# 📄 .env Example

Below is an example `.env` file you can create in the project root directory.  
Fill in your actual MySQL and MongoDB credentials.

```env
# MySQL configuration
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_mysql_password
MYSQL_PORT=3306

# MongoDB configuration
MONGO_HOST=localhost
MONGO_PORT=27017
MONGO_USER=your_mongo_username   
MONGO_PASSWORD=your_mongo_password 
```
