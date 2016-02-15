#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-mistralclient
Version  : 1.2.0
Release  : 5
URL      : http://tarballs.openstack.org/python-mistralclient/python-mistralclient-1.2.0.tar.gz
Source0  : http://tarballs.openstack.org/python-mistralclient/python-mistralclient-1.2.0.tar.gz
Summary  : Mistral Client Library
Group    : Development/Tools
License  : Apache-2.0
Requires: python-mistralclient-bin
Requires: python-mistralclient-python
BuildRequires : Jinja2
BuildRequires : PyYAML-python
BuildRequires : Pygments
BuildRequires : Sphinx-python
BuildRequires : astroid-python
BuildRequires : cliff-python
BuildRequires : cmd2-python
BuildRequires : debtcollector-python
BuildRequires : docutils-python
BuildRequires : extras
BuildRequires : extras-python
BuildRequires : fixtures-python
BuildRequires : flake8-python
BuildRequires : hacking
BuildRequires : jsonpatch-python
BuildRequires : jsonpointer-python
BuildRequires : jsonschema-python
BuildRequires : linecache2-python
BuildRequires : logilab-common-python
BuildRequires : mccabe-python
BuildRequires : msgpack-python-python
BuildRequires : netaddr
BuildRequires : netifaces-python
BuildRequires : nose-python
BuildRequires : os-client-config-python
BuildRequires : os-testr-python
BuildRequires : oslo.log-python
BuildRequires : paramiko-python
BuildRequires : pbr
BuildRequires : pep8
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pyflakes-python
BuildRequires : pylint-python
BuildRequires : pyparsing-python
BuildRequires : pytest
BuildRequires : python-cinderclient-python
BuildRequires : python-dev
BuildRequires : python-glanceclient-python
BuildRequires : python-keystoneclient-python
BuildRequires : python-mimeparse-python
BuildRequires : python-mock-python
BuildRequires : python-neutronclient-python
BuildRequires : python-novaclient-python
BuildRequires : python-openstackclient-python
BuildRequires : requests-python
BuildRequires : setuptools
BuildRequires : simplejson
BuildRequires : tempest-lib-python
BuildRequires : testtools
BuildRequires : testtools-python
BuildRequires : tox
BuildRequires : unittest2-python
BuildRequires : virtualenv
BuildRequires : warlock-python
Patch1: 0001-test.patch

%description
Mistral client
==============
Python client for Mistral REST API. Includes python library for Mistral API and Command Line Interface (CLI) library.

%package bin
Summary: bin components for the python-mistralclient package.
Group: Binaries

%description bin
bin components for the python-mistralclient package.


%package python
Summary: python components for the python-mistralclient package.
Group: Default
Requires: PyYAML-python
Requires: cliff-python
Requires: python-keystoneclient-python
Requires: python-openstackclient-python
Requires: requests-python

%description python
python components for the python-mistralclient package.


%prep
%setup -q -n python-mistralclient-1.2.0
%patch1 -p1

%build
python2 setup.py build -b py2

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test ||
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mistral

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
