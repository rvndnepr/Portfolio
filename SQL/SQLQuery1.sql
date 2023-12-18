/* создание новой таблицы в базе данных*/

create table cars (car_id int NOT NULL, brand_name text, model text, engine_type text, transmission text, production_year int, mileage int, color text, price int, client_id int);


/* добавление поля в таблицу и удаление*/

alter table cars add date int NULL;

alter table cars drop column date;


/* изменение типа данных в указанных полях указанной таблицы (в данном случае было изменено с text на varchar(50))*/

alter table cars alter column brand_name varchar(50) NULL;

alter table cars alter column model varchar(50) NULL;

alter table cars alter column engine_type varchar(50) NULL;

alter table cars alter column transmission varchar(50) NULL;

alter table cars alter column color varchar(50) NULL;


/* присвоение значений полям в указанной таблице*/

insert into cars values (1,'Ford','Focus','gas','mechanic',2018,39000,'white',13500, 35);					
insert into cars values (2,'Renault','Megane','diesel','mechanic',2014,95000,'silver',11500, 4);				
insert into cars values (3,'Chevrolet','Cruze','gas','automat',2017,82000,'red',12000, 44);					
insert into cars values (4,'Hyundai','Elantra','gas','mechanic',2015,78000,'black',12300, 17);					
insert into cars values (5,'Skoda ','Octavia','diesel','automat',2012,112000,'blue',11000, null);					
insert into cars values (6,'KIA','Cerrato','gas','variator',2014,91000,'grey',10500, 9);				
insert into cars values (7,'VolksWagen','Jetta','diesel','robot',2017,72000,'beige',12100, 38);					
insert into cars values (8,'Toyota','Avensis','gas','robot',2019,34000,'white',14900, 21);					
insert into cars values (9,'Volvo','S60','diesel','automat',2018,84000,'black',13700, 50);					
insert into cars values (10,'Nissan','Altima','gas','mechanic',2014,105000,'grey',11400, null);					
insert into cars values (11,'Reugeot','308','diesel','variator',2017,124000,'white',10800, 57);					
insert into cars values (12,'Honda','Accord','gas','automat',2013,118000,'red',10200, 55);	


/* удаление всех данных из указанной таблицы*/

delete from cars;


/* изменение данных для указанного поля указанной таблицы по любому из ключевых значений записи ( например car_id - 11)*/

update cars set brand_name = 'Peugeot' where car_id = 11;


/* простой вывод данных таблицы*/

select * from cars; /* вывод всех данных из указанной таблицы*/

select car_id, brand_name, model, production_year from cars; /* пвывод всех данных указанных полей из указанной таблицы*/


/* вывод всех данных из указанной таблицы соответствующих определенным условиям */

select * from cars where mileage <= 95000 and not production_year = 2018; /* вывод всех данных, где значение поля mileage больше либо равно 95000, а значение поля production_year не равно 2018*/

select * from cars where production_year > 2015 or price < 11000; /* вывод всех данных, где либо значение поля production_year больше 2015, либо значени поля price меньше 11000*/

select * from cars where transmission != 'mechanic' or brand_name = 'Ford'; /* вывод всех данных где значения поля transmission не равно 'mechanic', либо значения поля brand_name - слово 'Ford'*/

select * from cars where not model like 'A%' and engine_type like '_as%'; /* вывод всех данных где значения поля model начинаются не с буквы 'A', а 2-я и 3-я буквы значения поля engine_type - это буквы 'a' и 's'*/

select * from cars where model like '[ACO]%'; /* вывод всех данных где значения поля model начинаются либо с буквы 'A', либо, 'C', либо 'O'*/

select * from cars where brand_name like '[F-N]%'; /* вывод всех данных где значения поля model кначинаются с букв в диапазоне от 'F' до 'N'*/

select * from cars where not brand_name like '[HV]%'; /* вывод всех данных где значения поля model начинаются не с букв 'H' и 'V'*/

select * from cars where transmission in ('mechanic','automat'); /* вывод всех данных где значения поля transmission это 'mechanic' и 'automat'*/

select * from cars where transmission not in ('mechanic','automat'); /* вывод всех данных где значения поля transmission все кроме 'mechanic' и 'automat'*/


/* вывод всех данных соответствующих определенным условиям из указанной таблицы + сортировка данных по возрастанию/убыванию в указанном поле*/

select * from cars where not mileage between 50000 and 100000 order by mileage ASC; /* вывод всех данных, где значение поля mileage не в диапазоне от 50000 до 100000 и сортировка по возрастанию значений mileage*/

