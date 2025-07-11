# 📄 Project Setup

This project requires a **local MySQL** and **MongoDB** server to be installed and running.  
Please make sure both database services are properly installed and configured **before running the project**.

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
