<?php
# Connect to the database and retrieve all stock data
# To authenticate, give the password "une902n4oo" in GET 'pw' while requesting the website
include "connect_to_db.php";

$symbol = $_GET['symbol'];

if ($symbol == '') {
	die("No symbol passed. No data was written or recieved.");
}

$sql = "CREATE TABLE IF NOT EXISTS $symbol (
        id INT AUTO_INCREMENT PRIMARY KEY,
        timestamp DATETIME,
        open FLOAT,
        high FLOAT,
        low FLOAT,
        close FLOAT,
        volume INTEGER,
        rate_of_change DECIMAL(15,3)
        )";

$result = $conn->query($sql);


