Summary:	Neverwinter Nights - Linux dedicated server
Summary(pl):	Dedykowany serwer gry Neverwinter Nights  dla Linuxa
Name:		NWNDedicatedServer
Version:	1.32
Release:	0
Copyright:	Unknown
Group:		Games
Source0:	%{name}%{version}.zip
# Source0-md5	79a69c1fe539249181973f56b5b55a39
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Neverwinter Nights SoU v1.32 Linux Dedicated Server.

%description -l pl
Serwer gry Neverwinter Nights SoU w wersji 1.32

%define		_chroot_home	/home/nwn

%prep

%setup -n %{name}-%{version}

%build
mv nwn.ini nwn.ini.org
tar xvfz linuxdedserver132.tar.gz
mv -f nwn.ini.org nwn.ini
./fixinstall

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chroot_home}

#makind directories
install -d $RPM_BUILD_ROOT%{_chroot_home}/{ambient,data,\
database,dmvault,docs,erf,hak,localvault,logs,modules,music\
override,portraits,saves,servervault,temp,utils}
cp -a data/* $RPM_BUILD_ROOT%{_chroot_home}/data/
cp -a database/* $RPM_BUILD_ROOT%{_chroot_home}/database/
cp -a modules/* $RPM_BUILD_ROOT%{_chroot_home}/modules/
cp -a nwn/* $RPM_BUILD_ROOT%{_chroot_home}/nwn/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_chroot_home}/ambient
%attr(644,root,root) %{_chroot_home)/data/*.bif
%attr(644,root,root) %{_chroot_home)/database/*
%dir %{_chroot_home}/dmvault
%dir %{_chroot_home}/docs
%dir %{_chroot_home}/erf
%dir %{_chroot_home}/hak
%dir %{_chroot_home}/localvault
%dir %{_chroot_home}/logs
%attr(644,root,root) %{_chroot_home}/modules/*.mod
%dir %{_chroot_home}/music
%dir %{_chroot_home}/override
%dir %{_chroot_home}/portraits
%dir %{_chroot_home}/saves
%dir %{_chroot_home}/servervault
%dir %{_chroot_home}/temp
%attr(755, root,root) %{_chroot_home}/nwserver
%attr(644, root,root) %{_chroot_home}/*.ini
%attr(644, root,root) %{_chroot_home}/*.tlk
%attr(644, root,root) %{_chroot_home}/*.key
%attr(644, root,root) %{_chroot_home}/NWNv132.txt
%attr(644, root,root) %{_chroot_home}/readme.linuxserver.txt
