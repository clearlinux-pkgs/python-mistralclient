#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xC12B8E73B30F2FC8 (infra-root@openstack.org)
#
Name     : python-mistralclient
Version  : 4.1.1
Release  : 32
URL      : http://tarballs.openstack.org/python-mistralclient/python-mistralclient-4.1.1.tar.gz
Source0  : http://tarballs.openstack.org/python-mistralclient/python-mistralclient-4.1.1.tar.gz
Source1  : http://tarballs.openstack.org/python-mistralclient/python-mistralclient-4.1.1.tar.gz.asc
Summary  : Mistral Client Library
Group    : Development/Tools
License  : Apache-2.0
Requires: python-mistralclient-bin = %{version}-%{release}
Requires: python-mistralclient-license = %{version}-%{release}
Requires: python-mistralclient-python = %{version}-%{release}
Requires: python-mistralclient-python3 = %{version}-%{release}
Requires: PyYAML
Requires: cliff
Requires: keystoneauth1
Requires: osc-lib
Requires: oslo.i18n
Requires: oslo.serialization
Requires: oslo.utils
Requires: pbr
Requires: requests
Requires: stevedore
BuildRequires : PyYAML
BuildRequires : buildreq-distutils3
BuildRequires : cliff
BuildRequires : keystoneauth1
BuildRequires : osc-lib
BuildRequires : oslo.i18n
BuildRequires : oslo.serialization
BuildRequires : oslo.utils
BuildRequires : pbr
BuildRequires : requests
BuildRequires : stevedore

%description
Team and repository tags
        ========================

%package bin
Summary: bin components for the python-mistralclient package.
Group: Binaries
Requires: python-mistralclient-license = %{version}-%{release}

%description bin
bin components for the python-mistralclient package.


%package license
Summary: license components for the python-mistralclient package.
Group: Default

%description license
license components for the python-mistralclient package.


%package python
Summary: python components for the python-mistralclient package.
Group: Default
Requires: python-mistralclient-python3 = %{version}-%{release}

%description python
python components for the python-mistralclient package.


%package python3
Summary: python3 components for the python-mistralclient package.
Group: Default
Requires: python3-core
Provides: pypi(python_mistralclient)
Requires: pypi(cliff)
Requires: pypi(keystoneauth1)
Requires: pypi(osc_lib)
Requires: pypi(oslo.i18n)
Requires: pypi(oslo.serialization)
Requires: pypi(oslo.utils)
Requires: pypi(pbr)
Requires: pypi(pyyaml)
Requires: pypi(requests)
Requires: pypi(stevedore)

%description python3
python3 components for the python-mistralclient package.


%prep
%setup -q -n python-mistralclient-4.1.1
cd %{_builddir}/python-mistralclient-4.1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1599840915
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
mkdir -p %{buildroot}/usr/share/package-licenses/python-mistralclient
cp %{_builddir}/python-mistralclient-4.1.1/LICENSE %{buildroot}/usr/share/package-licenses/python-mistralclient/57aed0b0f74e63f6b85cce11bce29ba1710b422b
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mistral

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-mistralclient/57aed0b0f74e63f6b85cce11bce29ba1710b422b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
