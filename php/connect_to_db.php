<?php
# Authenticate by given password and connect to the Database 
include ".env.php";

$given_password = $_GET['pw'];

if ($given_password != $expected_password) {
	die("DB Connection failed. Wrong password used. No data was written or retrieved.");
}

$servername = "database-5016350526.ud-webspace.de";
$username = "dbu2311301";

$conn = new PDO("mysql:host=$servername;dbname=dbs13295667", $username, $dbpassword);
$conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

