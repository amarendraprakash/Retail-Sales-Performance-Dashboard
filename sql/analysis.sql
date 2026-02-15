CREATE DATABASE retail_analytics;
USE retail_analytics;
SELECT COUNT(*) FROM sales_data;

SELECT ROUND(SUM(Sales),2) AS Total_Sales FROM sales_data;

SELECT Category,
       ROUND(SUM(Sales),2) AS Revenue
FROM sales_data
GROUP BY Category
ORDER BY Revenue DESC;

SELECT Region,
       ROUND(SUM(Sales),2) AS Revenue
FROM sales_data
GROUP BY Region;

SELECT Order_Year,
       Order_Month,
       ROUND(SUM(Sales),2) AS Revenue
FROM sales_data
GROUP BY Order_Year, Order_Month
ORDER BY Order_Year, Order_Month;

SELECT `Customer Name`,
       ROUND(SUM(Sales),2) AS Total_Spent
FROM sales_data
GROUP BY `Customer Name`
ORDER BY Total_Spent DESC
LIMIT 10;
