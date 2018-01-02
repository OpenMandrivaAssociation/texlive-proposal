Name:		texlive-proposal
Version:	20170414
Release:	1
Summary:	A class for preparing proposals
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/proposal
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/proposal.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/proposal.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/proposal.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The process of preparing a collaborative proposal, to a major
funding body, involves integration of contributions of a many
people at many sites. It is therefore an ideal application for
a text-based document preparation system such as LaTeX, in
concert with a distributed version control system such as SVN.
The proposal class itself provides a basis for such an
enterprise. The dfgproposal and dfgproposal classes provide two
specialisations of the base class for (respectively) German and
European research proposals. The packages depend on the
author's stex bundle.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/proposal
%doc %{_texmfdistdir}/doc/latex/proposal
#- source
%doc %{_texmfdistdir}/source/latex/proposal

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
