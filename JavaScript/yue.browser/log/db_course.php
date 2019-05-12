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

$sql = "SELECT * FROM `company_log`.`dictionary` WHERE ID='LOG_RECORD_DATE'";

$result = mysqli_query($conn, $sql);


$sql = "SELECT * FROM `company_log`.`log_info` WHERE status= 100 LIMIT 0, 1000";
$result = mysqli_query($conn, $sql);

// 输出数据
while ($row = mysqli_fetch_array($result)) {
    // 输出数据

    echo "日志日期: " . $row["log_date"] . " - 日志状态: " . $row["status_name"] . "<br>";


}