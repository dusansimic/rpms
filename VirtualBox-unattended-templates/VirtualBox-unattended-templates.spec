%global pack_ver %{version}

Name:          VirtualBox-unattended-templates
Version:       7.0.14
Release:       1%{?dist}
Summary:       VirtualBox templates for unattended guest installation

License:       GPL3
URL:           https://www.virtualbox.org

Source0:       https://download.virtualbox.org/virtualbox/%{pack_ver}/VirtualBox-%{pack_ver}.tar.bz2

BuildArch:     noarch

Requires:      VirtualBox = %{pack_ver}

%description
Oracle VM VirtualBox templates for unattended installation of guest operating systems.

%prep
%autosetup -T -c %{name}-%{version}
mkdir tmp
tar -xf %{SOURCE0} -C tmp

%build

%install
install -d %{buildroot}%{_datadir}/virtualbox
cp -R tmp/VirtualBox-%{pack_ver}/src/VBox/Main/UnattendedTemplates %{buildroot}%{_datadir}/virtualbox

%files
%{_datadir}/virtualbox/UnattendedTemplates

%changelog
* Wed Feb 28 2024 dusansimic <dusan.simic1810@gmail.com> - 7.0.14-1
- Release 7.0.14
* Tue Jan  2 2024 dusansimic <dusan.simic1810@gmail.com> - 7.0.12-1
- Release 7.0.12
* Wed Mar 22 2023 dusansimic <dusan.simic1810@gmail.com> - 7.0.6-1
- Release 7.0.6
