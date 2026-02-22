%define	module	django-cms
%define oname django_cms

Name:		python-django-cms
Summary:	An advanced Django CMS
Version:	5.0.6
Release:	1
License:	BSD-3-Clause
Group:		Development/Python
URL:		https://www.django-cms.org/
Source0:	https://pypi.python.org/packages/source/d/%{module}/%{oname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(argon2-cffi)
BuildRequires:	python%{pyver}dist(bcrypt)
BuildRequires:	python%{pyver}dist(django)
BuildRequires:	python%{pyver}dist(django-classy-tags)
BuildRequires:	python%{pyver}dist(django-formtools)
BuildRequires:	python%{pyver}dist(django-treebeard)
BuildRequires:	python%{pyver}dist(django-sekizai)
BuildRequires:	python%{pyver}dist(djangocms-admin-style)
BuildRequires:	python%{pyver}dist(packaging)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(sphinx)
BuildRequires:	python%{pyver}dist(wheel)



%description
Django CMS is an application for managing hierarchical pages of
content, possibly in multiple languages and/or on multiple sites.

Django CMS handles the navigation rendering for you with clean, slug
based URLs, and this navigation can be extended by custom Django
applications.

%prep
%autosetup -n %{oname}-%{version} -p1
# Remove bundled egg-info
rm -rf %{oname}.egg-info

%build
%py_build

%install
%py_install

%files
%doc README.rst
%license LICENSE
%{_bindir}/djangocms
%{python_sitelib}/menus
%{python_sitelib}/cms
%{python_sitelib}/%{oname}-%{version}.dist-info
