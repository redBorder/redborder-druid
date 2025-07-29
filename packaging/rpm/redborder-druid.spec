Name: redborder-druid
Version: %{__version}
Release: %{__release}%{?dist}
BuildArch: noarch
Summary: Redborder package containing druid files

License: AGPL 3.0
URL: https://github.com/redBorder/redborder-druid
Source0: %{name}-%{version}.tar.gz
Source1: kafka-clients-3.6.1.jar
Source2: kafka-emitter-31.0.0.jar


BuildRequires: systemd

Requires: bash druid

%description
%{summary}

%prep
%setup -qn %{name}-%{version}

%build

%install
mkdir -p %{buildroot}/usr/lib/redborder/bin
mkdir -p %{buildroot}/usr/lib/druid/lib/
install -D -m 0755 resources/bin/rb_druid_start.sh %{buildroot}/usr/lib/redborder/bin/rb_druid_start.sh
install -D -m 0644 resources/systemd/druid-coordinator.service %{buildroot}/usr/lib/systemd/system/druid-coordinator.service
install -D -m 0644 resources/systemd/druid-broker.service %{buildroot}/usr/lib/systemd/system/druid-broker.service
install -D -m 0644 resources/systemd/druid-overlord.service %{buildroot}/usr/lib/systemd/system/druid-overlord.service
install -D -m 0644 resources/systemd/druid-historical.service %{buildroot}/usr/lib/systemd/system/druid-historical.service
install -D -m 0644 resources/systemd/druid-middlemanager.service %{buildroot}/usr/lib/systemd/system/druid-middlemanager.service
install -D -m 0644 resources/systemd/druid-indexer.service %{buildroot}/usr/lib/systemd/system/druid-indexer.service
install -D -m 0644 resources/systemd/druid-router.service %{buildroot}/usr/lib/systemd/system/druid-router.service
mkdir -p %{buildroot}/usr/lib/druid/extensions/kafka-emitter
cp -a $RPM_SOURCE_DIR/kafka-clients-3.6.1.jar %{buildroot}/usr/lib/druid/extensions/kafka-emitter/
cp -a $RPM_SOURCE_DIR/kafka-emitter-31.0.0.jar %{buildroot}/usr/lib/druid/extensions/kafka-emitter/

%files
%defattr(0755,root,root)
/usr/lib/redborder/bin/rb_druid_start.sh
%defattr(0644,root,root)
/usr/lib/systemd/system/druid-coordinator.service
/usr/lib/systemd/system/druid-broker.service
/usr/lib/systemd/system/druid-overlord.service
/usr/lib/systemd/system/druid-historical.service
/usr/lib/systemd/system/druid-middlemanager.service
/usr/lib/systemd/system/druid-indexer.service
/usr/lib/systemd/system/druid-router.service
/usr/lib/druid/extensions/kafka-emitter/kafka-clients-3.6.1.jar
/usr/lib/druid/extensions/kafka-emitter/kafka-emitter-31.0.0.jar

%post
%systemd_post druid.service
cd /usr/lib/druid
java -cp "lib/*" -Ddruid.extensions.directory="extensions" \
     org.apache.druid.cli.Main tools pull-deps \
     -c "org.apache.druid.extensions.contrib:kafka-emitter:31.0.0"

%changelog
* Tue Jul 15 2025 Pablo Torres <ptorres@redborder.com>
- Add druid metrics

* Tue Feb 11 2025 Miguel Álvarez <malvarez@redborder.com>
- Update druid to 31.0.1

* Thu Jan 25 2018 Juan J, Chorro <jjchorro@redborder.com> 1.0.0-9
- Add realtime mode

* Mon Aug 29 2016 Carlos J. Mateos <cjmateos@redborder.com> 1.0.0-8
- Added SIGAR lib

* Wed Jul 27 2016 Enrique Jimenez <ejimenez@redborder.com> 1.0.0-7
- Bugfix on %files spec part

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

* Thu Jul 26 2016 Enrique Jimenez <ejimenez@redborder.com> 1.0.0-1
- Add druid as dependency
- first spec version
