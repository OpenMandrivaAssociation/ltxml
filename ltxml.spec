%define name	ltxml
%define version	1.2.7
%define release	%mkrel 6
%define major	1
%define libname	%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

%define automake_version %(automake --version | awk '/^automake/ {print $4}')

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	High-speed C-language validating XML parser
License:	GPL
Group:		File tools
Url:		http://www.ltg.ed.ac.uk/software/xml
Source:		ftp://ftp.cogsci.ed.ac.uk/pub/LTXML/%{name}-%{version}.tar.bz2
Patch:		%{name}.maninstall.patch.bz2
BuildRequires:  zlib-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
LT XML is an integrated set of XML tools and a developers' tool-kit,
including a C-based API. The release now available will run on UNIX and
WIN32.
The LT XML tool-kit includes stand-alone tools for a wide range
of processing of well-formed XML documents, including searching and
extracting, down-translation (e.g. report generation, formatting),
tokenising and sorting. 

%package -n %{develname}
Summary:    Development header files for %{name}
Group:      Development/C
Requires:   %{name} = %{version}-%{release}
Provides:   %{name}-devel = %{version}-%{release}
Obsoletes:  %mklibname %{name} -d 1

%description -n %{develname}
Libraries, include files and other resources you can use to develop
%{name} applications.

%prep
%setup -q
%patch
cd XML
cp -f %{_datadir}/automake-%{automake_version}/config.* .

%build
cd XML
%configure2_5x
%make all

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

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/*.a
%{_includedir}/%{name}

