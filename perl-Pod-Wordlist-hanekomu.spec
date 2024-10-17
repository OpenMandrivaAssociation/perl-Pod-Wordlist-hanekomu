%define upstream_name    Pod-Wordlist-hanekomu
%define upstream_version 1.132680

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Add words for spell checking POD
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Pod/Pod-Wordlist-hanekomu-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Pod::Wordlist)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Spelling)
BuildArch:	noarch

%description
This module, when loaded, adds stopwords for POD spell checking, that is,
words that should be ignored by the spell check.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
#make test

%install
%makeinstall_std

%files
%doc META.yml README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.110.90-2mdv2011.0
+ Revision: 657829
- rebuild for updated spec-helper

* Wed Feb 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.110.90-1
+ Revision: 635212
- update to new version 1.110090

* Thu Nov 11 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.102.640-1mdv2011.0
+ Revision: 596007
- update to new version 1.102640

* Tue Aug 24 2010 Jérôme Quelin <jquelin@mandriva.org> 1.102.340-1mdv2011.0
+ Revision: 572706
- update to 1.102340

* Sun Aug 15 2010 Jérôme Quelin <jquelin@mandriva.org> 1.102.250-1mdv2011.0
+ Revision: 569955
- update to 1.102250

* Mon Mar 29 2010 Jérôme Quelin <jquelin@mandriva.org> 1.100.860-1mdv2011.0
+ Revision: 528762
- update to 1.100860

* Sat Mar 27 2010 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-1mdv2010.1
+ Revision: 527997
- import perl-Pod-Wordlist-hanekomu


* Sat Mar 27 2010 cpan2dist 0.02-1mdv
- initial mdv release, generated with cpan2dist


