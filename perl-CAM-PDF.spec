#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	CAM
%define		pnam	PDF
Summary:	CAM::PDF - PDF manipulation library
Name:		perl-CAM-PDF
Version:	1.06
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
#Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Source0:	http://search.cpan.org/CPAN/authors/id/C/CL/CLOTHO/%{pdir}-%{pnam}-%{version}.tgz
# Source0-md5:	4c538b7c8a01e9c3d2e109b8b54cd870

BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13

Requires:	perl(Text::PDF::File)  >= 0.18
Requires:	perl(Crypt::RC4)      >= 2.02
Requires:	perl(Digest::MD5)     >= 2.16
Requires:	perl(Getopt::Long)    >= 2.0
Requires:	perl(Pod::Usage)      >= 1.0
Requires:	perl(Test::More)      >= 0.01

BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
CAM::PDF - PDF manipulation library

This package reads and writes any document that conforms to the PDF
specification generously provided by Adobe at
http://partners.adobe.com/public/developer/pdf/index_reference.html
(link last checked Oct 2005).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/%{pdir}/*.pm
%dir %{perl_vendorlib}/%{pdir}/%{pnam}/
%{perl_vendorlib}/%{pdir}/%{pnam}/*.pm
%dir %{perl_vendorlib}/%{pdir}/%{pnam}/GS/
%{perl_vendorlib}/%{pdir}/%{pnam}/GS/*.pm
%dir %{perl_vendorlib}/%{pdir}/%{pnam}/Renderer/
%{perl_vendorlib}/%{pdir}/%{pnam}/Renderer/*.pm
%{_mandir}/man1/*
%{_mandir}/man3/*
