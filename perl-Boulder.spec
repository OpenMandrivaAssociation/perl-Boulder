%define module	Boulder

Name:		perl-%{module}
Version:	1.30
Release:	%mkrel 3
License:	GPL or Artistic
Group:		Development/Perl
Summary:	An API for hierarchical tag/value structures
URL:		http://search.cpan.org/dist/Boulder/
Source:		http://search.cpan.org/CPAN/modules/by-module/%{module}/%{module}-%{version}.tar.bz2
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
An API for hierarchical tag/value structures.

%prep
%setup -q -n %{module}-%{version}

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
%{perl_vendorlib}/%{module}
%{perl_vendorlib}/%{module}.pod
%{perl_vendorlib}/Stone.pm
%{perl_vendorlib}/Stone
%{_mandir}/man3/*
