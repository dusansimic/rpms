%define debug_package %{nil}

Name:           just
Version:        0.9.2
Release:        1%{?dist}
Summary:        A handy way to save and run project-specific commands

License:        CC0
URL:            https://just.systems
Source0:        https://github.com/casey/just/archive/v%{version}.tar.gz

BuildRequires:  cargo

%description
%{summary}

%prep
%autosetup

%build
cargo build --release

%install
install -Dm755 target/release/just %{buildroot}%{_bindir}/just
install -Dm644 LICENSE %{buildroot}%{_datadir}/licenses/just/LICENSE
install -Dm644 completions/just.zsh %{buildroot}%{_datadir}/zsh/site-functions/_just
install -Dm644 completions/just.bash %{buildroot}%{_datadir}/bash-completion/completions/just
install -Dm644 completions/just.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/just.fish
install -Dm644 man/just.1 %{buildroot}%{_mandir}/man1/just.1

%check
cargo check --release

%files
%license %{_datadir}/licenses/just/LICENSE
%{_bindir}/just
%{_datadir}/zsh/site-functions/_just
%{_datadir}/bash-completion/completions/just
%{_datadir}/fish/vendor_completions.d/just.fish
%{_mandir}/man1/just.1*

%changelog
* Thu May  6 2021 dusansimic <dusan.simic1810@gmail.com> - 0.9.2-1
- Release 0.9.2
