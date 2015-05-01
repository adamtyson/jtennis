#!/usr/bin/perl
use strict;
use warnings;
use CGI;
die unless $ENV{HTTP_HOST};
my $failed=0;
(my $cwd=$0)=~s/^(.*)\\.*?$/$1/;
$cwd=~s#\\#/#g;
my $dr_unsafe = $ENV{PATH_TRANSLATED};
$dr_unsafe=~s#(public_html|web.content).*#$1#;
(my $dr_safe = $dr_unsafe ) =~s/\\/\\\\/g;
(my $dr = $dr_unsafe)=~s#\\#/#g;
open(STDERR, ">/dev/null");

my $cgi=new CGI;
(my $request_path=$ENV{SCRIPT_NAME})=~s#[^/]+$##;

if ($request_path eq '//' ) {  # installing to root directory
    $request_path = '/';
}

sub mkpassword {
	my @good_chars=('a' .. 'z', 'A' .. 'Z', 0 .. 9, '#', '^', '!', '(',
		')', '-', '=', '_', '+', '/');
	return join("", map {$good_chars[int rand @good_chars]} (0 .. 7));
}
use POSIX;
(my $sslname=(POSIX::uname())[1])=~s/\..*//;
$sslname.=".secure-secure.co.uk";
(my $un=$ENV{PATH_TRANSLATED}) =~s/(?:.*\\home|D:\\Sites)\\([^\\]+)\\.*/$1/;
my %config=(
	cwd=>$cwd,
	http_host=>$cgi->virtual_host,
	request_path=>$request_path,
	password=>mkpassword,
	user=>$un,
	dbuser=>scalar($cgi->param("dbuser")),
    dbtype=>scalar($cgi->param("dbtype"))||"mysql",
    dbhost=>scalar($cgi->param("dbhost")),
	dbpassword=>scalar($cgi->param("dbpassword")),
	docroot=>$dr,
	docroot_unsafe=>$dr_unsafe,
	docroot_safe=>$dr_safe,
	ssl_host=>$sslname,
);

if(-r "$cwd/_inone.tar.bz2") {
        system("/usr/bin/bunzip2",  "$cwd/_inone.tar.bz2");
}

if(-r "$cwd/_inone.tar") {
	require Archive::Tar;
	my $tar = Archive::Tar->new;

	$tar->read("$cwd/_inone.tar",0);
	$tar->extract();
	unlink "$cwd/_inone.tar";
}

#  Cannot run /usr/local/bin/grant_create_temporary_tables.sh here because user does not have read
#  access to /root/.my.cnf.  
#
# if(-r ".needs-temp-tables") {
#	system("/usr/local/bin/grant_create_temporary_tables.sh", $cgi->param("dbuser"));
#	unlink(".needs-temp-tables");
# }
#
#  This functionality is done in extend:/home/heart/hostcp/public_html/install.cgi


sub recurse_fix {
	my $dir=shift;
	opendir DIR, $dir or die($dir);
	my @ditems=readdir DIR;
	closedir DIR;
	for my $update_file (grep {m/\.install-template$/} @ditems) {
		
		(my $output_file=$update_file)=~s/\.install-template$//;
		unless(open IFILE, "<", "$dir/$update_file") {
			$failed=1;
			last;
		}
		my $mode=(stat IFILE)[2];
		unless(open OFILE, ">", "$dir/$output_file") {
			$failed=1;
			last;
		}
		my $line;
		while((!$failed) and $line=<IFILE>) {
			$line=~s/\[\* (\w+) \*\]/$config{$1}/g;
			print OFILE $line;
		}
		close OFILE;
		close IFILE;
		unlink "$dir/$update_file";
		chmod $mode, "$dir/$output_file";
	}
	for(@ditems) {
		next if /^\.\.?$/;
		if(-d "$dir/$_") {
			recurse_fix("$dir/$_");
		}
	}
}

recurse_fix($cwd);
my $success;
if($failed==1) {
	die;
}
$success=1;

# Set permissions to something safe:  e-mail 6/3/2008 - suggested by Jarrod
#     directories 711
# Change only the installation directory $cwd.  It is the only one the user 
# could have set incorrectly since it must be empty for installation and all other files are
# copied in by this program.

chmod 0711, "$cwd";
chmod 0700, "$cwd/_files";

if(-f "$cwd/importme.sql") {
	system("mysql -u $config{dbuser} -p$config{dbpassword} $config{dbuser} < $cwd/importme.sql");
	unlink("$cwd/importme.sql");
}
print $cgi->header("text/plain");
print "$config{password}\n";
close(STDOUT);
if(-x "$cwd/post-install.cgi") {
	system("$cwd/post-install.cgi");
	unlink("$cwd/post-install.cgi");
}

sub END {
	unlink $0 if $success;
}
