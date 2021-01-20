select PriceBracket, count(*) as TotalCount from(
select a.StockItemName,
	   case
	     when a.UnitPrice >= 200 then 'Brkt1'
	     when a.UnitPrice >= 100 then 'Brkt2'
	     when a.UnitPrice >= 50 then 'Brkt3'
	     when a.UnitPrice >= 10 then 'Brkt4'
	     else 'Brkt5' 
	   end as PriceBracket
from Warehouse.StockItems as a) as Brackets
group by PriceBracket

