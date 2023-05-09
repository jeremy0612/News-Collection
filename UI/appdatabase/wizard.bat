@echo off
mode con: cols=80 lines=30
color 08
echo ========================= Hello Reader! =================================
echo --------------- WELCOME TO OUR NEWS COLLECTION APPLICATION --------------
echo    ------------------------------------------------------------------------
echo   / You are running a sample data construction built for this application. /
echo  / Our project was built in Python and the datas would be stored in MySQL /
echo / database.                                                              /
echo  ------------------------------------------------------------------------
echo                Please provide the password of you localhost 
mysql -u root -p < DDL_Script.sql