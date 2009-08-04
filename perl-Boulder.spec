%define upstream_name	 Boulder
%define upstream_version 1.30

%define _requires_exceptions perl(LabBase)

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	An API for hierarchical tag/value structures
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/Boulder/
Source0:	http://search.cpan.org/CPAN/modules/by-module/Boulder/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
An API for hierarchical tag/value structures.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{perl_vendorlib}/%{upstream_name}
%{perl_vendorlib}/%{upstream_name}.pod
%{perl_vendorlib}/Stone.pm
%{perl_vendorlib}/Stone
%{_mandir}/man3/*
