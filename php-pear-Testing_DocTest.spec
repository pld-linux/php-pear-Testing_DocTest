%include	/usr/lib/rpm/macros.php
%define		_class		Testing
%define		_subclass	DocTest
%define		_status		alpha
%define		_pearname	Testing_DocTest
Summary:	%{_pearname} - A Unit Test framework for writing tests in your php code docstrings
Summary(pl.UTF-8):	%{_pearname} - framework do pisania testów w kodzie php za pomocą docstrings
Name:		php-pear-%{_pearname}
Version:	0.3.1
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	238926831e2200b7e802215819545fa5
URL:		http://pear.php.net/package/Testing_DocTest/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-Console_CommandLine >= 1.0.0RC3
Requires:	php-pear-PEAR-core >= 1:1.4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Testing_DocTest allows the developer to write unit tests directly in
the <code></code> blocs of your functions, classes and class methods
doc comments.

It comes with a default runner (phpdt) that will parse all your
<code></code> blocs and will run the extracted tests. Running tests is
as simple as:

$ phpdt /path/to/your/code

There are several advantages in using Testing_DocTest:
- it makes unit tests writing funnier, easier and quicker (there's no
  infrastructure to setup, you just install the package, write your code
  examples tests and you're done !);
- it ensures that doc comments are up-to-date by verifying that all
  examples work as documented;
- it enforces writing of tutorial documentation, liberally illustrated
  with input-output examples.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Testing_DocTest pozwala developerowi na pisanie testów bezpośrednio
wewnątrz znaczników <code></code> w komentarzach funkcji, klas i ich
metod.

Dostarczany jest program (phpdt) który przetworzy bloki <code></code>
i wykona pobrane testy. Wywołanie jest proste:

$ phpdt /sciezka/do/kodu

Istnieje sporo korzyści z wykorzystania Testing_DocTest:
- sprawia, że pisanie testów jest prostsze i szybsze (brak
  infrastruktury do konfiguracji, wystarczy zainstalowanie pakietu i
  napisanie testu),
- zapewnia aktualność komentarzy poprzez weryfikację załączonych
  przykładów,
- wymusza pisanie dokumentacji, ilustrując za pomocą przykładów
  wejścia-wyjścia.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
AutoReq:	no
Requires:	%{name} = %{version}-%{release}
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_bindir}}
%pear_package_install
install usr/bin/phpdt $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%attr(755,root,root) %{_bindir}/phpdt
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Testing/DocTest
%{php_pear_dir}/Testing/DocTest.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/Testing_DocTest
