<?php 
include_once('config.php');
	
	$name=addslashes($_REQUEST['name']);
	$email=addslashes($_REQUEST['email']);
	$phone=addslashes($_REQUEST['phone']);
	$courseid=(int)addslashes($_REQUEST['courseid']);
	
	date_default_timezone_set("Asia/kolkata");
	$date= date("Y-m-d H:i:s");
		if(!((strlen($name)>0)&&(strlen($phone)>0)&&(strlen($email)>0)&&(strlen($courseid)>0)))
			{
			 echo "<span style='color:#990000'>All Fields Are Required.</span>";
			 
				}
				else 
				{
					$queryy="Insert Into course_enroll(id, name, email, phone, course_id, date_timesss)
	   					values(NULL,'$name','$email','$phone','$courseid','$date')";
						$resu= mysql_query($queryy);
						
						 echo "<span style='color:#009900'>Your Message Sent Sucessfully</span>";
				}
	
