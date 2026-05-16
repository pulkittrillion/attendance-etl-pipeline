-- =============================================
-- ATTENDANCE ETL PIPELINE - ANALYTICS QUERIES
-- =============================================

-- 1. Basic Overview
SELECT * FROM attendance LIMIT 20;

-- 2. Branch-wise Performance
SELECT 
    branch,
    COUNT(*) as total_records,
    ROUND(AVG(hours_worked), 2) as avg_hours_worked,
    ROUND(SUM(overtime_hours), 2) as total_overtime,
    ROUND(AVG(overtime_hours), 2) as avg_overtime,
    ROUND(COUNT(CASE WHEN compliance_flag = true THEN 1 END) * 100.0 / COUNT(*), 2) as compliance_rate_pct
FROM attendance 
GROUP BY branch
ORDER BY total_overtime DESC;

-- 3. Daily Trends
SELECT 
    date,
    COUNT(*) as employee_count,
    ROUND(AVG(hours_worked), 2) as avg_hours,
    ROUND(SUM(overtime_hours), 2) as total_overtime
FROM attendance 
GROUP BY date
ORDER BY date;

-- 4. High Overtime Employees
SELECT 
    employee_id,
    branch,
    ROUND(AVG(hours_worked), 2) as avg_hours,
    ROUND(SUM(overtime_hours), 2) as total_overtime,
    COUNT(*) as days_worked
FROM attendance 
GROUP BY employee_id, branch
HAVING AVG(hours_worked) > 9
ORDER BY total_overtime DESC;

-- 5. Overall Statistics
SELECT 
    COUNT(*) as total_records,
    MIN(date) as first_date,
    MAX(date) as last_date,
    ROUND(AVG(hours_worked), 2) as company_avg_hours,
    ROUND(SUM(overtime_hours), 2) as total_overtime_hours,
    ROUND(AVG(CASE WHEN compliance_flag THEN 1 ELSE 0 END) * 100, 2) as overall_compliance_pct
FROM attendance;