Summary:	X.org mouse driver
Summary(pl):	Sterownik myszy dla X.org
Name:		xorg-driver-input-mouse
Version:	1.0.0.1
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/driver/xf86-input-mouse-%{version}.tar.bz2
# Source0-md5:	fb2a899ea620b992918981e50e7ac2f8
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkgconfig >= 0.19
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org mouse driver

%description -l pl
Sterownik myszy dla X.org

%prep
%setup -q -n xf86-input-mouse-%{version}

%build
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

rm $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*{.la,.a}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xorg/modules/*/*.so
%{_mandir}/man4x/*.4x*
