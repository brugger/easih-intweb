#!/usr/bin/perl -w

use strict;
use lib "/software/installed/easih-toolbox/modules/";
use EASIH;
use EASIH::Sample;
use EASIH::Illumina::Sample_sheet;


my $sample_sheet = shift;

my $error_message = "";

validate_sample_sheet($sample_sheet);


if($error_message)				 
{			 		    
    print "$error_message\n";
}
else
{
    print "okay!\n";
}    



################################################################################
sub validate_sample_sheet {
  my ( $sample_sheet) = @_;
  my ($res, $errors, $warnings) = EASIH::Illumina::Sample_sheet::readin( $sample_sheet );


  if($warnings) 
  {
      print "$warnings\n";
  }


  if($errors) 
  {
      $error_message .= $errors;
      return;
  }


  $errors = EASIH::Illumina::Sample_sheet::validate($res);

  $error_message .= $errors, if($errors);

  return;  
}
