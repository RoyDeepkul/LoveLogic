<?php
// Get latitude and longitude data from POST request
$data = file_get_contents("php://input");
$dataObj = json_decode($data);
$latitude = $dataObj->latitude;
$longitude = $dataObj->longitude;

// Save location data to a text file
$filename = "user_locations.txt";
$file = fopen($filename, "a");
fwrite($file, "Location: {$latitude},{$longitude}\n");
fclose($file);
?>
