Name:           perl-Geo-MapInfo-MIF-Writer-Region
Version:        0.05
Release:        1%{?dist}
Summary:        Perl extension for writing MapInfo Interchange Format (MIF) Region files
License:        BSD
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Geo-MapInfo-MIF-Writer-Region/
Source0:        http://www.cpan.org/modules/by-module/Geo/Geo-MapInfo-MIF-Writer-Region-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(DateTime)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Package::New)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Test::Simple) >= 0.44
BuildRequires:  perl(Text::CSV_XS)
Requires:       perl(Package::New)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Perl extension for writing MapInfo Interchange Format (MIF) Region files.

%prep
%setup -q -n Geo-MapInfo-MIF-Writer-Region-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes LICENSE perl-Geo-MapInfo-MIF-Writer-Region.spec README Todo
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Jan 01 2012 Michael R. Davis (mdavis@stopllc.com) 0.05-1
- Updated for version 0.05
* Mon May 23 2011 Michael R. Davis (mdavis@stopllc.com) 0.01-1
- Specfile autogenerated by cpanspec 1.78.
