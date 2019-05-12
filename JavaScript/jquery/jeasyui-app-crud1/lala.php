<?php
$servername = "localhost";
$username = "oumingyuan";
$password = "new_password";
$dbname = "inventory_management";

// 创建连接
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("连接失败: " . $conn->connect_error);
}

$sql = "select * from users";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // 输出数据
    while($row = $result->fetch_assoc()) {
        echo $row["firstname"];echo "   ";
        echo $row["lastname"];echo "   ";
        echo $row["phone"];echo "   ";
        echo $row["email"];echo "   ";

        echo "\n";

    }
} else {
    echo "0 结果";
}
$conn->close();