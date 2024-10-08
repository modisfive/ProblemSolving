SELECT floor(price / 10000) * 10000 AS price_group, count(*) AS products
FROM product
GROUP BY price_group
ORDER BY price_group
