Summary: Library providing the Gnome XSLT engine
Name: libxslt
Version: 1.1.4
Release: 1
License: MIT
Group: Development/Libraries
Source: ftp://xmlsoft.org/XSLT/libxslt-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
URL: http://xmlsoft.org/XSLT/
Requires: libxml2 >= 2.6.5
BuildRequires: libxml2-devel >= 2.6.5
BuildRequires: python python-devel
BuildRequires: libxml2-python
Prefix: %{_prefix}
Docdir: %{_docdir}

%description
This C library allows to transform XML files into other XML files
(or HTML, text, ...) using the standard XSLT stylesheet transformation
mechanism. To use it you need to have a version of libxml2 >= 2.6.5
installed. The xsltproc command is a command line interface to the XSLT engine

%package devel
Summary: Libraries, includes, etc. to embed the Gnome XSLT engine
Group: Development/Libraries
Requires: libxslt = %{version}
Requires: libxml2-devel >= 2.5.6

%description devel
This C library allows to transform XML files into other XML files
(or HTML, text, ...) using the standard XSLT stylesheet transformation
mechanism. To use it you need to have a version of libxml2 >= 2.6.5
installed.

%package python
Summary: Python bindings for the libxslt library
Group: Development/Libraries
Requires: libxslt = %{version}
Requires: libxml2 >= 2.6.5
Requires: libxml2-python >= 2.6.5
Requires: python

%description python
The libxslt-python package contains a module that permits applications
written in the Python programming language to use the interface
supplied by the libxslt library to apply XSLT transformations.

This library allows to parse sytlesheets, uses the libxml2-python
to load and save XML and HTML files. Direct access to XPath and
the XSLT transformation context are possible to extend the XSLT language
with XPath functions written in Python.

%prep
%setup -q

%build
%configure
make

%install
rm -fr %{buildroot}

%makeinstall

%clean
rm -fr %{buildroot}

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-, root, root)

%doc AUTHORS ChangeLog NEWS README Copyright TODO FEATURES
%doc doc/*.html doc/html doc/tutorial doc/*.gif
%doc %{_mandir}/man1/xsltproc.1*
%{_libdir}/lib*.so.*
%{prefix}/bin/xsltproc

%files devel
%defattr(-, root, root)

%doc AUTHORS ChangeLog NEWS README Copyright TODO FEATURES
%doc doc/libxslt-api.xml
%doc doc/libxslt-refs.xml
%doc doc/EXSLT/libexslt-api.xml
%doc doc/EXSLT/libexslt-refs.xml
%doc %{_mandir}/man3/libxslt.3*
%doc %{_mandir}/man3/libexslt.3*
%{_libdir}/lib*.so
%{_libdir}/*a
%{_libdir}/*.sh
%{prefix}/share/aclocal/libxslt.m4
%{prefix}/include/*
%{prefix}/bin/xslt-config
%{_libdir}/pkgconfig/libxslt.pc
%{_libdir}/pkgconfig/libexslt.pc

%files python
%defattr(-, root, root)

%doc AUTHORS ChangeLog NEWS README Copyright FEATURES
%{_libdir}/python*/site-packages/libxslt.py
%{_libdir}/python*/site-packages/libxsltmod*
%doc python/TODO
%doc python/libxsltclass.txt
%doc python/tests/*.py
%doc python/tests/*.xml
%doc python/tests/*.xsl

%changelog
* Mon Feb 23 2004 Daniel Veillard <veillard@redhat.com>
- upstream release 1.1.4 see http://xmlsoft.org/XSLT/news.html

* Sun Nov  2 2003 Daniel Veillard <veillard@redhat.com>
- cleanup, removal of the deprecated breakpoint library and
  automated libxml2 dependancy level in the generated spec file.

* Wed Oct 23 2002 Daniel Veillard <veillard@redhat.com>
- revamped the spec file, cleaned up some rpm building problems

* Wed Sep  4 2002 Daniel Veillard <veillard@redhat.com>

- library paths fixed for x86-64

* Fri Feb  8 2002 Daniel.Veillard <veillard@redhat.com>

- added the python module
- changed the Licence to MIT

* Sat Nov 10 2001 Daniel.Veillard <daniel@veillard.com>

- cleaned up the specfile

* Mon Jan 22 2001 Daniel.Veillard <daniel@veillard.com>

- created based on libxml2 spec file
