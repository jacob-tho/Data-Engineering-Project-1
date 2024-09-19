<?php
# Connect to the database and upload stock information.
# Give a JSON Object in GET 'data' when requesting the database
# To authenticate, give the password "qinj73oqjn3p" as well in 'pw'

$data = $_GET['data'];
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

echo $data;

