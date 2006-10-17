Summary:	X.org mouse input driver
Summary(pl):	Sterownik wej¶ciowy myszy dla X.org
Name:		xorg-driver-input-mouse
Version:	1.1.2
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-input-mouse-%{version}.tar.bz2
# Source0-md5:	d8bcd9fb1b4efb02acd251495f9a30c1
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-inputproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 1.0.99.901
Requires:	xorg-xserver-server >= 1.0.99.901
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org mouse input driver. It supports most available mouse types and
interfaces, including USB and PS/2.

%description -l pl
Sterownik wej¶ciowy myszy dla X.org. Obs³uguje wiêkszo¶æ dostêpnych
rodzajów myszy i interfejsów, w tym USB i PS/2.

%prep
%setup -q -n xf86-input-mouse-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/xorg/modules/input/mouse_drv.so
%{_mandir}/man4/mousedrv.4*
