# Cosmetic

localhost:8000/api/products/ - api для связи бека и фронта;


localhost:8000/api/products/Creams/ - товары из категории кремы;

localhost:8000/api/products/Perfumes/ - товары из категории духи;


Фильтры:
  Кремы:
    brand - принимает: Levrana, Ecolab, Chocolatte, Cafe_Mimi;
    price;
    cream_for - принимает: child, woman, man;
    type_of_derm - принимает: dry, fat, old, sens, comb;
  
  Духи:
    brand - принимает: Reni, Mane, IFF;
    price;
    perfume_volume - числа; 
   
Фильтры настраиваются в таблице: Категории;

можно посмотреть вывод на localhost:8000/api/perfume/ или localhost:8000/api/cream/;
