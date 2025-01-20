class McCheck < Formula
  include Language::Python::Virtualenv

  desc "CLI tool to check Minecraft server status using the mcsrvstat.us API"
  homepage "https://github.com/alvaniss/mc-check"
  url "https://github.com/alvaniss/mc-check/archive/refs/tags/v1.0.2.tar.gz"
  sha256 "8a12827656e57ca96abd4182de80ae313c4c22197b8e31d2c669e34ffc380696"
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
