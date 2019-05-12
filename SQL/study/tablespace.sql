SELECT * FROM v$tablespace;

SELECT
    t.TS# AS "number",
    t.NAME AS "name",
    t.INCLUDED_IN_DATABASE_BACKUP AS "backup",   --就是说在rman备份数据库时，这个表空间是否也包含在备份中
    t.BIGFILE AS "bigFile",
    t.FLASHBACK_ON AS "flashBack"        
    /*
    闪回技术通常用于快速简单恢复数据库中出现的认为误操作等逻辑错误
    从闪回的方式可以分为基于数据库级别闪回、表级别闪回、事务级别闪回，
    根据闪回对数据的影响程度又可以分为闪回恢复，闪回查询。
    */
    
FROM v$tablespace t;
--table space   表格空间


/*分为四步 */
/*第1步：创建临时表空间  */
create temporary tablespace apple  
tempfile 'D:\oracleData\apple.dbf' 
size 50m  
autoextend on  
next 50m maxsize 100m  
extent management local;

/*第2步：创建数据表空间  */
create tablespace myApple
logging  
datafile 'D:\oracleData\myApple.dbf' 
size 50m  
autoextend on  
next 50m maxsize 100m  
extent management local; 

/*第3步：创建用户并指定表空间  */
create user cat identified by password  
default tablespace myApple  
temporary tablespace apple; 

/*第4步：给用户授予权限  */
grant connect,resource,dba to cat;

create or replace procedure proc1(      --or replace  的意思不管数据中是否有存储过程，如果没有的话就创建，有的话就覆盖；很强大的功能
para1 varchar2,
para2 out varchar2,
para3 in out varchar2
) as
v_name varchar2(20);
begin
 v_name :='zhangsf';
 para3 := v_name;
dbms_output.put_line('para3:'||para3);
end;

--INSERT INTO "CAT"."PERSON" (NAME) VALUES ('丁雪莲')

create or replace procedure fish as ...
begin
INSERT INTO "CAT"."PERSON" (NAME) VALUES ('丁浩')
end;

CREATE OR REPLACE PROCEDURE monkey AS
--声明语句段
v_name VARCHAR2(20);
BEGIN
--执行语句段
INSERT INTO "CAT"."PERSON" (NAME) VALUES ('丁浩');

END;

select * from cat.person;


