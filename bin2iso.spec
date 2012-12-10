%define name    bin2iso
%define version 0.4
%define release %mkrel 5

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Very simple utility to convert a BIN image
License:	GPLv2
Group:		File tools
URL:		http://mange.dynalias.org/linux/bin2iso
Source0:	http://mange.dynalias.org/linux/bin2iso/%{name}-%{version}.c
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This is a very simple utility to convert a BIN image
(either RAW/2352 or Mode2/2336 format) to standard ISO format (2048 b/s).

%prep
%setup -c -T
install -m 644 %{SOURCE0} %{name}.c


%build
gcc %{optflags} -o %{name} %{name}.c


%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_bindir}
install -m 755 %{name} %{buildroot}/%{_bindir}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root)
%{_bindir}/%{name}




%changelog
* Fri Aug 13 2010 Tomas Kindl <supp@mandriva.org> 0.4-5mdv2011.0
+ Revision: 569327
- rebuild

* Tue Jun 09 2009 Jérôme Brenier <incubusss@mandriva.org> 0.4-4mdv2010.0
+ Revision: 384153
- fix license

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 0.4-3mdv2009.0
+ Revision: 240445
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Sep 07 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.4-1mdv2008.0
+ Revision: 81662
- import bin2iso


* Fri Sep 07 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.4-1mdv2008.0
- first mdv release 
