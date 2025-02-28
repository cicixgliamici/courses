# SQL & MySQL: Essential Commands and Practical Usage  

## Universal SQL Commands (ANSI Standard)  

### 1. Data Manipulation Language (DML)  
| Command       | Example Syntax                         | Description                          |  
|---------------|----------------------------------------|--------------------------------------|  
| **SELECT**    | `SELECT * FROM customers WHERE age > 25;` | Retrieve data from tables            |  
| **INSERT**    | `INSERT INTO products (name, price) VALUES ('Tablet', 299.99);` | Add new records       |  
| **UPDATE**    | `UPDATE orders SET status = 'shipped' WHERE id = 1005;` | Modify existing data   |  
| **DELETE**    | `DELETE FROM logs WHERE date < '2023-01-01';` | Delete records        |  

### 2. Data Definition Language (DDL)  
| Command       | Example Syntax                         | Description                          |  
|---------------|----------------------------------------|--------------------------------------|  
| **CREATE**    | `CREATE TABLE employees (id INT PRIMARY KEY, name VARCHAR(50));` | Create DB objects |  
| **ALTER**     | `ALTER TABLE customers ADD COLUMN phone VARCHAR(15);` | Modify table structure |  
| **DROP**      | `DROP DATABASE legacy_archive;`        | Delete DB objects                    |  
| **TRUNCATE**  | `TRUNCATE TABLE temp_logs;`            | Clear table (faster than DELETE)     |  

### 3. Transaction Control (TCL)  
| Command       | Example Syntax             | Description                          |  
|---------------|----------------------------|--------------------------------------|  
| **COMMIT**    | `COMMIT;`                  | Finalize transactions                |  
| **ROLLBACK**  | `ROLLBACK TO SAVEPOINT sp1;`| Undo transactions                   |  
| **SAVEPOINT** | `SAVEPOINT sp1;`           | Create partial rollback point        |  

---  

## MySQL-Specific Commands  

### Database Management  
    -- Create database  
    CREATE DATABASE ecommerce CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;  

    -- List databases  
    SHOW DATABASES;  

    -- Select database  
    USE ecommerce;  

### Table Operations  
    -- Show table structure  
    DESCRIBE products;  

    -- Rename table  
    RENAME TABLE old_customers TO customer_archive;  

    -- Create index  
    CREATE INDEX idx_lastname ON customers(lastname);  

### Optimization  
    -- Query execution plan  
    EXPLAIN SELECT * FROM orders WHERE total > 1000;  

    -- Optimize table  
    OPTIMIZE TABLE access_logs;  

    -- Check active locks  
    SHOW OPEN TABLES WHERE In_use > 0;  

---  

## Advanced Functions  

### Joins & Subqueries  
    -- Inner Join  
    SELECT o.id, c.name  
    FROM orders o  
    JOIN customers c ON o.customer_id = c.id;  

    -- Correlated subquery  
    SELECT name, (SELECT COUNT(*) FROM orders WHERE customer_id = c.id)  
    FROM customers c;  

### Aggregate Functions  
    SELECT  
        COUNT(*) AS total_orders,  
        AVG(total) AS avg_spend,  
        MAX(order_date) AS last_order  
    FROM orders;  

### Access Control (DCL)  
    -- Create user  
    CREATE USER 'report_user'@'localhost' IDENTIFIED BY 'S3cur3P@ss!';  

    -- Grant permissions  
    GRANT SELECT ON ecommerce.* TO 'report_user'@'localhost';  

    -- Revoke permissions  
    REVOKE DELETE ON *.* FROM 'temp_user'@'%';  

---  

## Best Practices & Security  

1. **Regular Backups**  
    ```bash  
    mysqldump -u root -p ecommerce > backup.sql  
    ```  

2. **Prevent SQL Injection**  
    ```php  
    // Use prepared statements  
    $stmt = $conn->prepare("SELECT * FROM users WHERE email = ?");  
    $stmt->bind_param("s", $email);  
    ```  

3. **Secure Configuration**  
    ```sql  
    -- Disable remote root access  
    DELETE FROM mysql.user WHERE User='root' AND Host NOT IN ('localhost', '127.0.0.1');  
    FLUSH PRIVILEGES;  
    ```  

---  