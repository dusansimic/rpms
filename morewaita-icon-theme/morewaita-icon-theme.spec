%global debug_package %{nil}

%define __reponame MoreWaita
%define __lowername %(echo %{__reponame} | tr '[:upper:]' '[:lower:]')

%define __urlver 47.1

Name:           %{__lowername}-icon-theme
Version:        %__urlver
Release:        1%{?dist}
Summary:        An Adwaita style extra icons theme for Gnome Shell

License:        GPL-3.0-or-later
URL:            https://github.com/somepaulo/%{__reponame}
Source0:        %{url}/archive/refs/tags/%{__urlver}.tar.gz

Requires:       adwaita-icon-theme

%description
%{summary}.

%prep
%autosetup -n %{__reponame}-%{__urlver}

%build
rm -rf _dev/

%install
install -d %{buildroot}%{_datadir}/icons/%{__reponame}
cp -r * %{buildroot}%{_datadir}/icons/%{__reponame}/

%files
%{_datadir}/icons/%{__reponame}/

%changelog
* Fri Nov  1 2024 Dušan Simić <dusan.simic1810@gmail.com> - 47.1-1
- Bump to 47.1
* Sun Oct 15 2023 Dušan Simić <dusan.simic1810@gmail.com> - 45-1
- Bump to 45
* Wed Sep  6 2023 Dušan Simić <dusan.simic1810@gmail.com> - 44.2-1
- Bump to 44.2
* Mon May 15 2023 Dušan Simić <dusan.simic1810@gmail.com> - 44.1-1
- Bump to 44.1
* Mon May  8 2023 Dušan Simić <dusan.simic1810@gmail.com> - 44.0-1
- Bump to 44.0
- Switch from gnome-shell as dep to adwaita-icon-theme
* Tue Feb 14 2023 Dušan Simić <dusan.simic1810@gmail.com> - 43.3-1
- Bump to 43.3
* Fri Dec  2 2022 Dušan Simić <dusan.simic1810@gmail.com> - 43.2-1
- Bump to 43.2
* Tue Nov  8 2022 Dušan Simić <dusan.simic1810@gmail.com> - 43.1.2-1
- Bump to 43.1.2
* Sat Oct 29 2022 Dušan Simić <dusan.simic1810@gmail.com> - 43.1.1-1
- Bump to 43.1.1
* Tue Oct 18 2022 Dušan Simić <dusan.simic1810@gmail.com> - 1.0.0-1
- Add package
