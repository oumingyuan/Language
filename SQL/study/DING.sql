select * from table1;

create or replace procedure procedure1 as 
begin
    
  dbms_output.put_line('Hello World!');
end procedure1;

set serveroutput on 
exec procedure1;

/*没参数的话，直接 存储过程名就行
P1
有的话
exec P1 参数1,参数2

如果有输出参数的话

exec P1 参数1,参数2 output


当然参数要提前定义*/

select to_char(sysdate,'yyyy-mm-dd hh24:mi:ss') from dual; 

DECLARE
  SYSTEM_TIME VARCHAR2(200);
BEGIN

  PROCEDURE3(
    SYSTEM_TIME => SYSTEM_TIME
  );

DBMS_OUTPUT.PUT_LINE('SYSTEM_TIME = ' || SYSTEM_TIME);

  :SYSTEM_TIME := SYSTEM_TIME;
--rollback; 
END;
