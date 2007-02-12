%define		_realname	NWNDedicatedServer
Summary:	Neverwinter Nights - Linux dedicated server
Summary(pl.UTF-8):   Dedykowany serwer gry Neverwinter Nights dla Linuksa
Name:		nwnserver
Version:	1.64
Release:	0
License:	unknown
Group:		Applications/Games
Source0:        http://nwdownloads.bioware.com/neverwinternights/standaloneserver/%{_realname}%{version}.zip
# Source0-md5:	1b232bc2da01e2bf20570e691abfb29e
URL:		http://nwn.bioware.com/downloads/standaloneserver.html
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_chroot_home	/home/nwn

%description
Neverwinter Nights HotU v1.64 Linux Dedicated Server.

%description -l pl.UTF-8
Serwer gry Neverwinter Nights HotU w wersji 1.64.

%prep
%setup

%build
mv nwn.ini nwn.ini.org
tar xvfz linuxdedserver132.tar.gz
mv -f nwn.ini.org nwn.ini
./fixinstall

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chroot_home}/{ambient,data,\
database,dmvault,docs,erf,hak,localvault,logs,modules,music\
override,portraits,saves,servervault,temp,utils}

cp -a data/* $RPM_BUILD_ROOT%{_chroot_home}/data
cp -a database/* $RPM_BUILD_ROOT%{_chroot_home}/database
cp -a modules/* $RPM_BUILD_ROOT%{_chroot_home}/modules
cp -a nwn/* $RPM_BUILD_ROOT%{_chroot_home}/nwn

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_chroot_home}
%dir %{_chroot_home}/ambient
%dir %{_chroot_home}/data
%{_chroot_home)/data/*.bif
%dir %{_chroot_home}/database
%{_chroot_home)/database/*
%dir %{_chroot_home}/dmvault
%dir %{_chroot_home}/docs
%dir %{_chroot_home}/erf
%dir %{_chroot_home}/hak
%dir %{_chroot_home}/localvault
%dir %{_chroot_home}/logs
%dir %{_chroot_home}/modules
%{_chroot_home}/modules/*.mod
%dir %{_chroot_home}/music
%dir %{_chroot_home}/override
%dir %{_chroot_home}/portraits
%dir %{_chroot_home}/saves
%dir %{_chroot_home}/servervault
%dir %{_chroot_home}/temp
%attr(755,root,root) %{_chroot_home}/nwserver
%{_chroot_home}/*.ini
%{_chroot_home}/*.tlk
%{_chroot_home}/*.key
%{_chroot_home}/NWNv132.txt
%{_chroot_home}/readme.linuxserver.txt
