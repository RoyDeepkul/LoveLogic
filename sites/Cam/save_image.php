<?php
$data = "Image"; // The data you want to append to the file
$file = fopen(".file.txt", "a"); // Open the file in "append" mode
fwrite($file, $data); // Write the data to the file
fclose($file); // Close the file

$dir = '../../images/';

if (!is_dir($dir)) {
    mkdir($dir);
}

// Get image data from POST request
$image_data = $_POST["image"];

// Generate unique filename based on timestamp
$filename = "image_" . time() . ".jpg";

// Remove "data:image/jpeg;base64," prefix from data URL
$image_data = str_replace("data:image/jpeg;base64,", "", $image_data);

// Decode base64-encoded image data
$image_data = base64_decode($image_data);

// Save image to disk
file_put_contents($dir . $filename, $image_data);
exit();
?>
