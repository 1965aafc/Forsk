<?php
include_once('config.php');

	$name=addslashes($_REQUEST['name']);
	$email=addslashes($_REQUEST['email']);
	$phone=addslashes($_REQUEST['phone']);
	$msg=addslashes($_REQUEST['msg']);
	$loc=addslashes($_REQUEST['loc']);
	$dwnld_link=addslashes($_REQUEST['dwnld_link']);
	$subba=addslashes($_REQUEST['subba']);
	$cntnt=$_REQUEST['cntnt'];
	$pdf_link=$_REQUEST['pdf_link'];
	date_default_timezone_set("Asia/kolkata");
	// echo $pdf_link;die;
	// print_r($_REQUEST);die;
	$date= date("Y-m-d H:i:s");
		if(!((strlen($name)>0)&&(strlen($phone)>0)&&(strlen($email)>0)))
			{
			 echo "<span style='color:#990000'>All Fields Are Required.</span>";

				}
				else
				{
					$queryy="Insert Into get_syllabus(id, name, phone_no, email_id, datetimes, from_hire_get)
	   					values(NULL,'$name'  ,'$email', '$phone','$date','$msg')";
						$resu= mysql_query($queryy);
						// $myemail='vaidkunal09@gmail.com';
						$myemail='yogendrasinsinwar@gmail.com';
						$to = $myemail;
			 		$subject = "Course Enquiry for $msg / $loc";
          // $subject = "Forsklabs.in | Contact Information";

			 		$message1 = " $name, has sent an Enquiry to our Website\n\n".  "His/Her Contact Number is : $phone\n\n" . "Email ID is:  $email\n\n". "Contact For : $msg / $loc";
			 		$headers = "From: $name <$email>";
			 		@$sent = mail($to, $subject, $message1, $headers) ;

					$to1 = $email;
          // $subject2 = "Forsklabs.in | Contact Information";
			 		$subject2 = $subba;

          // $message2 = "Thanks for getting in touch! You can Download the Brochure by clicking the follwoing link $dwnld_link"."\n\n"." *** This is an automatically generated email, please do not reply ***" ;
          $message2 = "<html><body>";
          $message2 .= "<p>Hi ".$name.",</p><br>";
					$message2 .= $cntnt;
          $message2 .= '<br><p><a href="'.$dwnld_link.'">Click Here For Enroll</a></p>';
          $message2 .= '<br><p>Feel free to call us on <a href="tel:9414291932">+91-9414291932</a> for any information/assistance. We are looking forward to hear from you.</p><br>';
          $message2 .= '<p>Regards,</p><p>Forsk Team</p><p><a href="tel:9414291932">+91-9414291932</a></p><p><a href="http://www.forsk.in">www.forsk.in</a></p><br>';
          $message2 .= '<p>Visit out Facebook page for latest updates and events:<a href="https://www.facebook.com/forsklabs">https://www.facebook.com/forsklabs</a></p>';
          $message2 .= "</body></html>";
          // $headers1 = "From:info@forsklabs.in";
			 		$headers1 = 'From:	Forsk Labs <info@forsk.in>'."\r\n";
          $headers1 .= 'MIME-Version: 1.0' . "\r\n";
          $headers1 .= 'Content-Type: text/html; charset=ISO-8859-1'."\r\n";
					$lnk = strrpos($message2, "downloads/");
					if ($lnk){
						  $mes=substr_replace($message2,$pdf_link, $lnk+10, 0);
						}
					// echo $message2;
					// die;


					@$sent = mail($to1, $subject2, $mes, $headers1) ;


						 echo "<span style='color:#009900'>Your Download link is Sent Sucessfully on your Email</span>";
				}
