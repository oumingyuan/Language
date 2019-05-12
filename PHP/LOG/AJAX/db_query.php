<?php
/**
 * Created by PhpStorm.
 * User: oumin
 * Date: 2018-01-19
 * Time: 下午 08:29
 */

$servername = "rm-uf64d5uetcz154o74o.mysql.rds.aliyuncs.com";
$username = "root";
$password = "omy15609681930!";
$dbname = "company_log";

// 创建连接
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("连接失败: " . $conn->connect_error);
}

$sql = "SELECT * FROM `company_log`.`log_info` LIMIT 0, 1000";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // 输出数据
    while ($row = $result->fetch_assoc()) {
        echo "日志日期: " . $row["log_date"] . " - 日志状态: " . $row["status_name"] . "<br>";
    }
} else {
    echo "0 结果";
}
$conn->close();