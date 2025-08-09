%global pack_ver %{version}

Name:           VirtualBox-extpack
Version:        7.1.10
Release:        1%{?dist}
Summary:        VirtualBox Extension Pack

License:        PUEL
URL:            https://www.virtualbox.org

Source0:        https://download.virtualbox.org/virtualbox/%{pack_ver}/Oracle_VirtualBox_Extension_Pack-%{pack_ver}.vbox-extpack

BuildArch:      noarch

Requires:       VirtualBox = %{pack_ver}

%description
Oracle VM VirtualBox Extension Pack. Support for USB 2.0 and USB 3.0 devices, VirtualBox RDP, disk encryption, NVMe and PXE boot for Intel cards.

%prep
%autosetup -T -c %{name}-%{version}
mkdir tmp
tar xfC %{SOURCE0} tmp
rm -r tmp/{darwin*,solaris*,win*}

%build

%install
install -d %{buildroot}%{_libdir}/virtualbox/ExtensionPacks
cp -a tmp %{buildroot}%{_libdir}/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack

%files
%{_libdir}/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack

%changelog
* Sat Aug  9 2025 dusansimic <dusan.simic1810@gmail.com> - 7.1.10-1
- Release 7.1.10
* Sat Apr 19 2025 dusansimic <dusan.simic1810@gmail.com> - 7.1.6-1
- Release 7.1.6
* Wed Oct 23 2024 dusansimic <dusan.simic1810@gmail.com> - 7.1.4-1
- Release 7.1.4
* Tue Aug 20 2024 dusansimic <dusan.simic1810@gmail.com> - 7.0.20-1
- Release 7.0.20
* Sun Jun 16 2024 dusansimic <dusan.simic1810@gmail.com> - 7.0.18-1
- Release 7.0.18
* Wed Feb 28 2024 dusansimic <dusan.simic1810@gmail.com> - 7.0.14-1
- Release 7.0.14
* Tue Jan  2 2024 dusansimic <dusan.simic1810@gmail.com> - 7.0.12-1
- Release 7.0.12
* Wed Mar 22 2023 dusansimic <dusan.simic1810@gmail.com> - 7.0.6-1
- Release 7.0.6
* Tue Dec  6 2022 dusansimic <dusan.simic1810@gmail.com> - 7.0.4-1
- Release 7.0.4
* Thu Sep 22 2022 dusansimic <dusan.simic1810@gmail.com> - 6.1.38-1
- Release 6.1.38
* Wed May 11 2022 dusansimic <dusan.simic1810@gmail.com> - 6.1.34-1
- Release 6.1.34
* Sun Mar  6 2022 dusansimic <dusan.simic1810@gmail.com> - 6.1.32-1
- Release 6.1.32
* Mon Dec  6 2021 dusansimic <dusan.simic1810@gmail.com> - 6.1.30-1
- Release 6.1.30
* Sat Nov 20 2021 dusansimic <dusan.simic1810@gmail.com> - 6.1.28-1
- Release 6.1.28
