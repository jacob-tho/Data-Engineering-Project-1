<?php
# Connect to the database and insert stock data for a given symbol
# Transmit the symbol with GET 'symbol'
# Transfer the rest of the data in a JSON-stringified object. GET "stock_data"
# To authenticate, give the password in GET 'pw' while requesting the website
include "connect_to_db.php";

$symbol = $_GET['symbol'];
$stock_data = $_GET['stock_data'];

if ($symbol == '' || !isset($symbol)) {
	die("No symbol passed. No data was written or recieved.");
}
if ($stock_data == '' || !isset($stock_data)) {
	die("No stock data transmitted. No data was written or recieved.");
}

$stock_data = json_decode($stock_data, true);

ini_set('display_errors', '1');
ini_set('display_startup_errors', '1');
error_reporting(E_ALL);

$timestamp = $stock_data['timestamp'];
$open = $stock_data['open'];
$high = $stock_data['high'];
$low = $stock_data['low'];
$close = $stock_data['close'];
$volume = $stock_data['volume'];
$rate_of_change = $stock_data['rate_of_change'];

$sql = "INSERT INTO `$symbol` (`id`, `timestamp`, `open`, `high`, `low`, `close`, `volume`, `rate_of_change`) VALUES 
	(NULL, '$timestamp', '$open', '$high', '$low', '$close', '$volume', '$rate_of_change');";

$result = $conn->query($sql);

