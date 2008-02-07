%define		module pywebkitgtk
Summary:	GTK WebKit bindings for python
Name:		python-%{module}
Version:	0.2.1
Release:	0.20080107.1
License:	LGPL v2
Group:		Libraries/Python
Source0:	%{module}-git.tar.bz2
# Source0-md5:	a53dd40d51a77aa4c942264dcac9d548
URL:		http://live.gnome.org/PyWebKitGtk
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	gtk+2-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.5.0
BuildRequires:	gtk-webkit-devel
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define pydefsdir %(pkg-config --variable=defsdir pygtk-2.0)

%description
GTK WebKit bindings for python.

%prep
%setup -q -n %{module}-git

%build
%{__libtoolize}
%{__autoheader}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/webkitgtk.so
%{pydefsdir}/webkitgtk.defs
