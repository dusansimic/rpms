Name: ttyd
Summary: Share your terminal over the web
Version: 1.6.3
Release: 1%{?dist}
License: MIT
URL: https://tsl0922.github.io/ttyd/
Source0: https://github.com/tsl0922/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
	
BuildRequires: json-c-devel
BuildRequires: cmake
BuildRequires: openssl-devel
BuildRequires: libwebsockets-devel
BuildRequires: gcc
BuildRequires: zlib-devel

%description
ttyd is a simple command-line tool for sharing terminal over the web,
inspired by GoTTY.

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/ttyd
%{_mandir}/man1/ttyd.1.*

%changelog
* Sun May 23 2021 dusansimic <dusan.simic1810@gmail.com> - 1.6.3-1
- Release 1.6.3
