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

Version:        8.0.0
Release:        1%{?dist}

URL:            https://www.joypixels.com/download
Source0:        https://cdn.joypixels.com/arch-linux/font/%{version}/joypixels-android.ttf
Source1:        https://cdn.joypixels.com/arch-linux/license/free-license.pdf
Source2:        https://cdn.joypixels.com/arch-linux/appendix/joypixels-license-appendix.pdf
Source3:        65-joypixels.conf

%fontpkg

%prep
%setup -cT
cp %{SOURCE0} joypixels.ttf
cp %{SOURCE1} LICENSE.pdf
cp %{SOURCE2} LICENSE.appendix.pdf

%install
%fontinstall

%files
%fontfiles

%changelog
* Wed Jan  3 2024 dusansimic <dusan.simic1810@gmail.com> - 8.0.0-1
- Release 8.0.0
* Wed Jul 28 2021 dusansimic <dusan.simic1810@gmail.com> - 6.6.0-1
- Release 6.6.0
* Tue Apr  6 2021 dusansimic <dusan.simic1810@gmail.com> - 6.5.0-1
- Release 6.5.0
