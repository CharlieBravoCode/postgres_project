-- Creation index of product table
CREATE INDEX IF NOT EXISTS product_index
ON product(product_id, name);

-- Creation index of country table
CREATE INDEX IF NOT EXISTS country_name_index 
ON country(country_name);

-- Creation index of city table
CREATE INDEX city_name_idx 
ON city(city_name);


-- Creation index of store table
CREATE INDEX store_city_id_index
ON store(city_id);


-- Creation index of user table
CREATE INDEX users_on_name_index 
ON users (name);


-- Creation index of status_name table
CREATE INDEX status_name_index 
ON status_name (status_name);


-- Creation index of sale table
CREATE INDEX sale_product_id_index
  ON sale
  USING btree
  (product_id);
CREATE INDEX sale_user_id_index
  ON sale
  USING btree
  (user_id);
CREATE INDEX sale_store_id_index
  ON sale
  USING btree
  (store_id);


-- Creation index of order_status table
CREATE INDEX order_status_index
 ON order_status(order_status_id, update_at, sale_id, status_name_id);
