%define pkg_name artisan
%define pkg_summary Visual scope for coffee roasters
%define debug_package %{nil}

Name:           python-%{pkg_name}
Version:        2.0.0
Release:        1%{?dist}
Summary:        %{pkg_summary}

License:        GPLv3
URL:            https://github.com/artisan-roaster-scope/artisan
# to dowload tarbal, check the latest version: https://github.com/artisan-roaster-scope/artisan/releases
# then: wget --content-disposition "https://github.com/artisan-roaster-scope/artisan/archive/$version.tar.gz"
Source0:        %{pkg_name}-%{version}.tar.gz
Patch0:         0001-Add-setup.py-for-Fedora-COPR-build.patch
Patch1:         0002-Fix-imports-to-work-with-Fedora-COPR-build.patch

BuildArch:      noarch
BuildRequires:  python3-devel


%description
%{pkg_summary}

%package -n %{pkg_name}
Summary:        %{pkg_summary}
Requires:       python3-%{pkg_name} = %{version}-%{release}

%description -n %{pkg_name}
%{pkg_summary}


%package -n python3-%{pkg_name}
Summary:        %{pkg_summary}
%{?python_provide:%python_provide python3-%{pkg_name}}
Requires:       python3-bottle
Requires:       python3-colorspacious
Requires:       python3-keyring
Requires:       python3-matplotlib-qt5
Requires:       python3-Phidget
Requires:       python3-PyQt5
Requires:       python3-persist-queue
Requires:       python3-portalocker
Requires:       python3-pymodbus
Requires:       python3-pyserial
Requires:       python3-pyusb
Requires:       python3-qrcode
Requires:       python3-scipy
Requires:       python3-sip
Requires:       python3-snap7
Requires:       python3-unidecode

%description -n python3-%{pkg_name}
%{pkg_summary}


%prep
%autosetup -n %{pkg_name}-%{version} -p1


%build
# remove all unneeded files, some of them confuse rpmbuild
find src/ -maxdepth 1 -type f -a ! -name 'setup.py' -a ! -name 'artisan.py' -a ! -name 'LICENSE.txt' -a ! -name 'README.txt' -delete
rm -rf src/Wheels
rm -rf src/debian
rm -rf src/icons
rm -rf src/includes
rm -rf src/raspbian

# move additional modules under artisanlib as they don't make sense at site-packages level
mv src/const src/artisanlib/
mv src/plus src/artisanlib/

cd src
%py3_build


%install
rm -rf $RPM_BUILD_ROOT
cd src
%py3_install

# rename the binary
%{__mv} $RPM_BUILD_ROOT/%{_bindir}/artisan.py $RPM_BUILD_ROOT/%{_bindir}/artisan


%clean
rm -rf $RPM_BUILD_ROOT


%files -n %{pkg_name}
%{_bindir}/*
%doc src/README.txt
%license LICENSE


%files -n python3-%{pkg_name}
%{python3_sitelib}/*


%changelog
* Sat Jul 27 2019 Daniel Mach <daniel.mach@gmail.com> - 2.0.0-1
- Upgrade to new upstream version

* Sat Mar 23 2019 Daniel Mach <daniel.mach@gmail.com> - 1.6.2-1
- Upgrade to new upstream version

* Sat Nov 17 2018 Daniel Mach <daniel.mach@gmail.com> - 1.5.0-1
- Upgrade to new upstream version

* Sun Oct 14 2018 Daniel Mach <daniel.mach@gmail.com> - 1.4.0-1
- Upgrade to new upstream version

* Sat May 26 2018 Daniel Mach <daniel.mach@gmail.com> - 1.3.1-1
- Upgrade to new upstream version

* Sun Apr 22 2018 Daniel Mach <daniel.mach@gmail.com> - 1.3.0-1
- Upgrade to new upstream version

* Tue Dec 26 2017 Daniel Mach <daniel.mach@gmail.com> - 1.2.0-1
- Upgrade to new upstream version

* Thu Nov 16 2017 Daniel Mach <daniel.mach@gmail.com> - 1.2.0-0.1.beta3
- Initial build
