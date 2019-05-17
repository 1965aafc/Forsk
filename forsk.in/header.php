<!--

<script type="text/javascript">
// var j = jQuery.noConflict();
								$(function () {
								var url = window.location.href;
var lastPart = url.substr(url.lastIndexOf('/') + 1);
// alert(lastPart)
if (lastPart == "what-to-expect.php" || lastPart == "students-projects.php" ||  lastPart == "students-feedback.php" ||  lastPart == "industry-visit.php" ||  lastPart == "faq.php" ||  lastPart == "learn-from-anywhere.php" ) {
   $("#Students").addClass("btactive");
}
else if (lastPart == "computer-science-fundamentals.php" || lastPart == "mobile-app-development.php" ||  lastPart == "web-development.php" ||  lastPart == "industrial-c-programming.php" ||  lastPart == "iot.php"  ) {
   $("#Curriculum").addClass("btactive");
}
else if (lastPart == "forsk-labs-improve-practical-teaching.php" || lastPart == "forsk-labs-enhance-placement-readiness.php" ){
   $("#Universities").addClass("btactive");
}
else if (lastPart == "recruiting.php" ) {
   $("#Employer").addClass("btactive");
}
else if (lastPart == "ambassador-program.php") {
   $("#Champs").addClass("btactive");
}
else if (lastPart == "mission.php" || lastPart == "our-story.php" ||  lastPart == "team-and-mentors.php" ||  lastPart == "advisory-board.php" ||  lastPart == "career.php") {
   $("#Company").addClass("btactive");
}
 });
		</script> -->


<!--<div class="col-md-2 col-xs-4 col-sm-2">
                        <div class=" logo>
                            <a href="index.php"><img src="images/logo.png" alt="" /></a>
                        </div>
                    </div>
                    <div class="col-md-10 col-xs-8 col-sm-10">
                        <div class="menu-sec">
                            <div class="h_menu4">-->

							<!--menu-->
							 <nav class="navbar navbar-default">
  <div class="container">
  <div class="col-md-12 col-xs-12 col-sm-12">
    <!-- Brand and toggle get grouped for better mobile display -->
    <div class="navbar-header">
      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="index.php"><img src="images/Forsk_logo_bw.png" alt="" width="100px" /></a>

    </div>

    <!-- Collect the nav links, forms, and other content for toggling -->
    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
      <ul class="nav navbar-nav">

        <!-- <li class="dropdown">
          <a id="Students" href="what-to-expect.php" class="dropdown-toggle">Students <span class="caret"></span></a>
          <ul class="dropdown-menu" role="menu">
           <li><strong>Start Up University</strong></li>
           <li><a href="what-to-expect.php">What to Expect</a></li>
           <li><a href="students-projects.php">Student Project</a></li>
           <li><a href="students-feedback.php">Student Feedback</a></li>
           <li><a href="industry-visit.php">Industry Visit</a></li>
           <li><a href="faq.php">FAQs</a></li>
           <li><strong>Forsk Online Academy</strong></li>
           <li><a href="learn-from-anywhere.php">Learn From Anywhere</a></li>
          </ul>
        </li> -->

		<!-- <li class="dropdown">
		<a  id="Curriculum" class="dropdown-toggle" href="computer-science-fundamentals.php">Courses <span class="caret"></span></a>
         <ul class="dropdown-menu" role="menu">
         <li><a href="computer-science-fundamentals.php">Bigner's IoT Lab</a></li>
         <li><a href="mobile-app-development.php">Mobile App Development</a></li>
         <li><a href="web-development.php">Web Development</a></li>
         <li><a href="industrial-c-programming.php">Industrial C Programming</a></li>
         <li><a href="iot.php">IoT (Internet of Things)</a></li>
         <li><a id="Champs" href="industrial-c-programming.php">Test</a></li>

         <li><a id="Champs" href="blog/index.php">Blog</a></li>

         </ul></li> -->

		 <!-- <li class="dropdown">
		 <a id="Universities" class="dropdown-toggle"  href="forsk-labs-improve-practical-teaching.php">Forsk For Universities <span class="caret"></span></a>
         <ul class="dropdown-menu" role="menu">
         <li><a href="forsk-labs-improve-practical-teaching.php">Forsk Labs - Improve Practical Teaching</a></li>
         <li><a href="forsk-labs-enhance-placement-readiness.php">Forsk Labs - Enhance Placement Readiness</a></li>
         </ul>
         </li> -->
         <!-- <li><a id="Champs" href="ambassador-program.php">Forsk Champs</a></li> -->

         <li class="dropdown">
		 <a id="Company" class="dropdown-toggle" >Company <span class="caret"></span></a>
         <ul class="dropdown-menu" role="menu">
         <li><a href="about.php">About us</a></li>
         <li><a href="leadership.php">Leadership</a></li>
         <li><a href="advisory-board.php">Advisory Board</a></li>
         <li><a href="career.php">Career</a></li>
         <li><a href="contact.php">Contact us</a></li>
         </ul>
         </li>
		 <li><a id="Champs" href="https://medium.com/forsk-labs" target="_blank">Blog</a></li>

		
      </ul>

    </div>
    </div><!-- /.navbar-collapse -->
  </div><!-- /.container-fluid -->
