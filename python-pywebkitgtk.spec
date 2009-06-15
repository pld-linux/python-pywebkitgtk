%define		module pywebkitgtk
Summary:	GTK WebKit bindings for Python
Summary(pl.UTF-8):	Wiązania biblioteki GTK WebKit dla Pythona
Name:		python-%{module}
Version:	1.1.5
Release:	1
License:	LGPL v2
Group:		Libraries/Python
Source0:	http://pywebkitgtk.googlecode.com/files/%{module}-%{version}.tar.gz
# Source0-md5:	65d435ff62ac0f8a14b2850233b4d1cd
Patch0:		%{name}-codegen.patch
URL:		http://code.google.com/p/pywebkitgtk/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 1:2.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.5.0
BuildRequires:	python-pygtk-devel >= 2:2.0
BuildRequires:	gtk-webkit-devel >= 1.1.5
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define pydefsdir %(pkg-config --variable=defsdir pygtk-2.0)

%description
GTK WebKit bindings for Python.

%description -l pl.UTF-8
Wiązania biblioteki GTK WebKit dla Pythona.

%package devel
Summary:	Development files for GTK Webkit bindings for Python
Summary(pl.UTF-8):	Plik programistyczny wiązań biblioteki GTK WebKit dla Pythona
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python-pygtk-devel >= 2:2.0

%description devel
Development files for GTK Webkit bindings for Python.

%description devel -l pl.UTF-8
Plik programistyczny wiązań biblioteki GTK WebKit dla Pythona.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1

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
%attr(755,root,root) %{py_sitedir}/gtk-2.0/webkit.so
%dir %{_datadir}/pywebkitgtk

%files devel
%defattr(644,root,root,755)
%dir %{_datadir}/pywebkitgtk/defs
%{_datadir}/pywebkitgtk/defs/webkit*.defs
