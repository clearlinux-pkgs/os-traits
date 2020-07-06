#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : os-traits
Version  : 2.4.0
Release  : 25
URL      : https://files.pythonhosted.org/packages/68/4d/3c7e46c340e55adb0933f1644d5a2f06024bfe34b3b71f3ce54d434119fa/os-traits-2.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/68/4d/3c7e46c340e55adb0933f1644d5a2f06024bfe34b3b71f3ce54d434119fa/os-traits-2.4.0.tar.gz
Summary  : A library containing standardized trait strings
Group    : Development/Tools
License  : Apache-2.0
Requires: os-traits-license = %{version}-%{release}
Requires: os-traits-python = %{version}-%{release}
Requires: os-traits-python3 = %{version}-%{release}
Requires: pbr
BuildRequires : buildreq-distutils3
BuildRequires : pbr

%description
os-traits
        =========
        
        `os-traits` is an OpenStack library containing standardized trait strings.
        
        Traits are strings that represent a feature of a resource provider hosted by
        the Placement_ service. This library contains the catalog of constants that
        have been standardized in the OpenStack community to refer to a particular
        hardware, virtualization, storage, network, or device trait.

%package license
Summary: license components for the os-traits package.
Group: Default

%description license
license components for the os-traits package.


%package python
Summary: python components for the os-traits package.
Group: Default
Requires: os-traits-python3 = %{version}-%{release}

%description python
python components for the os-traits package.


%package python3
Summary: python3 components for the os-traits package.
Group: Default
Requires: python3-core
Provides: pypi(os_traits)
Requires: pypi(pbr)

%description python3
python3 components for the os-traits package.


%prep
%setup -q -n os-traits-2.4.0
cd %{_builddir}/os-traits-2.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1594049508
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/os-traits
cp %{_builddir}/os-traits-2.4.0/LICENSE %{buildroot}/usr/share/package-licenses/os-traits/294b43b2cec9919063be1a3b49e8722648424779
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/os-traits/294b43b2cec9919063be1a3b49e8722648424779

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
