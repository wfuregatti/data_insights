select
  Sum(case when a.UnitPrice >= 200 then 1 else 0 end) as Brkt1, 
  Sum(case when a.UnitPrice >= 100 and a.UnitPrice < 200 then 1 else 0 end) as Brkt2,
  Sum(case when a.UnitPrice >= 50 and a.UnitPrice < 100 then 1 else 0 end) as Brkt3,
  sum(case when a.UnitPrice >= 10 and a.UnitPrice < 50  then 1 else 0 end) as Brkt4,
  sum(case when a.UnitPrice <= 10 then 1 else 0 end) as Brkt5 
from Warehouse.StockItems as a