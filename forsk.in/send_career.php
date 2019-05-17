<?php
include_once('config.php');

	$name=addslashes($_REQUEST['name']);
	$email=addslashes($_REQUEST['email']);
	$phone=addslashes($_REQUEST['phone']);
	$city=addslashes($_REQUEST['city']);
	$msg=addslashes($_REQUEST['msg']);
	date_default_timezone_set("Asia/kolkata");
	$date= date("Y-m-d H:i:s");
		if(!((strlen($name)>0)&&(strlen($phone)>0)&&(strlen($email)>0)))
			{
			 echo "<span style='color:#990000'>All Fields Are Required.</span>";

				}
				else
				{
					$queryy="Insert Into career(id, name, phone_number, email_id, city, describe_yourself, datetimesss)
	   					values(NULL,'$name', '$phone','$email','$city','$msg','$date')";
						$resu= mysql_query($queryy);
            // $myemail='vaidkunal09@gmail.com';
            $myemail='yogendrasinsinwar@gmail.com';
						$to = $myemail;
			 		$subject = "Career Enquiry";
          $message1 = " $name, has sent an Enquiry to our Website about Career,\n\n".  "His/Her Contact Number is : $phone\n\n" . "Email ID is:  $email\n\n". "City is:  $city\n\n". "About Him/Her : $msg";
			 		$headers = "From: $name <$email>";
			 		@$sent = mail($to, $subject, $message1, $headers) ;

          $to1 = $email;
          $subject2 = "Forsk Labs | Career Response";
          $message2 = "<html><body>";
          $message2 .= "<p>Hi ".$name.",</p><br>";
          $message2 .= "<p>Welcome to Forsk Technologies,</p><p>We have innumerous career options based on new emerging technologies like FullStack Developer, IoT Developer, Data Scientist and much more.</p><p>We'll get in touch with you as soon as possible</p>";
          $message2 .= '<br><p>Feel free to call us on <a href="tel:9414291932">+91-9414291932</a> for any information/assistance. We are looking forward to hear from you.</p><br>';
          $message2 .= '<p>Regards,</p><p>Forsk Team</p><p><a href="tel:9414291932">+91-9414291932</a></p><p><a href="http://www.forsk.in">www.forsk.in</a></p><br>';
          $message2 .= '<p>Visit out Facebook page for latest updates and events:<a href="https://www.facebook.com/forsklabs">https://www.facebook.com/forsklabs</a></p>';
          $message2 .= "</body></html>";
          $headers1 = 'From:	Forsk Labs <info@forsk.in>'."\r\n";
          $headers1 .= 'MIME-Version: 1.0' . "\r\n";
          $headers1 .= 'Content-Type: text/html; charset=ISO-8859-1'."\r\n";
          @$sent = mail($to1, $subject2, $message2, $headers1) ;

						//  echo "<span style='color:#009900' title='Success'>Your Message Sent Sucessfully</span>";
						//  echo "<span style='color:#009900'>Your Message Sent Sucessfully</span>";
				}
