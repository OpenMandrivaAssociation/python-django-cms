%define	module	django-cms

%if %{_use_internal_dependency_generator}
%define __noautoreq 'pythonegg\\((django-sekizai\\)'
%endif

Summary:	An advanced Django CMS
Name:		python-%{module}
Version:	2.3.3
Release:	3
Source0:	http://pypi.python.org/packages/source/d/%{module}/%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://www.django-cms.org/
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
BuildRequires:	python-setuptools
BuildRequires:	python-sphinx

%description
Django CMS is an application for managing hierarchical pages of
content, possibly in multiple languages and/or on multiple sites.

Django CMS handles the navigation rendering for you with clean, slug
based URLs, and this navigation can be extended by custom Django
applications.

%prep
%setup -q -n %{module}-%{version}

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
sed -i 's/.*egg-info$//' FILE_LIST
pushd docs
make html
popd

%files -f FILE_LIST
%doc AUTHORS CHANGELOG.txt LICENSE README.rst docs/build/html/



%changelog
* Mon Dec 19 2011 Lev Givon <lev@mandriva.org> 2.2-1
+ Revision: 743844
- imported package python-django-cms

