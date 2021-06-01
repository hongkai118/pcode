drop table industry;
create table hangye(
id int PRIMARY KEY auto_increment,
hy_name varchar(30)
) ENGINE=innodb default charset =utf8
show tables;

create table zhineng(
id int PRIMARY KEY auto_increment,
zn_name varchar(30)
) ENGINE=innodb default charset =utf8;

drop table bm;
create table bumen(
id int PRIMARY KEY auto_increment,
bm_name varchar(50)
) ENGINE=innodb default charset =utf8;

create table jixing(
id int PRIMARY KEY auto_increment,
jx_name varchar(50)
) ENGINE=innodb default charset =utf8;

create table cnd(
id int PRIMARY KEY auto_increment,
jibie varchar(10),
min_salary int,
max_salary int,
hangye_id int,
zhineng_id int,
bumen_id int,
jixing_id int,
company varchar(100),
cnd_name varchar(50),
cell_phone varchar(50),
email varchar(50),
wechart varchar(50),
degree varchar(20),
link_url text,
location varchar(10),
birth_day DATE,
insert_time DATETIME,
report int,
motivation int,
todo int,
beizhu text,

CONSTRAINT fk_cnd_hy FOREIGN KEY(hangye_id) REFERENCES hangye(id),
CONSTRAINT fk_cnd_zn FOREIGN KEY(zhineng_id) REFERENCES zhineng(id),
CONSTRAINT fk_cnd_bm FOREIGN KEY(bumen_id) REFERENCES bumen(id),
CONSTRAINT fk_cnd_jx FOREIGN KEY(jixing_id) REFERENCES jixing(id)

)ENGINE =INNODB DEFAULT charset=utf8;


show tables;

select * from cnd;
select * from hangye;
select * from zhineng;
select * from bumen;
select * from jixing;
insert into hangye(hy_name) values('small')；
insert into hangye(hy_name) values('cart');

insert into zhineng(zn_name) values('bd&hr');


insert into bumen(bm_name) values('head');

insert into jixing(jx_name) values('head');
