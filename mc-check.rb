class McCheck < Formula
    include Language::Python::Virtualenv
    
    desc "CLI tool to check Minecraft server status using the mcsrvstat.us API"
    homepage "https://github.com/alvaniss/mc-check"
    url "https://github.com/alvaniss/mc-check/archive/refs/tags/v1.0.0.tar.gz"
    sha256 ""
    license "GPL-3.0"
  
    depends_on "python@3.9"
    depends_on "pip" => :build
  
    def install
      bin.install "mc-check.py" => "mc-check"
      virtualenv_install_with_resources
    end
  
    test do
      system "#{bin}/mc-check", "--help"
    end
  end
  