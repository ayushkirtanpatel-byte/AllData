use e_commerce;

-- Total Orders, Customers, Products

SELECT 
    (SELECT COUNT(*) FROM orders) AS total_orders,
    (SELECT COUNT(*) FROM customers) AS total_customers,
    (SELECT COUNT(*) FROM products) AS total_products;
    
-- Most Frequently Ordered Products

SELECT 
    p.product_name,
    SUM(oi.quantity) AS total_quantity
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_quantity DESC
LIMIT 10;

-- Average Order Value (AOV)

SELECT 
    AVG(order_total) AS avg_order_value
FROM (
    SELECT 
        oi.order_id,
        SUM((p.unit_price * oi.quantity) - oi.discount) AS order_total
    FROM order_items oi
    JOIN products p ON oi.product_id = p.product_id
    GROUP BY oi.order_id
) t;

-- Revenue Over Time (Monthly)

SELECT 
    DATE_FORMAT(o.order_date, '%Y-%m') AS month,
    SUM((p.unit_price * oi.quantity) - oi.discount) AS revenue
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
GROUP BY month
ORDER BY month;

-- Top 5 States by Revenue

SELECT 
    c.state,
    SUM((p.unit_price * oi.quantity) - oi.discount) AS revenue
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
GROUP BY c.state
ORDER BY revenue DESC
LIMIT 5;

-- New vs Returning Customers (Monthly)

SELECT 
    DATE_FORMAT(order_date, '%Y-%m') AS month,
    COUNT(DISTINCT customer_id) AS customers
FROM orders
GROUP BY month;

-- Top 10 Customers by Lifetime Value

SELECT 
    c.customer_id,
    CONCAT(c.first_name, ' ', c.last_name) AS name,
    SUM((p.unit_price * oi.quantity) - oi.discount) AS total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
GROUP BY c.customer_id, name
ORDER BY total_spent DESC
LIMIT 10;

-- Gender-wise Spending

SELECT 
    c.gender,
    SUM((p.unit_price * oi.quantity) - oi.discount) AS total_spending
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
GROUP BY c.gender;


-- Churn Customers (No Recent Orders)

SELECT 
    customer_id,
    MAX(order_date) AS last_order
FROM orders
GROUP BY customer_id
HAVING last_order < DATE_SUB(CURDATE(), INTERVAL 6 MONTH);


-- Best Selling Products

SELECT 
    p.product_name,
    SUM(oi.quantity) AS total_sold,
    SUM((p.unit_price * oi.quantity) - oi.discount) AS revenue
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_sold DESC;


-- Category-wise Revenue

SELECT 
    p.category,
    SUM((p.unit_price * oi.quantity) - oi.discount) AS revenue
FROM products p
JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY p.category;


-- Profit Margin Analysis

SELECT 
    p.product_name,
    SUM((p.unit_price - p.cost_price) * oi.quantity) AS profit
FROM products p
JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY p.product_name
ORDER BY profit DESC;


-- Underperforming Products

SELECT 
    p.product_name,
    SUM(oi.quantity) AS total_sales
FROM products p
LEFT JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY p.product_name
HAVING total_sales < 10;


-- Average Shipping Time

SELECT 
    AVG(DATEDIFF(s.shipping_date, o.order_date)) AS avg_shipping_days
FROM shipping s
JOIN orders o ON s.order_id = o.order_id;


-- Shipping Cost Analysis

SELECT 
    AVG(shipping_cost) AS avg_cost,
    MAX(shipping_cost) AS max_cost,
    MIN(shipping_cost) AS min_cost
FROM shipping;


-- Delayed vs On-Time Orders

SELECT 
    shipping_status,
    COUNT(*) AS total_orders
FROM shipping
GROUP BY shipping_status;


-- Rank Customers

SELECT 
    customer_id,
    total_spent,
    RANK() OVER (ORDER BY total_spent DESC) AS customer_rank
FROM (
    SELECT 
        c.customer_id,
        SUM((p.unit_price * oi.quantity) - oi.discount) AS total_spent
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    JOIN order_items oi ON o.order_id = oi.order_id
    JOIN products p ON oi.product_id = p.product_id
    GROUP BY c.customer_id
) t;


-- Customer Segmentation

SELECT 
    customer_id,
    CASE 
        WHEN total_spent > 5000 THEN 'High Value'
        WHEN total_spent > 2000 THEN 'Medium Value'
        ELSE 'Low Value'
    END AS segment
FROM (
    SELECT 
        c.customer_id,
        SUM((p.unit_price * oi.quantity) - oi.discount) AS total_spent
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    JOIN order_items oi ON o.order_id = oi.order_id
    JOIN products p ON oi.product_id = p.product_id
    GROUP BY c.customer_id
) t;