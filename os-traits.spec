#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : os-traits
Version  : 0.16.0
Release  : 13
URL      : https://files.pythonhosted.org/packages/60/d5/9fbd37407d79b974b24ff881ab31d30dc524fd99f55a8bd9cdd50a25539a/os-traits-0.16.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/60/d5/9fbd37407d79b974b24ff881ab31d30dc524fd99f55a8bd9cdd50a25539a/os-traits-0.16.0.tar.gz
Summary  : A library containing standardized trait strings
Group    : Development/Tools
License  : Apache-2.0
Requires: os-traits-license = %{version}-%{release}
Requires: os-traits-python = %{version}-%{release}
Requires: os-traits-python3 = %{version}-%{release}
Requires: pbr
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : pbr
BuildRequires : six

%description
=========
os-traits
=========
`os-traits` is a library containing standardized trait strings.

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

%description python3
python3 components for the os-traits package.


%prep
%setup -q -n os-traits-0.16.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1564684837
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/os-traits
cp LICENSE %{buildroot}/usr/share/package-licenses/os-traits/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/os-traits/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
