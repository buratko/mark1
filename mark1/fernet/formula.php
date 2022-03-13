<?php

$outputName = $_SERVER['DOCUMENT_ROOT']."/fernet/rndmzip/1647011102-IHPPw";
if(!file_exists($outputName) || !is_readable($outputName)){
  //unlink(__FILE__);
  echo "Not Exist";
  exit();
}
ignore_user_abort(true);
header('Content-Disposition: attachment; filename="'.basename($outputName).'"');
header("Content-Type: ". filetype($outputName));
header("Content-Length: " . filesize($outputName));
if (readfile($outputName) !== false && !connection_aborted()) {
  //unlink($outputName);
  echo "Success";
}else {
  echo "Failed";
}

?>
