Summary:	MATE Desktop documentation utilities
Summary(pl.UTF-8):	Narzędzia do generowania dokumentacji dla środowiska MATE Desktop
Name:		mate-doc-utils
Version:	1.6.2
Release:	2
License:	GPL v2+ (utilities), LGPL v2+ (XSLT files)
Group:		Development/Tools
Source0:	http://pub.mate-desktop.org/releases/1.6/%{name}-%{version}.tar.xz
# Source0-md5:	6bbbe07b54404a5bbe19e5d21e21aebe
URL:		http://wiki.mate-desktop.org/mate-doc-utils
BuildRequires:	docbook-dtd44-xml
BuildRequires:	gettext-devel
BuildRequires:	gnome-doc-utils
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libxml2-devel >= 1:2.6.12
BuildRequires:	libxslt-devel >= 1.1.8
BuildRequires:	mate-common
BuildRequires:	python >= 1:2.4
BuildRequires:	rarian-devel
BuildRequires:	rpmbuild(find_lang) >= 1.36
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
# for xml2po and mallard templates
Requires:	gnome-doc-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mate-doc-utils is a collection of documentation utilities for the MATE
project. Notably, it contains utilities for building documentation and
all auxiliary files in your source tree, and it contains the DocBook
XSLT style sheets that were once distributed with Yelp.

%description -l pl.UTF-8
mate-doc-utils to zbiór narzędzi związanych z dokumentacją dla
projektu MATE. W szczególności zawiera narzędzia do budowania
dokumentacji, wszystkie dodatkowe pliki potrzebne w drzewie źródeł
oraz szablony stylów XSLT, które były rozprowadzane wraz z Yelpem.

%prep
%setup -q

%build
%configure \
	--host=%{_host} \
	--build=%{_host} \
	--disable-scrollkeeper

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-omf --with-mate --all-name

# Remove xml2po utility and mallard templates provided by gnome-doc-utils
%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/xml2po
%{__rm} $RPM_BUILD_ROOT%{_bindir}/xml2po
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/xml2po.1*
%{__rm} $RPM_BUILD_ROOT%{_npkgconfigdir}/xml2po.pc
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/xml/mallard

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/mate-doc-prepare
%attr(755,root,root) %{_bindir}/mate-doc-tool
%{_datadir}/mate-doc-utils
%{_datadir}/xml/mate
%{_aclocaldir}/mate-doc-utils.m4
%{_npkgconfigdir}/mate-doc-utils.pc
