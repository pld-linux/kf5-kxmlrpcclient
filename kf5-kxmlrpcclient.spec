%define		kdeframever	5.85
%define		qtver		5.9.0
%define		kfname		kxmlrpcclient
#
Summary:	XML-RPC client library
Name:		kf5-%{kfname}
Version:	5.85.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/frameworks/%{kdeframever}/portingAids/%{kfname}-%{version}.tar.xz
# Source0-md5:	148e239b5fd08a66e655116a7399c22d
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Xml-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= %{version}
BuildRequires:	kf5-kio-devel >= %{version}
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	kf5-dirs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
XML-RPC client library.

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang libkxmlrpcclient5 --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f libkxmlrpcclient5.lang
%defattr(644,root,root,755)
%doc README.md
%ghost %{_libdir}/libKF5XmlRpcClient.so.5
%attr(755,root,root) %{_libdir}/libKF5XmlRpcClient.so.*.*
%{_datadir}/qlogging-categories5/kxmlrpcclient.categories
%{_datadir}/qlogging-categories5/kxmlrpcclient.renamecategories

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KXmlRpcClient
%{_includedir}/KF5/kxmlrpcclient_version.h
%{_libdir}/cmake/KF5XmlRpcClient
%{_libdir}/libKF5XmlRpcClient.so
%{qt5dir}/mkspecs/modules/qt_KXmlRpcClient.pri

