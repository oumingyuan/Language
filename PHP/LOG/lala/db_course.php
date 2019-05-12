*<?php
/**
 * Created by PhpStorm.
 * User: oumin
 * Date: 2018-01-19
 * Time: 下午 07:17
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

$sql = "SELECT * FROM `company_log`.`log_info` LIMIT 0, 1000";

$result = mysqli_query($conn, $sql);

if (mysqli_num_rows($result) > 0) {
    // 输出数据
    while ($row = mysqli_fetch_assoc($result)) {
        echo "日志日期: " . $row["log_date"] . " - 日志状态: " . $row["status_name"] . "<br>";
    }
} else {
    echo "0 结果";
}

mysqli_close($conn);