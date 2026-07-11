%global tl_name proposal
%global tl_revision 40538

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A set of LaTeX classes for preparing proposals for collaborative projects
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/proposal
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/proposal.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/proposal.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/proposal.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The process of preparing a collaborative proposal, to a major funding
body, involves integration of contributions of a many people at many
sites. It is therefore an ideal application for a text-based document
preparation system such as LaTeX, in concert with a distributed version
control system such as SVN. The proposal class itself provides a basis
for such an enterprise. The dfgproposal and dfgproposal classes provide
two specialisations of the base class for (respectively) German and
European research proposals. The packages depend on the author's stex
bundle.

