CREATE DATABASE Manufacturer
USE Manufacturer

CREATE SCHEMA product

CREATE TABLE product.product
(
Procuct_id INT IDENTITY(1,1) PRIMARY KEY,
Procuct_name VARCHAR(30),
Quantity_on_hand INT,
)
CREATE TABLE product.component
(
Component_id INT IDENTITY(1,1) PRIMARY KEY,
Component_name VARCHAR(30),
Comp_Description INT,
)
CREATE TABLE product.product_component
(
Component_id INT,
Used_product_id INT ,
PRIMARY KEY(Component_id, Used_product_id),
FOREIGN KEY(Component_id) REFERENCES product.component(Component_id ),
FOREIGN KEY(Used_product_id) REFERENCES product.product(Procuct_id )
)
CREATE TABLE product.supplier
(
Supplier_id INT IDENTITY(1,1) PRIMARY KEY,
Adres VARCHAR(80),
Phone NUMERIC,
)
CREATE TABLE product.supplier_component
(
Supplier_id INT,
Component_id INT ,
PRIMARY KEY(Supplier_id, Component_id),
FOREIGN KEY(Supplier_id) REFERENCES product.supplier(Supplier_id ),
FOREIGN KEY(Component_id ) REFERENCES product.component(Component_id )
)