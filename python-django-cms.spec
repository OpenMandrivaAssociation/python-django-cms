%define	module	django-cms
%define name	python-%{module}
%define version 2.2
%define release %mkrel 1

Summary:	An advanced Django CMS
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pypi.python.org/packages/source/d/%{module}/%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://www.django-cms.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	python-django >= 1.2.5
Requires:	python-django-classy-tags >= 0.3.4.1
Requires:	python-django-south >= 0.7.2
Requires:	python-html5lib
Requires:	python-django-mptt >= 0.4.2
Requires:	python-django-sekizai >= 0.4.2
BuildRequires:	python-django >= 1.2.5
BuildRequires:	python-django-classy-tags >= 0.3.4.1
BuildRequires:	python-django-south >= 0.7.2
BuildRequires:	python-html5lib
BuildRequires:	python-django-mptt >= 0.4.2
BuildRequires:	python-django-sekizai >= 0.4.2
BuildRequires:	python-setuptools, python-sphinx

%description
Django CMS is an application for managing hierarchical pages of
content, possibly in multiple languages and/or on multiple sites.

Django CMS handles the navigation rendering for you with clean, slug
based URLs, and this navigation can be extended by custom Django
applications.

%prep
%setup -q -n %{module}-%{version}

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
pushd docs
make html
popd

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc AUTHORS CHANGELOG.txt LICENSE README.rst docs/build/html/

