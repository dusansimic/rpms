%global debug_package %{nil}
%global _missing_build_ids_terminate_build 0

%define name eclipse-jee
%define exclusivearch x86_64
%define rel 2023-12/R
%define reldash 2023-12-R
%define srcfilename %{name}-%{reldash}-linux-gtk-%{exclusivearch}.tar.gz

%define _eclipsedir %{_libdir}/eclipse

Name:           %{name}
Version:        4.30
Release:        1%{?dist}
Summary:        Highly extensible IDE (Enterprise Java and Web version)

License:        EPL
URL:            https://www.eclipse.org
Source0:        %{url}/downloads/download.php?file=/technology/epp/downloads/release/%{rel}/%{srcfilename}&r=1#/%{name}-%{version}.tar.gz
Source1:        eclipse.desktop

ExclusiveArch:  %{exclusivearch}
Requires:       java
BuildRequires:  desktop-file-utils
Conflicts:      eclipse
Provides:       eclipse = %{version}

%description
Tools for Java developers creating Java EE and Web applications, including a Java IDE, tools for Java EE, JPA, JSF, Mylyn, EGit and others

%prep
%autosetup -c

%build

%install
install -d %{buildroot}%{_libdir}
cp -r eclipse %{buildroot}%{_eclipsedir}
install -d %{buildroot}%{_bindir}
ln -s "$(realpath -m --relative-to %{_bindir}/eclipse %{_libdir}/eclipse/eclipse)" %{buildroot}%{_bindir}/eclipse

desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
desktop-file-validate %{buildroot}/%{_datadir}/applications/eclipse.desktop

for i in 16 22 24 32 48 64 128 256 512 1024 ; do
  install -Dm644 eclipse/plugins/org.eclipse.platform_%{version}*/"eclipse$i.png" "%{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/eclipse.png"
done

find %{buildroot}%{_eclipsedir}/plugins/com.sun.jna_5.13.0.v20230812-1000/com/sun/jna -type d ! -iname '*linux-x86-64' ! -iname '*jna' | xargs rm -rf

%files
%{_eclipsedir}
%{_bindir}/eclipse
%{_datadir}/applications/eclipse.desktop
%{_datadir}/icons/hicolor/*/apps/eclipse.png

%changelog
* Sat Dec 09 2023 manojbaishya <28330014+manojbaishya@users.noreply.github.com> - 4.30-1
- Release 4.30
* Sat Oct 14 2023 manojbaishya <28330014+manojbaishya@users.noreply.github.com> - 4.29-1
- Release 4.29
- Add cleanup command for removing directories for different platforms
* Wed Mar 22 2023 dusansimic <dusan.simic1810@gmail.com> - 4.27-1
- Release 4.27
* Mon Dec 26 2022 dusansimic <dusan.simic1810@gmail.com> - 4.26-1
- Release 4.26
* Mon Oct 10 2022 dusansimic <dusan.simic1810@gmail.com> - 4.25-1
- Release 4.25
* Fri Dec 10 2021 dusansimic <dusan.simic1810@gmail.com> - 4.22-1
- Release 4.22
* Thu Nov  4 2021 dusansimic <dusan.simic1810@gmail.com> - 4.21-1
- Release 4.21
