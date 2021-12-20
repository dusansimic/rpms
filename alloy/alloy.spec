Name:           alloy
Version:        6.0.0
Release:        1%{?dist}
Summary:        A lightweight modelling language for software design

License:        MIT
URL:            https://alloytools.org
Source0:        https://github.com/AlloyTools/org.alloytools.alloy/releases/download/v%{version}/org.alloytools.alloy.dist.jar
Source1:        alloy.sh
Source2:        alloy.desktop
Source3:        alloy.png

BuildArch:      noarch

Requires:       java

%description
%{summary}.

%prep
%autosetup -cT

%install
install -Dm644 %{SOURCE0} -t %{buildroot}%{_libdir}/alloy
install -Dm755 %{SOURCE1} %{buildroot}%{_bindir}/alloy
install -Dm644 %{SOURCE2} -t %{buildroot}%{_datadir}/applications
install -Dm644 %{SOURCE3} -t %{buildroot}%{_datadir}/pixmaps

%files
%{_libdir}/alloy/org.alloytools.alloy.dist.jar
%{_bindir}/alloy
%{_datadir}/applications/alloy.desktop
%{_datadir}/pixmaps/alloy.png

%changelog
* Mon Dec 20 2021 dusansimic <dusan.simic1810@gmail.com> - 6.0.0-1
	- Release 6.0.0
