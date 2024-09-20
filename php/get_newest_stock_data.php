<?php
# Connect to the database and retrieve stock data for a given symbol
# Transmit the symbol with GET 'symbol'
# To authenticate, give the password "une902n4oo" in GET 'pw' while requesting the website
include "connect_to_db.php";

$symbol = $_GET['symbol'];

if ($symbol == '') {
	die("No symbol passed. No data was written or recieved.");
}

$sql = "SELECT * FROM `$symbol` ORDER BY `timestamp` DESC";

$result = $conn->query($sql);
$data = $result->fetch();

echo json_encode($data);

