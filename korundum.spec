Name: korundum
Summary: KDE bindings for Ruby
Version: 4.8.97
Release: 1
Epoch: 1
Group: Development/KDE and Qt
License: GPLv2 LGPLv2
URL: http://www.kde.org
Source: ftp://ftp.kde.org/pub/kde/unstable/%version/src/%name-%version.tar.xz
BuildRequires: ruby-qt4-devel >= 1:%version
BuildRequires: smokekde-devel >= 1:%version
BuildRequires: pkgconfig(shared-desktop-ontologies)
BuildRequires: akonadi-devel

Requires: ruby-qt4 >= 1:%version

Obsoletes: ruby-kde4 < 1:4.6.90

Provides: ruby-kde4 = %epoch:%version-%release
Provides: kderuby = %{epoch}:%{version}-%{release}

%description
A kde4 bindings for Ruby language.

%files
%_kde_bindir/krubyapplication
%_kde_libdir/kde4/krubypluginfactory.so
%ruby_sitearchdir/akonadi.so
%ruby_sitearchdir/khtml.so
%ruby_sitearchdir/kio.so
%ruby_sitearchdir/korundum4.so
%ruby_sitearchdir/ktexteditor.so
%ruby_sitearchdir/solid.so
%ruby_sitearchdir/soprano.so
%ruby_sitearchdir/nepomuk.so
%ruby_sitearchdir/plasma_applet.so
%ruby_sitearchdir/okular.so
%ruby_sitearchdir/kate.so
%ruby_sitelibdir/KDE
%ruby_sitelibdir/akonadi
%ruby_sitelibdir/khtml
%ruby_sitelibdir/ktexteditor
%ruby_sitelibdir/soprano
%ruby_sitelibdir/nepomuk
%ruby_sitelibdir/solid
%ruby_sitelibdir/okular
%ruby_sitelibdir/kio
%_kde_appsdir/plasma_applet_ruby_clock
%_kde_appsdir/plasma_ruby_digital_clock
%_kde_services/*.desktop

#------------------------------------------------------------------------------

%package devel
Summary: Tools for ruby-kde4
Group: Development/KDE and Qt
Requires: ruby-qt4-devel >= %epoch:%version
Requires: %name  = %epoch:%version-%release

Obsoletes: ruby-kde4-devel < 1:4.6.90

Provides: ruby-kde4-devel = %epoch:%version-%release

%description devel
ruby-kde4 devel files.

%files devel
%_kde_bindir/rbkconfig_compiler4
%_kde_datadir/applications/kde4/dbpedia_references.desktop
%_kde_appsdir/dbpedia_references

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4  -DKDE4_ENABLE_FINAL=ON
%make

%install
rm -fr %buildroot
%makeinstall_std -C build


