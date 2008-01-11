%define		_plugin		searchindex
Summary:	DokuWiki Searchindex Manager
Summary(pl.UTF-8):	Zarządca indeksu wyszukiwania dla DokuWiki
Name:		dokuwiki-plugin-%{_plugin}
Version:	20050904
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://wiki.splitbrain.org/_media/plugin:searchindex-plugin-2005-09-04.tgz
# Source0-md5:	e572e94f5842a23f7514ebb8cda1514b
URL:		http://wiki.splitbrain.org/plugin:searchindex
Requires:	dokuwiki >= 20061106
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_dokudir	/usr/share/dokuwiki
%define		_plugindir	%{_dokudir}/lib/plugins/%{_plugin}

%description
This admin plugin allows you to rebuild the index used by the fulltext
search. This isn't needed generally as the index builds and updates
itself while users browse your wiki. However if you just upgraded,
added or removed a lot of files it may be a good idea to cleanup the
index.

This Plugin needs a recent Browser as it makes use of modern
JavaScript to carry out multiple tasks in the background (using AJAX).

%description -l pl.UTF-8
Wtyczka administratora pozwalająca przebudować indeks używany przez
wyszukiwanie pełnotekstowe. Nie jest niezbędna w ogólnym przypadku,
jako że indeks buduje się i uaktualnia sam w czasie przeglądania wiki.
Jednakże po uaktualnieniu, dodaniu lub usunięciu wielu plików
wyczyszczenie indeksu może być dobrym pomysłem.

Wtyczka ta wymaga aktualnej przeglądarki, jako że wykorzystuje nową
wersję JavaScriptu do wykonywania wielu zadań w tle (z użyciem
AJAX-a).

%prep
%setup -q -n %{_plugin}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_plugindir}
cp -a . $RPM_BUILD_ROOT%{_plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_plugindir}
