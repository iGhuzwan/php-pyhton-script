<?php 

$command = escapeshellcmd('python3 save.py');
$output = shell_exec($command);
echo $output;

?>