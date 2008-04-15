%define		module pywebkitgtk
Summary:	GTK WebKit bindings for Python
Summary(pl.UTF-8):	Wiązania biblioteki GTK WebKit dla Pythona
Name:		python-%{module}
Version:	0.2.1
Release:	0.20080108.2
License:	LGPL v2
Group:		Libraries/Python
Source0:	%{module}-git.tar.bz2
# Source0-md5:	d519f8e2fe10312a070693d49108dcf9
URL:		http://live.gnome.org/PyWebKitGtk
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 1:2.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.5.0
BuildRequires:	python-pygtk-devel >= 2:2.0
BuildRequires:	gtk-webkit-devel >= 1.0.0-0.r30090.1
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

%files devel
%defattr(644,root,root,755)
%{pydefsdir}/webkitgtk.defs
