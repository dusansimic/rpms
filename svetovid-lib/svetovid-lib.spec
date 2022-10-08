%define remotever 0.5.1

Name:           svetovid-lib
Version:        0.5.1
Release:        1%{?dist}
Summary:        Supplement Library for Introductory Programming Courses

License:        Apache
URL:            https://github.com/ivanpribela/svetovid-lib
Source0:        https://github.com/ivanpribela/svetovid-lib/archive/refs/tags/v%{remotever}.tar.gz

BuildArch:      noarch

BuildRequires:  ant
BuildRequires:  inkscape
Requires: java-headless
Requires: javapackages-filesystem

%description
Supplement Library for Introductory Programming Courses

%package javadoc
Summary: Documentation for %{name}

BuildArch: noarch

BuildRequires:  ant
Requires: javapackages-filesystem

%description javadoc
%{summary}.

%prep
%autosetup -n %{name}-%{remotever}

%build
ant pack.jar
ant generate.apidoc

%install
# Installing main package files
install -Dm644 dist/%{name}.jar %{buildroot}%{_javadir}/%{name}.jar

# Installing javadoc files
install -dm755 %{buildroot}%{_javadocdir}
cp -a gendoc/api %{buildroot}%{_javadocdir}/%{name}

%files
%doc README.md
%license LICENSE
%license NOTICE
%{_javadir}/%{name}.jar

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Fri Nov 12 2021 dusansimic <dusan.simic1810@gmail.com> - 0.5.1-1
- Release 0.5.1
* Fri Aug 13 2021 dusansimic <dusan.simic1810@gmail.com> - 0.5.0-4
- Fix version for package
- Refactor install and files macro
* Fri Aug 13 2021 dusansimic <dusan.simic1810@gmail.com> - 0.5.0-3
- Fix install block so it follows packaging guidelines
* Tue Aug  3 2021 dusansimic <dusan.simic1810@gmail.com> - 0.5.0-2
- Use _javadir macro
- Link svetovid-lib.jar to svetovid-lib-version.jar
- Add javadoc package
* Wed Jun 16 2021 dusansimic <dusan.simic1810@gmail.com> - 0.5.0-1
- Release 0.5.0
