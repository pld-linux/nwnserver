Summary:	Neverwinter Nights - Linux dedicated server
Summary(pl):	Dedykowany serwer gry Neverwinter Nights  dla Linuxa
Name:		NWNDedicatedServer
Version:	1.32
Release:	0
Copyright:	Unknown
Group:		Games
Source0:	%{name}%{version}.zip
# Source0-md5	79a69c1fe539249181973f56b5b55a39
#Source1:	
BuildRequires:	unzip
#Requires:
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
-- empty --

%description -l pl
-- pusty --

%define		chroot_home	/home/nwn

%prep

%setup -n %{name}-%{version}

%build
mv nwn.ini nwn.ini.org
tar xvfz linuxdedserver132.tar.gz
mv -f nwn.ini.org nwn.ini
#./fixinstall

# make chroot jail
gcc -staitic -o nwsuexec  nwsuexec.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chroot_home}

%post
%postun

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
%attr(,,)
