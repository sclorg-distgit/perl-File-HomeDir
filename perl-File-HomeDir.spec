%{?scl:%scl_package perl-File-HomeDir}

Name:           %{?scl_prefix}perl-File-HomeDir
Version:        1.00
Release:        13%{?dist}
Summary:        Find your home and other directories on any platform
Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/File-HomeDir/
Source0:        http://www.cpan.org/authors/id/A/AD/ADAMK/File-HomeDir-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(Cwd) >= 3.12
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MM_Unix)
BuildRequires:  %{?scl_prefix}perl(File::Path) >= 2.01
BuildRequires:  %{?scl_prefix}perl(File::Spec) >= 3.12
# POSIX not used on Linux
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(vars)
# Run-time:
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(File::Temp) >= 0.19
BuildRequires:  %{?scl_prefix}perl(File::Which) >= 0.05
# Mac::Files not used on Linux
# Mac::SystemDirectory not used on Linux
# Win32 not used on Linux
# Tests:
BuildRequires:  %{?scl_prefix}perl(File::Spec::Functions)
BuildRequires:  %{?scl_prefix}perl(Test::More) >= 0.47
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:       %{?scl_prefix}perl(Cwd) >= 3.12
Requires:       %{?scl_prefix}perl(Exporter)
Requires:       %{?scl_prefix}perl(File::Path) >= 2.01
Requires:       %{?scl_prefix}perl(File::Spec) >= 3.12
Requires:       %{?scl_prefix}perl(File::Temp) >= 0.19
Requires:       %{?scl_prefix}perl(File::Which) >= 0.05

%if 0%{?rhel} < 7
# RPM 4.8 style
%{?filter_setup:
%filter_from_requires /%{?scl_prefix}perl(Cwd)/d
%filter_from_requires /%{?scl_prefix}perl(File::Path)/d
%filter_from_requires /%{?scl_prefix}perl(File::Spec)/d
%filter_from_requires /%{?scl_prefix}perl(File::Temp)/d
%filter_from_requires /%{?scl_prefix}perl(File::Which)/d
%filter_from_requires /%{?scl_prefix}perl(Mac::/d
%filter_from_requires /%{?scl_prefix}perl(Win32/d
%?perl_default_filter
}
%else
# RPM 4.9 style
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude}|perl\\(Cwd\\)|perl\\(File::Path\\)|perl\\(File::Spec\\)|perl\\(File::Temp\\)|perl\\(File::Which\\)|perl\\(Mac::|perl\\(Win32
%endif

%description
File::HomeDir is a module for locating the directories that are "owned"
by a user (typically your user) and to solve the various issues that
arise trying to find them consistently across a wide variety of
platforms.

%prep
%setup -q -n File-HomeDir-%{version}

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=%{buildroot}%{?scl:'}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
chmod -R u+w %{buildroot}/*

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc Changes LICENSE README
%{perl_vendorlib}/File/
%{_mandir}/man3/*.3pm*

%changelog
* Tue Jul 19 2016 Petr Pisar <ppisar@redhat.com> - 1.00-13
- SCL

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.00-12
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.00-9
- Perl 5.22 rebuild

* Thu Jan 15 2015 Petr Pisar <ppisar@redhat.com> - 1.00-8
- Correct dependencies

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.00-7
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 1.00-4
- Perl 5.18 rebuild
- Specify all dependencies

* Thu Jan 31 2013 Petr Šabata <contyk@redhat.com> - 1.00-3
- Use the Module::Install provided by upstream (#906007)

* Mon Nov 26 2012 Petr Šabata <contyk@redhat.com> - 1.00-2
- Re-enable the test suite
- Unbundle inc::Module::Install
- Modernize the spec

* Mon Oct 22 2012 Tom Callaway <spot@fedoraproject.org> - 1.00-1
- update to 1.00

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Petr Pisar <ppisar@redhat.com> - 0.99-3
- Perl 5.16 re-rebuild of bootstrapped packages

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 0.99-2
- Perl 5.16 rebuild

* Tue Jan 31 2012 Tom Callaway <spot@fedoraproject.org> - 0.99-1
- Update to 0.99

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.98-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.98-2
- Perl mass rebuild

* Tue Jul 12 2011 Tom Callaway <spot@fedoraproject.org> - 0.98-1
- update to 0.98

* Fri Jun 24 2011 Marcela Maslanova <mmaslano@redhat.com> - 0.97-2
- fix filters for future rebuild
- add perl_bootstrap macro
- rebuild for perl 5.14.1

* Mon Feb 21 2011 Tom Callaway <spot@fedoraproject.org> - 0.97-1
- update to 0.97

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.93-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.93-2
- 661697 rebuild for fixing problems with vendorach/lib

* Wed Sep 22 2010 Petr Pisar <ppisar@redhat.com> - 0.93-1
- 0.93 bump
- Consolidate dependencies
- Remove unversioned Requires
- Update Summary and Description
- Remove unneded file permission fixes

* Sat May 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.86-4
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.86-3
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.86-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun  1 2009 Marcela Mašláňová <mmaslano@redhat.com> - 0.86-1
- update for Padre

* Fri Mar 13 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 0.84-1
- update to 0.84

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.82-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 16 2008 Marcela Mašláňová <mmaslano@redhat.com> - 0.82-1
- update to the latest version for Padre editor

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.67-3
- Rebuild for perl 5.10 (again)

* Fri Jan 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.67-2
- rebuild for new perl

* Wed Dec 19 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 0.67-1
- 0.67

* Fri Nov 30 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 0.66-1
- 0.66

* Wed May 30 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.65-1
- Update to 0.65.

* Sat Feb 10 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.64-1
- Update to 0.64.

* Thu Jan 11 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.63-1
- Update to 0.63.

* Thu Jan  4 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.62-1
- Update to 0.62.

* Thu Aug 03 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.58-1
- First build.
