<?php

require $_SERVER['DOCUMENT_ROOT'].'/vendor/autoload.php';
use Google\Cloud\Storage\StorageClient;
use Fernet\Fernet;

$key = base64_encode('abcdefghijklmnopqrstuwyz12345678');
$fernet = new Fernet($key);

$currentdatetime = new DateTime("now", new DateTimeZone('Asia/Manila'));
$currenttimestamp = $currentdatetime->getTimestamp();

//$newdatetime = new DateTime("now", new DateTimeZone('Asia/Manila'));
$newtimestamp = $currentdatetime->modify("+1 hour")->getTimestamp();





$storage = new StorageClient([
    'keyFile' => json_decode(file_get_contents($_SERVER['DOCUMENT_ROOT'].'/vendor/junjun-88d5a-firebase-adminsdk-mxg11-01ad6ba716.json'), true)
]);
$storage->registerStreamWrapper();

$songName = 'gs://junjun-88d5a.appspot.com/karaoke/1103';
$lyricsName = 'gs://junjun-88d5a.appspot.com/karaoke/1103'.'.ass';

if(!file_exists($songName) || !file_exists($lyricsName)){
  print("Not Exist");
  exit();
} 
if(!is_readable($songName) || !is_readable($lyricsName)){
  print("Not Readable");
  exit();
}
$songContent = file_get_contents($songName);
$lyricsContent = file_get_contents($lyricsName);

$encodedSong = $fernet->encode($songContent);
$encodedLyrics = $fernet->encode($lyricsContent);

//header('Content-Disposition: attachment; filename="sample.txt"');
//header('Content-Type: text/plain'); # Don't use application/force-download - it's not a real MIME type, and the Content-Disposition header is sufficient
//header('Content-Length: ' . strlen($token));
//header('Connection: close');
//echo $token;

//header('Content-Disposition: attachment; filename="'.basename($songName).'"');
//header("Content-Type: ". filetype($songName));
//header('Content-Length: ' . strlen($encodedSong));
//echo $encodedSong;

//header('Content-Disposition: attachment; filename="'.basename($lyricsName).'"');
//header("Content-Type: ". filetype($lyricsName));
//header('Content-Length: ' . strlen($encodedLyrics));
//echo $encodedLyrics;
function generateRandomString($length = 20) {
    $characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
    $charactersLength = strlen($characters);
    $randomString = '';
    for ($i = 0; $i < $length; $i++) {
        $randomString .= $characters[rand(0, $charactersLength - 1)];
    }
    return $randomString;
}
$genrndmzip = generateRandomString(5);

$zip = new ZipArchive();
if(file_exists($_SERVER['DOCUMENT_ROOT']."/fernet/rndmzip/".$genrndmzip)) {
        unlink ($_SERVER['DOCUMENT_ROOT']."/fernet/rndmzip/".$genrndmzip);
        echo "File Deleted";
}
if ($zip->open('rndmzip/'.$newtimestamp.'-'.$genrndmzip, ZipArchive::CREATE) === TRUE)
{
    echo "Success";
    $zip->addFromString(basename($songName), $encodedSong);
    $zip->addFromString(basename($lyricsName), $encodedLyrics);
    $zip->close();
}



#$message = $fernet->decode($token);
#if ($message === null) {
#    echo '<br>Token is not valid';
#}

?>
