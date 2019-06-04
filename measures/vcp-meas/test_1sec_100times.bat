@echo off
SET /A "index=1"
SET /A "count=100"
:while
if %index% leq %count% (
   echo The value of index is %index%
   SET /A "index=index + 1"
   python uart_1sec_test.py
   goto :while
)

pause