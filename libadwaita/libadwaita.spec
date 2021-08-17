%global _version 1.0.0-alpha.2

Name:           libadwaita
Version:        1.0.0~alpha.2
Release:        1%{?dist}
Summary:        Building blocks for modern GNOME applications

License:        LGPLv2.1+
URL:            https://gitlab.gnome.org/GNOME/libadwaita
Source0:        %{url}/-/archive/%{_version}/%{name}-%{_version}.tar.gz

BuildRequires:  cmake
BuildRequires:  vala
BuildRequires:  meson

BuildRequires:  glib2-devel
BuildRequires:  gtk4-devel
BuildRequires:  sassc
BuildRequires:  gi-docgen

BuildRequires:  xorg-x11-server-Xvfb

%description
%{summary}.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{name}-%{_version}

%build
%meson -Dgtk_doc=true -Dexamples=false -Dtests=false
%meson_build

%install
%meson_install

%find_lang libadwaita

%check
%define _smp_build_ncpus 1
%{shrink:xvfb-run -w 10 -d %meson_test}

%files -f libadwaita.lang
%license COPYING
%doc AUTHORS
%doc HACKING.md
%doc NEWS
%doc README.md

%{_libdir}/girepository-1.0/
%{_libdir}/libadwaita-1.so.0


%files devel
%{_includedir}/libadwaita-1/

%{_libdir}/libadwaita-1.so
%{_libdir}/pkgconfig/libadwaita-1.pc

%{_datadir}/gir-1.0/
%{_datadir}/vala/
%{_docdir}/libadwaita-1/

%changelog
* Tue Aug 17 2021 dusansimic <dusan.simic1810@gmail.com> - 1.0.0~alpha.2-1
	- Fix version number
* Sat Aug 14 2021 dusansimic <dusan.simic1810@gmail.com> - 1.0.0alpha.2-1
	- Release version 1.0.0-alpha.2
