# 10 Example SQL Queries with Explanations  

---

## 1. Retrieve All Customers Older Than 25  
`SQL
SELECT * FROM customers WHERE age > 25;
`
**Explanation**:  
Selects all columns (`*`) from the `customers` table where the `age` column exceeds 25. The `WHERE` clause filters records conditionally.

---

## 2. Select Specific Columns with Sorting  
`SQL
SELECT name, email FROM users ORDER BY name ASC;
`
**Explanation**:  
Fetches only `name` and `email` columns from `users`, sorted alphabetically by `name` in ascending order (`ASC`). Remove `ASC` for default ascending sorting.

---

## 3. Combine Orders with Customer Data (Inner Join)  
`SQL
SELECT orders.id, customers.name 
FROM orders 
INNER JOIN customers ON orders.customer_id = customers.id;
`
**Explanation**:  
Matches `orders` with `customers` using the `customer_id` foreign key. Returns only records with matches in both tables.

---

## 4. List All Customers Including Those Without Orders (Left Join)  
`SQL
SELECT customers.name, orders.total 
FROM customers 
LEFT JOIN orders ON customers.id = orders.customer_id;
`
**Explanation**:  
Returns all customers regardless of order history. Unmatched orders show `NULL` in order-related columns.

---

## 5. Add New Product to Database  
`SQL
INSERT INTO products (name, price, category) 
VALUES ('Wireless Mouse', 29.99, 'Electronics');
`
**Explanation**:  
Inserts a new row into `products`. Column order in parentheses must match value order. Always specify columns explicitly for clarity.

---

## 6. Update User Email Address  
`SQL
UPDATE users 
SET email = 'new.email@example.com' 
WHERE id = 42;
`
**Explanation**:  
Modifies the `email` field for the user with `id = 42`. **Always** include a `WHERE` clause to avoid mass updates.

---

## 7. Delete Inactive Users  
`SQL
DELETE FROM users 
WHERE last_login < '2024-01-01';
`
**Explanation**:  
Removes users who haven't logged in since 2024. Test with `SELECT COUNT(*)` first to verify affected records.

---

## 8. Create Table with Constraints  
`SQL
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(id)
);
`
**Explanation**:  
Creates an `employees` table with:
- Primary key constraint on `id`
- Mandatory `name` field (`NOT NULL`)
- Foreign key relationship to `departments` table

---

## 9. Add New Column to Existing Table  
`SQL
ALTER TABLE products 
ADD COLUMN stock_quantity INT DEFAULT 0;
`
**Explanation**:  
Adds `stock_quantity` column to `products` table. Existing records get `0` as default value. Use `AFTER column_name` to position the new column.

---

## 10. Analyze Customer Order Frequency  
`SQL
SELECT customer_id, COUNT(*) AS order_count 
FROM orders 
GROUP BY customer_id 
HAVING COUNT(*) > 5;
`
**Explanation**:  
1. Groups orders by customer  
2. Counts orders per customer  
3. `HAVING` filters groups (unlike `WHERE` which filters rows)

---

**Key Security Tip**:  
`SQL
-- Always preview changes with SELECT first
SELECT * FROM users WHERE last_login < '2024-01-01';  -- Before DELETE
