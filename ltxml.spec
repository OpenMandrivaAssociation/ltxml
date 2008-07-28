%define name	ltxml
%define version	1.2.7
%define release	%mkrel 5
%define major	1
%define libname	%mklibname %{name} %{major}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	High-speed C-language validating XML parser
Url:		http://www.ltg.ed.ac.uk/software/xml
Source:		ftp://ftp.cogsci.ed.ac.uk/pub/LTXML/%{name}-%{version}.tar.bz2
Patch:		%{name}.maninstall.patch.bz2
License:	GPL
Group:		File tools
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
LT XML is an integrated set of XML tools and a developers' tool-kit,
including a C-based API. The release now available will run on UNIX and
WIN32.
The LT XML tool-kit includes stand-alone tools for a wide range
of processing of well-formed XML documents, including searching and
extracting, down-translation (e.g. report generation, formatting),
tokenising and sorting. 

%package -n %{libname}-devel
Summary:        Development header files for %{name}
Group:          Development/C
Requires:       %{name} = %{version}-%{release}
Provides:       lib%{name}-devel = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{libname}-devel
Libraries, include files and other resources you can use to develop
%{name} applications.

%prep
%setup -q
%patch

%build
(cd XML \
&& %configure \
&& %make all\
)

%install
rm -rf %{buildroot}
cd XML && %makeinstall \
    datadir=%{buildroot}%{_datadir}/%{name} \
    includedir=%{buildroot}%{_includedir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
%{_mandir}/man5/*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_libdir}/*.a
%{_includedir}/%{name}

