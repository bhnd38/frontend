-- db에 기존 테이블이 존재할 경우 먼저 삭제
DROP TABLE if exists orders;
DROP TABLE if exists products;
DROP TABLE if exists orderproducts;



-- 문제 테이블 생성
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    fulfilled BOOLEAN NOT NULL,
    order_time DATETIME NOT NULL
);


CREATE TABLE products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    stock INT NOT NULL
);


CREATE TABLE orderproducts (
    product_id INTEGER NOT NULL,
    order_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

INSERT INTO products (product_name, stock)
VALUES
('커피', 10),
('녹차', 10),
('홍차', 10),
('라떼', 10);

-- 1번 문제
INSERT INTO orders (fulfilled, order_time)
VALUES (FALSE, CURRENT_TIMESTAMP);


-- 2번 문제
INSERT INTO orderproducts (product_id, order_id, quantity)
VALUES (3, 1, 2);

-- 3번 문제
SELECT *
FROM orderproducts;

-- 4번 문제
UPDATE products
SET stock = stock - 2
WHERE product_id = 3;

UPDATE orders
SET fulfilled = TRUE
WHERE order_id = 1;

-- 5번 문제
SELECT *
FROM orders, products;



