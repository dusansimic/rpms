%global debug_package %{nil}

%define __reponame MoreWaita
%define __lowername %(echo %{__reponame} | tr '[:upper:]' '[:lower:]')

Name:           %{__lowername}-icon-theme
Version:        43.1.1
Release:        1%{?dist}
Summary:        An Adwaita style extra icons theme for Gnome Shell

License:        GPL-3.0-or-later
URL:            https://github.com/somepaulo/%{__reponame}
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

Requires:       gnome-shell >= 43

%description
%{summary}.

%prep
%autosetup -n %{__reponame}-%{version}

%build

%install
install -d %{buildroot}%{_datadir}/icons/%{__reponame}
cp -r * %{buildroot}%{_datadir}/icons/%{__reponame}/

%files
%{_datadir}/icons/%{__reponame}/

%changelog
* Sat Oct 29 2022 Dušan Simić <dusan.simic1810@gmail.com> - 43.1.1-1
- Bump to 43.1.1
* Tue Oct 18 2022 Dušan Simić <dusan.simic1810@gmail.com> - 1.0.0-1
- Add package
