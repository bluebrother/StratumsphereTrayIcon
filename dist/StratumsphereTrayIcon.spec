%define githash d152496
%define repo bluebrother
%define extraversion v0.5-53-g

Name:           StratumsphereTrayIcon
Version:        0.9375_g%{githash}
Release:        1%{?dist}
Summary:        Stratum0 status monitor

Group:          Applications/Internet
License:        GPL
URL:            https://stratum0.org/mediawiki/index.php/Open/Close-Monitor
Source0:        %{repo}-%{name}-%{extraversion}%{githash}.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:  qt-devel
Requires:       qt

%description
System tray application that shows the status of the Stratum0 hackerspace.


%prep
%setup -q -n %{repo}-%{name}-%{githash}


%build
qmake-qt4
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
install -m 755 -D s0trayicon %{buildroot}%{_bindir}/s0trayicon
install -m 755 -D res/open.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/s0trayicon.svg
install -m 755 -d %{buildroot}%{_datadir}/applications
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications res/StratumsphereTrayIcon.desktop


%clean
rm -rf $RPM_BUILD_ROOT

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_datadir}/icons/hicolor/scalable/apps/*
%{_datadir}/applications/*.desktop
%doc



%changelog
* Tue May 29 2012 Dominik Riebeling <bluebrother@gmx.de>
- initial version
