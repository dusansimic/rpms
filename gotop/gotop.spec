%define debug_package %{nil}

Name:           gotop
Version:        4.1.1
Release:        1%{?dist}
Summary:        A terminal based graphical activity monitor

License:        MIT
URL:            https://github.com/xxxserxxx/gotop
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  go
BuildRequires:  git
Requires:       glibc

%description
%{summary}

%prep
%autosetup

%build
CGO_ENABLED=0
go build \
  -gcflags "all=-trimpath=$PWD" \
	-asmflags "all=-trimpath=$PWD" \
	-ldflags "-X main.Version=v%{version} -extldflags $LDFLAGS" \
	-buildmode=pie \
	./cmd/gotop

%install
install -Dm755 gotop %{buildroot}%{_bindir}/gotop
install -Dm644 LICENSE %{buildroot}%{_datadir}/licenses/%{name}/LICENSE

%files
%license %{_datadir}/licenses/%{name}/LICENSE
%{_bindir}/gotop

%changelog
* Wed May 12 2021 dusansimic <dusan.simic1810@gmail.com> - 4.1.1-1
- Release 4.1.1
