%define		_class		DB
%define		_subclass	DataObject_FormBuilder
%define		upstream_name	%{_class}_%{_subclass}

Summary:	Automatically build HTML_QuickForm object from a DB_DataObject derived class
Name:		php-pear-%{upstream_name}
Version:	1.0.0
Release:	%mkrel 1
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/DB_DataObject_FormBuilder/
Source0:	http://pear.php.net/get/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
%{upstream_name} will aid you in rapid application development using the
packages DB_DataObject and HTML_QuickForm. For having quick but working
prototype of your application, simply model the database, run
DataObject`s CreateTable script over it and write a script that passes
one of the resulting objects to the FormBuilder class. The FormBuilder
class will automatically generate a simple but working HTML_QuickForm
object that you can use to test your application. It also provides a
processing method that will automatically detect if an insert() or
update() command has to be executed after the form has been submitted.
If you have set DataObject`s links.ini file correctly, it will also
automatically detect if a table field is a foreign key and will populate
a selectbox with the linked table`s entry. There are many optional
parameteres that you can place in DataObjects.ini or in properties of
your derived classes, that you can use to fine-tune the form generation,
gradually turning the prototypes into fully features forms and you can
take control of any stage at the process.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%post
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :

%preun
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/data/%{upstream_name}
%{_datadir}/pear/packages/%{upstream_name}.xml