select * from cars where production_year in (2017, 2018, 2019) order by mileage DESC; /* вывод всех данных, где значение поля production_year равно 2017, 2018, 2019 и сортировка по убыванию значений поля mileage*/

select * from cars where not transmission like 'robot' order by mileage ASC; /* вывод всех данных, где значение поля transmission любые кроме 'robot' и сортировка по возрастанию значений поля mileage*/

select * from cars where production_year > 2014 order by price DESC; /* вывод всех данных, где значение поля production_year больше 2014 и сортировка по убыванию значений поля price*/

select top 5 brand_name, model from cars where price < 12000 order by brand_name DESC; /* вывод для полей brand_name и model первых пяти записей для которых значения поля price < 12000 + обратная соритровка*/

select * from cars order by brand_name, model; /* вывод всех данных таблицы и сортировка по возрвстанию сначала для значений поля brand_name, а затем для значений поля model*/


/* вывод всех данных из указанной таблицы где выполнением условия для определенного поля этой таблицы будет выполнение условие поля с таким же названием (по ключевому значению client_id) в другой таблице*/

select * from clients where client_id in (select client_id from cars where production_year > 2014);

select * from cars where client_id in (select client_id from clients where city like 'Kiev');


/* Агрегатные команды*/

select avg (mileage) from cars; /*среднее значение указанного поля указанной таблицы*/

select sum (price) from cars; /*сумма всех значений указанного поля указанной таблицы*/

select min (production_year) from cars; /*минимальное значение указанного поля указанной таблицы*/

select count(*) from cars where transmission like 'automat'; /* количество всех записей указанной таблицы где для поля transmission соответствует значение 'automat'*/

select distinct color from cars; /* пвывод всех уникальных данных указаного поля из указанной таблицы*/


/* группировка по щдному из полей указанной таблицы*/

select color from cars group by color;

/* группировка по максимальному production_year для всех возможных вариантов значения поля transmission*/

select transmission, max(production_year) as max_year from cars group by transmission;

/* группировка по максимальному production_year для всех возможных вариантов значения поля transmission, для которых значение поля max_year будет равно 2018. Поскольку команду where нельзя использовать с агрегатными
командами, то в данном случае используется команда having вместо where*/

select transmission, max(production_year) as max_year from cars group by transmission having max(production_year) = 2018;

/* группировка по среднему значению mileage для всех возможных вариантов значения поля engine_type*/

select engine_type, avg(mileage) as mileage from cars group by engine_type;

/* группировка по одному из полей, подсчет количества значений в группах в данном поле*/

select color, count(*) as qantity from cars group by color;

/* группировка по одному из полей, подсчет количества значений в группах в данном поле + сортировка по убыванию*/

select color, count(*) as qantity from cars group by color order by count(*) DESC;



/* объединение двух таблиц (по ключевому значению client_id) и вывод данных указанных полей из одной и другой таблицы в одной общей таблице*/

select cars.brand_name, cars.production_year, clients.client_name, clients.city from cars join clients on cars.client_id = clients.client_id;

/* объединение двух таблиц по данным левой таблицы (по ключевому значению client_id) и вывод всех данных указанных полей в одной общей таблице*/

select * from cars left join clients on cars.client_id = clients.client_id;

/* объединение двух таблиц по данным левой таблицы (по ключевому значению client_id) и вывод всех только тех полей у которых во второй таблице для поле client_id имеет значение null*/

select * from cars left join clients on cars.client_id = clients.client_id where clients.client_id is null;



create table clients (client_id int NOT NULL, client_name text, drive_experience int, city text, car_id int);

alter table clients alter column city varchar(50) NULL;

alter table clients alter column client_name varchar(50) NULL;

insert into clients values (4,'Denis Sokolov',10,'Dnepr')			
insert into clients values (9,'Andrey Yurchenko',14,'Kiev')			
insert into clients values (17,'Marina Muzichenko',7,'Kharkov')			
insert into clients values (21,'Gleb Kovalevskiy',8,'Dnepr')			
insert into clients values (35,'Maxim Zinchuk',11,'Lvov')			
insert into clients values (38,'Kirill Vasiliev',21,'Odessa')			
insert into clients values (44,'Anastasia Sivko',5,'Kiev')			
insert into clients values (50,'Mikhail Dudnik',19,'Kiev')			
insert into clients values (55,'Tatiana Grineva',12,'Odessa')			
insert into clients values (57,'Sergey Bogosian',9,'Dnepr')


alter table clients add date int NULL;

alter table clients drop column date;


delete from clients;



select * from clients;

select * from clients order by client_name DESC;

select client_name, drive_experiense, city from clients where drive_experiense > 10 and client_id >= 6;

select * from clients right join cars on clients.client_id = cars.client_id;
