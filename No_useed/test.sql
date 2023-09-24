explain select * FROM ms_search_library.ms_data ms where ms.mz > 1000 and ms.mz <1001 limit 0, 1000000000;
explain select * FROM ms_search_library.ms_data ms where ms.id > 100;
select * FROM ms_search_library.ms_data ms where ms.mz > 1000.01 and ms.mz <1005.02 limit 0, 100000000000;
select * FROM ms_search_library.ms_data ms where ms.id > 100 and ms.id <110;
Insert into ms_search_library.ms_data (mz,rt) values (100.002,100);