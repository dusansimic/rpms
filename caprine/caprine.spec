%define debug_package %{nil}

Name:           caprine
Version:        2.52.2
Release:        1%{?dist}
Summary:        Elegant Facebook Messenger desktop app

License:        MIT
URL:            https://sindresorhus.com/caprine/
Source0:        https://github.com/sindresorhus/caprine/archive/refs/tags/v%{version}.tar.gz
Source1:        %{name}.desktop

BuildArch:      x86_64
BuildRequires:  npm
BuildRequires:  git-core
BuildRequires:  nodejs >= 14.0.0
BuildRequires:  nodejs-packaging
Requires:       desktop-file-utils
Requires:       gtk-update-icon-cache

%description
Caprine is an unofficial and privacy-focused Facebook Messenger app with many useful features.

%prep
%autosetup

%build
npm install
node_modules/.bin/tsc
node_modules/.bin/electron-builder --linux dir

%install
install -d %{buildroot}%{_libdir}/%{name}
cp -r dist/linux-unpacked/* %{buildroot}%{_libdir}/%{name}

install -d %{buildroot}%{_bindir}
ln -sf %{_libdir}/%{name}/%{name} %{buildroot}%{_bindir}/%{name}

for s in 16 32 48 64 128 256 512
do
	install -Dm644 build/icons/${s}x${s}.png %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps/%{name}.png
done

install -d %{buildroot}%{_datadir}/applications
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop

%post
/usr/bin/update-desktop-database
/usr/bin/gtk-update-icon-cache

%postun
/usr/bin/update-desktop-database
/usr/bin/gtk-update-icon-cache

%files
%license license
%doc readme.md
%{_libdir}/%{name}/
%{_bindir}/%{name}
%{_datadir}/applications/caprine.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Thu Mar 25 2021 dusansimic <dusna.simic1810@gmail.com> - 2.52.2-1
- Release 2.52.2
