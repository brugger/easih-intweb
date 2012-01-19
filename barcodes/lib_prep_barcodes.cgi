#!/usr/bin/perl -w

use CGI;
use strict;

my($project,$count,$start);

my $q = new CGI;
$project = $q->param('project');
$count = $q->param('count');
$start = $q->param('start');
print "Content-type:text/html\n\n";

print "<html><body>";
#print "<h1>Library Prep Barcodes</h1>";
print "<img src=lpb2.gif />";
print "<a href=http://www.easih.ac.uk><img src=easihbarcode.png alt=EASIH title=http://www.easih.ac.uk align=right /></a>";


unless($project and $count)
{
    print "<p> <b><font size=5 face=arial color=red>Need project and count! </font></b></p>";    
    die; 
}

$project = ucfirst($project);
unless($project =~ /[A-Z]\d{2}/)
{
    print "<p> <b><font size=5 face=arial color=red>Project name format invalid! Format: [A-Z] followed by 2 digits, <i> e.g.,</i> A32 </font></b></p>";
    die;
}

if($count =~ /[^\d]/)
{
    print "<p><b><font size=5 face=arial color=red> Count should be digit(s)!</font></b></p>";
    die;
}


$start= 1 unless $start;
$count++;
my $done = 0;
my @steps;
&read_data;

print "<hr>";
print "<b><font size=5 face=arial color=blue>Input:</font></b> <br />Project: $project, Count: $count, Start: $start";
print "<hr>";

print "<br /><b><font size=5 face=arial color=blue>Output:</font></b><br /><br />";

while ($done <= $count)  {
    $done++;    
    my $bc = $project . sprintf("%04d",$done+$start-1); 
    my $stepcount = 0;
    foreach (@steps){
	#print "$bc,$stepcount,$_";
	print "$bc,$stepcount,$_<br />";
	$stepcount++;
    }
}
sub read_data{
    while(<DATA>){
	push(@steps,$_);
    }
}

print "</html></body>";

__DATA__
RNase treatment
RNase + C Pre Frag
Pre-Frag
Post-Frag
AMPure Frag+C
Pre End Repair
Post End Repair Pre-Clean
AMPure ER+C
Pre-A+
Post-A+ Pre-Clean
AMPure A++C
Pre-Ligad
Post-Ligad Pre-Clean
AMPure Ligad+C
Pre-PCR
Post-PCR Pre-Clean
