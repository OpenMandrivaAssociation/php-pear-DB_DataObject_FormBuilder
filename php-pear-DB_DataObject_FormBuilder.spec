%define		_class		DB
%define		_subclass	DataObject_FormBuilder
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.0.1
Release:	%mkrel 3
Summary:	Automatically build HTML_QuickForm object from a DB_DataObject derived class
Epoch:      1
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/DB_DataObject_FormBuilder/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
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

rm -f %{buildroot}%{_datadir}/pear/package.php

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{upstream_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/data/%{upstream_name}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1:1.0.1-3mdv2012.0
+ Revision: 741840
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1:1.0.1-2
+ Revision: 679282
- mass rebuild

* Sat Nov 27 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1:1.0.1-1mdv2011.0
+ Revision: 602137
- new version

* Wed Dec 16 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1:1.0.0-2mdv2010.1
+ Revision: 479289
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Sun Sep 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1:1.0.0-1mdv2010.0
+ Revision: 450231
- new version
- use pear installer
- use fedora %%post/%%postun

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0.0RC7-3mdv2009.1
+ Revision: 321951
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.0RC7-2mdv2009.0
+ Revision: 236821
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Nov 09 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.0RC7-1mdv2008.1
+ Revision: 107107
- new release 1.0.0RC7


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.14.0-7mdv2007.0
+ Revision: 81483
- Import php-pear-DB_DataObject_FormBuilder

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.14.0-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.14.0-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.14.0-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.14.0-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.14.0-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.14.0-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.14.0-1mdk
- initial Mandriva package (PLD import)

