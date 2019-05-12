<?php
/**
 * Created by PhpStorm.
 * User: oumin
 * Date: 2018-01-19
 * Time: 下午 06:45
 */

$servername = "rm-uf64d5uetcz154o74o.mysql.rds.aliyuncs.com";
$username = "root";
$password = "omy15609681930!";

// 创建连接
$conn = new mysqli($servername, $username, $password);

// 检测连接
if ($conn->connect_error) {
    die("连接失败: " . $conn->connect_error);
}
echo "连接成功";

echo "<br>";
echo "<br>";
echo "<br>";


$sql = "SELECT * FROM `company_log`.`log_info` LIMIT 0, 1000";


$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // 输出数据
    while ($row = $result->fetch_assoc()) {

//      echo $result;

//        echo $row;
        echo "日志日期: " . $row["log_date"] . " - 日志状态: " . $row["status_name"] . "<br>";
    }
} else {
    echo "0 结果";
}
$conn->close();

