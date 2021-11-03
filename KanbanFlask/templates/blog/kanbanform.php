Success! <?php

if(isset($_POST['description'])){
    $type = $_POST['type'];
    $assignee = htmlspecialchars($_POST['assignee']);
    $description = htmlspecialchars($_POST['description']);
    $fp = fopen('data.txt', 'a');
    fwrite($fp, PHP_EOL . $type . " (" . $assignee . "): " . $description);
    fclose($fp);
}
?>