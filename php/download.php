<?php
# Connect to the database and retrieve all stock data
# To authenticate, give the password "qinj73oqjn3p" in GET 'pw' while requesting the website

$given_password = $_GET['pw'];
$expected_password = "qinj73oqjn3p";

if ($given_password != $expected_password) {
	die("DB Connection failed. Wrong password used. No data was written or retrieved.");
}

$servername = "database-5016350526.ud-webspace.de";
$username = "dbu2311301";
$password = "StockDataIsSafe1!";
$databsename = "dbs13295667";

$conn = new PDO("mysql:host=$servername;dbname=$databasename", $username, $password);
$conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);


