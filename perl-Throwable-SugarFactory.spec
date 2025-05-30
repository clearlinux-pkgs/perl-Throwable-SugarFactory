#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-Throwable-SugarFactory
Version  : 0.213360
Release  : 5
URL      : https://cpan.metacpan.org/authors/id/M/MI/MITHALDU/Throwable-SugarFactory-0.213360.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MI/MITHALDU/Throwable-SugarFactory-0.213360.tar.gz
Summary  : 'build a library of syntax-sugared Throwable-based exceptions'
Group    : Development/Tools
License  : CC0-1.0
Requires: perl-Throwable-SugarFactory-license = %{version}-%{release}
Requires: perl-Throwable-SugarFactory-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Class::Inspector)
BuildRequires : perl(Class::Method::Modifiers)
BuildRequires : perl(Import::Into)
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Moo)
BuildRequires : perl(Moo::Role)
BuildRequires : perl(Package::Variant)
BuildRequires : perl(Role::Tiny)
BuildRequires : perl(String::CamelCase)
BuildRequires : perl(Sub::Quote)
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(Test::InDistDir)
BuildRequires : perl(Throwable)
BuildRequires : perl(Throwable::Error)
BuildRequires : perl(Try::Tiny)
BuildRequires : perl(strictures)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
Throwable::SugarFactory - build a library of syntax-sugared
Throwable-based exceptions

%package dev
Summary: dev components for the perl-Throwable-SugarFactory package.
Group: Development
Provides: perl-Throwable-SugarFactory-devel = %{version}-%{release}
Requires: perl-Throwable-SugarFactory = %{version}-%{release}

%description dev
dev components for the perl-Throwable-SugarFactory package.


%package license
Summary: license components for the perl-Throwable-SugarFactory package.
Group: Default

%description license
license components for the perl-Throwable-SugarFactory package.


%package perl
Summary: perl components for the perl-Throwable-SugarFactory package.
Group: Default
Requires: perl-Throwable-SugarFactory = %{version}-%{release}

%description perl
perl components for the perl-Throwable-SugarFactory package.


%prep
%setup -q -n Throwable-SugarFactory-0.213360
cd %{_builddir}/Throwable-SugarFactory-0.213360

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Throwable-SugarFactory
cp %{_builddir}/Throwable-SugarFactory-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Throwable-SugarFactory/ff5cc3fd01ae22363b19c755395d4af56117274e || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Constructor::Sugar.3
/usr/share/man/man3/Constructor::SugarLibrary.3
/usr/share/man/man3/MooX::BuildClass.3
/usr/share/man/man3/MooX::BuildClass::Utils.3
/usr/share/man/man3/MooX::BuildRole.3
/usr/share/man/man3/MooX::SugarFactory.3
/usr/share/man/man3/Throwable::SugarFactory.3
/usr/share/man/man3/Throwable::SugarFactory::Hashable.3
/usr/share/man/man3/Throwable::SugarFactory::Utils.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Throwable-SugarFactory/ff5cc3fd01ae22363b19c755395d4af56117274e

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
