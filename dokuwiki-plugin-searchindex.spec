%define		plugin		searchindex
%define		php_min_version 5.0.0
%include	/usr/lib/rpm/macros.php
Summary:	DokuWiki Searchindex Manager
Summary(pl.UTF-8):	Zarządca indeksu wyszukiwania dla DokuWiki
Name:		dokuwiki-plugin-%{plugin}
Version:	20110502
Release:	6
License:	GPL v2
Group:		Applications/WWW
Source0:	http://github.com/splitbrain/dokuwiki-plugin-%{plugin}/zipball/master#/%{plugin}.zip
# Source0-md5:	ecf9e27851b6ef33df6e75ce144076a5
URL:		http://www.dokuwiki.org/plugin:searchindex
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.520
Requires:	dokuwiki >= 20090214
Requires:	php(core) >= %{php_min_version}
Requires:	php(session)
Requires:	php-date
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}
%define		find_lang 	%{_usrlibrpm}/dokuwiki-find-lang.sh %{buildroot}

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
%setup -qc
# for githug urls:
mv *-%{plugin}-*/* .

version=$(awk '/^date/{print $2}' plugin.info.txt)
if [ "$(echo "$version" | tr -d -)" != %{version} ]; then
	: %%{version} mismatch
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}
%{__rm} $RPM_BUILD_ROOT%{plugindir}/README

%find_lang %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post
# force js/css cache refresh
if [ -f %{dokuconf}/local.php ]; then
	touch %{dokuconf}/local.php
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%dir %{plugindir}
%{plugindir}/*.css
%{plugindir}/*.js
%{plugindir}/*.php
%{plugindir}/*.txt
