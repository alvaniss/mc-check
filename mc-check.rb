class McCheck < Formula
  include Language::Python::Virtualenv

  desc "CLI tool to check Minecraft server status using the mcsrvstat.us API"
  homepage "https://github.com/alvaniss/mc-check"
  url "https://github.com/alvaniss/mc-check/archive/refs/tags/v1.0.0.tar.gz"
  sha256 "7b45de81d1e04f2a6aa8898f717683c701be38d7a5cf445866a6a625b2c8fdbd"
  license "GPL-3.0"

  depends_on "python@3.9"

  def install
    virtualenv_install_with_resources
  end

  test do
    assert_match "Usage", shell_output("#{bin}/mc_check --help")
  end
end
