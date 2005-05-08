%include	/usr/lib/rpm/macros.php
%define		_class		XML
%define		_subclass	SVG
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - XML_SVG API
Summary(pl):	%{_pearname} - API XML_SVG
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	d242f2115dc0b84fd466873465cff223
URL:		http://pear.php.net/package/XML_SVG/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides and object-oriented way of building SVG
documents.

In PEAR status of this package is: %{_status}.

%description -l pl
Ten pakiet dostarcza zorientowanej obiektowo metody budowania
dokumentów SVG.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
