Name:		crush
Version:	0.93.1
Release:	1
Summary:	Glamorous agentic coding agent for the terminal
License:	FSL-1.1-MIT
Group:		Development/Other
URL:		https://github.com/charmbracelet/crush
Source0:	https://github.com/charmbracelet/crush/archive/refs/tags/v%{version}/crush-%{version}.tar.gz
#	go mod vendor
#	tar cJf ../godeps-for-crush-%{version}.tar.xz vendor
Source1:	godeps-for-crush-%{version}.tar.xz
BuildRequires:	golang
BuildRequires:	compiler(go-compiler)
Recommends:	llama-cpp-server
Recommends:	ollama

%description
Crush is Charm's terminal coding agent. It talks to OpenAI-compatible
and Anthropic-compatible APIs, including a local llama-server or
Ollama.

Point it at cooker llama.cpp after install:

  crush provider add llamacpp --type openai --base-url "http://127.0.0.1:8080/v1"
  crush model add llamacpp/local --name "llama-server" --context-window 131072

Or use Ollama at http://127.0.0.1:11434/v1.

%prep
%autosetup -p1 -n %{name}-%{version} -a1

%build
export CGO_ENABLED=0
export GO111MODULE=on
export GOFLAGS="-mod=vendor"
export GOPROXY=off
export GOTOOLCHAIN=local
go build -trimpath \
	-ldflags "-s -w -X github.com/charmbracelet/crush/internal/version.Version=%{version}" \
	-o crush .

%install
install -D -m 0755 crush %{buildroot}%{_bindir}/crush

%files
%license LICENSE.md
%doc README.md
%{_bindir}/crush
