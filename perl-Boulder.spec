%define upstream_name	 Boulder
%define upstream_version 1.30

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(LabBase\\)'
%else
%define _requires_exceptions perl(LabBase)
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	An API for hierarchical tag/value structures
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/Boulder/
Source0:	http://search.cpan.org/CPAN/modules/by-module/Boulder/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
An API for hierarchical tag/value structures.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%files
%{perl_vendorlib}/%{upstream_name}
%{perl_vendorlib}/%{upstream_name}.pod
%{perl_vendorlib}/Stone.pm
%{perl_vendorlib}/Stone
%{_mandir}/man3/*

%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.300.0-2mdv2011.0
+ Revision: 680659
- mass rebuild

* Tue Aug 04 2009 Jérôme Quelin <jquelin@mandriva.org> 1.300.0-1mdv2011.0
+ Revision: 408915
- rebuild using %%perl_convert_version

* Sun Jan 25 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.30-6mdv2009.1
+ Revision: 333473
- fix dependencies

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.30-5mdv2009.0
+ Revision: 255474
- rebuild

* Sat Dec 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.30-3mdv2008.1
+ Revision: 136899
- spec cleanup

* Sat Dec 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.30-2mdv2008.1
+ Revision: 136889
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Oct 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.30-1mdv2007.0
+ Revision: 73340
- import perl-Boulder-1.30-1mdv2007.0

* Fri Jul 07 2006 Buchan Milne <bgmilne@obsidian.co.za> 1.30-1mdv2007.0
- first Mandriva package