</nav>

							<!--menu end-->


                                <!-- start h_menu4 -->
                                <!--<a class="toggleMenu" href="#">Menu</a>
                                <ul class="nav">
                                    <li><a  id="Students" href="what-to-expect.php">Students</a>
                                        <ul>
                                            <li><strong>Start Up University</strong></li>
                                            <li><a href="what-to-expect.php">What to Expect</a></li>
                                            <li><a href="students-projects.php">Student Project</a></li>
                                            <li><a href="students-feedback.php">Student Feedback</a></li>
                                            <li><a href="industry-visit.php">Industry Visit</a></li>
                                            <li><a href="faq.php">FAQs</a></li>
                                            <li><strong>Forsk Online Academy</strong></li>
                                            <li><a href="learn-from-anywhere.php">Learn From Anywhere</a></li>
                                        </ul>
                                    </li>
                                    <li><a  id="Curriculum" href="computer-science-fundamentals.php">Curriculum</a>
                                        <ul>
                                            <li><a href="computer-science-fundamentals.php">Computer Science Fundamentals</a></li>
                                            <li><a href="mobile-app-development.php">Mobile App Development</a></li>
                                            <li><a href="web-development.php">Web Development</a></li>
                                            <li><a href="industrial-c-programming.php">Industrial C Programming</a></li>
                                            <li><a href="iot.php">IoT (Internet of Things)</a></li>
                                        </ul></li>
                                    <li><a  id="Universities" href="forsk-labs-improve-practical-teaching.php">Forsk For Universities</a>
                                        <ul>
                                            <li><a href="forsk-labs-improve-practical-teaching.php">Forsk Labs - Improve Practical Teaching</a></li>
                                            <li><a href="forsk-labs-enhance-placement-readiness.php">Forsk Labs - Enhance Placement Readiness</a></li>
                                        </ul>
                                    </li>
                                    <li><a  id="Employer" href="recruiting.php">Employer</a></li>
                                    <li><a  id="Champs" href="ambassador-program.php">Forsk Champs</a></li>
                                    <li><a  id="Company" href="mission.php">Company</a>
                                        <ul>
                                            <li><a href="mission.php">Mission</a></li>
                                            <li><a href="our-story.php">Our Story</a></li>
                                            <li><a href="team-and-mentors.php">Team and Mentors</a></li>
                                            <li><a href="advisory-board.php">Advisory Board</a></li>
                                            <li><a href="career.php">Career</a></li>
                                        </ul>
                                    </li>
                                </ul>-->


                            <!-- end h_menu4 -->
