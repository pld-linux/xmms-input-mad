Summary:	MP3 input plugin for xmms using MAD library
Summary(pl):	Wtyczka odtwarzaj�ca pliki MP3 dla xmms z u�yciem bilioteki MAD
Name:		xmms-input-mad
Version:	0.0.9
Release:	3
License:	GPL
Group:		X11/Applications/Sound
Source0:	xmms-mad-%{version}.tar.gz
Patch0:		%{name}-no-configure.patch
Requires:	xmms
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	libtool
BuildRequires:	mad-devel
BuildRequires:	xmms-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_xmms_plugin_dir	%(xmms-config --input-plugin-dir)

%description
xmms-mad is an input plugin for xmms that uses libmad to decode MPEG
layer 1/2/3 files and streams. It is not as configurable as mpg123
plugin, however it handles some evil mp3 files better.

%description -l pl
xmms-mad jest wtyczk� wej�ciow� dla xmms-a u�ywaj�c� libmad do
dekodowania plik�w i strumieni MPEG layer 1/2/3. Nie jest ona tak
konfigurowalna jak konkurencja (mpg123), jednak lepiej radzi sobie z
niekt�rymi uszkodzonymi plikami mp3.

%prep
%setup -q -n xmms-mad-%{version}
%patch0 -p1

%build
rm -f config/missing
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{_xmms_plugin_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_xmms_plugin_dir}/*
