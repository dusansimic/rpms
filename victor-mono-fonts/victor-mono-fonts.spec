%global fontlicense    MIT
%global fontlicenses   LICENSE.txt
%global fontfamily     Victor Mono
%global fontsummary    A free programming font with cursive italics and ligatures
%global fonts          TTF/*.ttf
%global fontdescription %{expand:
Victor Mono is an open-source monospaced font with optional semi-connected cursive italics and programming symbol ligatures.
}

Version:        1.4.2
Release:        1%{?dist}

URL:            https://rubjo.github.io/victo-mono
Source0:        https://github.com/rubjo/victor-mono/raw/v%{version}/public/VictorMonoAll.zip

%fontpkg

%prep
%setup -cT
unzip -q %{SOURCE0}

%install
%fontinstall

%files
%fontfiles

%changelog
* Thu Aug  5 2021 dusansimic <dusan.simic1810@gmail.com> - 1.4.2-1
	- Release 1.4.2
