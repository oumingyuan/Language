<?php

//$servername = "localhost";
//$username = "oumingyuan";
//$password = "new_password";
//
//try {
//    $conn = new PDO("mysql:host=$servername;dbname=inventory_management", $username, $password);
//    echo "连接成功";
//} catch (PDOException $e) {
//    echo $e->getMessage();
//}

$conn = @mysql_connect('localhost','oumingyuan','new_password');
if (!$conn) {
	die('Could not connect: ' . mysql_error());
}
mysql_select_db('inventory_management', $conn);

