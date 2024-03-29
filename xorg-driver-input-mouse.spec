Summary:	X.org mouse input driver
Summary(pl.UTF-8):	Sterownik wejściowy myszy dla X.org
Name:		xorg-driver-input-mouse
Version:	1.9.5
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/driver/xf86-input-mouse-%{version}.tar.xz
# Source0-md5:	9e2c33131f804476053c618859193dd1
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-proto-inputproto-devel
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xorg-xserver-server-devel >= 1.7
BuildRequires:	xz
%{?requires_xorg_xserver_xinput}
Requires:	xorg-xserver-server >= 1.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org mouse input driver. It supports most available mouse types and
interfaces, including USB and PS/2.

%description -l pl.UTF-8
Sterownik wejściowy myszy dla X.org. Obsługuje większość dostępnych
rodzajów myszy i interfejsów, w tym USB i PS/2.

%package devel
Summary:	Header file for mouse driver
Summary(pl.UTF-8):	Plik nagłówkowy sterownika myszy
Group:		Development/Libraries

%description devel
Header file for mouse driver.

%description devel -l pl.UTF-8
Plik nagłówkowy sterownika myszy.

%prep
%setup -q -n xf86-input-mouse-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/xorg/modules/input/mouse_drv.so
%{_mandir}/man4/mousedrv.4*

%files devel
%defattr(644,root,root,755)
%{_includedir}/xorg/xf86-mouse-properties.h
%{_pkgconfigdir}/xorg-mouse.pc
