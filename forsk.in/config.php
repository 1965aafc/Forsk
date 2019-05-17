<?php
session_start();

/*shiksha_forsk$conn=mysql_connect("shiksha_forsk","root","") or die("Unable to Create Connection");
$db=mysql_select_db("shiksha_forsk") or die ("Unable to Connect to DataBase");
*/

// $conn=mysql_connect("localhost","root","") or die("Unable to Create Connection");
// $db=mysql_select_db("forsk") or die ("Unable to Connect to DataBase"); 

$conn=mysql_connect("localhost","alphonic","alphonic123") or die("Unable to Create Connection");
$db=mysql_select_db("alphonicforsk") or die ("Unable to Connect to DataBase");
