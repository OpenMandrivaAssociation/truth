%{?_javapackages_macros:%_javapackages_macros}

Name:           truth
Version:        0.23
Release:        5%{?dist}
Summary:        An assertion framework for Java unit tests
License:        ASL 2.0
URL:            https://github.com/google/truth
# Created from revision 3c4492b0f72290c8b4a32f1b313b13501e96f44d
# of git@github.com:google/truth.git using the following command:
# git archive --format=tar --prefix=truth-0.23/ 3c4492b |xz >truth-0.23.tar.xz
Source0:        truth-0.23.tar.xz
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(com.google.auto.value:auto-value)
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(com.google.guava:guava)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)

%description
Truth is a library provides alternative ways to express assertions in
unit tests. It can be used as a replacement for JUnit's assertions or FEST
or it can be used alongside where other approaches seem more suitable.

%package        javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :gwt-maven-plugin core
%pom_remove_dep :gwt-user core
%pom_remove_dep :guava-gwt core
%pom_xpath_inject "pom:build/pom:plugins/pom:plugin[pom:artifactId[text()='maven-compiler-plugin']]/pom:configuration" "
          <testExcludes>
            <exclude>**/gwt/*.java</exclude>
          </testExcludes>" core

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%dir %{_javadir}/%{name}
%doc LICENSE
%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.23-4
- Regenerate build-requires

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 3 2015 Noa Resare <noa@resare.com> - 0.23-1
- Initial packaging
