SELECT * FROM ms_search_library.compound_data;
select max(length(name)),max(length(id)) FROM ms_search_library.compound_data;
select name from ms_search_library.compound_data where length(name) > 760;
explain select name from ms_search_library.compound_data where name like "%'tet%";
select count(*) from ms_search_library.compound_data;
