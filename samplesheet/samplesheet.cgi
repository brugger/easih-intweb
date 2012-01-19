#!/usr/bin/perl -w

use CGI;
use strict;
use lib "/software/installed/easih-toolbox/modules/";
use EASIH;
use EASIH::Sample;
use EASIH::Illumina::Sample_sheet;

my $q = new CGI;
my $fhandle = $q->param('samplesheet');

print "Content-type:text/html\n\n";
print "<html><title>EASIH - Sample Sheet Validator</title><body>";
print "<center><a href=\"http://www.easih.ac.uk/index.php\"><img src=\"../easih.gif\" alt=\"EASIH\" /></a></center><h1>Sample Sheet Validator</h1><br />"; 

my $pid = $$;
my $filename = "/tmp/${pid}_sample_sheet.csv";


open(SS, "> $filename") or die $!; 
while(<$fhandle>) 
{
    print SS "$_"; 
}
close(SS);


my $error_message;
validate_sample_sheet($filename);


if($error_message)				 
{			 		    
    print "<h2><font color=red>$error_message</font></h2>";
}
else
{
    print "<br /><br /><br /><h1><font color=green>okay!</font></h1>";
}    

print "</html></body>";

system("rm -f $filename");


################################################################################
sub validate_sample_sheet {
  my ( $sample_sheet) = @_;
  my ($res, $errors, $warnings) = EASIH::Illumina::Sample_sheet::readin( $sample_sheet );


 if($warnings) 
  {
      $warnings =~ s/\n/\<br\/>/g;
      print "<h2><font color=amber>$warnings</font></h2>";
  }


  if($errors) 
  {
      $error_message .= $errors;
      return;
  }
  

  $errors = EASIH::Illumina::Sample_sheet::validate($res);

  $errors =~ s/\n/\<br\/>/g;

  $error_message .= $errors, if($errors);

  return;
}
