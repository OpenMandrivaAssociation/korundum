Summary:	KDE4 bindings for Ruby
Name:		korundum
Version:	4.14.3
Release:	3
Epoch:		1
License:	GPLv2+ and LGPLv2.1+
Group:		Development/KDE and Qt
Url:		https://www.kde.org
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	ruby-qt4-devel >= 1:%{version}
BuildRequires:	smokekde-devel >= 1:%{version}
BuildRequires:	pkgconfig(akonadi)
BuildRequires:	pkgconfig(shared-desktop-ontologies)
Requires:	ruby-qt4 >= 1:%{version}
Obsoletes:	ruby-kde4 < 1:4.6.90
Provides:	ruby-kde4 = %{EVRD}
Provides:	kderuby = %{EVRD}

%description
A KDE4 bindings for Ruby language.

%files
%{_kde_bindir}/krubyapplication
%{_kde_libdir}/kde4/krubypluginfactory.so
%{ruby_sitearchdir}/akonadi.so
%{ruby_sitearchdir}/khtml.so
%{ruby_sitearchdir}/kio.so
%{ruby_sitearchdir}/korundum4.so
%{ruby_sitearchdir}/ktexteditor.so
%{ruby_sitearchdir}/solid.so
%{ruby_sitearchdir}/soprano.so
%{ruby_sitearchdir}/nepomuk.so
%{ruby_sitearchdir}/plasma_applet.so
%{ruby_sitearchdir}/okular.so
%{ruby_sitelibdir}/KDE
%{ruby_sitelibdir}/akonadi
%{ruby_sitelibdir}/khtml
%{ruby_sitelibdir}/ktexteditor
%{ruby_sitelibdir}/soprano
%{ruby_sitelibdir}/nepomuk
%{ruby_sitelibdir}/solid
%{ruby_sitelibdir}/okular
%{ruby_sitelibdir}/kio
%{_kde_appsdir}/plasma_applet_ruby_clock
%{_kde_appsdir}/plasma_ruby_digital_clock
%{_kde_services}/*.desktop

#------------------------------------------------------------------------------

%package devel
Summary:	Tools for ruby-kde4
Group:		Development/KDE and Qt
Requires:	ruby-qt4-devel >= %{epoch}:%{version}
Requires:	%{name} = %{EVRD}
Obsoletes:	ruby-kde4-devel < 1:4.6.90
Provides:	ruby-kde4-devel = %{EVRD}

%description devel
ruby-kde4 devel files.

%files devel
%{_kde_bindir}/rbkconfig_compiler4
%{_kde_datadir}/applications/kde4/dbpedia_references.desktop
%{_kde_appsdir}/dbpedia_references

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Tue Nov 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.14.3-1
- New version 4.14.3

* Wed Oct 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.14.2-1
- New version 4.14.2

* Mon Sep 29 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.14.1-1
- New version 4.14.1

* Tue Jul 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.13.3-1
- New version 4.13.3

* Wed Jun 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.13.2-1
- New version 4.13.2

* Wed Apr 02 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.4-1
- New version 4.12.4

* Tue Mar 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.3-1
- New version 4.12.3

* Tue Feb 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.2-1
- New version 4.12.2

* Tue Jan 14 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.1-1
- New version 4.12.1

* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.4-1
- New version 4.11.4

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.3-1
- New version 4.11.3

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.2-1
- New version 4.11.2

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.0-1
- New version 4.11.0

* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.5-1
- New version 4.10.5
- Drop no longer needed ruby1.9 patch

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.4-1
- New version 4.10.4

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.1-1
- New version 4.10.1

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- New version 4.10.0

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.1-1
- New version 4.9.1

* Tue Aug 14 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.0-1
- New version 4.9.0
- Add patch to fix build with Ruby 1.9

* Sun Jul 22 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.97-1
- New version 4.8.97

* Mon Jul 09 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.95-1
- New version 4.8.95

* Fri Jun 08 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.4-69.1mib2010.2
- New version 4.8.4
- MIB (Mandriva International Backports)

* Fri May 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.3-69.1mib2010.2
- New version 4.8.3
- MIB (Mandriva International Backports)

* Wed Apr 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.2-69.1mib2010.2
- New version 4.8.2
- MIB (Mandriva International Backports)

* Wed Mar 07 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.1-69.1mib2010.2
- New version 4.8.1
- MIB (Mandriva International Backports)

* Mon Feb 20 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.0-69.2mib2010.2
+ Revision: 744298
- Backport to 2010.2 for MIB users
- MIB (Mandriva International Backports)

* Thu Feb 16 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1:4.8.0-2
+ Revision: 775139
- add akonadi module..
- mass rebuild of ruby packages against ruby 1.9.1

* Thu Jan 19 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.8.0-1
+ Revision: 762479
- New upstream tarball

* Fri Jan 06 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.97-1
+ Revision: 758066
- New upstream tarball

* Tue Jan 03 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.95-1
+ Revision: 750455
- Fix file list
- Fix buildrequires
- Import korundum ( from mageia )
- Create structure

