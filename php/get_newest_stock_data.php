<?php
# Connect to the database and retrieve stock data (newest entry) for a given symbol
# Transmit the symbol with GET 'symbol'
include "connect_to_db.php";

$symbol = $_GET['symbol'];

if ($symbol == '') {
	die("No symbol passed. No data was written or recieved.");
}

$sql = "SELECT * FROM `$symbol` ORDER BY `timestamp` DESC";

$result = $conn->query($sql);
$data = $result->fetch();

echo json_encode($data);

