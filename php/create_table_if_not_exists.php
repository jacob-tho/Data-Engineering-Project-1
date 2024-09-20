<?php
include ".env.php";
# Connect to the database and retrieve all stock data
# To authenticate, give the password "une902n4oo" in GET 'pw' while requesting the website

$given_password = $_GET['pw'];
$symbol = $_GET['symbol'];

$expected_password = "une902n4oo";

if ($given_password != $expected_password) {
	die("DB Connection failed. Wrong password used. No data was written or retrieved.");
}

if ($symbol == '') {
	die("No symbol passed. No data was written or recieved.");
}

$servername = "database-5016350526.ud-webspace.de";
$username = "dbu2311301";
$password = "StockDataIsSafe1!";
$databsename = "dbs13295667";

$conn = new PDO("mysql:host=$servername;dbname=dbs13295667", $username, $password);
$conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

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


