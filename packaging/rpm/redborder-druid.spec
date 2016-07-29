Name: redborder-druid
Version: %{__version}
Release: %{__release}%{?dist}
BuildArch: noarch
Summary: Redborder package containing druid files

License: AGPL 3.0
URL: https://github.com/redBorder/redborder-druid
Source0: %{name}-%{version}.tar.gz

BuildRequires: systemd

Requires: bash druid

%description
%{summary}

%prep
%setup -qn %{name}-%{version}

%build

%install
mkdir -p %{buildroot}/usr/lib/redborder/bin
install -D -m 0755 resources/bin/rb_druid_start.sh %{buildroot}/usr/lib/redborder/bin/rb_druid_start.sh
install -D -m 0644 resources/systemd/druid-coordinator.service %{buildroot}/usr/lib/systemd/system/druid-coordinator.service
install -D -m 0644 resources/systemd/druid-broker.service %{buildroot}/usr/lib/systemd/system/druid-broker.service
install -D -m 0644 resources/systemd/druid-overlord.service %{buildroot}/usr/lib/systemd/system/druid-overlord.service
install -D -m 0644 resources/systemd/druid-historical.service %{buildroot}/usr/lib/systemd/system/druid-historical.service
install -D -m 0644 resources/systemd/druid-middlemanager.service %{buildroot}/usr/lib/systemd/system/druid-middlemanager.service

%files
%defattr(0755,root,root)
/usr/lib/redborder/bin/rb_druid_start.sh
%defattr(0644,root,root)
/usr/lib/systemd/system/druid-coordinator.service

%post
%systemd_post druid.service

%changelog
* Wed Jul 27 2016 Enrique Jimenez <ejimenez@redborder.com> 1.0.0-6
- Add rest of services

* Wed Jul 27 2016 Enrique Jimenez <ejimenez@redborder.com> 1.0.0-5
- Fix systemd service 

* Wed Jul 27 2016 Enrique Jimenez <ejimenez@redborder.com> 1.0.0-4
- Fix test comments

* Wed Jul 27 2016 Enrique Jimenez <ejimenez@redborder.com> 1.0.0-3
- Fix system druid name

* Wed Jul 27 2016 Enrique Jimenez <ejimenez@redborder.com> 1.0.0-2
- Fix systemd service

* Wed Jul 26 2016 Enrique Jimenez <ejimenez@redborder.com> 1.0.0-1
- Add druid as dependency
- first spec version

