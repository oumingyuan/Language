<?php
/**
 * Created by PhpStorm.
 * User: oumin
 * Date: 2018-01-19
 * Time: 下午 08:34
 */

$servername = "rm-uf64d5uetcz154o74o.mysql.rds.aliyuncs.com";
$username = "root";
$password = "omy15609681930!";
$dbname = "company_log";

// 创建连接
$conn = mysqli_connect($servername, $username, $password, $dbname);
// Check connection
if (!$conn) {
    die("连接失败: " . mysqli_connect_error());
}

$sql = "SELECT * FROM `company_log`.`log_info` WHERE status= 100 LIMIT 0, 1000";
$result = mysqli_query($conn, $sql);

if (!$result) {

    printf("Error:%s\n", mysqli_error($conn));
    exit();

}

$jarr = array();

while ($rows = mysqli_fetch_array($result, MYSQLI_ASSOC)) {
    $count = count($rows);//每次删除都会变小，不能放循环

    for ($i = 0; $i < $count; $i++) {
        unset($rows[$i]);//删除冗余数据
    }

    array_push($jarr, $rows);
}

//print_r($jarr);//查看数组
//echo "<br>";
//echo "<br>";

$response = json_encode($jarr);

echo $response;





