class McCheck < Formula
  include Language::Python::Virtualenv

  desc "CLI tool to check Minecraft server status using the mcsrvstat.us API"
  homepage "https://github.com/alvaniss/mc-check"
  url "https://github.com/alvaniss/mc-check/archive/refs/tags/v1.0.1.tar.gz"
  sha256 "61c89ad91f28a5cd04c58df908ec98ebafa929f6c930494f8255b596c70f89cd"
  license "GPL-3.0"

  depends_on "python@3.9"

  def install
    venv = virtualenv_create(libexec, "python3")
    venv.pip_install "requests"
    venv.pip_install "urllib3"
    venv.pip_install "idna"
    venv.pip_install "certifi"
    venv.pip_install "chardet"
    venv.pip_install_and_link buildpath
  end  

  test do
    assert_match "Usage", shell_output("#{bin}/mc_check --help")
  end
end
