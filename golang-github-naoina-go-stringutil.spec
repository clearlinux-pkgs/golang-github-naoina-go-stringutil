Name     : golang-github-naoina-go-stringutil
Version  : 0.1.0
Release  : 1
URL      : https://github.com/naoina/go-stringutil/archive/v0.1.0.tar.gz
Source0  : https://github.com/naoina/go-stringutil/archive/v0.1.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : go

%description
# stringutil [![Build Status](https://travis-ci.org/naoina/go-stringutil.svg?branch=master)](https://travis-ci.org/naoina/go-stringutil)

%prep
%setup -q -n go-stringutil-0.1.0

%build
export LANG=C

%install
rm -rf %{buildroot}
%global gopath /usr/lib/golang
%global library_path github.com/naoina/go-stringutil

# Copy all *.go and *.s files
install -d -p %{buildroot}%{gopath}/src/%{library_path}/
for ext in go s src golden template; do
    for file in $(find . -iname "*.$ext") ; do
         install -d -p %{buildroot}%{gopath}/src/%{library_path}/$(dirname $file)
         cp -pav $file %{buildroot}%{gopath}/src/%{library_path}/$file
    done
done

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export GOPATH=%{buildroot}%{gopath}
go test %{library_path}/... || :

%files
%defattr(-,root,root,-)
/usr/lib/golang/src/github.com/naoina/go-stringutil/da.go
/usr/lib/golang/src/github.com/naoina/go-stringutil/strings.go
/usr/lib/golang/src/github.com/naoina/go-stringutil/strings_bench_test.go
/usr/lib/golang/src/github.com/naoina/go-stringutil/strings_test.go
