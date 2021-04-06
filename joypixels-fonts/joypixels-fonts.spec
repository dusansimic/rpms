%global debug_package  %{nil}

%global foundry        JoyPixels
%global fontlicense    Custom
%global fontlicenses   LICENSE.pdf LICENSE.appendix.pdf
%global fontfamily     JoyPixels
%global fontsummary    Emoji as a Service
%global fonts          *.ttf
%global fontconfs      %{SOURCE3}
%global fontdescription %{expand:
Beautiful colored emoji font for personal use.
}

Name:           joypixels-fonts
Version:        6.5.0
Release:        1%{?dist}
Summary:        Emoji as a Service (formerly EmojiOne)

License:        JoyPixels Free
URL:            https://www.joypixels.com/download
Source0:        https://cdn.joypixels.com/arch-linux/font/%{version}/joypixels-android.ttf
Source1:        https://cdn.joypixels.com/arch-linux/license/free-license.pdf
Source2:        https://cdn.joypixels.com/arch-linux/appendix/joypixels-license-appendix.pdf
Source3:        65-joypixels.conf

%description
Beautiful colored emoji font for personal use.

%fontpkg

%prep
%setup -cT

%build
%fontbuild

%install
%fontinstall
install -d %{buildroot}%{_datadir}/fontconfig/conf.avail
install -d %{buildroot}%{_sysconfdir}/fonts/conf.d

install -Dm644 %{SOURCE0} %{buildroot}%{_datadir}/fonts/joypixels/JoyPixels.ttf
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/licenses/%{name}/LICENSE.pdf
install -Dm644 %{SOURCE2} %{buildroot}%{_datadir}/licenses/%{name}/LICENSE.appendix.pdf
install -Dm644 %{SOURCE3} %{buildroot}%{_datadir}/fontconfig/conf.avail

ln -sf %{_datadir}/fontconfig/conf.avail/65-joypixels.conf %{buildroot}%{_sysconfdir}/fonts/conf.d

%check
%fontcheck

%fontfiles
%license %{_datadir}/licenses/%{name}/LICENSE.pdf
%{_datadir}/fonts/joypixels/
%{_datadir}/fontconfig/conf.avail/65-joypixels.conf
%{_sysconfdir}/fonts/conf.d/65-joypixels.conf
%{_datadir}/licenses/%{name}/

%changelog
* Tue Apr  6 2021 dusansimic <dusan.simic1810@gmail.com> - 6.5.0-1
- Release 6.5.0
