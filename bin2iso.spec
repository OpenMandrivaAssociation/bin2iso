%define name    bin2iso
%define version 0.4
%define release %mkrel 4

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


