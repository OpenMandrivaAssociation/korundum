Summary:	KDE bindings for Ruby
Name:		korundum
Version:	4.10.5
Release:	1
Epoch:		1
License:	GPLv2 LGPLv2
Group:		Development/KDE and Qt
Url:		http://www.kde.org
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	ruby-qt4-devel >= 1:%{version}
BuildRequires:	smokekde-devel >= 1:%{version}
BuildRequires:	pkgconfig(shared-desktop-ontologies)
BuildRequires:	pkgconfig(akonadi)
Requires:	ruby-qt4 >= 1:%{version}
Obsoletes:	ruby-kde4 < 1:4.6.90
Provides:	ruby-kde4 = %{EVRD}
Provides:	kderuby = %{EVRD}

%description
A kde4 bindings for Ruby language.

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
%{ruby_sitearchdir}/kate.so
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

