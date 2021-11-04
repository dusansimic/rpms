%define name eclipse-jee
%define buildarch x86_64
%define rel 2021-09/R
%define reldash 2021-09-R
%define srcfilename %{name}-%{reldash}-linux-gtk-%{buildarch}.tar.gz

%define _eclipsedir %{_libdir}/eclipse

Name:           %{name}
Version:        4.21
Release:        1%{?dist}
Summary:        Highly extensible IDE (Enterprise Java and Web version)

License:        EPL
URL:            https://www.eclipse.org
Source0:        %{url}/downloads/download.php?file=/technology/epp/downloads/release/%{rel}/%{srcfilename}&r=1
Source1:        eclipse.desktop

BuildArch:      %{buildarch}
Provides:       eclipse
Requires:       java
Conflicts:      eclipse

%description
Tools for Java developers creating Java EE and Web applications, including a Java IDE, tools for Java EE, JPA, JSF, Mylyn, EGit and others

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
* Thu Nov  4 2021 dusansimic <dusan.simic1810@gmail.com> - 4.21-1
	- Release 4.21
