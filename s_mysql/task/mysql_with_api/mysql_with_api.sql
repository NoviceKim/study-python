use test;

create table tbl_ocr(
    id bigint auto_increment primary key,
    url varchar(255) not null,
    text varchar(255) not null
);

select * from tbl_ocr;

create table tbl_papago(
    id bigint auto_increment primary key,
    kor varchar(255) not null,
    eng varchar(255) not null
);

select * from tbl_papago;

