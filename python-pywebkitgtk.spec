%define		module pywebkitgtk
Summary:	GTK WebKit bindings for Python
Summary(pl.UTF-8):	Wiązania biblioteki GTK WebKit dla Pythona
Name:		python-%{module}
Version:	1.1.8
Release:	7
License:	LGPL v2
Group:		Libraries/Python
Source0:	http://pywebkitgtk.googlecode.com/files/%{module}-%{version}.tar.gz
# Source0-md5:	158335385354ba38090c9324b37bf225
Patch0:		%{name}-codegen.patch
URL:		http://code.google.com/p/pywebkitgtk/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	geoclue-devel
BuildRequires:	gtk+2-devel >= 1:2.0
BuildRequires:	gtk-webkit-devel >= 1.1.10
BuildRequires:	libicu-devel
BuildRequires:	libtool
BuildRequires:	libxslt-devel
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.5.0
BuildRequires:	python-pygtk-devel >= 2:2.0
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_comp  $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/webkit/webkit.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitedir}/webkit
%attr(755,root,root) %{py_sitedir}/webkit/webkit.so
%{py_sitedir}/webkit/*.py[co]
%dir %{_datadir}/pywebkitgtk

%files devel
%defattr(644,root,root,755)
%dir %{_datadir}/pywebkitgtk/defs
%{_datadir}/pywebkitgtk/defs/webkit*.defs
%{_pkgconfigdir}/pywebkitgtk-1.0.pc
