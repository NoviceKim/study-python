use test;

create table tbl_member(
    email varchar(255) primary key,
    password varchar(255) not null,
    name varchar(255)
);

select * from tbl_member;
commit;

create table tbl_product(
    id bigint auto_increment primary key,
    name varchar(255) not null,
    price int default 0,
    created_date datetime
);

select * from tbl_product;

update tbl_product set price = price * 0.9
                   where price >= 3000;

rollback;

(select avg(p.price) from (select count(id) total_count from tbl_product
group by created_date) cp join tbl_product p);