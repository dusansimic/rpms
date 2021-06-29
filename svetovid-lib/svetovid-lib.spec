Name:           svetovid-lib
Version:        0.5
Release:        1%{?dist}
Summary:        Supplement Library for Introductory Programming Courses

License:        Apache
URL:            https://github.com/ivanpribela/svetovid-lib
Source0:        https://github.com/ivanpribela/svetovid-lib/archive/refs/tags/v%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  ant
BuildRequires:  inkscape
#Requires:

%description
Supplement Library for Introductory Programming Courses

%prep
%autosetup

%build
ant pack.jar

%install
install -Dm644 "dist/%{name}.jar" "%{buildroot}%{_datadir}/java/%{name}/%{name}.jar"

install -Dm644 "LICENSE" "%{buildroot}%{_datadir}/licenses/%{name}/LICENSE"
install -Dm644 "NOTICE" "%{buildroot}%{_datadir}/licenses/%{name}/NOTICE"

%check

%files
%license %{_datadir}/licenses/%{name}/LICENSE
%{_datadir}/licenses/%{name}/NOTICE
%{_datadir}/java/%{name}/%{name}.jar

%changelog
* Wed Jun 16 2021 dusansimic <dusan.simic1810@gmail.com> - 0.5.0-1
- Release 0.5.0