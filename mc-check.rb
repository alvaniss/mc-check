class McCheck < Formula
  include Language::Python::Virtualenv

  desc "CLI tool to check Minecraft server status using the mcsrvstat.us API"
  homepage "https://github.com/alvaniss/mc-check"
  url "https://github.com/alvaniss/mc-check/archive/refs/tags/v1.0.0.tar.gz"
  sha256 "4b6a7f1e1ee2887a939564d89364e63be9ff11adea94304d41add69d7f80bda7"
  license "GPL-3.0"

  depends_on "python@3.9"

  def install
    virtualenv_install_with_resources
  end

  test do
    assert_match "Usage", shell_output("#{bin}/mc_check --help")
  end
end
