-- seed_data.sql
-- =====================================
--  SAMPLE DATA SEED FOR DJANGO MODELS
-- =====================================


-- 2️⃣ PROMOTIONS
INSERT INTO store_promotion (id, description, discount_applied)
VALUES
(1, '10% off electronics', 10.0),
(2, 'Buy one get one free', 50.0),
(3, 'Black Friday Sale', 30.0);

-- 3️⃣ COLLECTIONS
INSERT INTO store_collection (id, title, featured_product_id)
VALUES
(1, 'Electronics', NULL),
(2, 'Home Appliances', NULL),
(3, 'Books', NULL);

-- 4️⃣ PRODUCTS
INSERT INTO store_product (id, title, slug, description, unit_price, inventory, last_updated, collection_id)
VALUES
(1, 'Smartphone X', 'smartphone-x', 'Latest 5G smartphone', 699.99, 50, NOW(), 1),
(2, 'LED TV 55"', 'led-tv-55', 'Ultra HD Smart LED TV', 899.50, 30, NOW(), 1),
(3, 'Microwave Oven', 'microwave-oven', '1000W compact oven', 120.00, 25, NOW(), 2),
(4, 'Python Programming Book', 'python-book', 'Learn Python with examples', 45.00, 100, NOW(), 3);

-- Link promotions to products (M2M table)
INSERT INTO store_product_promotions (id, product_id, promotion_id)
VALUES
(1, 1, 1),
(2, 2, 3),
(3, 4, 3);

-- 5️⃣ CUSTOMERS
INSERT INTO store_customer (id, phone, birth_date, membership, user_id)
VALUES
(1, '+1234567890', '1990-06-15', 'G', 1),
(2, '+9876543210', '1995-03-22', 'S', 2);

-- 6️⃣ ADDRESSES
INSERT INTO store_address (id, street, city, customer_id)
VALUES
(1, '123 Main Street', 'New York', 1),
(2, '456 Elm Avenue', 'Los Angeles', 2);

-- 7️⃣ CARTS
INSERT INTO store_cart (id, created_at)
VALUES
('08f8ee31-aed7-4a09-9981-19b17b526223', NOW()),
('12b5ae93-bb52-4d1b-a112-1eaa12345678', NOW());

-- 8️⃣ CART ITEMS
INSERT INTO store_cartitem (id, cart_id, product_id, quantity)
VALUES
(1, '08f8ee31-aed7-4a09-9981-19b17b526223', 1, 2),
(2, '08f8ee31-aed7-4a09-9981-19b17b526223', 3, 1),
(3, '12b5ae93-bb52-4d1b-a112-1eaa12345678', 2, 1);

-- 9️⃣ ORDERS
INSERT INTO store_order (id, placed_at, payment_status, customer_id)
VALUES
(1, NOW(), 'C', 1),
(2, NOW(), 'P', 2);

-- 🔟 ORDER ITEMS
INSERT INTO store_orderitem (id, order_id, product_id, quantity, unit_price)
VALUES
(1, 1, 1, 2, 699.99),
(2, 1, 3, 1, 120.00),
(3, 2, 4, 1, 45.00);


