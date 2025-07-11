# 📄 Project Dependencies

This project depends on **MySQL**, **SQLite**, **DuckDB**, and **MongoDB** as data sources.  
Please note the following requirements:

- ✅ **MySQL** — requires a **local MySQL server** to be installed and running.  
  You must provide the host, port, username, and password in the `.env` file.  
  The application connects to the running MySQL service on your machine or specified host.

- ✅ **MongoDB** — requires a **local MongoDB server** to be installed and running.  
  Similarly, configure the host, port, and (if applicable) username and password in the `.env` file.  
  The application connects to the running MongoDB service on your machine or specified host.

- 📄 **SQLite** — does **not** require a separate service.  
  SQLite is a file-based database. The application directly reads and writes `.db` files from your filesystem.

- 📄 **DuckDB** — does **not** require a separate service.  
  DuckDB is also a file-based, embedded database. The application directly accesses `.db` files as needed.

> Only **MySQL** and **MongoDB** require you to have their respective servers running locally (or accessible on a specified host). Please make sure both database services are properly installed and configured **before running the project**. 
> **SQLite** and **DuckDB** work as standalone files — no separate server installation is needed for them.


## ⚙️ Prerequisites

### 1️⃣ Install MySQL

- Install MySQL on your machine according to your operating system.
- After installation, start the MySQL server.
- Verify that you can connect using:
  ```bash
  mysql -u root -p
  ```
  
2️⃣ Install MongoDB
- Install MongoDB Community Edition on your machine according to your operating system.
- After installation, start the MongoDB server.
- Verify that you can connect

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
MONGO_USER=your_mongo_username   # leave empty if not required
MONGO_PASSWORD=your_mongo_password # leave empty if not required
```
