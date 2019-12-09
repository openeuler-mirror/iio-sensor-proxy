Name:           iio-sensor-proxy
Version:        2.4
Release:        5
Summary:        IIO accelerometer sensor to input device proxy

License:        GPLv3+
URL:            https://github.com/hadess/iio-sensor-proxy
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  make gcc gtk-doc
BuildRequires:  pkgconfig(udev) pkgconfig(systemd) pkgconfig(gio-2.0) pkgconfig(gudev-1.0) systemd
%{?systemd_requires}

%description
%{summary}.

%package docs
Summary:        Documentation for %{name}
BuildArch:      noarch

%description docs
The documentation for %{name}.

%prep
%autosetup 

%build
%configure \
  --disable-silent-rules \
  --enable-gtk-doc       \
  --disable-gtk-tests    \ # not really interested in sample progs
  %{nil}
%make_build

%install
%make_install

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%defattr(-,root,root)
%doc README COPYING
%{_bindir}/monitor-sensor
%{_sbindir}/%{name}
%{_unitdir}/%{name}.service
%{_udevrulesdir}/*-%{name}.rules
%{_sysconfdir}/dbus-1/system.d/net.hadess.SensorProxy.conf

%files docs
%{_datadir}/gtk-doc/html/%{name}/

%changelog
* Wed Dec 4 2019 Senlin Xia <xiasenlin1@huawei.com> - 2.4.5
- Package init
