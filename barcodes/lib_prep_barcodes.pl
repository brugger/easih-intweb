#!/usr/bin/perl -w
use Getopt::Long;

my $project;
my $count;
my $start;

GetOptions ("project=s" => \$project, 
	    "count=i"   => \$count,
	    "start=i"   => \$start
    );


$start= 1 unless $start;

die "need project and count\n" unless ($project and $count);
die "project name format invalid\n" unless ($project =~ /[A-Z]\d{2}/);
die "count should be digit(s)\n" if ($count =~ /[^\d]/);
$count++;
my $done = 0;
my @steps;
&read_data;

while ($done <= $count)  {
    $done++;    
    my $bc = $project . sprintf("%04d",$done); 
    my $stepcount = 0;
    foreach (@steps){
	print "$bc,$stepcount,$_";
	$stepcount++;
    }
}
sub read_data{
    while(<DATA>){
	push(@steps,$_);
    }
}

__DATA__
RNase treatment
RNase + C, Pre Frag
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
