%define modname	Boulder

Name:		perl-%{modname}
Version:	1.30
Release:	%mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Boulder - An API for hierarchical tag/value structures
Source:		http://search.cpan.org/CPAN/modules/by-module/%{modname}/%{modname}-%{version}.tar.bz2
URL:		http://search.cpan.org/dist/Boulder/
BuildRequires:	perl
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
Boulder - An API for hierarchical tag/value structures

%prep
%setup -q -n %{modname}-%{version}

%build
%{__perl} Makefile.PL
%make

%install
rm -Rf %{buildroot}
%make DESTDIR=%{buildroot} pure_vendor_install \
INSTALLSITELIB=%perl_vendorlib \
INSTALLSITEMAN1DIR=%{_mandir}/man1 \
INSTALLSITEMAN3DIR=%{_mandir}/man3
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'


%clean
rm -Rf %{buildroot}

%files
%defattr(-,root,root)
%dir %{perl_vendorlib}/%{modname}
%{perl_vendorlib}/%{modname}
%{perl_vendorlib}/%{modname}.pod
%exclude %{perl_vendorlib}/%{modname}/Labbase.pm
%{perl_vendorarch}/*/%{modname}
%{perl_vendorlib}/Stone.pm
%{perl_vendorlib}/Stone

%{_mandir}/man?/*
#%{_bindir}/*



