
<!DOCTYPE html>
<html>
<head>
    <title>Forsk</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <link rel="shortcut icon" href="images/favicon.ico" type="image/x-icon">
    <link href="css/bootstrap.css" rel='stylesheet' type='text/css' />
    <script type="text/javascript" src="js/jquery-1.11.0.min.js"></script>
    <link href="css/Reset.css" rel="stylesheet" type="text/css" />
    <link href="css/style.css" rel="stylesheet" type="text/css" media="all" />
    <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
    <script src="https://code.jquery.com/jquery-1.12.4.js"></script>
  <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
  <!-- <link rel="stylesheet" href="/resources/demos/style.css"> -->
 <script src="js/bootstrap.min.js"></script>
	<script src="js/navcall.js"></script>
	<script src="js/wow.min.js"></script>
    <script>new WOW().init();</script>
    <style>
         .ui-widget-header,.ui-state-default, ui-button {
            background:#b9cd6d;
            border: 1px solid #b9cd6d;
            /*border: 1px solid #b9cd6d;*/
            color: #FFFFFF;
            font-weight: bold;
         }
         .ui-dialog-titlebar-close {
    visibility: hidden;
}
      </style>
<script language="javascript">
  $( function() {
  $( "#messagediv" ).dialog({
    autoOpen: false,
    draggable: false,
    hide:"puff"
  });
  } );
	function send_message(){
	var name = document.getElementById("name").value;
	var email = document.getElementById("email").value;
	var phone = document.getElementById("phone").value;
	var city = document.getElementById("city").value;
	var msg = document.getElementById("msg").value;

	var xmlhttp;
if (window.XMLHttpRequest)
  {// code for IE7+, Firefox, Chrome, Opera, Safari
  xmlhttp=new XMLHttpRequest();
  }
else
  {// code for IE6, IE5
  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
xmlhttp.onreadystatechange=function()
  {
  if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {

    // document.getElementById("messagediv").innerHTML = xmlhttp.responseText;
    $(function() {
        $( "#messagediv" ).dialog( "open" );
    });
    setTimeout(function() { $( "#messagediv" ).dialog('close'); }, 3000);
    document.getElementById("ff").reset();
	}
  }
xmlhttp.open("GET","send_career.php?name="+name+"&email="+email+"&phone="+phone+"&msg="+msg+"&city="+city,true);




	xmlhttp.send(null);
	return false;
	}
</script>
</head>
<body>
    <div class="header box css3-shadow" id="head">
        <div class="container">
            <div class="row">
                <div class="header-top">
                    <?php include('header.php'); ?>


                    <div class="clearfix"> </div>
                </div>
            </div><!-- end header -->
        </div>
    </div>


    <div class="btmmenu">
        <div class="container">
            <ul class="btmnav">
                <li><a href="about.php">About us</a></li>
                <li><a href="leadership.php">Leadership</a></li>
                <li><a href="advisory-board.php">Advisory Board</a></li>
                <li><a href="career.php" class="btactive">Career</a></li>
                <li><a href="contact.php">Contact us</a></li>
            </ul>
        </div>
    </div>

    <div class="sec-banner txt-center"><img src="images/career.jpg" width="100%" /> </div>


			<div class="container">
                <div class="pagecontent txt-center col-md-12">
                    <h1 class="wow fadeInUp txt-center" data-wow-delay="0.4s">Personal Information</h1>


                    <div class="contact main">

                        <p class="wow fadeInUp animated animated" data-wow-delay="0.4s">Come join Forsk team to be part of a very exciting journey where you get to be part of the dynamic start up ecosystem, learn and evolve into a top mobile/IoT/web professional and along the way, create a great career for yourself.</p>
                        <form class="wow fadeInUp animated" data-wow-delay="0.4s" onsubmit="return send_message()" id="ff">
                            <input type="text" class="text" value="Full Name *" id="name"  required onfocus="this.value = '';" onblur="    if (this.value == '') { this.value = 'Full Name *'; }">
                            <input type="text" class="text" value="Phone Number *" pattern="[0-9]{10,10}" maxlength="10" id="phone" onfocus="this.value = '';" onblur="    if (this.value == '') { this.value = 'Phone Number *'; }">
                            <input type="email" class="text" value="Email *" id="email" required onfocus="this.value = '';" onblur="    if (this.value == '') { this.value = 'Email *'; }">
                            <input type="text" class="text" value="City" id="city" onfocus="this.value = '';" onblur="    if (this.value == '') { this.value = 'City'; }">
                            <input type="text" class="text" value="Describe Yourself" id="msg" onfocus="this.value = '';" onblur="    if (this.value == '') { this.value = 'Describe Yourself'; }">


                            <input type="submit" value="SEND DETAILS" >
                        </form>
                    </div>
<div id="messagediv" title="Success">
<p style="padding:15px;"><i style="color: forestgreen;">Your Mail is sent Successfully</i></p></div>
<!-- <h1 style="font-size:16px;" id="messagediv"></h1> -->





                </div>
		</div>
		<!--//end-services-->

                   <div class="sep30"></div>
        <!--/start-footer-section-->
    <?php include('footer.php'); ?>



</body>
</html>
