%global pack_ver %{version}
%global license_sha 33d7284dc4a0ece381196fda3cfe2ed0e1e8e7ed7f27b9a9ebc4ee22e24bd23c

Name:           VirtualBox-extpack
Version:        6.1.28
Release:        1%{?dist}
Summary:        VirtualBox Extension Pack

License:        PUEL
URL:            https://www.virtualbox.org

Source0:        https://download.virtualbox.org/virtualbox/%{pack_ver}/Oracle_VM_VirtualBox_Extension_Pack-%{pack_ver}.vbox-extpack

Requires:       VirtualBox = %{version}

%description
Oracle VM VirtualBox Extension Pack. Support for USB 2.0 and USB 3.0 devices, VirtualBox RDP, disk encryption, NVMe and PXE boot for Intel cards.

%prep
%autosetup -T -c %{name}-%{version}

%install
install -Dm644 %{SOURCE0} %{buildroot}%{_datadir}/virtualbox/Oracle_VM_VirtualBox_Extension_Pack-%{pack_ver}.vbox-extpack

%post
VBoxManage extpack install --replace %{_datadir}/virtualbox/Oracle_VM_VirtualBox_Extension_Pack-%{pack_ver}.vbox-extpack --accept-license=%{license_sha}

%files
%{_datadir}/virtualbox/Oracle_VM_VirtualBox_Extension_Pack-%{pack_ver}.vbox-extpack

%changelog
* Sat Nov 20 2021 dusansimic <dusan.simic1810@gmail.com> - 6.1.28-1
	- Release 6.1.28
