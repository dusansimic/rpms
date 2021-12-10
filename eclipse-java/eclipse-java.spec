%define name eclipse-java
%define buildarch x86_64
%define rel 2021-12/R
%define reldash 2021-12-R
%define srcfilename %{name}-%{reldash}-linux-gtk-%{buildarch}.tar.gz

%define _eclipsedir %{_libdir}/eclipse

Name:           %{name}
Version:        4.22
Release:        1%{?dist}
Summary:        Highly extensible IDE (Java version)

License:        EPL
URL:            https://www.eclipse.org
Source0:        %{url}/downloads/download.php?file=/technology/epp/downloads/release/%{rel}/%{srcfilename}&r=1
Source1:        eclipse.desktop

BuildArch:      %{buildarch}
Provides:       eclipse
Requires:       java
Conflicts:      eclipse

%description
The essential tools for any Java developer, including a Java IDE, a CVS client, Git client, XML Editor, Mylyn, Maven integration and WindowBuilder

%prep
tar xf %{_sourcedir}/1

%install
install -d %{buildroot}%{_libdir}
cp -r eclipse %{buildroot}%{_eclipsedir}
install -d %{buildroot}%{_bindir}
ln -s %{_libdir}/eclipse/eclipse %{buildroot}%{_bindir}/eclipse

install -Dm644 %{SOURCE1} -t %{buildroot}%{_datadir}/applications

for i in 16 22 24 32 48 64 128 256 512 1024 ; do
	install -Dm644 eclipse/plugins/org.eclipse.platform_%{version}*/"eclipse$i.png" "%{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/eclipse.png"
done

%files
%config %{_eclipsedir}/eclipse.ini
%doc %{_eclipsedir}/readme
%{_eclipsedir}
%{_bindir}/eclipse
%{_datadir}/applications/eclipse.desktop
%{_datadir}/icons/hicolor/*/apps/eclipse.png

%changelog
* Fri Dec 10 2021 dusansimic <dusan.simic1810@gmail.com> - 4.22-1
	- Release 4.22
* Thu Nov  4 2021 dusansimic <dusan.simic1810@gmail.com> - 4.21-1
	- Release 4.21
