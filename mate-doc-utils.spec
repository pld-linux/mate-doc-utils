Summary:	MATE Desktop doc utils
Name:		mate-doc-utils
Version:	1.6.1
Release:	1
License:	GPL v2+ and LGPL v2+
Group:		Development/Tools
Source0:	http://pub.mate-desktop.org/releases/1.6/%{name}-%{version}.tar.xz
# Source0-md5:	373060e1ee08a5904a7ebe43accc487b
URL:		http://wiki.mate-desktop.org/mate-doc-utils
BuildRequires:	docbook-dtd44-xml
BuildRequires:	gnome-doc-utils
BuildRequires:	intltool
BuildRequires:	libxml2-devel >= 1:2.6.12
BuildRequires:	libxslt-devel
BuildRequires:	mate-common
BuildRequires:	rarian-devel
BuildRequires:	rpmbuild(find_lang) >= 1.36
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	automake
#Requires:	docbook-dtds
Requires:	gnome-doc-utils
Requires:	mate-common
Requires:	pkgconfig
#Requires:	xml-common
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mate-doc-utils is a collection of documentation utilities for the Mate
project. Notably, it contains utilities for building documentation and
all auxiliary files in your source tree, and it contains the DocBook
XSLT style sheets that were once distributed with Yelp.

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

# Remove unnecessary python sitepackages provided by gnome-doc-utils
rm -rf $RPM_BUILD_ROOT%{py_sitescriptdir}/*
rm -rf $RPM_BUILD_ROOT%{py_sitescriptdir}/xml2po/
rm -rf $RPM_BUILD_ROOT%{_mandir}/man1/*
rm -rf $RPM_BUILD_ROOT%{_datadir}/xml/mallard
rm -rf $RPM_BUILD_ROOT%{_bindir}/xml2po
rm -rf $RPM_BUILD_ROOT%{_npkgconfigdir}/xml2po.pc
# Debian script not needed
rm -rf $RPM_BUILD_ROOT%{_datadir}/mate-doc-utils/mate-debian.sh

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README NEWS COPYING COPYING.GPL COPYING.LGPL
%attr(755,root,root) %{_bindir}/mate-doc-prepare
%attr(755,root,root) %{_bindir}/mate-doc-tool
%{_aclocaldir}/mate-doc-utils.m4
%{_datadir}/mate-doc-utils
%{_datadir}/xml/mate
%{_npkgconfigdir}/mate-doc-utils.pc
