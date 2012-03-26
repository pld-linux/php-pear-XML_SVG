%define		status		stable
%define		pearname	XML_SVG
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - XML_SVG API
Summary(pl.UTF-8):	%{pearname} - API XML_SVG
Name:		php-pear-%{pearname}
Version:	1.1.0
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	7edff10ef3f38eacdea4693a435f9bd7
URL:		http://pear.php.net/package/XML_SVG/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php-common >= 3:4.2.0
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides and object-oriented way of building SVG
documents.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Ten pakiet dostarcza zorientowanej obiektowo metody budowania
dokumentów SVG.

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup

mv .%{php_pear_dir}/data/XML_SVG/README .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/XML/SVG.php
%{php_pear_dir}/XML/SVG
