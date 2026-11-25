# SQL / PostgreSQL

```sql
CREATE TEMP TABLE orders (
  id integer PRIMARY KEY,
  total numeric(12,2) NOT NULL CHECK (total >= 0),
  paid boolean NOT NULL DEFAULT false
);
INSERT INTO orders VALUES (1, 120.00, true), (2, 80.00, false);
SELECT paid, COUNT(*) AS orders, SUM(total) AS total
FROM orders GROUP BY paid;
SELECT id, total FROM orders WHERE paid ORDER BY total DESC;
BEGIN;
UPDATE orders SET paid = true WHERE id = 2;
ROLLBACK;
```
Use parameterized queries in applications, transactions for related writes, and `EXPLAIN` to investigate queries. Never interpolate user input into SQL.

## Official reference

[SQL / PostgreSQL documentation](https://www.postgresql.org/docs/current/tutorial-sql.html)
