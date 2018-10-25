#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xC36CDCB4DF00C68C (infra-root@openstack.org)
#
Name     : python-mistralclient
Version  : 3.7.0
Release  : 17
URL      : http://tarballs.openstack.org/python-mistralclient/python-mistralclient-3.7.0.tar.gz
Source0  : http://tarballs.openstack.org/python-mistralclient/python-mistralclient-3.7.0.tar.gz
Source99 : http://tarballs.openstack.org/python-mistralclient/python-mistralclient-3.7.0.tar.gz.asc
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
Requires: six
Requires: stevedore
BuildRequires : buildreq-distutils3
BuildRequires : pbr

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

%description python3
python3 components for the python-mistralclient package.


%prep
%setup -q -n python-mistralclient-3.7.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1540493829
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-mistralclient
cp LICENSE %{buildroot}/usr/share/package-licenses/python-mistralclient/LICENSE
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
/usr/share/package-licenses/python-mistralclient/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
